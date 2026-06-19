---
module: 9
unit: 2
lesson: 6
type: answer_key
title: "Answer Key — Target Selection: Which Fruit, Which Pose?"
audience: coaches
---

# Answer Key 2.2 — Target Selection: Which Fruit, Which Pose?

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Filter (ripe ∧ reachable) → rank (cost/distance) → commit.

**Q2 — B.** Feasibility dominates the rank: a nearer fruit that is unripe or unreachable must never be chosen.

**Q3 — B.** Selection hands forward a target pose; IK (joint angles) and the timed path (Plan) come later.

**Q4 — B.** An empty feasible set is a valid "nothing to pick now," not a crash.

**Q5 — True.** Retaining the ranked fallback list lets Recover try the next-best fruit after a failure.

---

**Q6 — model answer.** Filter to ripe ∧ reachable: F2 drops (unripe), leaving {F1, F3}. Rank by distance: F3 (0.9) before F1 (1.4). Commit F3; fallback order [F3, F1]. F2 is nearest (0.5) but excluded by the filter because it is unripe — feasibility dominates cost.
*Grading: require F3 committed and the filter-before-rank reasoning; F2's exclusion despite nearness is the key point.*
