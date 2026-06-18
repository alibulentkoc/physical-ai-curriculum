---
title: "Module 8 — Installment A (Units 1–2) — Milestone Report"
module: 08
installment: A
units: [1, 2]
lessons: "L01–L08"
decision: D-067
launch_decision: D-066
status: delivered — paused for architect review
date: 2026-06
---

# Module 8 — Installment A Milestone Report

## EXECUTIVE SUMMARY

- **Module:** 8 — Feedback Control and Real-Time Execution (ROS 2)
- **Status:** Installment A (Units 1–2, lessons L01–L08) **delivered and verified**; **paused at the milestone for architect review** (no auto-proceed to Installment B).
- **What was built:** 8 lessons (full 12-section template + AI Learning Companion + Global Learning Support in 4 languages), 8 SVG diagrams, 8 runnable notebooks (all "All checks passed." under Restart & Run All), 1 flagship interactive demo (L07 PID Playground), 8 interactive quizzes (5 MC + 3 short), 8 coaches' answer keys. Generator registered for Module 8; nav added; `mkdocs build --strict` passes at **237 lesson pages** (229 M1–M7 + 8 M8).
- **Key educational achievement:** the **open-loop-vs-closed-loop demonstration** the architect asked to lead with — shown three numerically-agreeing ways (the m08-l1 SVG, the L01 notebook, and the engine): under a sustained load the **open-loop** arm drifts away from the reference (q → −3.26, tracking RMS ≈ 2.14), while the **closed-loop** controller drives it back onto the reference (q → 0.99, RMS ≈ 0.036). Students *feel* why feedback is necessary before any PID term is introduced. This carries straight into the PID arc: P leaves a steady-state offset ≈ load/Kp; I erases it; D damps the overshoot (PI 5.5% → PID 0.8%).
- **Architect review focus:** (1) the open-loop-vs-closed-loop opening spine of Unit 1 and the error → correction build of Unit 2; (2) confirmation that the §9 fences held — **no formal manipulator dynamics** (disturbance/load/friction/saturation/model-mismatch intuition only), **no control-theory formalism** (no Laplace/transfer functions/Bode/Nyquist), plant = **integrator + disturbance + saturation**; (3) the **M7 continuity seam** — the controller consumes M7's `q_d`, and feedforward `q̇_d, q̈_d` is introduced as the lead term, set up to be fully developed in Unit 4.
- **Next:** Installment B — Units 3 (Stability, Response, and Tuning) and 4 (Tracking the Whole Arm: Feedforward + Feedback) + the midpoint assessment after Unit 4, on approval.

---

## 1. Decision-id reconciliation

No collision this installment. Module 8 launch package = **D-066**; Installment A = **D-067**, following directly from Module 7's last id (D-065). Both recorded in `ARCHITECT_DECISIONS.md`. No action required.

## 2. What was delivered

**Unit 1 — The Tracking Problem and the Feedback Loop** (taught open-loop-vs-closed-loop first)
- **L01 (1.1)** Why Open-Loop Isn't Enough: the reference-vs-reality gap — the open-loop arm runs the M7 reference blind and drifts under load/friction/model error; the closed-loop arm measures and corrects.
- **L02 (1.2)** Tracking Error: the quantity control fights — e = q_d − q, the single number every controller drives toward zero; how it evolves over a move.
- **L03 (1.3)** The Feedback Loop: sense → compare → correct → actuate — the four-stage cycle, drawn as a closed signal path.
- **L04 (1.4)** Anatomy of a Control System: reference, plant, controller, feedback — the canonical block diagram, with the M7 reference as the origin and the disturbance/sensor entering explicitly.

**Unit 2 — Proportional, Integral, and Derivative Control** (PID built from error intuition)
- **L05 (2.1)** Proportional Control: correction proportional to error — u = Kp·e; why P alone settles with a steady-state offset ≈ load/Kp.
- **L06 (2.2)** Integral Control: erasing steady-state error — the accumulator that removes the offset; windup and the anti-windup clamp.
- **L07 (2.3) [FLAGSHIP DEMO]** Derivative Control: anticipate and damp — D reacts to the *rate* of error, cutting overshoot and ringing; the measurement-noise caveat. Demo: PID Playground.
- **L08 (2.4)** The PID Controller: the complete single-joint tracker — u = Kp·e + Ki·∫e + Kd·ė; the P → PI → PID metric progression; first explicit mention of M7 feedforward as the lead term.

## 3. Engine

A reusable Module 8 engine is **embedded in each notebook** (`m8_engine.py`):
- **Plant:** `Joint(m, b, load, u_max, …)` — a per-joint **integrator + injectable disturbance/load/friction + actuator saturation** (the §9.4 plant model); `.step(u, dt, extra_disturbance)`, `.reset`, `.saturate`.
- **Controllers:** `PIDController(Kp, Ki, Kd, i_clamp).command(q_d, q, dt, qd, qd_d)` (e = q_d − q, derivative-on-error, integral with optional anti-windup clamp), `p_command`, and `feedforward_command(qdd_d, m_nominal, load_comp)` — the M7 feedforward hook.
- **Simulation + analysis:** `simulate_open_loop`, `simulate_closed_loop` (both return t/q/q_d/error/u), `step_response_metrics` (overshoot %, settling time, rise time, steady-state error), `classify_stability` (settles / oscillates / diverges, envelope-based), `tracking_rms`; plus `quintic_reference`/`setpoint_reference` for the reference signal.

