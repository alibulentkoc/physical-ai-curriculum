#!/usr/bin/env python3
"""
Single-source site generator.

Builds each site_src/module01/lessonNN.md from the AUTHORITATIVE canonical lesson
markdown in modules/module01/lessons/, injecting the produced assets (SVG, Mermaid,
interactive demo, notebook link, interactive quiz) at the right sections, and copies
those assets into site_src/ for serving.

Canonical lesson markdown is the only place prose is maintained. Re-run this script
after editing any lesson or adding assets:  python3 tools/generate_site_pages.py
"""
import re, os, glob, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LES  = os.path.join(ROOT, "modules/module01/lessons")
DIAG = os.path.join(ROOT, "assets/diagrams")
QUIZ = os.path.join(ROOT, "modules/module01/quizzes")
DEMO = os.path.join(ROOT, "modules/module01/demos")
NB   = os.path.join(ROOT, "modules/module01/notebooks")
SITE = os.path.join(ROOT, "site_src/module01")
S_ASSETS = os.path.join(ROOT, "site_src/assets")
S_QUIZ   = os.path.join(ROOT, "site_src/quizzes")
S_DEMO   = os.path.join(ROOT, "site_src/demos")
for d in (SITE, S_ASSETS, S_QUIZ, S_DEMO): os.makedirs(d, exist_ok=True)

# canonical lesson files in order; file index NN drives all asset names by convention
def lesson_files():
    return sorted(glob.glob(os.path.join(LES, "lesson[0-9][0-9]_*.md")))

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

def build(path):
    nn = idx_of(path)
    raw = open(path).read()
    num = lesson_number(raw)
    title = title_of(raw)
    body = strip_frontmatter(raw)

    # assets by convention (file index NN)
    li = str(int(nn))  # 01->1 ... 09->9 ... matches m01-lN naming
    svgs = sorted(glob.glob(os.path.join(DIAG, "m01-l%s-*.svg" % li)))
    quiz = glob.glob(os.path.join(QUIZ, "lesson%s_quiz.html" % nn))
    demos = [d for d in glob.glob(os.path.join(DEMO, "lesson%s_*.html" % nn))]
    nbs  = glob.glob(os.path.join(NB, "lesson%s_*.ipynb" % nn))

    # copy assets into site_src
    for s in svgs: shutil.copy(s, S_ASSETS)
    for q in quiz: shutil.copy(q, S_QUIZ)
    for d in demos: shutil.copy(d, S_DEMO)

    # SVG figures -> after "## 4. Visual Explanation"
    if svgs:
        figs = "\n\n".join(
            '<figure markdown>\n  ![%s](../assets/%s){ width="680" }\n</figure>' %
            (title, os.path.basename(s)) for s in svgs)
        body, _ = inject_after_heading(body, r'^##\s+(?:\d+\.\s+)?Visual Explanation\s*$', figs)

    # demo iframe -> after "## 7. Interactive Demonstration"
    if demos:
        d = os.path.basename(sorted(demos)[0])
        iframe = ('<iframe src="../../demos/%s" title="%s interactive demo" '
                  'style="width:100%%;height:520px;border:1px solid #e2e8f0;border-radius:12px"></iframe>\n\n'
                  '[Open this demo in a new tab \u2197](../demos/%s)'
                  % (d, title, d))
        body, _ = inject_after_heading(body, r'^##\s+(?:\d+\.\s+)?Interactive Demonstration\s*$', iframe)

    # notebook tip -> after "## 8. Coding Exercise"
    if nbs:
        nbname = os.path.basename(sorted(nbs)[0])
        tip = ('!!! tip "Run the hands-on notebook"\n'
               '    `modules/module01/notebooks/%s` — open in JupyterLab and run **Kernel → Restart & Run All**.' % nbname)
        body, _ = inject_after_heading(body, r'^##\s+(?:\d+\.\s+)?Coding Exercise\s*$', tip)

    # quiz iframe -> after "## 9. Knowledge Check"
    if quiz:
        q = os.path.basename(quiz[0])
        iframe = ('Formative — unlimited attempts, immediate feedback; does not affect your grade.\n\n'
                  '<iframe src="../../quizzes/%s" title="%s knowledge check" '
                  'style="width:100%%;height:720px;border:1px solid #e2e8f0;border-radius:12px"></iframe>\n\n'
                  '[Open this quiz in a new tab \u2197](../quizzes/%s)'
                  % (q, title, q))
        body, _ = inject_after_heading(body, r'^##\s+(?:\d+\.\s+)?Knowledge Check\s*$', iframe)

    out = os.path.join(SITE, "lesson%s.md" % nn)
    published = bool(svgs or quiz or demos)

    # strip authoring scaffolding so the STUDENT page shows only figure + real prose/Mermaid
    body = re.sub(r'^`\[Visual:.*?`\s*\n', '', body, flags=re.M)                 # [Visual: ...] placeholder
    body = re.sub(r'\*\*Rendered assets?:?\*\*.*?\n\n', '', body, flags=re.S)    # maintainer "Rendered asset(s)" note
    body = re.sub(r'\*\*Diagram Specification\*\*.*?(?=\n## )', '', body, flags=re.S)  # production spec (incl. Animation Notes)
    body = re.sub(r'\n{3,}', '\n\n', body)                                       # tidy blank lines

    if published:
        open(out, "w").write(body)
    else:
        # don't publish text-only (assets pending) — avoids orphan pages under --strict
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
    rows = []
    for f in lesson_files():
        num, title, nn, feats = build(f)
        rows.append((num, nn, title, feats))
        print(f"  {num:4s} (lesson{nn}) {title:32s} [{feats}]")
    print("\nDone. %d pages generated." % len(rows))
