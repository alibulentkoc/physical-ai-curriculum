---
title: "Module 9 — System Integration: Completion Report"
module: 09
status: COMPLETE
decisions: D-071 (A), D-072 (B), D-073 (C), D-074 (D)
date: 2026-06
---

# Module 9 — System Integration: Completion Report

## What was built

Module 9 is the integration course. It takes the eight layers built across Modules 1–8 — perception (M3), inverse kinematics (M5), the velocity layer (M6), the reference layer (M7), and the control layer (M8) — and wires them, **as the real layers**, into one greenhouse harvesting robot that runs along a single workflow spine:

> **Perceive → Understand → Plan → Execute → Track → Recover**

The deliverable is an integrated, **self-healing** system. It perceives a row of fruit, selects each target, plans and executes the reach, judges whether the pick succeeded, detects and localises any failure, and recovers from it — completing the whole row with a definite, accounted-for outcome for every fruit. The entire system runs in one call, `harvest_row(world)`.

## The governing discipline

Two rules held across all eight units and are the pedagogical heart of the module:

- **Wrap, do not redefine.** Every stage calls a *real existing layer*. The integration package `modules/module09/integration/` vendors the actual M5/M6/M7/M8 libraries verbatim; the adapter `layers.py` only wires their inputs and outputs together.
- **Coordinate, do not re-theorise.** Detection is *reading* existing health signals against thresholds; recovery is *coordination plus bookkeeping* over existing layer calls. **No new estimation, planning, or control theory is introduced anywhere in Module 9.** The intelligence lives in the composition — the stage order, the seam contracts, the detection guards, and the recovery loop.

## The arc, installment by installment

- **Installment A — Units 1–2 (Perceive → Understand), D-071.** Why integration is hard; the six-stage workflow; tracing one tomato. `model_perception` (the M3 boundary, fault-injectable via noise / occlude / duplicate) and `understand` (dedupe → ripe ∧ reachable → nearest) commit a target from raw detections. Flagship: **Pipeline Data-Flow Explorer**.
- **Installment B — Units 3–4 (Understand → Plan → Execute), D-072.** `to_configuration` (the M5 IK seam, FK-verified) and `plan_reference` (the M7 planner) turn a target pose into a validated reference; the motion stack (M6 velocity + M8 control) and `execute_reference` drive it into tracked motion. Midpoint (L16): the forward path is assembled and runs once (rms ≈ 0.0001, reached), with feedback recovering from a disturbance — but no failure handling yet. Flagship: **Motion-Stack Visualizer**.
- **Installment C — Units 5–6 (Execute → Track + Failure Detection), D-073.** `track` returns a success verdict against explicit criteria (final error, RMS, pose) with a localising reason; `system_monitor` collects the health signals every layer already emits into one dashboard (*reached ≠ succeeded*, *health ≠ success*). The six-event `FAILURE_TAXONOMY`, health-signal **guards** (`run_pipeline`), and `localize` answer **What failed? → Where? → Who owns the fix?** — with the insight that where a fault *surfaces* can differ from who *owns* it. Flagship: **Failure-Injection Sandbox**.
- **Installment D — Units 7–8 (Recover + Full System Integration, capstone), D-074.** `recover` is the orchestrator: it consumes the localised fault and dispatches a targeted response by owner (re-perceive / retry / re-select / skip), tagged **retryable vs deterministic**, bounded by a retry budget with state across attempts so a transient fault recovers, a persistent one escalates at the budget, and a deterministic one escalates immediately. `harvest_row` loops the full pick cycle across a row under a ledger — **graceful degradation**: recover what it can, skip-with-reason what it can't, finish the row, never stall on one fruit. Flagship: **End-to-End Pick-Cycle Player**.

## Scope boundaries (held)

No new estimation, planning, fault-diagnosis, or control theory. Detection is thresholded reading of existing layer outputs; recovery is coordination over existing layer calls. The plant remains the qualitative M8 model. The system is explicitly **best-effort with graceful degradation**, not a guarantee that every fruit is picked; it **localises** faults but does not **diagnose** root-cause physics; it harvests in selection order, not an optimal sequence. These boundaries are stated as a deliverable (Lesson 8.3), not hidden.

## Verification

- **All 32 Module 9 notebooks** pass under Restart-and-Run-All (each ends "All checks passed."), importing the real integration package.
- **`mkdocs build --strict`** is green at **293 lesson pages** (261 + 32); every lesson page has its figure, notebook tip, and quiz injected; the four demo iframes are injected on L1.2 / L4.1 / L6.2 / L8.2 only.
- **32 SVGs** XML-valid (one figure per lesson). **4 flagship demos** parse clean with no browser storage.
- The detection and recovery substrate was smoke-tested on the real layers: occlude-all → `NO_TARGET` halt at Understand; obstacle over goal → `PLAN_INVALID` halt at Plan; strong disturbance → `TRACKING_FAILURE` + `EXCESS_EFFORT`; transient fault → recovers; persistent fault → escalates at budget; clean row → all ripe-reachable fruit harvested; mid-row injected fault → recovered or skipped while the rest harvest.

## Totals

8 units · 32 lessons · 32 notebooks · 32 SVGs · **4 demos** (L02 Pipeline Data-Flow Explorer, L13 Motion-Stack Visualizer, L22 Failure-Injection Sandbox, L30 End-to-End Pick-Cycle Player) · 32 quizzes · 32 answer keys · integration package `modules/module09/integration/`.

## Handoff to Module 10

Module 9 completes the **M6 → M7 → M8 → M9** chain: the integrated, self-healing harvester. **Module 10 — the Digital Twin Capstone** (single robot, not a fleet) takes this finished system into a mirror for simulation, visualisation, and validation. The handoff is clean: `harvest_row` exposes the whole system in one call for the twin to wrap.

**Module 9 is COMPLETE — 9 of 10 modules signed off. Paused at the Installment D milestone.**
