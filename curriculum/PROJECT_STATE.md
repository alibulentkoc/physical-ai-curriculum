---
title: Project State — Physical AI Curriculum
status: AUTHORITATIVE current-state snapshot
purpose: A single, current picture of where production stands — current module, what is complete, what is in progress, what is deferred, known issues, and the next milestone. Update this whenever a unit/installment/module completes or a decision changes state.
authority: Subordinate to ARCHITECT_DECISIONS.md. Counts mirror master_progress.md.
last_updated: 2026-06 — Module 6 (Jacobians and Differential Motion) COMPLETE (32/32, Installments A–D, D-060); 6 of 10 modules done. Next: Module 7 — Trajectory Generation and Motion Planning.
---

# Project State

> Snapshot of production status. For the full decision history see `ARCHITECT_DECISIONS.md`; for counts see `master_progress.md`.

## Current module

**None active — Module 6 just completed; Module 7 awaiting launch package.**

**Module 6 — Jacobians and Differential Motion: COMPLETE (D-060).** All 8 units / 32 lessons delivered across Installments A–D, plus the midpoint assessment (after Unit 4) and the four-part velocity-layer capstone. The Jacobian, used in M5 only as the numerical solver's local linear map, is now the subject: differential motion & twists → geometric/analytic Jacobian → manipulability, SVD, singularity theory → inverse velocity kinematics, redundancy, and damped least squares (re-derived from the SVD) → the open-loop resolved-rate **velocity layer** handed to Module 7. Paused at Module 6 completion for architect review before Module 7.

Module 6 deliverables (in repo):
- 32 lessons — `modules/module06/lessons/lesson01..32_*.md` (12-section numbered template).
- 32 SVGs — `assets/diagrams/m06-l1..l32-*.svg` (embedded in §4 Visual Explanation).
- 32 notebooks — `modules/module06/notebooks/lesson01..32_*.ipynb`.
- 4 demos — `modules/module06/demos/`: `lesson07_jacobian_column_explorer.html`, `lesson17_ellipsoid_collapse.html`, `lesson21_svd_bars.html`, `lesson29_resolved_rate_tracker.html`.
- 32 quizzes — `modules/module06/quizzes/lesson01..32_quiz.html` (5 MC + 3 short answer; MathJax-enabled for LaTeX).
- 32 answer keys — `coaches/answer-keys/module06/lesson01..32_answer_key.md` (+ `midpoint_answer_key.md`).
- **Midpoint assessment** — `assessments/module06_midpoint_assessment.md` (after Unit 4) + coaches' key.
- Completion report — `curriculum/module06_completion_report.md`.
- Nav blocks for all 8 units; `mkdocs build --strict` passes at **197 lesson pages**.

Educational boundary held end to end: M6 is the first-order (velocity) relationship and its geometry only — no trajectory/path planning (Module 7), no dynamics or feedback control (Module 8). Resolved-rate motion is open-loop and explicitly handed to Module 7 as the velocity layer. Running example: planar 2-link arm L1=0.4, L2=0.3, extended to a redundant chain for null-space motion.

---

**Module 5 — Inverse Kinematics: COMPLETE (D-056).** All 8 units / 32 lessons delivered across Installments A–D, plus the midpoint assessment and the Reach-the-Fruit capstone.

Module 5 deliverables (in repo):
- 32 lessons — `modules/module05/lessons/lesson01..32_*.md` (12-section template + 2 standard components).
- 32 SVGs — `assets/diagrams/m05-l1..l32-*.svg` (XML-valid; embedded in §4).
- 32 notebooks — `modules/module05/notebooks/M05_U01..U08_*` (all execute "All checks passed."; shared fk_two_link / ik_2link_closed / jacobian_2link / ik_newton / ik_dls / det_jacobian / verify / cam_to_base / reach_the_fruit helpers).
- 4 demos — `modules/module05/demos/`: `lesson07_two_solution_explorer.html`, `lesson17_convergence_stepper.html`, `lesson21_singularity_visualizer.html`, `lesson29_reach_the_fruit.html` (flagship capstone — drag the fruit, set camera offset + joint limits, watch the full pipeline run live).
- 32 quizzes — `modules/module05/quizzes/lesson01..32_quiz.html` (reference renderer).
- 32 answer keys — `coaches/answer-keys/module05/lesson01..32_answer_key.md`.
- **Midpoint assessment** — `assessments/module05_midpoint_assessment.md` (after Unit 4) + coaches' key.
- Nav blocks for all 8 units; `mkdocs build --strict` passes at **165 pages**.

