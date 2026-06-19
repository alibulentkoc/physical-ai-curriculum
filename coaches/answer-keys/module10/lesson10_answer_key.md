---
module: 10
unit: 3
lesson: 3.2
type: answer_key
title: "Answer Key — The Twin as a Sandbox"
---

# Answer Key — Lesson 3.2

**MC1:** B — inject faults/what-ifs and study outcomes safely on a copy.
**MC2:** B — they run on a copy, isolated from reality.
**MC3:** B — skip that fruit and harvest the rest (graceful degradation).
**MC4:** B — reuses Module 9's existing injection mechanism.
**TF5:** True — a sandbox result is only as trustworthy as the twin is faithful.

**Short answer 6 — model response.**
The obstacle makes that fruit's plan invalid, so the harvester skips it (localised reason) and harvests the rest — all-but-one harvested, one skipped. Because simulate ran on a copy, the twin's own state and the real robot are unchanged: a fresh simulate() with no injection still predicts the clean harvest.

*Grading notes (3 pts): (1) blocked fruit skipped via plan failure, rest harvested; (2) ran on a copy → reality + twin state unaffected; (3) re-run is clean (non-destructive). Full credit needs the predicted outcome and the non-destructive confirmation.*
