---
title: Project State — Physical AI Curriculum
status: AUTHORITATIVE current-state snapshot
purpose: A single, current picture of where production stands — current module, what is complete, what is in progress, what is deferred, known issues, and the next milestone. Update this whenever a unit/installment/module completes or a decision changes state.
authority: Subordinate to ARCHITECT_DECISIONS.md. Counts mirror master_progress.md.
last_updated: 2026-06 — Module 8 IN PRODUCTION: Installments A–C delivered (Units 1–6, L01–L24 + midpoint; A = D-067, B = D-068, C = D-069); paused at the Installment C milestone. Site at 253 lesson pages, mkdocs --strict green. Modules 1–7 COMPLETE; 7 of 10 modules signed off.
---

# Project State

> Snapshot of production status. For the full decision history see `ARCHITECT_DECISIONS.md`; for counts see `master_progress.md`.

## Current module

**Module 8 — Feedback Control and Real-Time Execution (ROS 2): IN PRODUCTION** — Installments A–C delivered (Units 1–6, L01–L24 + midpoint; launch package = D-066, A = D-067, B = D-068, C = D-069); paused at the Installment C milestone.

Module 8 answers "How do we make the robot actually follow that motion — on a real, imperfect machine?" It consumes Module 7's reference layer `reference(t) → (q_d, q̇_d, q̈_d)` and closes the loop: tracking error → correction → stability → implementation, on a simulated plant (integrator + disturbance + saturation). The launch package was approved with all §9 rulings: dynamics as **disturbance/load/friction/saturation/model-mismatch intuition only** (no formal manipulator dynamics); **no control-theory formalism** (no Laplace/transfer functions/root-locus/Bode/Nyquist) — teach error → correction → stability → implementation; **ROS 2 conceptual + lightweight code only**; plant = integrator + disturbance + saturation; intuition-first across all domains; title "Feedback Control and Real-Time Execution (ROS 2)"; **explicitly consume M7's q_d, q̇_d, q̈_d** with feedforward + feedback as a major continuity theme; and **begin by repeatedly contrasting open-loop vs closed-loop** before introducing PID. Installment A (Units 1–2) establishes the tracking problem / feedback loop and builds the full single-joint PID controller. Demos land at L07/L17/L21/L29; midpoint after Unit 4. Capstone (U8) = the `tracking_controller` control layer as a ROS 2 node — the Module 9 handoff. Running example: planar 2-link arm L1=0.4, L2=0.3, now driven against the simulated plant.

**Installment C deliverables (Units 5–6, L17–L24, in repo):**
- 8 lessons — `modules/module08/lessons/lesson17..24_*.md` (12-section template + AI Learning Companion + Global Learning Support in 4 languages).
- 8 SVGs — `assets/diagrams/m08-l17..l24-*.svg` (XML-valid; embedded in §4 Visual Explanation).
- 8 notebooks — `modules/module08/notebooks/lesson17..24_*.ipynb` (all end "All checks passed." under Restart & Run All; embed the extended Module 8 engine verbatim).
- 2 flagship demos — `modules/module08/demos/lesson17_actuator_bench.html` (dial requested command; toggle deadband/saturation/rate limit; live transfer curve + step ramp) and `lesson21_message_bus.html` (watch a message traverse each hop; loop latency accumulates as Σ hops). Accessible; no browser storage.
- 8 quizzes — `modules/module08/quizzes/lesson17..24_quiz.html` (5 MC + 3 short, MathJax).
- 8 answer keys — `coaches/answer-keys/module08/lesson17..24_answer_key.md` (model answers + grading notes + common misconceptions).
- Engine extension — `engine/m8_engine.py` extended additively for Installment C (Unit 5: `Actuator` with deadband/saturation/rate limit, `apply_stiction`, `step_plant`, `track_reference_actuated`, `feasibility_envelope`; Unit 6: `Bus` pub/sub, `loop_latency`, `latency_to_steps`, `zoh_reference`, `run_pubsub_loop`). A+B API unchanged; B-state backup at `engine/m8_engine_B_backup.py`.
- Nav for Units 5–6 added; generator unit titles ("08","05")="Actuator Control", ("08","06")="Communication"; `mkdocs build --strict` passes at **253 lesson pages** (245 + 8).