Educational boundary held end to end: the FK Jacobian is the numerical solver's local linear map only; **singularities (Lesson 6.1) are recognition-only** — det J = L₁L₂ sin θ₂ = 0 at θ₂ = 0° (straight) / 180° (folded) — with velocity interpretation, differential motion, manipulability, full singularity theory, and SVD analysis deferred to Module 6 (re-flagged in Lesson 8.4). The Unit 8 capstone "Reach the Fruit" integrates Modules 2 (frames), 3 (perception), 4 (forward kinematics), and 5 (inverse kinematics) into one perceive → place → solve → verify → select workflow. Running example: planar 2-link arm L1=0.4, L2=0.3.

## Completed modules

| # | Module | Lessons | Signed off |
|---|--------|--------:|-----------|
| 01 | Mathematical Foundations | 33 | ✅ (D-036) |
| 02 | Spatial Transformations and SE(3) | 36 | ✅ (D-044) |
| 03 | Camera Geometry and Robotic Perception | 32 | ✅ (D-048) |
| 04 | Forward Kinematics (DH parameters) | 32 | ✅ (D-052) |
| 05 | Inverse Kinematics | 32 | ✅ (D-056) |
| 06 | Jacobians and Differential Motion | 32 | ✅ (D-060) |

All six are production-complete with lessons, notebooks, SVGs, interactive quizzes, answer keys, midpoint assessments, and (M3/M4/M5/M6) capstone mini-projects. Each has a completion report in `curriculum/moduleNN_completion_report.md`. **Do not redesign or rewrite these** — they are the reference implementations and the quality bar.

## Modules in progress

*(none — Module 6 complete; paused for Module 6 review before Module 7 launch.)*

## Next milestone

**Module 7 — Trajectory Generation and Motion Planning (not yet started; awaiting architect launch package).** This is where the **velocity layer** Module 6 produced (resolved-rate motion, the Jacobian as a velocity map, singularity-robust inversion) becomes the substrate for planning *paths and time-parameterized trajectories* through the workspace — beyond the instantaneous, open-loop motion of Module 6. Downstream: Module 8 — communication, embedded systems, and control. Awaiting the architect's Module 7 launch package before production begins.

Then resume the standing production directive (produce module-by-module, pause at module completion).

## Deferred work (parked — do not implement until approved)

Tracked in `curriculum/future_roadmap.md`. Summary:

- **Asset-hardening & audit pass** (after all modules complete): verify every Visual Explanation renders its intended diagram; tighten cramped/low-contrast SVG layouts; unify HTML demo controls/readouts/styling; confirm faux-3D viewers render; nav-label wording consistency; confirm notebook naming everywhere; page-header ("You are here") consistency.
- **Module 3 SVG backlog:** `m03-l17-distortion-types.svg` barrel/pincushion grids are hand-drawn approximations with a minor top-edge artifact (reads correctly; could be regenerated from an actual radial model). Unit 5–6 ray diagrams (`m03-l21/l22/l24`) use flat 2D schematics; could be upgraded to the isometric faux-3D style during hardening.

None of the above blocks production.

## Known issues

- **`curriculum/roadmap.md` §7 ("Status") is stale.** It still reads "Module 1 is the only module designed so far … Modules 2–10 ⬜," which predates Modules 2–4. The body of `roadmap.md` (the arc, dependency chain, software progression) is correct and current; only the trailing status table is out of date. Non-blocking — `master_progress.md`, `PROJECT_STATE.md`, and `ARCHITECT_DECISIONS.md` are the live trackers. Fix opportunistically.
- **`curriculum/assessment_strategy.md` is scoped to Module 1.** Its weights (D-010) and thresholds (D-015) are curriculum-wide, but the document is explicitly "calibrated to Module 1." Later modules apply the same formative/midpoint/capstone pattern in practice; a generalization pass is optional, not required.
- **Mermaid/MkDocs platform note:** the build runs on `mkdocs build --strict` with Material theme; the Material team prints a forward-looking MkDocs-2.0 advisory banner during builds. It is **advisory only** — not a build warning — and does not affect `--strict` (build exits 0).
- **Single-source integrity:** prose must stay only in `modules/.../lessons/`. `site_src/` pages are generated; never hand-edit them or the two layers will drift (the recurring "stale build" symptom). Always re-run the generator before building.

## Verification at last update (Module 6 complete)

- Generator: `python tools/generate_site_pages.py` → **197 pages generated** (M1–M6), validator clean, no `[Visual:]` placeholder leaks; every M6 lesson injects [1 SVG, notebook, quiz] (+ demo on 2.3/5.1/6.1/8.1).
- Build: `mkdocs build --strict` → **PASS** (exit 0, 197 lesson pages + site index). Module 5 generation was restored to the generator (`"05"` + titles) so M5's served assets re-emit; an earlier merge had dropped it, which was breaking `--strict`.
- Counts reconcile with `master_progress.md`: 6/10 modules · 197 lessons · 197 notebooks · 198 SVGs · 34 demos · 197 quizzes · 6 midpoint assessments (+ M3/M4/M5/M6 capstones).
