---
title: Project State — Physical AI Curriculum
status: AUTHORITATIVE current-state snapshot
purpose: A single, current picture of where production stands — current module, what is complete, what is in progress, what is deferred, known issues, and the next milestone. Update this whenever a unit/installment/module completes or a decision changes state.
authority: Subordinate to ARCHITECT_DECISIONS.md. Counts mirror master_progress.md.
last_updated: 2026-06 — Module 7 COMPLETE: 8 units, 32/32 lessons, 4 demos (A–D; A/B/C APPROVED, D=D-065 capstone delivered); paused at module completion. Next: Module 8 — Feedback Control. Midpoint assessment APPROVED (no revisions). Modules 1–7 COMPLETE; 7 of 10 modules signed off.
---

# Project State

> Snapshot of production status. For the full decision history see `ARCHITECT_DECISIONS.md`; for counts see `master_progress.md`.

## Current module

**Module 7 — Trajectory Generation and Motion Planning: COMPLETE** (8 units, 32/32 lessons, 4 demos; Installments A–D = D-062…D-065 approved/delivered; paused at module completion).**

Module 7 answers "How do I move from here to there smoothly, safely, and efficiently?" — it turns a goal into a path, a path into a smooth, feasible, validated trajectory, and (open-loop, via the M6 velocity layer) demonstrates that motion, producing the reference trajectory Module 8 will later track with feedback. The launch package was approved with all §9 rulings (planning depth = C-space + collision + RRT + smoothing; SLERP/screw applied; strict M7-defines / M8-tracks boundary; open-loop execution via M6; dynamics excluded; demos at L07/L17/L21/L29; static obstacle only).

**Installment A deliverables (in repo):**
- 8 lessons — `modules/module07/lessons/lesson01..08_*.md` (12-section template + AI Learning Companion + Global Learning Support in 4 languages).
- 8 SVGs — `assets/diagrams/m07-l1..l8-*.svg` (embedded in §4 Visual Explanation).
- 8 notebooks — `modules/module07/notebooks/lesson01..08_*.ipynb` (all end "All checks passed." under Restart & Run All; embed the M6 velocity-layer engine verbatim + new time utilities).
- 1 flagship demo — `modules/module07/demos/lesson07_polynomial_profile_shaper.html` (cubic↔quintic toggle, drag duration, live pos/vel/accel/jerk, accessible, no browser storage).
- 8 quizzes — `modules/module07/quizzes/lesson01..08_quiz.html` (5 MC + 3 short, MathJax).
- 8 answer keys — `coaches/answer-keys/module07/lesson01..08_answer_key.md` (model answers + grading notes + common misconceptions).
- Nav for Units 1–8; generator wired (`"07"` + module/8 unit titles); `mkdocs build --strict` passes at **229 lesson pages** (197 M1–M6 + 32 M7).

Unit 1 (Motion, Paths, and Trajectories) builds motion literacy — smooth/safe/efficient motion, path q(s) vs trajectory q(t)=q(s(t)), the four quality criteria with the C⁰/C¹/C² ladder, and the plan→parameterize→execute-open-loop(M6)→track(M8) pipeline with both fences drawn. Unit 2 (Time Parameterization and Smoothness) builds the timing toolkit — q(t)=q(s(t)) and its derivatives via the chain rule (incl. jerk), continuity classes and why C² means no force jumps, **cubic vs quintic** (cubic leaves endpoint accel ±6Δ/T² → C¹; quintic zeros it → C², at higher mid-move peaks), and trapezoidal (time-optimal, C¹) vs S-curve (jerk-limited, C²) velocity profiles.

**Decision-id note:** the launch package proposed D-058; the architect ruled the authoritative mapping **D-061 Launch · D-062 Installment A**, continuing sequentially (B=D-063, C=D-064, D=D-065). No content impact.

Educational boundaries held in Installment A: no feedback/closed-loop control and no dynamics; open-loop execution is via the imported M6 velocity layer only, to demonstrate feasibility. Running example: planar 2-link arm L1=0.4, L2=0.3 (engine length-agnostic via the DH table).

**Remaining for Module 7:** All four installments delivered (A–D); Module 7 complete. The capstone produced the **reference_trajectory_layer** (reference(t)→q_d,q̇_d,q̈_d) consumed by Module 8 — bookending M6's velocity_layer.

---

**Module 6 — Jacobians and Differential Motion: COMPLETE (D-060).** All 8 units / 32 lessons delivered across Installments A–D, plus the midpoint assessment (after Unit 4) and the four-part velocity-layer capstone. The Jacobian, used in M5 only as the numerical solver's local linear map, is now the subject: differential motion & twists → geometric/analytic Jacobian → manipulability, SVD, singularity theory → inverse velocity kinematics, redundancy, and damped least squares (re-derived from the SVD) → the open-loop resolved-rate **velocity layer** handed to Module 7 (now consumed by M7 Installment A).

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

*(none — Module 7 complete; paused at module completion before Module 8 launch.)*

## Next milestone

**Module 8 — Feedback Control (not yet started; awaiting architect launch package).** This is where the **reference trajectory layer** Module 7 produced (the validated open-loop reference `reference(t) → q_d, q̇_d, q̈_d`) becomes the substrate for *closed-loop tracking* — building the controller that follows the reference on the real arm, adding feedback control, dynamics, and actuator control (all explicitly out of Module 7's scope). Awaiting the architect's Module 8 launch package before production begins.

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

## Verification at last update (Module 7 complete)

- Generator: `python tools/generate_site_pages.py` → **229 pages generated** (M1–M7), validator clean, no `[Visual:]` placeholder leaks; every M7 lesson injects [1 SVG, notebook, quiz] (+ demo on L07/L17/L21/L29).
- Build: `mkdocs build --strict` → **PASS** (exit 0, 229 lesson pages + site index).
- Counts reconcile with `master_progress.md`: 7/10 modules · 229 lessons · 229 notebooks · 230 SVGs · 38 demos · 229 quizzes · 7 midpoint assessments (+ M3/M4/M5/M6/M7 capstones).
