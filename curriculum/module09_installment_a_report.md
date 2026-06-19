---
title: "Module 9 — Installment A Report (Units 1–2)"
module: 09
installment: A
decision: D-071
status: delivered
---

# Module 9 · Installment A — Perceive → Understand

**Scope.** Units 1–2, lessons L01–L08. The integration course launches: the seams between the real M3–M8 layers are the work, not the parts. Running example: planar 2-link arm L1=0.4, L2=0.3 (canonical, reconciled at re-base).

**Unit 1 — Why integration, the workflow, tracing one tomato.** Integration is hard because the seams are where systems break; the six-stage workflow **Perceive → Understand → Plan → Execute → Track → Recover** is introduced as the data-flow contract from a detection to a harvested fruit.

**Unit 2 — Perception → Understand.** `model_perception(world, …)` is the M3 perception boundary as Module 9 consumes it (fault-injectable: noise / occlude / duplicate). `understand(detections, world) → (targets, current_target)` dedupes, filters to ripe ∧ reachable, and selects the nearest — committing a target or returning None.

**Flagship A — Pipeline Data-Flow Explorer (L1.2):** trace one detection through the stages.

**Substrate.** Integration package `modules/module09/integration/`: vendored real M5/M6/M7/M8 layers verbatim, the greenhouse `world.py`, and the `layers.py` adapter.

**Boundaries.** Wrap don't redefine; no new perception theory; canonical 0.4/0.3 arm locked. **APPROVED (D-071).**
