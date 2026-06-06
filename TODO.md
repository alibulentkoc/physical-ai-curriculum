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

**Next: Installment C** — Unit 5 Lens Distortion (radial/tangential, undistortion) + Unit 6 Back-Projection (pixel = ray, add depth → 3D point). Keep OpenCV notebooks degrading gracefully (try/except cv2, NumPy ground truth).

Then Installment D (U7 From Pixels to the Robot + U8 Mini Project capstone + completion report).

> Workflow: edit canonical lessons → `python3 tools/generate_site_pages.py` → `mkdocs build --strict`. Pause only at unit/module/milestone completion or for the 5 escalation reasons.

