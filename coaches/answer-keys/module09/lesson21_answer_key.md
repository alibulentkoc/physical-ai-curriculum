---
module: 9
unit: 6
lesson: 21
type: answer_key
title: "Answer Key — The Failure Taxonomy: Integration Events"
audience: coaches
---

# Answer Key 6.1 — The Failure Taxonomy: Integration Events

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Integration events: a known signal crossing a line at a known seam — a finite list.

**Q2 — C.** SENSOR_OVERHEAT is not in the taxonomy; component physics is out of scope.

**Q3 — B.** A warning may ride on a successful run (fragile); only hard failures halt.

**Q4 — B.** Every condition is a threshold on an existing signal — no new estimator.

**Q5 — True.** The taxonomy names seam events, not internal component physics.

---

**Q6 — model answer.** Event NEAR_SINGULAR, stage Execute (planned path), severity warning. The run succeeded, so it is not a hard failure, but the manipulability signal crossed its threshold — a fragile, near-singular pass. The severity split flags fragility without calling a successful pick a failure.
*Grading: require NEAR_SINGULAR + warning + the success-with-flag reasoning.*
