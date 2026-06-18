---
title: Master Progress Tracker
purpose: Single-glance status of curriculum production across all modules.
authority: Updated continuously during production; ARCHITECT_DECISIONS.md remains the decision record.
---

# Master Progress Tracker

_Last updated: 2026-06 — Module 7 (Trajectory Generation and Motion Planning) **COMPLETE** (8 units, 32/32 lessons, 4 demos, midpoint; Installments A–D = D-062…D-065, all approved/delivered; paused at module completion). Modules 1–7 COMPLETE (7 of 10 modules done). Next: Module 8 — Feedback Control._

## Module status

| # | Module | Status | Lessons | Notebooks | SVGs | Demos | Quizzes | Answer keys | Assessments |
|---|--------|--------|--------:|----------:|-----:|------:|--------:|------------:|-------------|
| 01 | Mathematical Foundations | ✅ COMPLETE | 33 | 33 | 34 | 12 | 33 | 33 + midpoint key | midpoint |
| 02 | Spatial Transformations and SE(3) | ✅ COMPLETE | 36 | 36 | 36 | 6 | 36 | 36 + midpoint key | midpoint |
| 03 | Camera Geometry and Robotic Perception | ✅ COMPLETE | 32 | 32 | 32 | 4 | 32 | 32 | midpoint + capstone |
| 04 | Forward Kinematics using Denavit–Hartenberg Parameters | ✅ COMPLETE | 32 | 32 | 32 | 4 | 32 | 32 + midpoint key | midpoint + capstone |
| 05 | Inverse Kinematics | ✅ COMPLETE | 32 | 32 | 32 | 4 | 32 | 32 + midpoint key | midpoint + Reach-the-Fruit capstone |
| 06 | Jacobians and Differential Motion | ✅ COMPLETE | 32 | 32 | 32 | 4 | 32 | 32 + midpoint key | midpoint + 4-part velocity-layer capstone |
| 07 | Trajectory Generation and Motion Planning | ✅ COMPLETE | 32 | 32 | 32 | 4 | 32 | 32 + midpoint key | midpoint + harvest-cycle capstone |
| 08 | Communication, Embedded Systems, and Control (ROS 2) | ⬜ planned | — | — | — | — | — | — | — |
| 09 | Physical AI System Integration | ⬜ planned | — | — | — | — | — | — | — |
| 10 | Digital Twin Capstone | ⬜ planned | — | — | — | — | — | — | — |

## Totals (completed modules + in-production, repo-verified)

- **Modules complete:** 7 of 10  (Module 7 COMPLETE: 8 units, 32/32 lessons, 4 demos)
- **Lessons:** 229  (33 + 36 + 32 + 32 + 32 + 32 + **32**)
- **Notebooks:** 229  (one per lesson; all execute clean)
- **SVGs:** 230  (M1 lesson 1 ships two; `assets/diagrams/`, mirrored to `site_src/assets/`)
- **Demos (interactive HTML):** 38  (12 + 6 + 4 + 4 + 4 + 4 + **4** — M7 L07/L17/L21/L29)
- **Quizzes (interactive HTML widgets):** 229  (one per lesson)
- **Answer keys:** 229 lesson keys in `coaches/answer-keys/` + midpoint keys (M1, M2, M4, M5, M6, M7) and capstone rubrics
- **Assessments:** 7 midpoint assessments (`assessments/moduleNN_midpoint_assessment.md`) + M3 & M4 Unit-8 capstone mini-projects + M5/M6/M7 Unit-8 capstones (M7 = the greenhouse harvest cycle)
- **Site:** `mkdocs build --strict` PASS — 229 lesson pages (133 M1–M4 + 32 M5 + 32 M6 + **32 M7**) + index

## In production

*(none — Module 7 complete; paused at module completion, awaiting the Module 8 launch package.)*

## Recently completed

