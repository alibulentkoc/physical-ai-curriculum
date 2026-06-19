---
module: 10
unit: 4
lesson: 4.2
type: answer_key
title: "Answer Key — Measuring the Gap"
---

# Answer Key — Lesson 4.2

**MC1:** B — the predicted harvest vs the actual harvest (sets + attempts).
**MC2:** B — localisable, directional, trackable.
**MC3:** B — twin predicted F3 harvested but reality did not (too optimistic).
**MC4:** B — existing harvest_row outputs (harvested/skipped sets, picks).
**TF5:** True — measuring the gap (a number) is what makes it actionable.

**Short answer 6 — model response.**
The outcomes agree on every fruit except F3: the twin predicted F3 harvested, reality skipped it — the twin was too optimistic about F3 (didn't model what stopped the real pick). No attempt diffs, so F3's fate is the only divergence. The gap is small (n_diffs=2, one fruit) and directional, telling calibration where to look: add the missing effect on F3.

*Grading notes (3 pts): (1) only F3 differs; (2) direction = too optimistic (predicted harvested, actually skipped); (3) implication for calibration / which fruit. Full credit needs the direction plus the localisation to F3.*
