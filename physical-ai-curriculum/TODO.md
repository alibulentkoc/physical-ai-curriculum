# TODO — Physical AI Curriculum

Build plan and status tracker for the curriculum. Work proceeds **foundation → architecture → content → integration**, one module at a time.

Legend: `[x]` done · `[~]` in progress · `[ ]` not started

---

## Phase 0 — Repository foundation ✅

- [x] Create directory structure (`docs/`, `curriculum/`, `modules/`, `assets/`, `coaches/`, `projects/`)
- [x] Placeholder `README.md` in every directory
- [x] Top-level `README.md`
- [x] `CONTRIBUTING.md`
- [x] `LICENSE` (MIT)
- [x] `TODO.md`

## Phase 1 — Curriculum architecture (current focus)

- [x] **`curriculum/module01_manifest.md`** — Module 1 manifest ✅
- [x] `curriculum/ARCHITECT_DECISIONS.md` — source-of-truth decisions log ✅
- [x] `curriculum/learning_philosophy.md` ✅
- [x] `curriculum/assessment_strategy.md` ✅ (finalized · D-015)
- [x] `curriculum/mathematical_prerequisites.md` ✅
- [x] `curriculum/software_environment.md` ✅
- [x] `curriculum/roadmap.md` (master roadmap) ✅
- [x] `curriculum/notebook_strategy.md` ✅ (per-unit pipeline, D-019)
- [ ] Manifests for Modules 2–10
- [ ] Notation & symbol glossary in `docs/`
- [ ] Authoring/style guide in `docs/`
- [ ] Define standard lesson file layout per module

## Phase 2 — Module content

Content for each module is authored only after its manifest exists. Each module includes lessons, notebooks, demos, and exercises, with every topic following the 12-part template.

- [~] Module 01 — Mathematical Foundations *(scaffolding done; lessons pending topic-granularity decision)*
  - [x] `modules/module01/README.md`
  - [x] `modules/module01/learning_objectives.md`
  - [x] `modules/module01/topic_map.md`
  - [x] `modules/module01/assessments.md`
  - [x] `lessons/`, `notebooks/`, `assets/` directories (empty, .gitkeep)
  - [~] Lessons — 66 planned (D-014). **Units 1–2 complete** (1.1–1.6, 2.1–2.9) ✅; template at `templates/lesson_template.md`. Units 3–9 pending.
  - [ ] Notebooks — per-unit pipeline (D-019); `notebook_strategy.md` ✅. Unit 1–2 notebooks pending generation.
  - [ ] Quizzes — blocked on lessons
- [ ] Module 02 — Spatial Transformations and SE(3)
- [ ] Module 03 — Camera Geometry and Robotic Perception
- [ ] Module 04 — Forward Kinematics using Denavit–Hartenberg Parameters
- [ ] Module 05 — Inverse Kinematics
- [ ] Module 06 — Jacobians and Differential Motion
- [ ] Module 07 — Trajectory Generation and Motion Planning
- [ ] Module 08 — Robot Communication, Embedded Systems, and Control
- [ ] Module 09 — Physical AI System Integration
- [ ] Module 10 — Digital Twin Capstone Project

## Phase 3 — Visual assets

- [ ] Diagram style guide & palette in `assets/branding/`
- [ ] Per-module diagrams (`assets/diagrams/`)
- [ ] Animation storyboards (`assets/storyboards/`)
- [ ] Rendered animations (`assets/animations/`)

## Phase 4 — Coaching & assessment

- [ ] Instructor guides per module (`coaches/instructor-guides/`)
- [ ] AI tutor prompts/personas (`coaches/ai-coach/`)
- [ ] Rubrics & mastery criteria (`coaches/rubrics/`)
- [ ] Answer keys (`coaches/answer-keys/`)

## Phase 5 — Projects & capstone

- [ ] Greenhouse robot integration scaffolding (`projects/greenhouse-robot/`)
- [ ] Starter kits (`projects/starter-kits/`)
- [ ] Digital Twin capstone brief & milestones (`projects/capstone/`)

---

## Immediate next step

🔧 **MODULE 3 IN PRODUCTION** — *Camera Geometry and Robotic Perception*.

