---
title: Master Progress Tracker
purpose: Single-glance status of curriculum production across all modules.
authority: Updated continuously during production; ARCHITECT_DECISIONS.md remains the decision record.
---

# Master Progress Tracker

_Last updated: Module 3 Installment B (Units 3–4) complete; module midpoint reached._

## Module status

| # | Module | Status | Lessons | Notebooks | SVGs | Demos | Quizzes | Answer keys | Assessments |
|---|--------|--------|--------:|----------:|-----:|------:|--------:|------------:|-------------|
| 01 | Mathematical Foundations | ✅ COMPLETE | 33 | 33 | 34 | 12 | 33 | 34 | midpoint + module (2) |
| 02 | Spatial Transformations and SE(3) | ✅ COMPLETE | 36 | 36 | 36 | 6 | 36 | 36 | midpoint + key (2) |
| 03 | Camera Geometry and Robotic Perception | ✅ COMPLETE | 32 | 32 | 32 | 4 | 32 | 32 | midpoint + capstone ✓|
| 04 | Forward Kinematics (DH parameters) | ⬜ planned | — | — | — | — | — | — | — |
| 05 | Inverse Kinematics | ⬜ planned | — | — | — | — | — | — | — |
| 06 | Jacobians and Differential Motion | ⬜ planned | — | — | — | — | — | — | — |
| 07 | Trajectory Generation and Motion Planning | ⬜ planned | — | — | — | — | — | — | — |
| 08 | Control and Actuation (ROS 2) | ⬜ planned | — | — | — | — | — | — | — |
| 09 | System Integration | ⬜ planned | — | — | — | — | — | — | — |
| 10 | Digital Twin Capstone | ⬜ planned | — | — | — | — | — | — | — |

## Totals (completed modules)

- **Modules complete:** 3 of 10
- **Lessons:** 101
- **Notebooks:** 101
- **SVGs:** 102
- **Demos:** 22
- **Quizzes:** 101
- **Answer keys:** 102
- **Assessments:** 6 (midpoint + capstone/module per module)

## In production

- _(none — Module 3 complete; Module 4 next.)_

<!-- Module 3 (now complete): -->
- **Module 3 — Camera Geometry and Robotic Perception.** Scope (per roadmap D-004): how a camera turns the world into pixels and back; perceive fruit and estimate its position. Absorbs the perception stack deferred from Module 2 (intrinsics, projection, image formation). OpenCV enters here. Feeds the Module 2 extrinsics chain to place a detection in the world.

## Deferred / parked

- **Asset-hardening audit** (post-production): SVG embedding, HTML demo consistency, nav labels, notebook naming, page-header consistency — tracked in `curriculum/future_roadmap.md`.

## Conventions (stable)

- Generator: `tools/generate_site_pages.py`; `MODULES` list drives which modules build. Gate: `mkdocs build --strict`.
- Per module MM: lessons `modules/moduleMM/lessons/lessonNN_*.md`; diagrams `assets/diagrams/mMM-lNN-*.svg`; notebooks `MMM_UUU_L*_*.ipynb`; quizzes/demos `lessonNN_*`; answer keys `coaches/answer-keys/moduleMM/`.
- Five-layer pedagogy; greenhouse-harvesting-robot narrative; AI Learning Companion + Global Learning Support on every lesson.
