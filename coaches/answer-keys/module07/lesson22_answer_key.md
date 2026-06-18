---
module: 7
unit: 6
lesson: 2
type: answer_key
title: "Answer Key — Collision Checking: Is This Configuration Safe?"
audience: coaches
---

# Answer Key 6.2 — Collision Checking: Is This Configuration Safe?

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Compute the link geometry (FK) and test each link against the obstacle.

**Q2 — B.** Densely sample configurations along the path and test each.

**Q3 — B.** Tunneling: coarse sampling misses a thin obstacle swept through between samples.

**Q4 — B.** Use a step small relative to obstacle thinness and arm speed.

**Q5 — B.** It's the inner loop of planning (called constantly), so it's kept cheap.

---

**Q6 — model answer.** From the configuration, forward kinematics gives the base, elbow, and tool points, so the two links are known line segments. For a disk obstacle (center c, radius r), compute the shortest distance from each link segment to c; the arm is in collision if either distance is ≤ r. The configuration is in free space iff both links clear the disk. Real systems use richer geometry (capsules, meshes), but the principle is identical: build the body's geometry, test it against the obstacle.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** A motion is safe only if every configuration along it is clear, but we can only test finitely many, so we sample configurations along each edge. Tunneling is the failure where the samples are too far apart: the arm is clear at each sampled instant but sweeps through a thin obstacle in between, so the edge is wrongly reported collision-free — like stepping over a tripwire because you only checked your foot every two metres. The fix is a step size small relative to the obstacle's thinness and the arm's speed.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** Planners explore by testing huge numbers of candidate configurations and edges, calling the collision check as the inner loop — millions of times for a hard problem. Its cost dominates planning time. Real systems speed it up with fast geometric proxies (capsules, convex hulls, bounding-volume hierarchies) so a single check is microseconds, and use swept/continuous collision detection where tunneling must be ruled out exactly. Cheap, correct checks are what make sampling-based planning practical.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Checking only the tool/gripper (a mid-link can collide while the tool is clear).
- Checking only edge endpoints; sampling too coarsely (tunneling).
- Forgetting the obstacle's radius — collision is 'within r of the segment'.
