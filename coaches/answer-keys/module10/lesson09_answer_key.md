---
module: 10
unit: 3
lesson: 3.1
type: answer_key
title: "Answer Key — Running the System Inside the Twin"
---

# Answer Key — Lesson 3.1

**MC1:** B — running the M9 harvester forward on the twin's own world.
**MC2:** B — a fresh copy of the twin's world (reality untouched, repeatable).
**MC3:** B — none; it reuses harvest_row verbatim.
**MC4:** B — a reflection into a predictor.
**TF5:** True — simulating on the live state would consume it; run on a copy.

**Short answer 6 — model response.**
harvest_row mutates the world as it picks (fruit marked, arm moved). Simulating on the twin's live state would consume it, so the twin couldn't run a second scenario from the same start nor keep mirroring. A fresh copy each time keeps the twin's state intact, making simulation repeatable and non-destructive.

*Grading notes (3 pts): (1) harvest_row mutates the world; (2) live-state simulation would consume/destroy the state; (3) the copy gives repeatability + non-destructiveness. Full credit needs the mutation reason plus one consequence.*
