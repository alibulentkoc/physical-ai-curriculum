---
title: Production Standards
status: production contract (authority for all lesson production)
authority: D-022 (Claude owns asset production), D-015 (assessment), D-019 (notebook pipeline)
---

# Production Standards

> The production contract for the entire curriculum. Every produced lesson must meet the **Definition of Done** below. This document governs lessons, diagrams, notebooks, quizzes, accessibility, MkDocs, and the demo policy.

## 1. Definition of Done (per lesson)

A lesson is "done" only when **all** of these exist, are in-repo, and render:

- [ ] **Lesson markdown** with YAML frontmatter, all 12 template sections, greenhouse narrative.
- [ ] **At least one SVG diagram** in `assets/diagrams/`, namespaced `mNN-lN-slug.svg`, embedded in §4.
- [ ] **Notebook** in `modules/moduleNN/notebooks/`, runnable end-to-end (Restart & Run All), with a self-check cell.
- [ ] **Quiz** as an interactive HTML widget (formative; immediate feedback; unlimited attempts) + an **answer key/rubric in `coaches/`**.
- [ ] **MkDocs page** in `site_src/`, in the nav, embedding the SVG(s), the quiz, and a link to the notebook.
- [ ] **MkDocs build passes** `mkdocs build --strict`.
- [ ] **Accessibility:** alt text / ARIA labels on all visuals; keyboard-operable interactives.
- [ ] Optional: **Mermaid** diagram where a flow/structure reads better as a graph; **interactive HTML demo** only where manipulation clearly improves learning.

## 2. SVG standards

- Format: hand-authored SVG (vector), not raster. `viewBox` set; no fixed pixel `width`/`height` on the root (scales responsively).
- Colours from the design system palette only (`assets/design-system/colors.md`).
- Typography per `assets/design-system/typography.md` (system sans-serif; title ~18px, label ~15px, caption ~12px).
- Every SVG has a `role="img"` and an `aria-label` (or `<title>`) describing it.
- Namespacing: `mNN-lN-slug.svg`. One concept per diagram.
- Must read clearly at ~320px wide (inline) and full width.

## 3. Diagram conventions

- Lead with the physical idea; label every meaningful element.
- Stage/role colours are consistent curriculum-wide (see `assets/design-system/diagram_standards.md`): perceive = blue, reason = violet, act = green; correct = green, error = red; ink = slate-900, muted = slate-500.
- Arrows: solid for primary flow, dashed for feedback/return.
- Never rely on colour alone — always pair with a label.

## 4. Notebook standards

- Jupyter `.ipynb`, Python 3.12+, stack limited to NumPy / Matplotlib / SymPy (Module 1).
- Passes **Restart & Run All** with no hidden state; deterministic (`np.random.default_rng(seed)`).
- Structure mirrors the lesson: intro → demonstration (§7) → coding exercise (§8, marked `# YOUR CODE HERE`) → **self-check** cell (asserts) ending in a clear pass message.
- Plots label axes with quantity and unit; equal aspect where geometry matters.
- Greenhouse framing in examples; comments explain the *why*.

## 5. Quiz standards

- The canonical quiz artifact is an **interactive HTML widget** (`modules/moduleNN/quizzes/lessonNN_quiz.html`): multiple-choice / true-false give instant correct/incorrect feedback with a short explanation; matching is checkable; open questions reveal a model answer for self-assessment.
- Formative only (D-015): unlimited attempts, immediate feedback, nothing stored, not graded.
- **Answer key + challenge-problem rubric live in `coaches/answer-keys/moduleNN/`** — never in the learner-facing folders. (Formative in-widget feedback is expected; *graded* keys stay in `coaches/`.)
- Self-contained: no external dependencies, no `localStorage`/`sessionStorage`.

## 6. Accessibility requirements

- All SVGs: `role="img"` + `aria-label`/`<title>`.
- All interactive HTML: keyboard-operable (focusable controls, arrow-key support where dragging exists), `aria-live` on dynamic readouts, visible focus, colour never the sole signal.
- Lesson prose: meaningful headings in order; link text is descriptive.

## 7. MkDocs validation requirements

- Page added to `nav` in `mkdocs.yml`.
- Site builds with `mkdocs build --strict` (no warnings/errors).
- Embedded assets verified present in the built `site/` output (SVG served, quiz/demo iframes load).
- Math via `pymdownx.arithmatex` (MathJax); Mermaid via the superfences custom fence.

## 8. Demo policy

- **SVG: always.** Every lesson ships at least one.
- **Mermaid: when a flow/sequence/tree is clearer as a graph** (e.g. pipelines, taxonomies).
- **Interactive HTML demo: only when manipulation clearly improves learning** — e.g. dragging a vector, adjusting bias/scatter, moving a target. Do **not** force a demo onto a lesson where it adds little; an SVG + interactive quiz is a complete experience.

## 9. Single-source note (site_src)

`site_src/` is the presentation layer; `modules/` holds authoring sources. For Unit 1, pages are authored directly. Before large-scale scaling, adopt a single-source mechanism (MkDocs `pymdownx.snippets` include or a sync script) so the site and source lessons cannot drift. (Open architect decision.)
