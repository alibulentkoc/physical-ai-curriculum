---
module: 10
unit: 3
lesson: 3.3
type: answer_key
title: "Answer Key — Replay and Reproduce: Determinism"
---

# Answer Key — Lesson 3.3

**MC1:** B — same world + same seed → identical outcome.
**MC2:** B — replay a harvest and run controlled comparisons.
**MC3:** B — changes exactly one thing, so any difference is attributable to it.
**MC4:** B — inherited from Module 9's seeded execution.
**TF5:** True — a difference under identical inputs means an input actually changed.

**Short answer 6 — model response.**
With a fixed world and seed, M9's seeded execution is deterministic, so identical inputs must yield identical outcomes. A difference means an input was not actually identical — something varied (different seed, mutated world, stray injection, leaked state). It's a signal to find the hidden variation, not inherent randomness.

*Grading notes (3 pts): (1) determinism ⇒ identical inputs give identical outputs; (2) a difference implies an input changed; (3) names a plausible hidden variation. Full credit needs the determinism logic plus the "find the variation" conclusion.*
