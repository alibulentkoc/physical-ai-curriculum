# Contributing to the Physical AI Curriculum

Thank you for your interest in improving this curriculum! This project is built collaboratively, and contributions of all kinds are welcome — lessons, code, diagrams, corrections, and ideas.

Please read this guide before opening an issue or pull request.

---

## Ways to contribute

- **Content** — write or improve lessons, worked examples, exercises, or challenge problems
- **Code** — Jupyter notebooks, interactive demos, simulation and digital-twin scaffolding
- **Visuals** — diagrams, animations, storyboards, and figures for `assets/`
- **Coaching material** — instructor guides, rubrics, AI-tutor prompts for `coaches/`
- **Fixes** — typos, broken links, math errors, clearer explanations
- **Ideas** — open an issue to propose new topics, restructurings, or improvements

## Before you start

1. **Open an issue first** for anything substantial (a new lesson, a structural change). This avoids duplicated effort and lets us agree on scope.
2. **Check [`TODO.md`](TODO.md)** to see what is planned and what is in progress.
3. **Respect the build order.** Content is authored module by module. Please don't submit Module 5 lessons before the Module 1 foundation exists, unless coordinated through an issue.

## Authoring guidelines

### Follow the educational philosophy

Every topic should move through the five layers in order: **physical intuition → visual understanding → mathematical formulation → computational implementation → system integration.** Lead with *why it matters*, not with equations.

### Follow the standard topic template

Every topic must include all 12 sections, in this order:

1. Why This Matters
2. Physical Intuition
3. Mathematical Foundations
4. Visual Explanation
5. Engineering Example
6. Worked Example
7. Interactive Demonstration
8. Coding Exercise
9. Knowledge Check
10. Challenge Problem
11. Common Mistakes
12. Key Takeaways

If a section genuinely doesn't apply, keep the heading and explain why rather than dropping it.

### Tie back to the Greenhouse Harvesting Robot

The curriculum's power comes from one continuous example. Where possible, frame examples in terms of the harvesting robot — perceiving fruit, transforming frames, reaching a target, planning motion, and so on.

## Style conventions

### Writing
- Write for an engineering student who is smart but new to the topic.
- Prefer plain language; define jargon on first use.
- Keep notation consistent across modules (see the glossary in `docs/` once available).

### Files and naming
- Markdown lessons: `kebab-case.md` (e.g. `pinhole-camera-model.md`).
- Notebooks: `kebab-case.ipynb`, runnable top to bottom with no hidden state.
- Assets: namespace by module, e.g. `m04-dh-frames.svg`.
- Prefer **SVG** for diagrams so they stay scalable and editable.

### Math
- Use LaTeX in Markdown (`$...$` inline, `$$...$$` display).
- State conventions explicitly (e.g. right-handed frames, column vectors, radians) to avoid sign-convention confusion.

### Code
- Notebooks and demos should run with a clearly stated environment.
- Comment the *why*, not just the *what*.
- Keep solutions out of learner-facing folders — answer keys belong in `coaches/`.

## Pull request process

1. **Fork** the repository and create a descriptive branch (e.g. `m03-add-projection-lesson`).
2. **Make focused changes** — one logical change per pull request.
3. **Check your work** — notebooks run cleanly, links work, math renders.
4. **Describe your change** in the PR: what, why, and which module/topic it touches.
5. **Link the related issue** if there is one.
6. A maintainer will review; please be responsive to feedback.

## Commit messages

Use clear, present-tense messages, ideally prefixed with the area touched:

```
docs: add notation glossary
m01: draft worked example for matrix multiplication
assets: add SE(3) frame diagram
fix: correct DH alpha sign in module 4 intro
```

## Code of conduct

Be respectful, constructive, and welcoming. Assume good faith, critique ideas rather than people, and help newcomers. Harassment or disrespect of any kind is not tolerated.

## License of contributions

By contributing, you agree that your contributions are licensed under the project's [MIT License](LICENSE).

---

Questions? Open an issue and start a conversation. Thank you for helping build this!
