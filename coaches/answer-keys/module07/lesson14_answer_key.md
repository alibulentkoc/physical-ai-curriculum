---
module: 7
unit: 4
lesson: 2
type: answer_key
title: "Answer Key — Position Interpolation and the IK-per-Sample Loop"
audience: coaches
---

# Answer Key 4.2 — Position Interpolation and the IK-per-Sample Loop

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Sample the straight tool path in time and solve IK at each sample.

**Q2 — B.** An IK branch is one of the distinct solutions (elbow-up/down) for the same tool pose.

**Q3 — B.** A branch flip makes the joint trajectory jump discontinuously.

**Q4 — B.** Pick the solution nearest the previous sample, or fix the elbow sign.

**Q5 — B.** Branch consistency and singularity avoidance are both required for smooth joints.

---

**Q6 — model answer.** Because the joint motion comes from IK applied along the path, and IK has two failure modes that a smooth tool path doesn't prevent. First, a branch flip (elbow-up to elbow-down) makes the joints jump discontinuously even though the tool point moved smoothly. Second, near a singularity the joints stay continuous but the joint rates needed to keep the tool on the line spike. So smooth p(t) needs a consistent IK branch and a singularity-free path to yield smooth q(t).
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** At each sample, choose the IK solution closest to the previous configuration (minimizing ‖q_k−q_{k−1}‖), or simply fix the elbow sign for the whole path. This keeps q(t) continuous. It matters because a branch flip is a large instantaneous jump in joint angles — the velocity layer would have to execute an impossible instantaneous reconfiguration, and physically the arm would convulse, possibly colliding, even though the tool path was perfectly smooth.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** Each sampled tool point needs an IK solution; if any point lies outside the workspace, no joint configuration realizes it and the straight-line move is infeasible there. Reachable endpoints don't guarantee a reachable line. The loop should detect the unreachable sample and fail cleanly (raise an error / reject the move) rather than return an invalid or silently wrong configuration — so the planner can reroute (add a via-point) or reorient.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Letting IK pick any solution per sample (causes branch flips).
- Checking only the endpoints for reachability instead of every sample.
- Equating a smooth tool path with smooth joints (branch flips/singularities break it); sampling too coarsely.