**Installment A COMPLETE (Units 1–2, lessons 01–08):** 8 lessons, 8 SVGs, 8 notebooks (execute clean), 8 quizzes, 8 answer keys, 1 demo (perspective projection). `mkdocs build --strict` passes; all embeds + "You are here" headers resolve. Manifest `curriculum/module03_manifest.md`; topic map `modules/module03/topic_map.md`; tracker `curriculum/master_progress.md`.

**Installment B COMPLETE (Units 3–4, lessons 09–16):** 8 lessons, 8 SVGs, 8 notebooks (execute clean; OpenCV cross-check vs NumPy ground truth), 8 quizzes, 8 answer keys, 1 demo (full projection pipeline, lesson13), midpoint assessment + key, and `modules/module03/software_environment_module3.md` (OpenCV introduction; graceful-degradation notebook policy). `mkdocs build --strict` passes; all embeds + "You are here" headers resolve. **Module 3 midpoint reached** — forward map world→pixel complete and OpenCV-verified. (D-046)

**Installment C COMPLETE (Units 5–6, lessons 17–24):** 8 lessons, 8 SVGs (m03-l17..l24), 8 notebooks (execute clean; fixed a NumPy in-place aliasing bug in the 5.4 undistortion round-trip), 8 quizzes, 8 answer keys, 1 demo (back-projection ray, lesson21). `mkdocs build --strict` passes; all embeds + "You are here" headers resolve. Lens distortion (radial k1,k2,k3 + tangential p1,p2, before K) + undistortion (iterative) and back-projection (pixel→ray via K⁻¹, +depth → camera-frame point) complete. (D-047)

**Installment D COMPLETE (Units 7–8, lessons 25–32):** 8 lessons, 8 SVGs (m03-l25..l32), 8 notebooks (execute clean), 8 quizzes, 8 answer keys, flagship capstone demo (lesson29 See the Fruit, Place It in the World). `mkdocs build --strict` passes (101 pages); all embeds + "You are here" resolve. Unit 7 connects perception to Module 2 extrinsics; Unit 8 assembles/verifies/visualizes the full pixel→world pipeline (canonical P_w=(1.06,0.47,0.4)). (D-048)

**MODULE 3 COMPLETE.** 32 lessons / 32 notebooks / 32 SVGs / 32 quizzes / 4 demos / 32 answer keys / midpoint + Unit-8 capstone. Completion report: `curriculum/module03_completion_report.md`. Totals now M1+M2+M3 = 101/101/102/22/101/102.

**Module 4 LAUNCHED — Installment A (Units 1–2, lessons 01–08) COMPLETE.** Manifest, topic map (8 units × 4), scaffold, generator wiring (MODULES+="04", titles, nav) done. 8 lessons, 8 SVGs (m04-l1..l8), 8 notebooks (execute clean), 1 demo (lesson05 one-joint arm), 8 quizzes, 8 answer keys. `mkdocs build --strict` passes (109 pages). Unit 1 = Why Kinematics (FK: θ → pose = T(world←arm); links/joints/DOF; config vs pose, many-to-one). Unit 2 = One Joint at a Time (T_0^1(θ); joint transform; pose extraction; FK = product). (D-049)

**Module 4 Installment B (Units 3–4, lessons 09–16) COMPLETE — midpoint reached.** 8 lessons, 8 SVGs (m04-l9..l16), 8 notebooks (execute clean, incl. SymPy symbolic FK), 1 demo (lesson09 two-link arm), midpoint assessment + key, 8 quizzes, 8 answer keys. Nav added; generated (117 pages); `mkdocs build --strict` passes; site cleared. Unit 3 = Chaining Transforms (2-/3-link, accumulated angles, matrix product = Module 2 composition). Unit 4 = General T_0^n(θ) + position/orientation + FK in code (NumPy + SymPy) + midpoint. (D-050)

**Module 4 Installment C (Units 5–6, lessons 17–24) COMPLETE.** 8 lessons, 8 SVGs (m04-l17..l24), 8 notebooks (execute clean, incl. symbolic DH FK via SymPy), 1 demo (lesson18 DH parameter explorer), 8 quizzes, 8 answer keys. Nav added; generated (125 pages); `mkdocs build --strict` passes (clean); site cleared. Unit 5 = Denavit–Hartenberg Parameters (why a convention; the four params θ,d,a,α; assigning frames; recap). Unit 6 = Building and Using a DH Table (DH link transform; reading a robot into a table — 3-DOF capstone arm; DH FK in code; recap). (D-051)

