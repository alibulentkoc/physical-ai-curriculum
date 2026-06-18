---
module: 7
unit: 4
lesson: 1
type: answer_key
title: "Answer Key — Why Cartesian Space? Straight-Line Tool Motion"
audience: coaches
---

# Answer Key 4.1 — Why Cartesian Space? Straight-Line Tool Motion

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Forward kinematics is nonlinear, so a joint move curves the tool path.

**Q2 — B.** Interpolate the tool path, then solve IK at each sample.

**Q3 — B.** Cartesian planning controls the tool path, at the cost of computation and new failure modes.

**Q4 — B.** A straight path can leave the workspace even with reachable endpoints.

**Q5 — B.** Cartesian moves straighten the tool path; the joint path curves.

---

**Q6 — model answer.** Because the task constrains the tool's path through space, not just the endpoints — e.g. approaching a fruit straight along its stem axis, inserting a peg, or following a weld seam. A joint move only guarantees smooth joint motion and leaves the tool path curved, so it can't promise 'straight in' or 'along this line.' Cartesian planning designs the tool path directly and derives the joint motion from it via IK.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** Recipe: define the tool path p(t)=p0+(p1−p0)s(t) with a smooth time scaling s(t), then solve inverse kinematics q(t)=IK(p(t)) at each sampled time. Costs: (1) IK must be solved many times along the path (computation); (2) every path point must be reachable — a straight line can leave the workspace even with reachable endpoints; (3) the path can pass near a singularity, where the required joint rates blow up.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** The straight line between the two reachable endpoints can pass through a point outside the workspace — for the planar arm, through the inner hole (r < L1−L2) or beyond the reach (r > L1+L2). Reachability of the endpoints doesn't imply reachability of every point on the connecting line, so IK fails partway and the Cartesian move is infeasible (even though a joint move between the same endpoints would succeed).
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Using a joint move where the tool path matters (approaches, insertions, seams).
- Assuming reachable endpoints imply a reachable straight line between them.
- Ignoring singularities on the path; forgetting orientation must also be interpolated.
