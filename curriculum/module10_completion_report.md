---
title: "Module 10 — Digital Twin Capstone: Completion Report"
module: 10
status: COMPLETE
decisions: D-075 (A), D-076 (B), D-077 (C), D-078 (D)
date: 2026-06
---

# Module 10 — Digital Twin Capstone: Completion Report

## What was built

Module 10 is the capstone course. It takes the finished, self-healing greenhouse harvester from Module 9 — exposed in one call, `harvest_row(world)` — and builds a **digital twin** around it: a lightweight virtual replica that mirrors, runs, watches, forecasts, and steers the real system along a single spine:

> **Model → Mirror → Simulate → Monitor → Predict → Adapt**

The deliverable is a **twin-in-the-loop** harvester. Reality (`GroundTruth`) does the physical work; the twin (`DigitalTwin`) holds its own world copy and advises — synchronising to the real state, running the system forward, comparing reality against itself, forecasting outcomes, and pre-validating actions so the real harvest comes out better than a blind plan. The module closes the entire ten-module curriculum: a single tomato is traced through all ten modules, and the through-line from mathematics to a digital twin is made explicit.

## The governing discipline

Two rules held across all eight units and are the pedagogical heart of the module:

- **Wrap, do not redefine.** The twin never re-implements Modules 1–9. Simulation is `harvest_row` run forward on the twin's own copy; monitoring reads the existing divergence; prediction is run-ahead over the existing system. The twin substrate `modules/module10/twin/` is purely additive over the Module 9 integration package.
- **No new theory.** The twin is a small Python replica — no Gazebo/Isaac, no physics engine, no formal dynamics, no estimation, no control theory, **no machine learning**. Prediction is run-ahead / what-if; adaptation is pre-validation + action-selection. The intelligence lives in *how the existing system is used*, not in new machinery.

A second discipline is specific to this module: **reality and the twin are represented separately**, with an explicit sim-to-real gap. Unmodeled effects live in reality; the twin only knows what it has been calibrated with. That separation is the engine of the monitoring, prediction, and adaptation lessons.

## The arc, installment by installment

- **Installment A — Units 1–2 (Model → Mirror), D-075.** What a digital twin is (a living mirror of the robot, distinct from a model and from a simulation); what is being twinned (the Module 9 system as the physical asset); building the mirror by **state synchronisation** (`DigitalTwin.sync`), and what it means when the mirror drifts (sync error). Flagship: **Twin vs Model vs Simulation** (L1.2). The spine's *Model* and *Mirror* are lit.
- **Installment B — Units 3–4 (Simulate + the Sim-to-Real Gap), D-076; midpoint.** The twin learns to **run** (`DigitalTwin.simulate` — `harvest_row` forward on a copy, the sandbox for risk-free what-ifs, determinism for replay) and to **know its limits** (the sim-to-real gap: why twin and reality diverge, measuring the gap via `outcome_gap`, calibrating by modeling a known effect — *modeling, not learning*, with a residual that always remains). Midpoint at L16: **faithful but intentionally imperfect.** Flagship: **Sim-to-Real Gap Explorer** (L4.1).
- **Installment C — Units 5–6 (Monitor + Predict), D-077.** **Monitoring** as a Reality ↔ Twin comparison answering *what is happening now?* — divergence is the signal (`monitor`), with the move from divergence to diagnosis. **Prediction** as run-ahead simulation answering *what is likely to happen next?* — lookahead and what-if (`predict`, `compare_futures`), and the honest limits of prediction (a forecast is only as faithful as the twin). Flagship: **Lookahead & What-If Explorer** (L6.2).
- **Installment D — Units 7–8 (Adapt + Capstone & Curriculum Close), D-078.** **Adaptation** as pre-validation (`prevalidate` — rehearse an action in the twin before committing) + action-selection (`select_action` — rank candidate forecasts by a stated score and choose), assembled into the **twin-in-the-loop cycle** (`twin_in_the_loop` — monitor → re-sync if drifted → predict → adapt). **Capstone:** the *Self-Improving Greenhouse Harvest* runs the full spine on one row — the twin foresees a doomed pick and adapts, beating the blind plan with equal harvest and less wasted effort (*self-improving = loop-improved, not learned*). **Curriculum close:** one tomato traced through all ten modules (M1 vector → M10 twin), and the through-line *represent → perceive → reach → move → integrate → twin* with scope boundaries framed as the edges of a foundation. Flagship: **Twin-in-the-Loop Harvest** (L8.2).

## Scope boundaries (held)

No new estimation, control theory, dynamics, or machine learning anywhere in Module 10. Simulation is `harvest_row` run forward; monitoring is reading divergence; prediction is run-ahead; calibration models a *known* effect (not fitting); adaptation is pre-validation + action-selection over a *given* candidate set with *stated* rules (`ok`, `score`) — no RL, no adaptive control, no optimization framework. The twin is lightweight (no Gazebo/Isaac); reality and twin are separate with an explicit, preserved sim-to-real gap; a single robot / twin / greenhouse throughout. These boundaries are stated as deliverables (the limits-of-prediction lesson and the course close), not hidden.

## Verification

- **All 32 Module 10 notebooks** pass under Restart-and-Run-All (each ends "All checks passed."), importing the real Module 9 integration package and the additive twin substrate.
- **`mkdocs build --strict`** is green at **325 lesson pages** (293 + 32); every lesson page has its figure, notebook tip, and quiz injected; the four demo iframes are injected on L1.2 / L4.1 / L6.2 / L8.2 only.
- **32 SVGs** XML-valid (one figure per lesson); the twin-in-the-loop ring (7.3) and the ten-module pipeline (8.3) visually confirmed.
- **4 flagship demos** parse clean with no browser storage.
- The twin substrate was verified end to end: sync zeroes divergence; an unmodeled effect opens a measurable `outcome_gap`; calibration closes it and a new effect reopens it; `monitor` is quiet in sync and alerts on drift; `predict`/`compare_futures` run candidates forward; `prevalidate` rejects a doomed pick and accepts a clear one; `select_action` ranks the better action; `twin_in_the_loop` re-syncs on drift and chooses; the capstone's twin-in-the-loop run scores at least as well as the blind plan with less wasted effort.

## Totals

8 units · 32 lessons · 32 notebooks · 32 SVGs · **4 demos** (L02 Twin vs Model vs Simulation, L13 Sim-to-Real Gap Explorer, L22 Lookahead & What-If Explorer, L30 Twin-in-the-Loop Harvest) · 32 quizzes · 32 answer keys · 1 midpoint assessment + coaches' key · twin substrate `modules/module10/twin/`.

## Curriculum close

Module 10 completes the spine **Model → Mirror → Simulate → Monitor → Predict → Adapt** and, with it, the ten-module Physical AI curriculum. The capstone demonstrates the whole arc on one harvest; the close traces one tomato through all ten modules and names the through-line from mathematics to a digital twin. The handoff is no longer to a next module — it is to the student, who can now represent, perceive, reach, move, integrate, and twin a robot.

**Module 10 is COMPLETE — 10 of 10 modules signed off. Paused at full curriculum completion.**
