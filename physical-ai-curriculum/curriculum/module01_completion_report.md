---
title: Module 1 — Completion Report (Archival Record)
module: 01
title_full: Mathematical Foundations for Physical AI
status: COMPLETE — architect signed off
units: 4
theme: Greenhouse Harvesting Robot
---

# Module 1 — Completion Report

**Module 1: Mathematical Foundations for Physical AI** is production-complete and signed off by the Curriculum Architect. This report is the archival record: objectives achieved, full inventories, lessons learned, and recommendations carried into Module 2.

## 1. Module objectives achieved

A student completing Module 1 can:

- Describe **physical quantities** with correct units, dimensions, and an honest account of measurement error, accuracy, and precision.
- Reason with **vectors**: position, displacement, magnitude, direction, unit vectors, dot product, cross product, and distance — each tied to a robot decision.
- Understand **coordinate frames** and that a coordinate is meaningless without "relative to whom."
- Distinguish **local vs global** viewpoints and read the same point in world, robot, and camera frames.
- Interpret **robot and camera frames** as a perceive → act → remember chain.
- Understand **transformations geometrically** — identity, rotation, scaling, reflection — *before* algebra.
- Hold the core belief: **a matrix is an action applied to space, not a table of numbers**, and that **composition is ordered**.

The module's two signature insights landed:
- Unit 3: *the same point can have different coordinates — the tomato has not moved, only the observer changed.*
- Unit 4: *the same point can be transformed in different ways — and order matters.*

## 2. Lesson inventory (33 lessons)

**Unit 1 — Physical Quantities & Measurement (6):** 1.1 Physical AI and the Physical World · 1.2 Units and Dimensions · 1.3 Scalars and Physical Quantities · 1.4 Measurement Error · 1.5 Accuracy and Precision · 1.6 Engineering Estimation.

**Unit 2 — Vectors (10):** 2.1 What Is a Vector? · 2.2 Vector Representation · 2.3 Vector Addition · 2.4 Vector Subtraction · 2.5 Magnitude and Direction · 2.6 Unit Vectors · 2.7 Dot Product · 2.8 Cross Product · 2.9 Distance Between Points · 2.10 Vectors in Physical AI (recap).

**Unit 3 — Coordinate Systems & Reference Frames (8):** 3.1 Why Coordinate Frames Matter · 3.2 Cartesian Coordinates · 3.3 2D Coordinate Systems · 3.4 3D Coordinate Systems · 3.5 Local and Global Frames · 3.6 Conceptual Frame Transformations · 3.7 Robot and Camera Frames · 3.8 Coordinate Frames in Physical AI (recap).

**Unit 4 — Matrices as Transformations (9):** 4.1 Matrices as Operators · 4.2 Matrix Addition · 4.3 Matrix Multiplication · 4.4 The Identity Matrix · 4.5 Rotation Matrices · 4.6 Scaling Transformations · 4.7 Reflection Transformations · 4.8 Composition of Transformations · 4.9 Transformations in Physical AI (recap).

Each lesson follows the 12-section template with a `core_idea` field and the two standard sections (AI Learning Companion; Global Learning Support — English authoritative, with Español/中文/Türkçe prompts).

## 3. Asset inventory

- **Canonical lessons:** 33 Markdown files in `modules/module01/lessons/` (authoritative source; retain Diagram Specifications, hidden from student pages by the generator).
- **SVG diagrams:** 34 in `assets/diagrams/` (`m01-l1` … `m01-l33`; 1.1 has two), all validated as XML and visually checked via PNG render.
- **Site pages:** 33 generated into `site_src/module01/` by `tools/generate_site_pages.py` (single source of truth → no double maintenance).
- **Mermaid diagrams:** in canonical 1.1 (perception→action pipeline) and 1.4 (error taxonomy).

## 4. Demo inventory (12 interactive demos)

All self-contained HTML + vanilla JS + inline SVG; no dependencies, no browser storage; keyboard-operable; embedded via iframe with a validated "open in new tab" fallback.

