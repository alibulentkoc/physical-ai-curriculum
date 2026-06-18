---
module: 7
unit: 5
lesson: 4
type: answer_key
title: "Answer Key — Feasibility Across the Whole Trajectory: Reachability, Limits, and the Workspace"
audience: coaches
---

# Answer Key 5.4 — Feasibility Across the Whole Trajectory: Reachability, Limits, and the Workspace

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Feasibility must hold at every point along the trajectory.

**Q2 — B.** Velocity/acceleration violations are timing-fixable (slow down).

**Q3 — B.** Reachability is geometric: needs a different path, not slowing.

**Q4 — B.** A momentary interior violation requires dense sampling to catch.

**Q5 — B.** Joint limits, velocity, acceleration, reachability.

---

**Q6 — model answer.** Checks: (1) joint-angle limits — geometric; (2) velocity limits — timing-fixable; (3) acceleration limits — timing-fixable; (4) reachability of every Cartesian path point — geometric. Velocity/acceleration violations mean the motion is just too fast (slow down). Joint-limit and reachability violations mean the trajectory wants a pose or point that can't exist (change the path). All must hold at every sampled point.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** Slowing down divides velocities by k and accelerations by k², so a large enough stretch always brings speed/acceleration peaks under their limits — those are about how fast the motion runs. A reachability violation is about geometry: a tool point lies outside the workspace, so no joint configuration realizes it, at any speed. The clock has no effect on whether a point can be reached; only a different path (rerouting, a via-point, reorientation) can fix it.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** It's a geometric violation, so slowing down won't help — the path itself must change to keep that joint within range. The minimal fix is to reroute the trajectory through an intermediate configuration that stays within the joint limit while preserving the endpoints — i.e. insert a via-point and re-blend (Unit 3). So the remedy lives in path design, not timing: it's a via-point/routing problem, the same machinery used to avoid bad regions.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Checking only the endpoints (interior violations get missed).
- Slowing down to fix a geometric (reachability / joint-limit) violation.
- Forgetting joint-angle limits and IK branch consistency in the audit.
