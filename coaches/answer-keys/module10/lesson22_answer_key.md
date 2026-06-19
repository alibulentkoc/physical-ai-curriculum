---
module: 10
unit: 6
lesson: 6.2
type: answer_key
title: "Answer Key — 6.2 Lookahead and What-If"
---

# Answer Key — Lesson 6.2

**MC1:** A — what-if runs several candidate futures and compares outcomes.
**MC2:** A — lookahead runs far enough ahead to foresee an event in time to act.
**MC3:** A — a fixed seed makes differences attributable to the scenario, not noise.
**TF4:** True — comparing futures is the seed of action selection (Unit 7).
**TF5:** False — what-if trains nothing; it is repeated run-ahead of the existing system.

**Short 6 — model answer.** Sync the twin to the current state, then run two what-if futures from the *same* seed: a nominal one and one with the obstacle injected. Compare their outcomes with the outcome gap — the fruit harvested in the nominal future but skipped in the obstacle future is precisely what the obstacle costs. The fixed seed guarantees the difference is due to the obstacle, not randomness. *Grading:* full credit for same-start/same-seed comparison and reading the cost from the outcome difference.
