---
module: 10
unit: 7
lesson: 7.1
type: answer_key
title: "Answer Key — 7.1 Pre-Validating Actions in the Twin"
---

# Answer Key — Lesson 7.1

**MC1:** A — pre-validation runs a candidate action forward in the twin before committing it; no learning or optimization.
**MC2:** A — the acceptance test is a simple, stated rule a human can read and edit.
**MC3:** A — it reuses `simulate` (the Unit 6 run-ahead) applied to a candidate action.
**TF4:** True — the rehearsal runs on the twin's own copy, so reality is untouched.
**TF5:** False — a verdict is only as trustworthy as the twin's calibration (it inherits the sim-to-real gap).

**Short 6 — model answer.** Pre-validation runs the *existing* system on a candidate action inside the twin and applies a *stated* accept/reject rule to the forecast; no parameters are updated (so it is not learning) and no objective is searched over a space (so it is not optimization). *Grading:* full credit for naming both — existing-system run + stated rule — and tying each to "not learning" and "not optimization."
