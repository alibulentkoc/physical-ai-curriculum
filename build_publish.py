#!/usr/bin/env python3
"""build_publish.py — scope the published site to a subset of modules.

Two-branch release model:
  main      = full curriculum source (all 10 modules, always complete)
  publish   = the built site GitHub Pages serves (a slice of modules)

Produces a pruned docs tree (publish_src/) and a scoped MkDocs config
(mkdocs.publish.yml) with ONLY the requested modules, so
  mkdocs build --strict -f mkdocs.publish.yml
builds a site nav-scoped AND content-pruned to those modules.

Usage:
  python tools/build_publish.py --modules all      # full preview (1..10)
  python tools/build_publish.py --modules 1        # Module 1 only
  python tools/build_publish.py --modules 1 2 3    # Modules 1-3 (cumulative slice)

The config is edited as TEXT (only nav, docs_dir, site_name) so MkDocs-specific
YAML tags (!!python/name:...) are preserved verbatim. Never touches site_src,
mkdocs.yml, or any module content.
"""
import argparse, os, re, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "site_src")
PUB = os.path.join(ROOT, "publish_src")
FULL_CFG = os.path.join(ROOT, "mkdocs.yml")
PUB_CFG = os.path.join(ROOT, "mkdocs.publish.yml")
MODNUM = re.compile(r'Module\s+(\d+)\b')


def parse_modules(args):
    toks = [t for a in args for t in re.split(r"[,\s]+", a) if t]
    if any(t.lower() == "all" for t in toks):
        return set(range(1, 11))
    nums = set()
    for t in toks:
        if not t.isdigit():
            sys.exit(f"bad module token {t!r} (use ints 1..10 or 'all')")
        nums.add(int(t))
    if not nums or min(nums) < 1 or max(nums) > 10:
        sys.exit("modules must be in 1..10")
    return nums


def scope_config_text(published):
    lines = open(FULL_CFG, encoding="utf-8").read().splitlines()
    out, i, n = [], 0, len(lines)
    while i < n:
        line = lines[i]
        if line.rstrip() == "nav:":
            out.append(line); i += 1
            while i < n and (lines[i].startswith((" ", "\t")) or lines[i].strip() == ""):
                if re.match(r"^  - ", lines[i]):
                    block = [lines[i]]; j = i + 1
                    while j < n and not re.match(r"^  - ", lines[j]):
                        if lines[j] and not lines[j].startswith((" ", "\t")):
                            break
                        block.append(lines[j]); j += 1
                    m = MODNUM.search(block[0])
                    if (m is None) or (int(m.group(1)) in published):
                        out.extend(block)
                    i = j
                else:
                    i += 1
            continue
        if re.match(r"^docs_dir:", line):
            out.append("docs_dir: publish_src"); i += 1; continue
        if re.match(r"^site_name:", line):
            label = "full curriculum" if published == set(range(1, 11)) else \
                    "Modules " + ",".join(str(x) for x in sorted(published))
            out.append(f"site_name: Physical AI Curriculum ({label})"); i += 1; continue
        out.append(line); i += 1
    return "\n".join(out) + "\n"


def prune_docs(published):
    if os.path.exists(PUB):
        shutil.rmtree(PUB)
    shutil.copytree(SRC, PUB)
    for k in range(1, 11):
        if k in published:
            continue
        z = f"module{k:02d}"
        for sub in (z, os.path.join("demos", z), os.path.join("quizzes", z)):
            p = os.path.join(PUB, sub)
            if os.path.exists(p):
                shutil.rmtree(p)
    idx = os.path.join(PUB, "index.md")
    if os.path.exists(idx):
        lo = min(published)
        t = open(idx, encoding="utf-8").read()
        open(idx, "w", encoding="utf-8").write(re.sub(r"module\d{2}/lesson01", f"module{lo:02d}/lesson01", t))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--modules", nargs="+", required=True,
                    help="module numbers 1..10 (space/comma) or 'all'")
    published = parse_modules(ap.parse_args().modules)
    prune_docs(published)
    open(PUB_CFG, "w", encoding="utf-8").write(scope_config_text(published))
    pages = sum(1 for k in published
                for p in os.listdir(os.path.join(PUB, f"module{k:02d}"))
                if p.startswith("lesson") and p.endswith(".md"))
    print(f"published modules : {sorted(published)}")
    print(f"docs tree         : publish_src/ ({pages} lesson pages)")
    print(f"scoped config     : mkdocs.publish.yml")
    print(f"next              : mkdocs build --strict -f mkdocs.publish.yml")


if __name__ == "__main__":
    main()
