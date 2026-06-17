---
title: Module 2 — Completion Report
module: 02
status: COMPLETE
units: 8
lessons: 36
---

# Module 2 — "Spatial Transformations and SE(3)" — Completion Report

## Status: COMPLETE

Module 2 teaches how spatial transformations are represented and composed — homogeneous coordinates, rigid-body transforms, SE(2), SE(3), composition, pose, and camera-to-robot reasoning — culminating in a perception-to-pose capstone. It deliberately stops short of full kinematics and camera intrinsics (both deferred to Module 3).

## Deliverables (census)

| Asset | Count |
|---|---|
| Lessons (canonical + generated pages) | 36 |
| Diagrams (SVG, `m02-l*`) | 36 |
| Notebooks (`M02_UYY_*`, all execute "All checks passed.") | 36 |
| Quizzes (`lessonNN_quiz.html`) | 36 |
| Answer keys (`coaches/answer-keys/module02/`) | 36 + midpoint key |
| Interactive demos | 6 |
| Midpoint assessment (+ coaches' key) | after Unit 5 |

## Unit-by-unit

1. **Why Transformations Matter** (1.1–1.4, lesson01–04) — the robot's constant problem; position+orientation = pose; the Module-1 limit (2×2 can't translate); recap.
2. **Homogeneous Coordinates** (2.1–2.5, lesson05–09) — one extra coordinate; points (w=1) vs directions (w=0); translation as a matrix; rotation+translation block form; recap. *Demo: translation-as-a-matrix.*
3. **SE(2) Transformations** (3.1–3.5, lesson10–14) — what "rigid" means; the SE(2) 3×3 matrix; applying it; inverse transformations (geometric); recap. *Demo: SE(2) playground (with inverse).*
4. **SE(3) Transformations** (4.1–4.6, lesson15–20) — 2D→3D; 3D rotation (axis+angle, Rx/Ry/Rz); the SE(3) 4×4; 3D translation vectors; applying SE(3) + inverses; recap. Faux-3D isometric diagrams (no WebGL). *Demo: SE(3) viewer.*
5. **Transformation Composition** (5.1–5.4, lesson21–24) — chaining (product, right-to-left); order matters (non-commutativity); frames as a graph (compose along path, invert backward edges); recap. *Demo: composition chain (order toggle).* **Midpoint checkpoint placed here.**
6. **Robot Pose Representation** (6.1–6.4, lesson25–28) — what a pose is; a pose is a transformation; reading/writing/updating poses; recap. *Demo: pose explorer.*
7. **Camera-to-Robot Transformations** (7.1–7.4, lesson29–32) — the camera sees its own world; camera extrinsics (the camera's pose); building the transformation chain; recap. **Extrinsics only** — intrinsics/projection deferred to Module 3.
8. **Mini Project: Perception-to-Pose Pipeline** (8.1–8.4, lesson33–36) — the capstone. From detection to reach; building the pipeline; verifying and visualizing; wrap-up and the road to kinematics. *Flagship demo: perception-to-pose (with verification view).*

## The capstone

The mini project integrates every Module 2 idea into one question — **"how does a detected object become a robot pose?"** — answered by:

$$T_{\text{world}\leftarrow\text{tomato}} = T_{\text{world}\leftarrow\text{arm}}\;T_{\text{arm}\leftarrow\text{cam}}\;T_{\text{cam}\leftarrow\text{tomato}}.$$

Students build it in code, **verify** it (inverse round-trip recovers the detection; rigidity/distance preserved; valid-pose checks), and **visualize** the frames and target. The flagship demo shows the composed target and the verification live.

## Standards upheld

- Intuition-first: no lesson opens with matrix algebra; every unit leads with a physical scenario.
- Greenhouse-robot narrative throughout.
- Each notebook carries a Module/Unit/Lesson identity header and ends in "All checks passed."
- Every lesson has the AI Learning Companion and Global Learning Support sections (EN authoritative + ES/中文/TR prompts).
- Manual Module→Unit→Lesson nav; "You are here" context header on every page; single-source generator + validator; `mkdocs build --strict` PASS.

## Assessment structure

- Per-lesson formative Knowledge Checks (25%), Coding exercises (40%), Challenge problems (15%), Mini Project (20%) — weights consistent with Module 1.
- Midpoint readiness checkpoint after Unit 5 (composition); the Unit 8 mini project is the module assessment centerpiece.

## Through-line

Module 1 (coordinate frames, matrices as transformations) → Module 2 (homogeneous coords → SE(2) → SE(3) → composition → pose → extrinsics → pipeline) → **Module 3** (kinematics; camera intrinsics/projection/perception).

## Deferred (by design, to Module 3)

Camera intrinsics, projection models, image formation, and computer-vision mathematics; full forward/inverse kinematics. A separate **asset-hardening audit** (SVG embedding, HTML demo consistency, nav labels, notebook naming, page-header consistency) is parked in `curriculum/future_roadmap.md` for after all modules are drafted.

## Build state

`python3 tools/generate_site_pages.py` then `mkdocs build --strict` → **PASS**. All 36 Module 2 pages render with their diagram, notebook link, quiz, and (where present) demo; all embeds and "You are here" headers resolve; all notebooks execute clean; all quiz/demo JS validates.
