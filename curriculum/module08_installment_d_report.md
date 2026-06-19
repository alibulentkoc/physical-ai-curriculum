---
title: "Module 8 — Installment D Report (Units 7–8, Capstone)"
module: 8
installment: D
units: [7, 8]
lessons: "L25–L32"
decision: D-070
status: DELIVERED — Module 8 COMPLETE
date: 2026-06
---

# Module 8 — Installment D Report (Units 7–8, Capstone)

> **SUMMARY.** Installment D delivers the final two units of Module 8 — **Unit 7 Embedded Execution and Real-Time Control** and **Unit 8 ROS 2 Integration and the Control Stack** — lessons **L25–L32**, including the **L29 Closed-Loop Tracking Studio** demo, the **Module 8 capstone**, and the **control-layer handoff to Module 9**. Built straight through to module completion per the architect directive (no further installment reviews within the module). `mkdocs build --strict` passes at **261 lesson pages**. **Module 8 is COMPLETE — 8 of 10 modules signed off.**

---

## 1. What this installment had to do

Installments A–C built the controller (PID, stability, feedforward + feedback), the actuator pipeline, and the communication layer, and ended on a warning: the inner loop cannot tolerate much delay before it goes unstable, so its timing must be small **and** predictable. Installment D had to (1) deliver real-time execution — what it means and how the inner loop achieves it; (2) assemble the whole module into a ROS 2 control stack; and (3) package the result as the **control layer** Module 9 will consume — while holding three boundaries: **no formal dynamics, no advanced control theory, no system integration beyond the control layer.**

## 2. Unit 7 — Embedded Execution and Real-Time Control (L25–L28)

- **L25 (7.1) What real-time means.** Real-time = correct **and on time**; the figure of merit is the **worst case, not the average**. Verified: a bounded-interval loop is stable, while a loop far faster on average but with rare long stalls is unstable (mean interval ≈ 14.7 steps yet worst ≈ 182). Hard vs soft real-time; the inner loop is hard.
- **L26 (7.2) The periodic control loop.** The inner loop as a periodic task — sense → compute → actuate every control period $T_c$ (rate $1/T_c$), within a per-period timing budget. Verified: a fixed-rate periodic loop tracks a moving reference (RMS ≈ 0.0007, 101 updates). The period is the execution of the continuous control law (held between samples), framed qualitatively (no discrete-time/$z$-transform).
- **L27 (7.3) Jitter, overruns, missed deadlines.** The three timing hazards all **add loop delay** — the Unit-6 destabiliser. Verified at identical gains: deterministic stable, jitter unstable, overruns unstable. The fix is predictable, not faster, timing.
- **L28 (7.4) The real-time target.** The inner loop runs on a protected, deterministic target (stable); the same loop on a best-effort target jitters and goes unstable; the slow outer layer tolerates loose timing (RMS ≈ 0.086). Placement rule: latency-critical → real-time, latency-tolerant → best-effort — the 6.4 timing split realised.

## 3. Unit 8 — ROS 2 Integration and the Control Stack (L29–L32)

- **L29 (8.1) The closed-loop control stack in ROS 2.** The loop as a node/topic graph: sensor node → `joint/state` → controller node (tracker) → `joint/command` → actuator node → loop closed — the 6.2 publish/subscribe pattern now carrying real control, with the controller node on the Unit-7 real-time target. Verified: tracks via the two topics, RMS ≈ 0.0015. **Flagship demo: L29 Closed-Loop Tracking Studio.**
- **L30 (8.2) A lightweight ROS 2 tracker node.** Two subscriptions, one publication, one control-law evaluation per cycle — **intelligence (the law) vs plumbing (the node)**. Verified: one command published per state (1001 → 1001).
- **L31 (8.3) The control layer: the Module 9 handoff.** `tracking_controller(reference, measured_state) → actuator_command`, completing **velocity layer (M6) → reference layer (M7) → control layer (M8) → integrated system (M9)**. Inside: feedforward + feedback + actuator; outside (Module 9): planning, coordination, supervision. Verified: the interface returns an actuator command (feedforward + feedback, delivered) and tracks closed-loop.
- **L32 (8.4) Capstone.** The 2-link greenhouse arm tracks a Module 7 reference through the closed-loop control layer (overall RMS ≈ 0.0000), and **feedback rejects a disturbance feedforward alone cannot** (final joint error ≈ 0.012 with feedback vs ≈ 4.9 feedforward-only). Produces the control layer; recaps Units 1–8; bridges to Module 9.

