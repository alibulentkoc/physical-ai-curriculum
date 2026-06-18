---
module: 7
unit: 7
lesson: 2
type: answer_key
title: "Answer Key — Validating a Trajectory: The Complete Check"
audience: coaches
---

# Answer Key 7.2 — Validating a Trajectory: The Complete Check

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Validation samples densely along the whole reference.

**Q2 — B.** valid = AND of all individual checks.

**Q3 — B.** A failed check localizes the problem and dictates the remedy.

**Q4 — B.** Validation is the gate between planning and execution.

**Q5 — B.** Whole-arm collision-free is part of the suite.

---

**Q6 — model answer.** Endpoints match the requested start/goal; boundary rest (zero velocity/acceleration at the ends for rest-to-rest); continuity (no position/velocity/acceleration jumps); within the velocity limit; within the acceleration limit; collision-free for the whole arm along the path; and reachable at every configuration. The overall verdict is valid = AND of all of these — every check must pass, evaluated by dense sampling. A failed check names the remedy.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** A velocity violation is a timing problem, so the remedy is to re-time (slow down / time-scale) the trajectory — not re-plan. The collision-free and reachability checks are about geometry (the path's shape), which slowing down doesn't change, so they remain True; only the speed-dependent checks were affected. This is the localization benefit: the failing check tells you it's a timing fix, and the unchanged checks confirm the geometry was fine.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** A trajectory can be feasible and collision-free at every sampled instant yet still have a discontinuity at a segment join — e.g. a velocity jump where two pieces meet with mismatched speeds. No single-point check catches this, because each point individually is fine; only comparing successive samples reveals the leap. A velocity discontinuity is dangerous: it demands an instantaneous change the hardware can't deliver and the tracker can't follow, so validation must test continuity explicitly.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Validating only the endpoints (interior violations get missed).
- Not localizing the failed check to its remedy (re-time vs re-plan vs fix).
- Skipping continuity; executing an unvalidated trajectory.
