---
title: "Module 8 — Installment C (Units 5–6) — Milestone Report"
module: 08
installment: C
units: [5, 6]
lessons: "L17–L24"
decision: D-069
status: delivered — paused for architect review
date: 2026-06
---

# Module 8 — Installment C Milestone Report

## EXECUTIVE SUMMARY

Installment C delivers **Units 5 (Actuator Control) and 6 (Communication)**, lessons **L17–L24**, taking the Module 8 control stack from "the controller decides" to "a real, distributed, delay-bound, actuator-limited system moves the arm." Unit 5 replaces the Units 1–4 fiction that the command reaches the joint exactly: an **actuator** converts a requested command into a delivered effort shaped by **deadband, saturation, and a rate limit**, which produce **integral windup** (cured by the Unit-2 anti-windup clamp), a **deadband/stiction stall** that only **integral action** can clear, and a **feasibility envelope** that ties back to Module 7. Unit 6 replaces the single-place, instantaneous-loop fiction: the loop is **messages** between separate subsystems on a **publish/subscribe** bus, where **latency and a finite control rate** destabilise a fixed-gain loop (the Unit-3 lesson, now communication-sourced), motivating a **data-flow architecture layered by timing** — a latency-critical inner loop and latency-tolerant outer layers — that frames real-time (Unit 7) and the ROS 2 stack (Unit 8).

All artifacts are in the repo and verified: 8 lessons, 8 SVGs, 8 notebooks (all "All checks passed."), 2 flagship demos (L17 Actuator Bench, L21 Message Bus), 8 quizzes, 8 answer keys. `mkdocs build --strict` passes at **253 lesson pages** (245 + 8). **Paused at the Installment C milestone.**

---

## 1. Decision-id reconciliation

Module 8: launch **D-066**, Installment A **D-067**, Installment B **D-068**, **Installment C = D-069** (this report). Installment D (Units 7–8 + capstone) will be D-070. No content impact.

## 2. What was delivered

**Unit 5 — Actuator Control (L17–L20).**
- **5.1 The Actuator: From Requested Command to Delivered Effort** — the request→delivery converter; deadband, saturation, rate limit; the transfer characteristic. Flagship demo **L17 Actuator Bench**.
- **5.2 Saturation and Integral Windup** — saturation degrades tracking and feeds windup; the anti-windup clamp cures it (≈69% vs ≈18% overshoot, same gains).
- **5.3 Deadband, Stiction, and Why Integral Wins the Last Millimetre** — P/PD stall short (|e| ≈ 0.44); integral reaches the target (|e| ≈ 0.003).
- **5.4 The Command Pipeline and the Feasibility Envelope** — the full pipeline; the envelope decides trackability (gentle: no clip, RMS ≈ 0; aggressive: ~60% clipped, RMS ≈ 0.29); ties back to Module 7 feasibility.

**Unit 6 — Communication (L21–L24).**
- **6.1 The Robot as a Nervous System: The Loop as Messages** — distributed subsystems; loop latency = Σ hops. Flagship demo **L21 Message Bus**.
- **6.2 Publish and Subscribe: Nodes, Topics, and Messages** — the pub/sub pattern and decoupling; ROS 2 placed as one implementation.
- **6.3 Latency and Control Rate: How Communication Destabilises the Loop** — latency + finite control rate → loop delay; fixed-gain loop marches stable→unstable; motivates real-time.
- **6.4 A Data-Flow Architecture Layered by Timing** — latency-critical inner loop vs latency-tolerant outer layers; verified asymmetry (inner latency unstable; slow outer reference stable, RMS ≈ 0.086); frames Units 7–8.

Each lesson uses the 12-section template + the AI Learning Companion and Global Learning Support (English/Español/中文简体/Türkçe) blocks. Demo lessons are 5.1 (L17) and 6.1 (L21).

## 3. Engine

`engine/m8_engine.py` was extended **additively** — every Installment-A/B function is unchanged, with a B-state backup at `engine/m8_engine_B_backup.py`.

