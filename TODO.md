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
  - [~] Lessons — 66 planned (D-014). **Pilot 1.1 drafted** ✅, awaiting architect review; then unit-by-unit (D-016)
  - [ ] Notebooks — blocked on lessons
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

➡️ Pilot lesson **1.1 Physical AI and the Physical World** is drafted (~2,100 words) and awaiting architect review. On approval, the 12-part format is locked and Unit 1 (lessons 1.2–1.6) is authored, reviewed, then the curriculum proceeds unit-by-unit (D-016). Gemini is greenlit to draft storyboard briefs for Units 2–4 in parallel.

> Do **not** generate further lessons until the pilot format is approved.