- **Module 7 — Trajectory Generation and Motion Planning: Installment A delivered (Units 1–2, D-062).** 8 lessons (L01–L08, 12-section template + companion blocks), 8 SVGs (m07-l1..l8), 8 notebooks (all "All checks passed." via Restart & Run All), **1 flagship demo** (L07 Polynomial Profile Shaper — cubic↔quintic, live pos/vel/accel/jerk), 8 quizzes (5 MC + 3 short), 8 answer keys. `mkdocs build --strict` passes at 205 lesson pages. Unit 1 establishes motion literacy (smooth/safe/efficient, path vs trajectory, quality criteria, the plan→parameterize→execute-open-loop→track pipeline); Unit 2 builds the time-parameterization toolkit (s(t) & derivatives, C⁰/C¹/C² + jerk, cubic vs quintic, trapezoidal vs S-curve). Both M7/M8 fences held: no feedback control, no dynamics; open-loop execution via the imported M6 velocity layer only. Running example: planar 2-link arm L1=0.4, L2=0.3. **Installment A APPROVED by architect.** Installment B (Units 3–4 + midpoint, D-063) now in production. Remaining after B: C (U5–U6, D-064), D (U7–U8 + capstone, D-065).
- **Module 7 — Installment B delivered (Units 3–4 + midpoint, D-063).** 8 lessons (L09–L16, 12-section template + companion blocks), 8 SVGs (m07-l9..l16), 8 notebooks (all "All checks passed." via Restart & Run All), **no new flagship demo** (per the architect's demo schedule — demos at L07/L17/L21/L29), 8 quizzes (5 MC + 3 short), 8 answer keys, **+ the Module 7 midpoint assessment** (after Unit 4) and its coaches' key. `mkdocs build --strict` passes at **213 lesson pages**. Unit 3 builds joint-space trajectories motion-first (per-joint polynomials → synchronization with the slowest joint setting the pace → via-points stop-vs-flow → C² cubic-spline blending); Unit 4 builds Cartesian-space trajectories (why Cartesian / straight-line tool motion → position interpolation via the IK-per-sample loop with branch consistency → orientation by SLERP → unified position+orientation by screw motion). M7/M8 fences held: no feedback control, no dynamics; the trajectory is an open-loop reference the M6 velocity layer executes. Engine extended with `ik_2link`, `joint_traj`/`sync_duration`, `cubic_spline_natural`, `cartesian_traj_ik`, `slerp`/`slerp_angle`, `screw_interp_se2` (all verified). **Paused at the Installment B milestone for architect review.**
- **Module 7 — Installment C delivered (Units 5–6 + 2 demos, D-064).** 8 lessons (L17–L24, 12-section template + companion blocks), 8 SVGs (m07-l17..l24), 8 notebooks (all "All checks passed." via Restart & Run All), **2 flagship demos** (L17 Velocity & Acceleration Limit Explorer — drag T & displacement, peak bars vs limit lines, reports the binding limit; L21 Configuration Space & Obstacle Visualizer — drag the obstacle, the forbidden region redraws in (q1,q2), drag the configuration point, the arm moves and reddens in the C-obstacle), 8 quizzes (5 MC + 3 short), 8 answer keys. `mkdocs build --strict` passes at **221 lesson pages**. Unit 5 leads with **physical feasibility** (why a trajectory is impossible → slowing down via uniform time scaling → the fastest feasible timing under limits → the whole-trajectory check with timing-vs-geometric triage); Unit 6 builds **motion planning** intuitively (obstacles → forbidden regions / configuration space → collision checking → RRT → smoothing + time scaling), realizing the **Obstacle → Constraint → Safe Path → Feasible Trajectory** chain. Engine extended with `quintic_peaks`, `is_feasible`/`feasible_duration`, `uniform_time_scale_factors`, `arm_hits_disk`/`cspace_grid`, `edge_collision_free`/`path_collision_free`, `rrt`, `shortcut_smooth`/`path_length` (all verified; canonical RRT scenario solves across seeds). Boundaries held: no advanced/optimization/kinodynamic planning, no feedback, no dynamics; plan-then-time decoupling; the trajectory is an open-loop reference the M6 velocity layer executes. **Paused at the Installment C milestone for architect review.**
- **Module 7 COMPLETE — Installment D delivered (Units 7–8, capstone, D-065).** Final installment: 8 lessons (L25–L32), 8 SVGs (m07-l25..l32), 8 notebooks (all "All checks passed."), the **L29 flagship Trajectory Studio demo** (run Plan→Parameterize→Validate→Execute on the greenhouse arm: drag obstacle/start/goal, watch the RRT route, the timing vs limit lines, the validation checklist, and the executed reference signal handed to M8), 8 quizzes (5 MC + 3 short), 8 answer keys. `mkdocs build --strict` passes at **229 lesson pages**. **Unit 7** (Trajectory Quality, Validation, Tracking Prerequisites): quality metrics rank feasible trajectories (7.1) → the complete validation suite as one gate (7.2) → tracking prerequisites and the explicit **M7/M8 boundary** — the reference must provide q_d, q̇_d, q̈_d, with no feedback/dynamics/actuators here (7.3) → discretizing/representing the reference for execution (7.4). **Unit 8** (Capstone): the complete **Plan → Parameterize → Validate → Execute** workflow (8.1, Trajectory Studio) → plan-then-time in depth (8.2) → validate-and-package the **reference trajectory layer** — the M8 handoff bookending M6's velocity_layer (8.3) → the greenhouse harvest cycle end-to-end + Module 7 recap + bridge to M8 (8.4). Engine extended+verified: `piecewise_quintic`, `sample_reference`, `trajectory_metrics`, `validate_trajectory` (7-check suite), `plan_parameterize`, and the capstone **`reference_trajectory_layer`** returning `reference(t)→(q_d,q̇_d,q̈_d,info)` (validated end-to-end on the canonical scenario). Boundaries held throughout: **no feedback control, no dynamics, no actuator control** (all Module 8); "Execute" = open-loop reference handoff. **Module 7 totals:** 8 units · 32 lessons · 32 notebooks · 32 SVGs · **4 demos** (L07,L17,L21,L29) · 32 quizzes · 33 answer keys (incl. midpoint) · 1 midpoint assessment. **Module 7 is complete; pause at module completion (no further installment reviews).** Next: **Module 8 — Feedback Control**, which builds the tracker consuming the reference trajectory layer.

- **Module 6 — Jacobians and Differential Motion: COMPLETE.** Installments A–D delivered (D-057/058/059/060). All **8 units / 32 lessons** done: 32 lessons (12-section template), 32 SVGs (m06-l1..l32), 32 notebooks, **4 demos** (lesson07 Jacobian Column Explorer, lesson17 Ellipsoid Collapse, lesson21 SVD Bars, lesson29 Resolved-Rate Tracker), 32 quizzes, 32 answer keys, **+ midpoint assessment** (after Unit 4) and its coaches' key. `mkdocs build --strict` passes at **197 lesson pages**. The Jacobian, used in M5 only as the numerical solver's local linear map, is now the subject: differential motion & twists → geometric/analytic Jacobian → manipulability, SVD, singularity theory → inverse velocity kinematics, redundancy, damped least squares (re-derived from the SVD) → the open-loop resolved-rate **velocity layer** handed to Module 7. Running example: planar 2-link arm L1=0.4, L2=0.3, extended to a redundant chain for null-space motion.
- **Post-integration fix (generator):** the site generator's scaffolding strip only matched the plain `**Diagram Specification**` header, but 28 M6 lessons use a qualifier (e.g. `(multi-panel)`), so asset-production scaffolding was leaking onto student pages. The strip regex now allows an optional qualifier; the 28 pages were regenerated. Backward-compatible — no change to M1–M5 (which use the plain header). `mkdocs build --strict` re-verified clean (0 scaffolding leaks, all 32 figures embedded).
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