**✅ MODULE 4 COMPLETE (D-052).** Installment D (Units 7–8, lessons 25–32) done: 8 lessons, 8 SVGs (m04-l25..l32), 8 notebooks (execute clean; 5-check FK verification suite + SymPy), flagship capstone demo (lesson29 From Joints to the Fruit), 8 quizzes, 8 answer keys. Nav added; generated (133 pages); `mkdocs build --strict` passes (clean); site cleared; completion report at curriculum/module04_completion_report.md.

**Module 4 totals:** 32 lessons / 32 notebooks / 32 SVGs / 4 demos (lesson05, lesson09, lesson18, lesson29) / 32 quizzes / 32 answer keys / midpoint + capstone. Forward kinematics only; IK deferred to M5.

**Curriculum totals after M4:** 4 of 10 modules · 133 lessons · 133 notebooks · 134 SVGs · 26 demos · 133 quizzes · 134 answer keys · 7 assessments.

**PAUSE — Module 4 completion checkpoint per standing directive.** Next: Module 5 — Inverse Kinematics (awaiting architect launch decision: scope, unit breakdown, sequencing). M5 inverts the forward map T_0^n(θ) built in M4.

---
_(superseded note kept for history)_
**Next: Module 4 Installment D — Units 7–8 (lessons 25–32) — FINAL installment.** Unit 7 Pose, Workspace, and Back to Perception (reading the end-effector pose; the reachable workspace; closing the loop with perception T_0^n = T(world←arm), reconnect to M3 pipeline; recap). Unit 8 Mini Project: From Joints to the Fruit (the project; building the arm's DH model; verifying the FK; wrap-up + road to inverse kinematics — flagship capstone demo, place a perceived fruit target in the arm's frame, points to Module 5). Then Module 4 COMPLETION: completion report, totals (4 of 10 / 133 lessons), rebuild zip, present_files, short report, PAUSE.

---
_(superseded note kept for history)_
**Next: Module 4 Installment C — Units 5–6 (lessons 17–24).** Unit 5 Denavit–Hartenberg Parameters (why a convention; the four params θ,d,a,α; assigning frames; standard/distal convention). Unit 6 Building and Using a DH Table (DH link transform from 4 params; reading a robot into a table; DH FK in code, SymPy for symbolic DH). Then D (Units 7–8: pose/workspace/back-to-perception 25–28; capstone From Joints to the Fruit 29–32). Pause at Module 4 completion (completion report, rebuild zip, present_files, short report).

---
_(superseded note kept for history)_
**Next: Module 4 Installment B — Units 3–4 (lessons 09–16, includes midpoint).** Unit 3 Chaining Transforms (two/three links, Module 2 composition, planar 2-link worked example). Unit 4 The Forward Kinematics Map T_0^n(θ) (general chain, position+orientation, FK in code) + write assessments/module04_midpoint_assessment.md + key. Then C (Units 5–6 DH parameters, 17–24), D (Units 7–8 capstone, 25–32). Pause at Module 4 completion.

---
_(superseded note kept for history)_
**Next: Module 4 — Forward Kinematics using Denavit–Hartenberg Parameters.** Create manifest (`curriculum/module04_manifest.md`), topic map (`modules/module04/topic_map.md`), scaffold dirs, `coaches/answer-keys/module04/`; lessons/notebooks/quizzes/answer-keys/SVGs/demos per standards. Wire generator: MODULES += "04", MODULE_TITLES["04"], UNIT_TITLES for M4 units, manual nav. Numbering restarts (module04/lesson01…, m04-l01…, M04_U0Y_*). Kinematics now permitted. M4 computes T(world←arm) — the transform M3 assumed. Pause at Module 4 completion.

> Workflow: edit canonical lessons → `python3 tools/generate_site_pages.py` → `mkdocs build --strict`. Pause only at unit/module/milestone completion or for the 5 escalation reasons.

