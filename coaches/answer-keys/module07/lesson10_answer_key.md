---
module: 7
unit: 3
lesson: 2
type: answer_key
title: "Answer Key — Synchronizing Multiple Joints"
audience: coaches
---

# Answer Key 3.2 — Synchronizing Multiple Joints

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** A shared clock makes all joints start and finish together (coordinated).

**Q2 — B.** T* = max over joints of each joint's minimum feasible time.

**Q3 — C.** Only the bottleneck joint runs at its limit; the rest are below it.

**Q4 — C.** The bottleneck is whichever joint needs the most time; with unequal limits it may not be the largest-displacement joint.

**Q5 — B.** Independent timing breaks coordinated arrival and bends the configuration-space path.

---

**Q6 — model answer.** For each joint compute its minimum feasible time T_i^min from its displacement and limit (for a quintic, 15|Δq_i|/(8·v_max)). The synchronizing duration is T* = max_i T_i^min — the slowest-limited joint. Then every joint runs its polynomial over the same [0,T*]: the bottleneck joint runs at its limit, and all faster joints are stretched (slowed) to finish at the same time, giving coordinated arrival.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** Because the bottleneck depends on displacement relative to the joint's limit, not displacement alone. A joint with a small displacement but a very low velocity (or acceleration) limit can need more time than a large-displacement joint with a high limit. Computing each joint's T_i^min and taking the maximum reveals the true bottleneck.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** Coordinated: all joints share one time scaling over a common duration, so their ratios are fixed for all t and they start and arrive together — the configuration sweeps the straight joint-space segment. Independent: each joint runs on its own clock and finishes whenever it can, so they arrive at different times, the arm appears to settle joint-by-joint, and the configuration-space path bends.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Picking T arbitrarily (too short violates the bottleneck's limits).
- Assuming the largest-displacement joint is always the bottleneck.
- Checking only velocity when acceleration/jerk limits can also set the bottleneck.
