#!/usr/bin/env python3
"""
Per-module publish builder.

Produces an isolated, scoped documentation tree and an mkdocs config that
contains ONLY the requested modules, so the site can be built and deployed one
module (or a growing range) at a time:

    python tools/build_publish.py --modules 1          # Module 1 only   -> 33 pages
    python tools/build_publish.py --modules 1 2 3      # Modules 1-3     -> 101 pages
    python tools/build_publish.py --modules all        # full preview    -> 325 pages

    mkdocs build --strict -f mkdocs.publish.yml        # must be exit 0
    mkdocs serve         -f mkdocs.publish.yml         # preview at 127.0.0.1:8000
    mkdocs gh-deploy     -f mkdocs.publish.yml -b gh-pages -m "Publish: Module 1"

What it writes (both git-ignored build artifacts):
  publish_src/        scoped docs_dir: index.md + assets/ + only the selected
                       module pages, demos, and quizzes (so gh-deploy publishes
                       exactly those modules — nothing else leaks in).
  mkdocs.publish.yml   `INHERIT: mkdocs.yml` (reuses theme/extensions/plugins),
                       overrides docs_dir -> publish_src and nav -> Home + the
                       selected modules' nav sub-trees lifted verbatim from
                       mkdocs.yml.

The selected modules are regenerated from the canonical lessons first (reusing
tools/generate_site_pages.py), so this is a single deterministic command.
"""
import sys, os, re, shutil, argparse, builtins

# --- Force UTF-8 for all text I/O (Windows default cp1252 cannot encode the
#     arrows/dashes in the lesson pages). Wrapping open() also fixes the writes
#     done inside generate_site_pages.py without editing that file. ---
_real_open = builtins.open
def _utf8_open(file, mode="r", *args, **kwargs):
    if "b" not in mode and kwargs.get("encoding") is None:
        kwargs["encoding"] = "utf-8"
    return _real_open(file, mode, *args, **kwargs)
builtins.open = _utf8_open
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import generate_site_pages as gsp  # noqa: E402  (after open() patch & sys.path)

MKDOCS   = os.path.join(ROOT, "mkdocs.yml")
PUB_CFG  = os.path.join(ROOT, "mkdocs.publish.yml")
SITE_SRC = os.path.join(ROOT, "site_src")
SITE_PUB = os.path.join(ROOT, "publish_src")


def parse_selection(values):
    """['all'] -> every module present; ['1','2'] -> ['01','02']."""
    present = [m for m in gsp.MODULES
              if gsp.lesson_files(os.path.join(ROOT, "modules/module%s/lessons" % m))]
    if len(values) == 1 and values[0].lower() == "all":
        return present
    out = []
    for v in values:
        try:
            code = "%02d" % int(v)
        except ValueError:
            sys.exit("error: --modules takes integers or 'all', not %r" % v)
        if code not in present:
            sys.exit("error: module %s has no canonical lessons" % code)
        if code not in out:
            out.append(code)
    return out


def regenerate(selected):
    """Regenerate the selected modules into site_src/. Returns published count."""
    print("Regenerating canonical pages for modules: %s\n" % ", ".join(selected))
    published = 0
    for mod in selected:
        les_dir = os.path.join(ROOT, "modules/module%s/lessons" % mod)
        files = gsp.lesson_files(les_dir)
        if not files:
            continue
        print("Module %s:" % mod)
        for f in files:
            num, title, nn, feats = gsp.build(f, mod)
            print(f"  {num:4s} (lesson{nn}) {title:40s} [{feats}]")
            if "PENDING" not in feats:
                published += 1
        print()
    return published


def assemble_publish_src(selected):
    """Build an isolated docs_dir holding ONLY the selected modules + shared files."""
    if os.path.exists(SITE_PUB):
        shutil.rmtree(SITE_PUB)
    os.makedirs(SITE_PUB)

    selected_dirs = {"module%s" % c for c in selected}
    for entry in sorted(os.listdir(SITE_SRC)):
        src = os.path.join(SITE_SRC, entry)
        dst = os.path.join(SITE_PUB, entry)
        if entry in ("demos", "quizzes"):
            continue  # copied selectively below
        if entry.startswith("module") and entry not in selected_dirs:
            continue  # skip non-selected module page dirs
        if os.path.isdir(src):
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)

    # selectively copy per-module demos/quizzes for the selected modules only
    for kind in ("demos", "quizzes"):
        for code in selected:
            sub = os.path.join(SITE_SRC, kind, "module%s" % code)
            if os.path.isdir(sub):
                shutil.copytree(sub, os.path.join(SITE_PUB, kind, "module%s" % code))


def extract_nav(selected):
    """Lift the Home entry and the selected modules' nav sub-trees verbatim."""
    lines = _real_open(MKDOCS, encoding="utf-8").read().splitlines()
    nav_i = next(i for i, l in enumerate(lines) if l.rstrip() == "nav:")
    end = len(lines)
    for i in range(nav_i + 1, len(lines)):
        if lines[i] and not lines[i][0].isspace():   # next top-level key ends nav
            end = i
            break

    kept, keep = [], False
    for l in lines[nav_i + 1:end]:
        if re.match(r"^  - ", l):                     # a top-level nav entry
            if l.startswith("  - Home"):
                keep = True
            else:
                m = re.match(r'^  - "?Module (\d+)', l)
                keep = bool(m) and ("%02d" % int(m.group(1))) in selected
        if keep:
            kept.append(l)
    return kept


def write_publish_config(selected):
    nav = extract_nav(selected)
    with _real_open(PUB_CFG, "w", encoding="utf-8") as fh:
        fh.write("# AUTO-GENERATED by tools/build_publish.py — do not edit by hand.\n")
        fh.write("# Scoped publish config for modules: %s\n" % ", ".join(selected))
        fh.write("INHERIT: mkdocs.yml\n")
        fh.write("docs_dir: publish_src\n")
        fh.write("site_dir: publish_site\n")
        fh.write("nav:\n")
        for l in nav:
            fh.write(l + "\n")


def main():
    ap = argparse.ArgumentParser(description="Build a scoped per-module publish preview.")
    ap.add_argument("--modules", nargs="+", required=True, metavar="N",
                    help="module numbers (e.g. 1 2 3) or 'all'")
    args = ap.parse_args()

    selected = parse_selection(args.modules)
    count = regenerate(selected)
    assemble_publish_src(selected)
    write_publish_config(selected)

    print("Wrote %s (docs_dir: publish_src, %d module%s)."
          % (os.path.basename(PUB_CFG), len(selected), "" if len(selected) == 1 else "s"))
    print("-> %d pages" % count)
    print("\nNext:")
    print("  mkdocs build --strict -f mkdocs.publish.yml")
    print("  mkdocs serve         -f mkdocs.publish.yml")


if __name__ == "__main__":
    main()
