#!/usr/bin/env python3
"""
Single-source, multi-module site generator.

Builds each site_src/moduleMM/lessonNN.md from the AUTHORITATIVE canonical lesson
markdown in modules/moduleMM/lessons/, injecting produced assets (SVG, Mermaid,
interactive demo, notebook link, interactive quiz) at the right sections, and copies
those assets into site_src/ for serving.

Canonical lesson markdown is the only place prose is maintained. Re-run after edits:
    python3 tools/generate_site_pages.py

Conventions per module MM (01, 02, ...):
  canonical lessons : modules/moduleMM/lessons/lessonNN_*.md
  diagrams          : assets/diagrams/mMM-lN-*.svg        (N = int(NN))
  quizzes           : modules/moduleMM/quizzes/lessonNN_quiz.html
  demos             : modules/moduleMM/demos/lessonNN_*.html
  notebooks         : modules/moduleMM/notebooks/lessonNN_*.ipynb
Served copies:
  site_src/assets/mMM-*.svg            (flat; module prefix avoids collisions)
  site_src/quizzes/moduleMM/*.html     (namespaced by module)
  site_src/demos/moduleMM/*.html       (namespaced by module)
Paths:
  iframe src (raw HTML, browser-resolved against output URL /moduleMM/lessonNN/):
      demo  -> ../../demos/moduleMM/<file>
      quiz  -> ../../quizzes/moduleMM/<file>
  markdown fallback link (MkDocs-rewritten, source-relative to site_src/moduleMM/lessonNN.md):
      demo  -> ../demos/moduleMM/<file>
      quiz  -> ../quizzes/moduleMM/<file>
"""
import re, os, glob, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIAG = os.path.join(ROOT, "assets/diagrams")
S_ASSETS = os.path.join(ROOT, "site_src/assets")
os.makedirs(S_ASSETS, exist_ok=True)

# modules to build (extend as new modules are produced)
MODULES = ["01", "02"]

# module + unit titles, for the in-page context header (Module / Unit / Lesson)
MODULE_TITLES = {
    "01": "Mathematical Foundations",
    "02": "Spatial Transformations and SE(3)",
}
UNIT_TITLES = {
    ("01", "01"): "Physical Quantities & Measurement",
    ("01", "02"): "Vectors",
    ("01", "03"): "Coordinate Systems & Reference Frames",
    ("01", "04"): "Matrices as Transformations",
    ("02", "01"): "Why Transformations Matter",
    ("02", "02"): "Homogeneous Coordinates",
    ("02", "03"): "SE(2) Transformations",
    ("02", "04"): "SE(3) Transformations",
    ("02", "05"): "Transformation Composition",
    ("02", "06"): "Robot Pose Representation",
    ("02", "07"): "Camera-to-Robot Transformations",
    ("02", "08"): "Mini Project: Perception-to-Pose Pipeline",
}

def unit_of(text):
    m = re.search(r'^unit:\s*([0-9]+)', text, re.M)
    return ("%02d" % int(m.group(1))) if m else None

def lesson_files(les_dir):
    return sorted(glob.glob(os.path.join(les_dir, "lesson[0-9][0-9]_*.md")))

def idx_of(path):
    return re.search(r'lesson(\d\d)_', os.path.basename(path)).group(1)

def lesson_number(text):
    m = re.search(r'^lesson:\s*([0-9.]+)', text, re.M)
    return m.group(1) if m else "?"

def title_of(text):
    m = re.search(r'^# Lesson [0-9.]+ — (.+)$', text, re.M)
    return m.group(1).strip() if m else "Lesson"

def strip_frontmatter(text):
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end+4:].lstrip("\n")
    return text

def inject_after_heading(body, heading_regex, snippet):
    pat = re.compile(heading_regex, re.M)
    m = pat.search(body)
    if not m: return body, False
    insert_at = m.end()
    before = body[:insert_at].rstrip()
    after = body[insert_at:].lstrip("\n")
    return before + "\n\n" + snippet.strip() + "\n\n" + after, True

