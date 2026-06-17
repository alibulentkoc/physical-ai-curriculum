---
title: Master Progress Tracker
purpose: Single-glance status of curriculum production across all modules.
authority: Updated continuously during production; ARCHITECT_DECISIONS.md remains the decision record.
---

# Master Progress Tracker

_Last updated: 2026-06 — Module 6 (Jacobians and Differential Motion) COMPLETE (32/32 lessons, Installments A–D; D-060). 6 of 10 modules done._

## Module status

| # | Module | Status | Lessons | Notebooks | SVGs | Demos | Quizzes | Answer keys | Assessments |
|---|--------|--------|--------:|----------:|-----:|------:|--------:|------------:|-------------|
| 01 | Mathematical Foundations | ✅ COMPLETE | 33 | 33 | 34 | 12 | 33 | 33 + midpoint key | midpoint |
| 02 | Spatial Transformations and SE(3) | ✅ COMPLETE | 36 | 36 | 36 | 6 | 36 | 36 + midpoint key | midpoint |
| 03 | Camera Geometry and Robotic Perception | ✅ COMPLETE | 32 | 32 | 32 | 4 | 32 | 32 | midpoint + capstone |
| 04 | Forward Kinematics using Denavit–Hartenberg Parameters | ✅ COMPLETE | 32 | 32 | 32 | 4 | 32 | 32 + midpoint key | midpoint + capstone |
| 05 | Inverse Kinematics | ✅ COMPLETE | 32 | 32 | 32 | 4 | 32 | 32 + midpoint key | midpoint + Reach-the-Fruit capstone |
| 06 | Jacobians and Differential Motion | ✅ COMPLETE | 32 | 32 | 32 | 4 | 32 | 32 + midpoint key | midpoint + 4-part velocity-layer capstone |
| 07 | Trajectory Generation and Motion Planning | ⬜ planned | — | — | — | — | — | — | — |
| 08 | Communication, Embedded Systems, and Control (ROS 2) | ⬜ planned | — | — | — | — | — | — | — |
| 09 | Physical AI System Integration | ⬜ planned | — | — | — | — | — | — | — |
| 10 | Digital Twin Capstone | ⬜ planned | — | — | — | — | — | — | — |

## Totals (completed modules, repo-verified)

- **Modules complete:** 6 of 10
- **Lessons:** 197  (33 + 36 + 32 + 32 + 32 + 32)
- **Notebooks:** 197  (one per lesson; all execute clean)
- **SVGs:** 198  (M1 lesson 1 ships two; `assets/diagrams/`, mirrored to `site_src/assets/`)
- **Demos (interactive HTML):** 34  (12 + 6 + 4 + 4 + 4 + 4)
- **Quizzes (interactive HTML widgets):** 197  (one per lesson)
- **Answer keys:** 197 lesson keys in `coaches/answer-keys/` + midpoint keys (M1, M2, M4, M5, M6) and capstone rubrics
- **Assessments:** 6 midpoint assessments (`assessments/moduleNN_midpoint_assessment.md`) + M3 & M4 Unit-8 capstone mini-projects + M5/M6 Unit-8 capstones
- **Site:** `mkdocs build --strict` PASS — 197 lesson pages (133 M1–M4 + 32 M5 + 32 M6) + index

## In production

- *(none — Module 6 complete; Module 7 not yet started)*

## Recently completed

- **Module 6 — Jacobians and Differential Motion: COMPLETE.** Installments A–D delivered (D-057/058/059/060). All **8 units / 32 lessons** done: 32 lessons (12-section template), 32 SVGs (m06-l1..l32), 32 notebooks, **4 demos** (lesson07 Jacobian Column Explorer, lesson17 Ellipsoid Collapse, lesson21 SVD Bars, lesson29 Resolved-Rate Tracker), 32 quizzes, 32 answer keys, **+ midpoint assessment** (after Unit 4) and its coaches' key. `mkdocs build --strict` passes at **197 lesson pages**. The Jacobian, used in M5 only as the numerical solver's local linear map, is now the subject: differential motion & twists → geometric/analytic Jacobian → manipulability, SVD, singularity theory → inverse velocity kinematics, redundancy, damped least squares (re-derived from the SVD) → the open-loop resolved-rate **velocity layer** handed to Module 7. Running example: planar 2-link arm L1=0.4, L2=0.3, extended to a redundant chain for null-space motion.
- **Next:** Module 7 — Trajectory Generation and Motion Planning (consumes the M6 velocity layer). Not yet started; awaiting architect launch package.
- **Module 5 — Inverse Kinematics: COMPLETE.** Launch package approved (D-053); Installments A–D delivered (D-053/054/055/056). All **8 units / 32 lessons** done: 32 lessons (12-section template + 2 standard components), 32 SVGs (m05-l1..l32), 32 notebooks (all "All checks passed."), **4 demos** (lesson07 Two-Solution Explorer, lesson17 Convergence Stepper, lesson21 Singularity Visualizer, lesson29 **Reach-the-Fruit capstone**), 32 quizzes, 32 answer keys, **+ midpoint assessment** (after Unit 4) and its coaches' key. `mkdocs build --strict` passes at **165 pages**. Educational boundary held throughout: the FK Jacobian is the numerical solver's local linear map only, and singularities (Lesson 6.1) are **recognition only** (det J = L₁L₂ sin θ₂ = 0 at θ₂ = 0°/180°) — velocity, differential motion, manipulability, singularity theory, and SVD all deferred to Module 6 (and re-flagged in Lesson 8.4). The Unit 8 capstone "Reach the Fruit" integrates Modules 2 (frames), 3 (perception), 4 (forward kinematics), and 5 (inverse kinematics) into one perceive → place → solve → verify → select workflow. Running example: planar 2-link arm L1=0.4, L2=0.3.
- **Next:** Module 6 — Differential Kinematics (the Jacobian as a velocity relationship: differential motion, manipulability, singularity theory, SVD). Not yet started; awaiting architect launch package.

## Deferred / parked

- **Asset-hardening audit** (post-production): SVG embedding/contrast, HTML demo consistency, nav labels, notebook-naming confirmation, page-header consistency, and the Module 3 SVG backlog — all tracked in `curriculum/future_roadmap.md`.

## Known doc drift (non-blocking)

- `curriculum/roadmap.md` §7 status table is stale (predates Modules 2–4); the live trackers are this file, `PROJECT_STATE.md`, and `ARCHITECT_DECISIONS.md`.

## Conventions (stable)

- Generator: `tools/generate_site_pages.py`; `MODULES` list drives which modules build. Gate: `mkdocs build --strict`.
- Per module MM: lessons `modules/moduleMM/lessons/lessonNN_*.md`; diagrams `assets/diagrams/mMM-lNN-*.svg`; notebooks `MMM_UUU_L*_*.ipynb`; quizzes/demos `lessonNN_*`; answer keys `coaches/answer-keys/moduleMM/`.
- Five-layer pedagogy; greenhouse-harvesting-robot narrative; AI Learning Companion + Global Learning Support on every lesson.