## 4. The capstone artifact — the Module 9 handoff

The capstone produces the **control layer**:

```
tracking_controller(reference, measured_state) → actuator_command
```

where `reference = (q_d, q̇_d, q̈_d)` is a Module 7 sample and `measured_state = (q, q̇)` is the measured joint state. It combines **feedforward** (anticipation, consuming M7's q̇_d/q̈_d), **PID feedback** (correction), and the **actuator pipeline** (delivery within limits), and is stateful and periodic (runs once per control period on the real-time target). This is the third link in the chain **velocity layer (M6) → reference layer (M7) → control layer (M8) → integrated system (M9)**; Module 9 integrates it into a full autonomous system. Everything beyond the interface — planning the world, coordinating subsystems, supervising the task — is Module 9, deliberately left out of Module 8.

## 5. Engine and verification

Extended **additively** (every A/B/C function unchanged; C-state backup at `engine/m8_engine_C_backup.py`):

- **Unit 7:** `track_reference_variable_delay` (per-step measurement-delay schedule, for the worst-case-vs-average demonstration); `track_reference_rt` (periodic loop with `period_steps`, `jitter_steps`, `overrun_prob`, and rare-`spike_prob`/`spike_steps` heavy-tail stalls; reports updates, missed deadlines, mean/max interval).
- **Unit 8:** `control_layer(...)` → the stateful `tracking_controller(reference_sample, measured_state, dt) → (actuator_command, info)` with `.reset()` (the M9 handoff); `run_control_stack` (ROS-2-style pub/sub closed loop over the `Bus`, topics `joint/state` + `joint/command`); `run_arm_control_stack` (N-joint closed loop for the capstone).

All asserted behaviours were verified before the notebooks were built; all 8 notebooks pass Restart & Run All ("All checks passed.").

## 6. Deliverables

8 lessons (L25–L32) · 8 SVGs (m08-l25..l32, XML-valid; L29/L32 spot-rendered clean) · 8 notebooks (all "All checks passed.") · **1 flagship demo** (L29 Closed-Loop Tracking Studio — scrub the reference, toggle feedback on/off, inject a disturbance; watch the measured trajectory converge and the tracking error shrink; accessible, ARIA, no browser storage) · 8 quizzes (5 MC + 3 short) · 8 answer keys. Generator unit titles added for ("08","07")/("08","08"); nav extended with Units 7–8 ("· demo" on 8.1/L29); `mkdocs build --strict` passes at **261 lesson pages**.

## 7. Boundaries held

**No formal dynamics** (the plant stays integrator + disturbance + load + saturation + latency through the actuator; joints independent, coupling treated as disturbance). **No advanced control theory** (real-time scheduling formalism — rate-monotonic / WCET — named only as out-of-scope; stability stays qualitative settle/oscillate/diverge; no discrete-time/sampling/$z$-transform). **ROS 2 conceptual + lightweight** (the pub/sub `Bus` stands in for the middleware; no `rclpy`/DDS/executors/QoS). **No system integration beyond the control layer** (planning, coordination, supervision are Module 9).

## 8. Status and next

**Module 8 is COMPLETE** — Installments A–D (D-066 launch through D-070) plus a midpoint assessment. Totals: **8 units · 32 lessons · 32 notebooks · 32 SVGs · 4 demos (L07, L17, L21, L29) · 32 quizzes · 32 answer keys · 1 midpoint assessment**; site at **261 lesson pages**, `mkdocs build --strict` green. **Paused at module completion** per directive — no Module 9 work begun. **Next:** Module 9 — the integrated autonomous system, which consumes the Module 8 control layer.