1. 1.1 Trace-the-loop (perception→action)
2. 1.5 Accuracy vs precision (sliders)
3. 2.3 Vector addition (tip-to-tail)
4. 2.7 Dot product (alignment)
5. 2.8 Cross product (normal + area)
6. 3.5 Frame viewpoint switcher (world/robot/camera)
7. 3.6 Conceptual frame transform (offset + rotation)
8. 3.7 Tri-frame pick (flagship Unit 3)
9. 4.4 Identity = do nothing
10. 4.5 Rotation slider (0°→360°)
11. 4.6 Scaling sliders (uniform/non-uniform)
12. 4.8 Composition: order matters (flagship Unit 4)

## 5. Notebook inventory (33 notebooks)

One runnable Jupyter notebook per lesson in `modules/module01/notebooks/` (NumPy; Matplotlib where useful). Every notebook executes headless to **"All checks passed."** Each follows the pattern: worked code → a `# YOUR CODE HERE` exercise → assert-based self-check.

## 6. Assessment inventory

- **33 interactive quizzes** (`modules/module01/quizzes/`): formative, unlimited attempts, immediate feedback; question types MC/TF/match/short.
- **34 answer keys** (`coaches/answer-keys/module01/`): per-lesson keys + the midpoint assessment key with a readiness rubric. Kept in `coaches/`, never in learner folders.
- **Module 1 Midpoint Assessment** (`assessments/module01_midpoint_assessment.md`): readiness checkpoint between Unit 3 and Unit 4; no matrices; the readiness signal is whether a student can explain why one point has multiple correct coordinates.

## 7. Lessons learned

- **Single-source generation was the highest-leverage decision.** Authoring canonical lessons and generating site pages (injecting assets at section anchors, stripping authoring scaffolding) eliminated double-maintenance and let `--strict` validate every asset path.
- **Geometry/intuition first, formalism second** worked across units — especially Unit 3 (frames before transform math) and Unit 4 (actions before matrix arithmetic). The "pause for review" gate between installments kept quality high and prevented runaway scope.
- **Embedding pitfalls were real and now solved:** raw-HTML iframes resolve against the *output URL* (`../../demos/`), while Markdown fallback links resolve against the *source* (`../demos/`) and are MkDocs-rewritten; a validated fallback link under every embed makes `--strict` catch any broken path. Blank-line separation around injected blocks is required.
- **Rendering gotchas:** cairosvg does not honor 8-digit hex alpha (use `fill-opacity`); CSS classes in `<style>` override presentation attributes (set contrasting fills inline); dense single-scene diagrams fail — split into a clean scene + a legend.
- **Workflow friction** centered on the manual zip→sync loop and occasional stale/cached pages; the durable fix is working directly in the repo (e.g. Claude Code) rather than transferring archives.
- **Transient sandbox I/O errors** appeared a few times during builds/writes; they were one-off and cleared on retry (not content issues).

## 8. Recommendations for future modules

- **Keep the single-source generator and the `--strict` gate** as the build contract; extend the lesson-file glob/asset conventions per module (Module 1 used `lessonNN` / `m01-lNN`).
- **Continue the five-layer flow** (physical intuition → visual → math → computation → integration) and the two standard sections on every lesson.
- **Maintain recaps** at the end of each unit and a module-level assessment — they consolidate and create clean bridges.
- **Preserve the greenhouse-robot narrative** for continuity.
- **Honor stated boundaries explicitly** (e.g. Module 1 deferred homogeneous/translation matrices to Module 2); call them out in lessons as forward pointers.
- **For Module 2**, lead with physical movement and changing viewpoints before homogeneous-coordinate algebra, mirroring how Unit 4 led with geometry.

## 9. Numbering & conventions (for continuity)

- Module 1 files: `modules/module01/lessons/lessonNN_*.md` (NN 01–33); diagrams `m01-lNN-*.svg`; quizzes `lessonNN_quiz.html`; notebooks `lessonNN_*.ipynb`; demos `lessonNN_*.html`.
- Generator: `tools/generate_site_pages.py` (anchors accept optional section numbers; lesson-file glob `lesson[0-9][0-9]_*.md`).
- Governing docs: `curriculum/ARCHITECT_DECISIONS.md` (authoritative log), `curriculum/production_standards.md`, `assets/design-system/*`, `curriculum/internationalization_strategy.md`, `TODO.md`.

**Module 1: COMPLETE.** Next: Module 2 — Spatial Transformations and SE(3).
