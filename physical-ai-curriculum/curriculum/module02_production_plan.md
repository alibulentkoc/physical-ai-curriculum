---
title: Module 2 — Production Plan (Roadmap, Demos, Assets, Risks)
module: 02
status: proposed (no lessons generated yet)
---

# Module 2 — Production Plan

Covers the production roadmap, demo roadmap, asset roadmap, and risks/recommendations. Lesson generation begins only after architect review of this plan and the manifest/topic map.

## 1. Production roadmap (installments)

Produced unit by unit, intuition-first, with a **pause for architect review between installments** (the cadence that worked in Module 1). Each lesson ships complete: lesson + SVG + notebook + quiz + answer key + the two standard sections; demos where they add the most.

| Installment | Units | Why grouped | Gate |
|---|---|---|---|
| **A** | Unit 1 (Why Transformations Matter) + Unit 2 (Homogeneous Coordinates) | Motivation + the key device that unlocks everything; lead with physical movement, then introduce the extra coordinate | Review before SE(2)/SE(3) |
| **B** | Unit 3 (SE(2)) + Unit 4 (SE(3)) | Rigid motion in 2D then 3D, with inverses; the representational core | Midpoint checkpoint + review |
| **C** | Unit 5 (Composition) + Unit 6 (Pose) | Chaining and pose representation build directly on B | Review |
| **D** | Unit 7 (Camera-to-Robot) + Unit 8 (Mini Project) | Applied chain + integrative capstone; module assessment | Module completion review → bridge to kinematics |

Within each installment, lead with the intuition/visual lessons before the formal ones (e.g. in Unit 2: "one extra coordinate" and "translation as a matrix" before composing rotation+translation).

## 2. Demo roadmap

Same engineering standard as Module 1: self-contained HTML + vanilla JS + inline SVG; no dependencies; no browser storage; keyboard-operable; `aria-live` readouts; design-system colors; iframe-embedded with a validated fallback link. Each transform demo should display the **matrix currently applied** beside the geometry.

Proposed demos (required ones marked ★):

- ★ **2.3 Translation-as-a-matrix** — toggle between "2×2 can't translate" and the homogeneous 3×3 that can; drag a translation and watch the matrix and the point move together. *(The "aha" of the module.)*
- ★ **3.x SE(2) playground** — sliders for rotation θ and translation (tx, ty); apply to a shape; show the 3×3 matrix; include an **inverse** button that sends the shape back. 
- ★ **4.x SE(3) viewer (faux-3D)** — isometric scene; rotate about an axis and translate in 3D; show the 4×4 matrix; emphasize rigid motion (size/shape preserved).
- ★ **5.x Composition chain** — chain two/three SE(2) (or SE(3)) transforms; reorder them; show the combined matrix and that order matters (callback to Module 1's 4.8).
- **6.x Pose explorer** — place a robot pose (position + heading) in the world; read it as a transform; move the robot and watch the pose/matrix update.
- ★ **8.x Perception-to-pose pipeline (flagship)** — the mini project visualized: a tomato in the camera frame flows camera→robot→world via composed SE(3) transforms; all frames and the resulting world pose shown; drag the robot/camera to see the chain update. *Flagship Module 2 demo.*

(Five ★ required demos; pose explorer optional-but-recommended. Final per-unit demo decisions confirmed at installment time, as in Module 1.)

## 3. Asset roadmap

- **SVGs** (`assets/diagrams/m02-lNN-*.svg`): geometry-first; reuse Module 1's conventions (ghost-original + transformed, legend layouts for multi-item scenes, faux-3D isometric for 3D). Expect ~1–2 per lesson; SE(3) lessons likely 2 (a 3D scene + a matrix-anatomy panel).
- **Notebooks** (`modules/module02/notebooks/lessonNN_*.ipynb`): NumPy; homogeneous coordinates as 3-vectors/4-vectors; SE(2)/SE(3) as 3×3/4×4 matrices; assert-based self-checks (rigid transforms preserve distances; inverse undoes; composition order). All execute headless to "All checks passed."
- **Quizzes** (`modules/module02/quizzes/lessonNN_quiz.html`): reuse the Module 1 quiz engine (copy an existing quiz, swap title + questions).
- **Answer keys** (`coaches/answer-keys/module02/`): per-lesson + checkpoints.
- **Generator:** extend `tools/generate_site_pages.py` to discover Module 2 (a second module root or a parameterized module list; asset prefix `m02-`; same anchor/injection logic and validated-fallback rules). MkDocs nav gains a Module 2 section. `mkdocs build --strict` remains the gate.
- **Design system / standards / i18n:** inherited unchanged; the two standard sections on every lesson.

## 4. Risks and recommendations

**Risks**
1. **Conceptual spike at homogeneous coordinates.** The extra coordinate is the module's hardest "why." *Mitigation:* dedicate Unit 1 to motivation and Unit 2 entirely to the device; lead with the translation-as-a-matrix demo before any 3×3 algebra.
2. **3D legibility without WebGL.** SE(3) is hard to show in static 2D. *Mitigation:* faux-3D isometric SVG + interactive 2.5D demos; keep one consistent 3D viewpoint; verify every diagram via PNG render (cairosvg) before shipping, watching the known gotchas (8-digit hex alpha → use `fill-opacity`; CSS class fills overriding inline → set contrasting fills inline).
3. **Scope creep into kinematics / camera intrinsics.** Tempting in Units 6–7. *Mitigation:* hold the stated boundaries (pose & extrinsics only; no joint kinematics, no projection); flag them as forward pointers, as Module 1 did with translation.
4. **Matrix-first drift.** Risk of opening lessons with algebra. *Mitigation:* enforce the five-layer flow in review; every lesson opens with movement/viewpoint, not a matrix.
5. **Generator multi-module support.** Extending the single-source generator could introduce path bugs. *Mitigation:* extend incrementally, keep the iframe-vs-markdown path rules and the resolve-check script; `--strict` + the embed-resolution check catch regressions.
6. **Workflow friction (zip/sync, stale cache).** Same as Module 1. *Recommendation:* strongly consider working directly in the repo (e.g. Claude Code) for Module 2 to retire the manual loop.

**Recommendations**
- Keep the **pause-for-review cadence** between installments; it was the main quality lever in Module 1.
- Produce a **per-unit recap** and the **midpoint checkpoint** as planned; they consolidate a representation-heavy module.
- Lead Module 2 with **Unit 1's physical re-grounding** before any homogeneous-coordinate math — this is the single most important pedagogical choice for the module.
- Reuse Module 1's **validated-fallback embedding** and **resolve-check** from day one so `--strict` guarantees every Module 2 asset path.

## 5. Status

**PLANNING complete; awaiting architect review.** No Module 2 lessons generated. On approval, begin **Installment A** (Unit 1 + Unit 2), leading with the physical-movement motivation and the translation-as-a-matrix demo.
