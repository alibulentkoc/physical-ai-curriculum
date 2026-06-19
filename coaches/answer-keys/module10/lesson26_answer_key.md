---
module: 10
unit: 7
lesson: 7.2
type: answer_key
title: "Answer Key — 7.2 Twin-Informed Decisions"
---

# Answer Key — Lesson 7.2

**MC1:** A — pre-validate several candidates, then choose the better-forecast one.
**MC2:** A — the score is a simple, stated rule (kept readable for accountability).
**MC3:** A — the candidate set is given and small; ranking-and-picking is not searching a space.
**MC4:** A — clear_path (4,0) outranks ignore_obstacle (3,1): more harvested, fewer skipped.
**TF5:** True — changing the score changes the choice predictably, which is what makes it accountable.

**Short 6 — model answer.** Candidate forecasts must be compared from the same, current twin state because action-selection only makes sense relative to one shared starting point; ranking forecasts run from different or stale states would not be a fair comparison, so the twin is synced to "now" before the candidates are pre-validated. *Grading:* full credit for "same shared current state → fair comparison," with mention of syncing first.