Installment C scope held to the architect rulings: Unit 5 actuators are plant-level only (NO motor electrodynamics / current loops / actuator dynamics); Unit 6 communication is conceptual — pub/sub is a PATTERN not a framework (ROS 2 named only as the Unit 8 implementation); L23 control-rate framing stays qualitative (NO discrete-time/sampling formalism); the L21 nervous-system analogy is retained with explicit limits. The Unit-5 feasibility envelope ties back to Module 7 feasibility; the Unit-6 timing split (latency-critical inner loop vs latency-tolerant outer layers) motivates real-time (Unit 7) and frames the ROS 2 stack (Unit 8).

**Installment A deliverables (in repo):**
- 8 lessons — `modules/module07/lessons/lesson01..08_*.md` (12-section template + AI Learning Companion + Global Learning Support in 4 languages).
- 8 SVGs — `assets/diagrams/m07-l1..l8-*.svg` (embedded in §4 Visual Explanation).
- 8 notebooks — `modules/module07/notebooks/lesson01..08_*.ipynb` (all end "All checks passed." under Restart & Run All; embed the M6 velocity-layer engine verbatim + new time utilities).
- 1 flagship demo — `modules/module07/demos/lesson07_polynomial_profile_shaper.html` (cubic↔quintic toggle, drag duration, live pos/vel/accel/jerk, accessible, no browser storage).
- 8 quizzes — `modules/module07/quizzes/lesson01..08_quiz.html` (5 MC + 3 short, MathJax).
- 8 answer keys — `coaches/answer-keys/module07/lesson01..08_answer_key.md` (model answers + grading notes + common misconceptions).
- Nav for Units 1–8 (M7) + Units 1–4 (M8); generator wired (`"08"` + module/unit titles 01–04); `mkdocs build --strict` passes at **245 lesson pages** (229 M1–M7 + 16 M8).

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

**Module 8 — Feedback Control and Real-Time Execution (ROS 2): Installments A–C (Units 1–6) delivered; paused at the Installment C milestone for architect review.** Units 1–2 cover the tracking problem/feedback loop and PID control; Units 3–4 cover stability/response/tuning and tracking the whole arm with feedforward + feedback; Units 5–6 (Installment C) cover actuator control (the request→delivery converter and its deadband/saturation/rate-limit nonlinearities, integral windup and the anti-windup cure, deadband/stiction and why integral wins the final approach, and the command pipeline + feasibility envelope tying back to Module 7) and communication (the loop as messages over a pub/sub bus, nodes/topics/messages and decoupling, latency + finite control rate destabilising a fixed-gain loop, and the data-flow architecture layered by timing — inner loop vs outer layers). 24 lessons · 24 notebooks (all pass) · 24 SVGs · 3 demos (L07, L17, L21) · 24 quizzes · 24 keys · 1 midpoint + key. Remaining: D (U7–U8 + capstone).

## Next milestone

**Module 8 — Installment D (Units 7–8 + capstone): awaiting architect go-ahead.** Unit 7 (Embedded and Real-Time Execution) and Unit 8 (ROS 2 Implementation) complete the module — real-time scheduling/timing guarantees for the latency-critical inner loop (motivated by Installment C's Unit 6) and the ROS 2 implementation of the layered node/topic stack, culminating in the capstone `tracking_controller` control layer as a ROS 2 node (the Module 9 handoff). Demos planned at L29. The Installment-A–C work (Units 1–6 + midpoint) is paused at the Installment C milestone pending architect review before D begins.

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

## Verification at last update (Module 8 Installment B)

- Generator: `python tools/generate_site_pages.py` → **253 pages generated** (M1–M8), validator clean, no `[Visual:]` placeholder leaks; every M8 lesson injects [1 SVG, notebook, quiz] (+ demo on L07/L17/L21).
- Build: `mkdocs build --strict` → **PASS** (exit 0, 253 lesson pages + site index).
- Counts reconcile with `master_progress.md`: 7/10 modules complete (M8 in production) · 253 lessons · 253 notebooks · 254 SVGs · 41 demos · 253 quizzes · 8 midpoint assessments (+ M3/M4/M5/M6/M7 capstones).
