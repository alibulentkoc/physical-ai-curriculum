---
title: "Module 8 — Completion Report (Feedback Control and Real-Time Execution (ROS 2))"
module: 8
status: COMPLETE — paused at module completion
decisions: [D-066, D-067, D-068, D-069, D-070]
date: 2026-06
---

# Module 8 — Completion Report

> **EXECUTIVE SUMMARY**
>
> - **Module:** 8 — Feedback Control and Real-Time Execution (ROS 2). **COMPLETE** across four installments (A–D) and a midpoint assessment; decisions **D-066** (launch) through **D-070** (capstone).
> - **Status:** Fully built and in the repo; `mkdocs build --strict` passes at **261 lesson pages**. **Paused at Module 8 completion** — no further installment reviews within this module.
> - **Totals:** **8 units · 32 lessons · 32 notebooks · 32 SVGs · 4 flagship demos · 32 quizzes · 32 coaches' answer keys · 1 midpoint assessment.** Every notebook passes Restart & Run All ("All checks passed."); every SVG is XML-valid; every quiz is interactive HTML (5 MC + 3 short, MathJax, no browser storage); all demos are self-contained, accessible, and storage-free.
> - **Capstone deliverable:** the **control layer** — `tracking_controller(reference, measured_state) → actuator_command` — that turns a Module 7 reference sample and the measured joint state into the actuator command that drives the joint, via feedforward + feedback through the actuator, on a real-time periodic loop in a ROS 2 stack. It is the **Module 9 handoff**, completing **velocity layer (M6) → reference layer (M7) → control layer (M8) → integrated system (M9)**.
> - **Pedagogical arc:** from *"open-loop execution drifts"* (the tracking problem) to a *real, distributed, actuator-limited, real-time control stack* that makes the greenhouse arm follow its trajectory and recover from disturbances — taught intuition-first, contrasting open-loop vs closed-loop before any formalism.
> - **Boundaries held end to end:** dynamics as disturbance/load/friction/saturation/model-mismatch **intuition only**; **no control-theory formalism** (no Laplace/transfer functions/root-locus/Bode/Nyquist; no discrete-time/sampling/z-transform; no real-time scheduling theory); **ROS 2 conceptual + lightweight**; **no system integration beyond the control layer** (that is Module 9).
> - **Next:** Module 9 — the integrated autonomous system, which consumes this control layer.

---

## 1. Scope and structure