- **Unit 5:** `Actuator(u_max, deadband, rate_max)` (`.deliver`, `.characteristic`, `.reset`, `clipped`/`rate_limited` flags); `apply_stiction(net, qd, stiction)`; `step_plant(plant, u_delivered, dt, stiction, extra_disturbance)`; `track_reference_actuated(...)` (full reference→controller→actuator→plant pipeline, with `sensor_delay_steps` and `control_period_steps` timing levers; reports requested vs delivered effort and clip/rate fractions and RMS); `feasibility_envelope(actuator)`.
- **Unit 6:** `Bus` (`subscribe`, `publish`, `latest`, `topics`); `loop_latency(hops)`; `latency_to_steps(latency, dt)`; `zoh_reference(ref, hold_T)`; `run_pubsub_loop(...)` (the loop run as messages over the Bus, latency realised from the summed hops).

## 4. Verification

- **Engine behaviours** verified before the notebook build: same request → distinct deliveries (5/0/3); saturation degrades tracking and windup (≈69%) vs anti-windup (≈18%); deadband/stiction stall (0.44) vs integral (0.003); envelope clean-vs-clipped (RMS ≈ 0 vs ≈ 0.29); latency sweep and control-rate sweep each march stable→unstable; pub/sub loop runs through `joint/state`/`joint/command` and `loop_latency` = Σ hops; inner-loop latency unstable while a slow outer reference stays stable (RMS ≈ 0.086).
- **Notebooks:** all 8 executed headlessly (Restart & Run All); each prints **"All checks passed."**
- **SVGs:** all 8 XML-valid; spot-rendered (L17/L23/L24) and corrected for layout.
- **Quizzes:** all 8 parse to 5 MC + 3 short; boilerplate identical to the L16 reference (title + questions array swapped).
- **Site:** generator produced all 8 pages with [1 SVG, notebook, quiz] (+ demo on L17/L21); validator clean; `mkdocs build --strict` exits 0 at **253 lesson pages**; both demos and all 8 quizzes copied to the served dirs; figures injected on every Visual Explanation.

## 5. Boundaries held (§9 + the three rulings)

- **Unit 5 plant-level only:** no motor electrodynamics, no current loops, no formal actuator dynamics. Actuator = static transfer characteristic (deadband + saturation) + rate limit; stiction = plant-level static/Coulomb friction; plant unchanged (integrator + disturbance + saturation), driven by the delivered effort.
- **Unit 6 conceptual:** publish/subscribe is a **pattern** (nodes/topics/messages, decoupling), not a framework; **ROS 2 named only** as the Unit 8 implementation.
- **L23 qualitative:** control rate framed as "acts N times per second on stale info"; stability stays envelope-based (settle/oscillate/diverge); no discrete-time/sampling theory, no Laplace/Nyquist/phase-margin.
- **L21 analogy with limits:** the nervous-system framing is flagged as an analogy for "distributed and delayed," not a model of computation.
- No control-theory formalism anywhere; M6→M7→M8→M9 chain intact; the Unit-5 envelope ties to Module 7 feasibility and the Unit-6 timing split sets up Units 7–8.

## 6. Repository changes

- `modules/module08/lessons/lesson17..24_*.md` — 8 lessons.
- `assets/diagrams/m08-l17..l24-*.svg` — 8 diagrams (mirrored to `site_src/assets/` by the generator).
- `modules/module08/notebooks/lesson17..24_*.ipynb` — 8 notebooks.
- `modules/module08/demos/lesson17_actuator_bench.html`, `lesson21_message_bus.html` — 2 demos.
- `modules/module08/quizzes/lesson17..24_quiz.html` — 8 quizzes.
- `coaches/answer-keys/module08/lesson17..24_answer_key.md` — 8 answer keys.
- `engine/m8_engine.py` (extended) + `engine/m8_engine_B_backup.py` (A+B backup).
- `tools/generate_site_pages.py` — unit titles ("08","05")/("08","06").
- `mkdocs.yml` — Units 5–6 nav.
- `site_src/module08/lesson17..24.md` + served demo/quiz/asset copies (generated).
- Tracking: `curriculum/PROJECT_STATE.md`, `curriculum/master_progress.md`, `curriculum/ARCHITECT_DECISIONS.md` (D-069), and this report.

## 7. Milestone

**Module 8 status after Installment C:** 24 of 32 lessons · 24 notebooks (all pass) · 24 SVGs · 3 demos (L07, L17, L21) · 24 quizzes · 24 answer keys · 1 midpoint assessment. **Paused at the Installment C milestone for architect review.** Installment D (Units 7–8 + capstone, D-070) is **not** auto-started.