Verified properties: open-loop drifts under load while closed-loop tracks (RMS 2.14 → 0.036); P-only steady-state offset ≈ load/Kp (0.199 at Kp=10, load=2); integral removes it (≈ −0.004); derivative cuts overshoot (PI 5.5% → PID 0.8%); feedforward + feedback beats feedback-only. Running example: planar 2-link arm L₁=0.4, L₂=0.3, now driven against the simulated plant.

## 4. Verification

- **Notebooks:** all 8 execute clean end-to-end via nbclient Restart-and-Run-All (0 failures); each prints "All checks passed." Two checks were built to use a manual step-from-rest loop rather than the setpoint helper (which resets the plant to the target), so the proportional offset (L02) and the P-vs-PI offset-removal + windup contrast (L06) demonstrate a true step response.
- **SVGs:** all 8 XML-valid; `role="img"` + `aria-label` + `viewBox`; no fixed root width; design-system colors. Real response curves are computed from the engine; block diagrams are hand-drawn. l1/l4/l8 were rasterized and confirmed on-message.
- **Quizzes:** all 8 are self-contained interactive HTML (5 MC + 3 short), MathJax-enabled, no `localStorage`/`sessionStorage`.
- **Answer keys:** all 8 in coaches' format — MC answer + rationale, 3 short model answers, and a "Common misconceptions to watch for" section.
- **Demo:** L07 PID Playground — Kp/Ki/Kd sliders, live overshoot/settling/steady-state readouts, noise toggle; aria-labels + aria-live + focus-visible; no storage; self-contained.
- **Site:** generator registered (`"08"` in `MODULES`, module title, Unit 1–2 titles); the run injected SVG/demo/notebook/quiz into every page; the visual-embed validator passed (no missing figure, no `[Visual:]` placeholder leaked, Diagram Specification stripped). `mkdocs build --strict` **passes clean (exit 0)** at 237 lesson pages.
- **DoD matrix:** all 8 lessons meet every gate (12 sections · SVG · passing notebook · 5 MC + 3 short quiz · answer key · companion blocks · published site page).

## 5. Boundaries held (§9)

- **§9.1 / §9.4 Dynamics:** dynamics appears only as **disturbance, load, friction, saturation, and model mismatch** — the things the loop rejects. The plant is an integrator + disturbance + saturation; no mass matrix, Coriolis, computed-torque, or Lagrangian anywhere.
- **§9.2 Formalism:** stability and response are **qualitative** (settles / oscillates / diverges, overshoot, settling, steady-state offset). No Laplace transforms, transfer functions, root locus, Bode, or Nyquist — boundary-scanned across all 8 lessons (0 hits).
- **§9.7 M7 continuity:** the controller tracks M7's reference `q_d`; the feedforward triple `q̇_d, q̈_d` is introduced (L08) as the lead term that lets the controller anticipate rather than only react — feedforward + feedback flagged as the major theme to be fully built in Unit 4.
- **Opening guidance:** Unit 1 leads by repeatedly contrasting **open-loop vs closed-loop** (L01 alone references the contrast throughout) so the necessity of feedback is experienced before PID is introduced.

## 6. Repository changes

- `modules/module08/lessons/lesson01..08_*.md` (8)
- `modules/module08/notebooks/lesson01..08_*.ipynb` (8)
- `modules/module08/demos/lesson07_pid_playground.html` (1)
- `modules/module08/quizzes/lesson01..08_quiz.html` (8)
- `assets/diagrams/m08-l1..l8-*.svg` (8)
- `coaches/answer-keys/module08/lesson01..08_answer_key.md` (8)
- `tools/generate_site_pages.py` — Module 08 registered (MODULES + module title + Unit 1–2 titles)
- `mkdocs.yml` — Units 1–2 nav added (demo marked on 2.3)
- `curriculum/ARCHITECT_DECISIONS.md` — **D-066** (launch) + **D-067** (Installment A) appended
- `curriculum/master_progress.md`, `curriculum/PROJECT_STATE.md` — updated to Module 8 IN PRODUCTION (Installment A); totals → 237 lessons / 238 SVGs / 39 demos / 237 pages
- `site_src/module08/lesson01..08.md` + `site/` — generated; strict build passing

## 7. Milestone

**Installment A is complete and paused for architect review.** On approval, Installment B (Units 3–4 + midpoint assessment) follows, beginning with L09 (3.1) What Stability Means: settle, oscillate, or diverge — the qualitative stability foundation, then the response shape, the failure modes, and a practical tuning workflow, before Unit 4 extends control to the whole arm with feedforward + feedback.