Module 8 turns a validated reference trajectory (Module 7's `reference(t) → q_d, q̇_d, q̈_d`) into
**actual motion on a real, imperfect machine** by closing the loop: tracking error → correction →
stability → implementation. It was delivered in four installments plus a midpoint assessment:

- **Installment A (Units 1–2, L01–L08; D-067):** the tracking problem and the feedback loop (U1);
  the full single-joint PID controller — proportional, integral, derivative (U2). Demo at L07.
- **Installment B (Units 3–4 + midpoint, L09–L16; D-068):** stability, response, and tuning (U3);
  tracking the whole arm with feedforward + feedback (U4); the Module 8 midpoint assessment.
- **Installment C (Units 5–6, L17–L24; D-069):** actuator control — deadband, saturation, rate
  limits, the command pipeline, the feasibility envelope (U5); communication — the loop as messages,
  publish/subscribe, latency and control rate, the timing-layered architecture (U6). Demos at L17 and L21.
- **Installment D (Units 7–8, L25–L32; D-070):** embedded execution and real-time control (U7);
  ROS 2 integration and the control stack — the capstone control layer (U8). Flagship Closed-Loop
  Tracking Studio demo at L29.

## 2. The eight units (one line each)

1. **The Tracking Problem and the Feedback Loop** — why open-loop drifts; error → correction; open-loop vs closed-loop.
2. **Proportional, Integral, and Derivative Control** — the full single-joint PID controller, term by term, with anti-windup.
3. **Stability, Response, and Tuning** — settle/oscillate/diverge, the response metrics, and how the gains shape them.
4. **Tracking the Whole Arm: Feedforward and Feedback** — feedforward anticipates from M7's q̇_d/q̈_d, feedback corrects; the whole arm tracks.
5. **Actuator Control** — request → delivery (deadband, saturation, rate limit), windup, the command pipeline, the feasibility envelope.
6. **Communication** — the loop as messages, publish/subscribe, latency + control rate destabilise the loop, the timing-layered architecture.
7. **Embedded Execution and Real-Time Control** — real-time = correct and on time (worst case), the periodic loop, jitter/overruns/deadlines, the real-time target.
8. **ROS 2 Integration and the Control Stack** — the closed-loop stack as nodes/topics, the lightweight tracker node, the control layer, and the capstone.

## 3. The teaching approach that held throughout

Module 8 was taught **intuition-first**, with the open-loop-vs-closed-loop contrast returned to
repeatedly before any formalism, and with one running example — the planar 2-link greenhouse arm
(L1 = 0.4, L2 = 0.3) — carried from the first drift to the final disturbance-rejecting stack. Each
unit added one real-world complication and showed the loop coping with it: first the controller
(U1–U4), then the actuator's limits (U5), then the fact that the loop is distributed and delayed
(U6), then that it must run on time every cycle (U7), then that it lives as a graph of communicating
nodes (U8). Stability was always the qualitative **settle / oscillate / diverge** picture; every
claim was demonstrated by a verified notebook (each ending "All checks passed.") and anchored by an
SVG and, at the four milestones, an interactive demo. The five-layer pedagogy (physical intuition →
visual → math → computational → system integration) and the AI Learning Companion + Global Learning
Support (English / Español / 中文简体 / Türkçe) appear on every lesson.

## 4. The capstone artifact (the Module 9 handoff)

The module's deliverable is the **control layer**:

```
tracking_controller(reference, measured_state) → actuator_command
```

- **Inputs:** `reference = (q_d, q̇_d, q̈_d)` — one sample of Module 7's reference; `measured_state = (q, q̇)` — the measured joint state.
- **Output:** `actuator_command` — the delivered effort that drives the joint toward the reference.
- **Inside:** feedforward (anticipate, from M7's q̇_d/q̈_d) + PID feedback (correct the error) + the actuator pipeline (deliver within limits). Stateful and periodic — runs once per control period on the real-time target, inside the ROS 2 tracker node.
- **Outside (Module 9):** deciding/planning the references against the world, coordinating subsystems, supervising the task — no system integration beyond the control layer.

This is the third link in the chain **velocity layer (M6) → reference layer (M7) → control layer
(M8) → integrated system (M9)**, deliberately mirroring how M6 handed M7 a velocity layer and M7
handed M8 a reference layer. The capstone verifies it end to end on the arm: near-perfect tracking
of a Module 7 reference (overall RMS ≈ 0.0000), and disturbance rejection by feedback that
feedforward alone cannot achieve (final joint error ≈ 0.012 with feedback vs ≈ 4.9 feedforward-only).

## 5. Engine and verification

A single engine, `engine/m8_engine.py`, grew **additively** across the four installments (each
installment's backup retained: `m8_engine_B_backup.py`, `m8_engine_C_backup.py`). It models the
plant as an integrator + disturbance + load + saturation + latency through the actuator — never
formal manipulator dynamics. Key components: the reference samplers (`setpoint_reference`,
`quintic_reference`, `multi_quintic`, `zoh_reference`); the `Joint` plant and `step_plant`; the
`PIDController` with anti-windup; the feedforward (`feedforward_command`, `feedforward_full`); the
`Actuator` (deadband / saturation / rate limit) and `track_reference_actuated` (full pipeline with
latency and control-rate levers); the `Bus` pub/sub broker with `loop_latency` / `run_pubsub_loop`;
the real-time loop `track_reference_rt` (jitter / overruns / rare-spike stalls) and
`track_reference_variable_delay`; and the capstone `control_layer` + `run_control_stack` +
`run_arm_control_stack`. Every asserted behaviour was verified before the notebooks were built, and
all 32 notebooks pass Restart & Run All.

## 6. The four flagship demos

- **L07 — PID Playground** (Unit 2): tune Kp/Ki/Kd live and watch the step response settle, oscillate, or diverge.
- **L17 — Actuator Bench** (Unit 5): dial the requested command and toggle deadband / saturation / rate limit; the live transfer curve and step ramp show request vs delivery.
- **L21 — Message Bus** (Unit 6): a message traverses each hop and the loop latency accumulates as the sum of the per-hop times.
- **L29 — Closed-Loop Tracking Studio** (Unit 8): the control stack closing the loop — scrub the reference, toggle feedback on/off, inject a disturbance, and watch the measured trajectory converge onto the reference and the tracking error shrink. All four are self-contained, accessible (ARIA, keyboard-operable), and use no browser storage.

## 7. Boundaries held

Held end to end and re-flagged where tempting: dynamics as **disturbance / load / friction /
saturation / model-mismatch intuition only** (no formal manipulator dynamics; joints independent,
coupling treated as a disturbance); **no control-theory formalism** (no Laplace / transfer functions
/ root-locus / Bode / Nyquist; no discrete-time / sampling / z-transform; no real-time scheduling
theory — rate-monotonic / WCET named only as out-of-scope); stability always the qualitative
settle / oscillate / diverge picture; **ROS 2 conceptual + lightweight** (the pub/sub Bus stands in
for the middleware; no rclpy / DDS / executors / QoS); and **no system integration beyond the control
layer** — planning, coordination, and supervision are Module 9. The module produces and verifies the
control layer; it does not integrate the robot.

## 8. Status and next

**Module 8 is COMPLETE** and paused at module completion, with **8 of 10 modules** of the Physical AI
Curriculum now signed off (Modules 1–8). The M6 → M7 → M8 → M9 chain is complete through M8: the
velocity layer, the reference layer, and now the control layer are all built and handed forward.
**Next:** Module 9 — the integrated autonomous system, which consumes the Module 8 control layer
`tracking_controller(reference, measured_state) → actuator_command` and wraps it in perception-driven
planning, subsystem coordination, and task supervision to harvest autonomously.
