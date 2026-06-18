---
module: 7
unit: 3
lesson: 3
type: answer_key
title: "Answer Key — Via-Points and Multi-Segment Joint Trajectories"
audience: coaches
---

# Answer Key 3.3 — Via-Points and Multi-Segment Joint Trajectories

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** A via-point is an intermediate configuration the trajectory must pass through.

**Q2 — B.** Stop-at-each is rest-to-rest, so velocity is zero at every interior via-point.

**Q3 — B.** Stopping at each via-point is a full halt/restart — slow and jerky.

**Q4 — B.** Flow-through needs a nonzero passing velocity/acceleration matched on both sides.

**Q5 — B.** Each segment is a joint move, so the tool path between vias is curved.

---

**Q6 — model answer.** Stop-at-each chains rest-to-rest segments: the trajectory passes through each via-point but the joint comes to a complete stop there (zero velocity), so the motion stutters and is slow — every via-point is a halt and restart. Flow-through assigns each interior via-point a nonzero passing velocity (and acceleration), matched on both sides, so the motion glides through the via-points as one continuous trajectory without stopping.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** Because a single straight joint-space move from start to goal may take the tool through a bad region — dragging the gripper through the canopy or approaching from the wrong side. Routing the motion through intermediate configurations (via-points) keeps the in-between path clear and lines up the final approach. Via-points let the trajectory follow a chosen route instead of the single direct segment.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** When an action must happen at the via-point that requires the arm to be momentarily still — e.g. taking a precise sensor/camera reading, performing a regrasp, or waiting for an external trigger. There, stopping is intentional, not waste; flow-through would be wrong because the task needs zero velocity at that configuration.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Stopping at every via-point by default (slow, jerky) when flow-through is available.
- Confusing joint-space via-points (full configurations) with tool-space waypoints.
- Assuming the path between via-points is straight in space.