def build(path, mod):
    les_dir = os.path.join(ROOT, "modules/module%s/lessons" % mod)
    quiz_dir = os.path.join(ROOT, "modules/module%s/quizzes" % mod)
    demo_dir = os.path.join(ROOT, "modules/module%s/demos" % mod)
    nb_dir   = os.path.join(ROOT, "modules/module%s/notebooks" % mod)
    site_dir = os.path.join(ROOT, "site_src/module%s" % mod)
    s_quiz   = os.path.join(ROOT, "site_src/quizzes/module%s" % mod)
    s_demo   = os.path.join(ROOT, "site_src/demos/module%s" % mod)
    for d in (site_dir, s_quiz, s_demo): os.makedirs(d, exist_ok=True)

    nn = idx_of(path)
    raw = open(path).read()
    num = lesson_number(raw)
    title = title_of(raw)
    uu = unit_of(raw) or "01"
    body = strip_frontmatter(raw)

    # Context header (Issue 3): make Module / Unit / Lesson visible on every page,
    # inserted just above the lesson H1 ("# Lesson X.Y — Title").
    mod_title = MODULE_TITLES.get(mod, "")
    unit_title = UNIT_TITLES.get((mod, uu), "")
    context = (
        '!!! abstract "You are here"\n'
        '    **Module %s — %s**  ·  **Unit %s — %s**  ·  **Lesson %s — %s**'
        % (str(int(mod)), mod_title, str(int(uu)), unit_title, num, title)
    )
    # place the admonition immediately before the first H1
    m_h1 = re.search(r'^# Lesson .+$', body, re.M)
    if m_h1:
        body = body[:m_h1.start()] + context + "\n\n" + body[m_h1.start():]

    li = str(int(nn))
    svgs  = sorted(glob.glob(os.path.join(DIAG, "m%s-l%s-*.svg" % (mod, li))))
    quiz  = glob.glob(os.path.join(quiz_dir, "lesson%s_quiz.html" % nn))
    demos = glob.glob(os.path.join(demo_dir, "lesson%s_*.html" % nn))
    nbs   = glob.glob(os.path.join(nb_dir, "M%s_U%s_L%s_*.ipynb" % (mod, uu, num.replace(".", "_")))) \
            or glob.glob(os.path.join(nb_dir, "lesson%s_*.ipynb" % nn))

    for s in svgs: shutil.copy(s, S_ASSETS)
    for q in quiz: shutil.copy(q, s_quiz)
    for d in demos: shutil.copy(d, s_demo)

    # SVG figures -> after "## 4. Visual Explanation"
    if svgs:
        figs = "\n\n".join(
            '<figure markdown>\n  ![%s](../assets/%s){ width="680" }\n</figure>' %
            (title, os.path.basename(s)) for s in svgs)
        body, _ = inject_after_heading(body, r'^##\s+(?:\d+\.\s+)?Visual Explanation\s*$', figs)

    # demo iframe -> after "## 7. Interactive Demonstration"
    if demos:
        d = os.path.basename(sorted(demos)[0])
        iframe = ('<iframe src="../../demos/module%s/%s" title="%s interactive demo" '
                  'style="width:100%%;height:520px;border:1px solid #e2e8f0;border-radius:12px"></iframe>\n\n'
                  '[Open this demo in a new tab \u2197](../demos/module%s/%s)'
                  % (mod, d, title, mod, d))
        body, _ = inject_after_heading(body, r'^##\s+(?:\d+\.\s+)?Interactive Demonstration\s*$', iframe)

    # notebook tip -> after "## 8. Coding Exercise"
    if nbs:
        nbname = os.path.basename(sorted(nbs)[0])
        tip = ('!!! tip "Run the hands-on notebook"\n'
               '    `modules/module%s/notebooks/%s` — open in JupyterLab and run **Kernel → Restart & Run All**.' % (mod, nbname))
        body, _ = inject_after_heading(body, r'^##\s+(?:\d+\.\s+)?Coding Exercise\s*$', tip)

    # quiz iframe -> after "## 9. Knowledge Check"
    if quiz:
        q = os.path.basename(quiz[0])
        iframe = ('Formative — unlimited attempts, immediate feedback; does not affect your grade.\n\n'
                  '<iframe src="../../quizzes/module%s/%s" title="%s knowledge check" '
                  'style="width:100%%;height:720px;border:1px solid #e2e8f0;border-radius:12px"></iframe>\n\n'
                  '[Open this quiz in a new tab \u2197](../quizzes/module%s/%s)'
                  % (mod, q, title, mod, q))
        body, _ = inject_after_heading(body, r'^##\s+(?:\d+\.\s+)?Knowledge Check\s*$', iframe)

    out = os.path.join(site_dir, "lesson%s.md" % nn)
    published = bool(svgs or quiz or demos)

    # strip authoring scaffolding from the STUDENT page
    body = re.sub(r'^`\[Visual:.*?`\s*\n', '', body, flags=re.M)
    body = re.sub(r'\*\*Rendered assets?:?\*\*.*?\n\n', '', body, flags=re.S)
    body = re.sub(r'\*\*Diagram Specification\*\*.*?(?=\n## )', '', body, flags=re.S)
    body = re.sub(r'\n{3,}', '\n\n', body)

    if published:
        # VALIDATOR (Issue 1): a published page that has a "Visual Explanation"
        # heading MUST contain an injected figure. This makes the recap-style
        # "anchor missing -> figure silently dropped" bug impossible to ship.
        if re.search(r'^##\s+(?:\d+\.\s+)?Visual Explanation\s*$', body, re.M):
            section = body.split("Visual Explanation", 1)[1]
            nxt = re.search(r'\n##\s', section)
            section = section[:nxt.start()] if nxt else section
            if "<figure" not in section and "<img" not in section:
                raise SystemExit(
                    "VISUAL EMBED MISSING: module %s lesson %s (%s) has a 'Visual Explanation' "
                    "section but no figure was injected. Check that an SVG named "
                    "assets/diagrams/m%s-l%s-*.svg exists." % (mod, nn, num, mod, str(int(nn)))
                )
        # also: a leftover [Visual: ...] placeholder should never reach a student page
        if re.search(r'`\[Visual:', body):
            raise SystemExit(
                "VISUAL PLACEHOLDER LEFTOVER: module %s lesson %s (%s) still contains a "
                "`[Visual: ...]` placeholder in the published page." % (mod, nn, num)
            )
        open(out, "w").write(body)
    else:
        if os.path.exists(out): os.remove(out)

    feats = []
    if svgs: feats.append("%d SVG" % len(svgs))
    if "```mermaid" in body: feats.append("mermaid")
    if demos: feats.append("demo")
    if nbs: feats.append("notebook")
    if quiz: feats.append("quiz")
    return num, title, nn, (", ".join(feats) if published else "PENDING (not published)")

if __name__ == "__main__":
    print("Generating site pages from canonical lessons...\n")
    total = 0
    for mod in MODULES:
        les_dir = os.path.join(ROOT, "modules/module%s/lessons" % mod)
        files = lesson_files(les_dir)
        if not files: continue
        print("Module %s:" % mod)
        for f in files:
            num, title, nn, feats = build(f, mod)
            print(f"  {num:4s} (lesson{nn}) {title:40s} [{feats}]")
            total += 1
        print()
    print("Done. %d pages generated." % total)
