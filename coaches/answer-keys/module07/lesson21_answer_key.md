---
module: 7
unit: 6
lesson: 1
type: answer_key
title: "Answer Key — Obstacles and Forbidden Regions: Configuration Space"
audience: coaches
---

# Answer Key 6.1 — Obstacles and Forbidden Regions: Configuration Space

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** The C-obstacle is every configuration where any part of the arm collides.

**Q2 — B.** Robot = a single point; motion = a curve (collision-free if in C_free).

**Q3 — B.** The nonlinear joint-to-shape map distorts a round obstacle into a curved band.

**Q4 — B.** Planning = find a curve in C_free from start to goal.

**Q5 — B.** Both endpoints free doesn't imply the direct segment is free.

---

**Q6 — model answer.** Many arm poses (shoulder, elbow combinations) bump a given pole; charting shoulder vs elbow and shading every colliding pair makes a blob — the pole's forbidden region. Now forget the extended arm: you're a single dot on that chart at your current angles. To move your hand without hitting the pole, just slide the dot from its position to the target without entering the blob. The awkward arm-dodging-a-pole problem becomes 'move a point around a region' — that's configuration space, and it's why planning is tractable.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** Because a C-obstacle is defined by whether ANY part of the arm collides, not just the gripper — so a single point in C-space already encodes the entire arm's clearance. Reasoning in the workspace means repeatedly checking an extended, jointed body against the obstacle for every pose; reasoning in C-space collapses that to point-vs-region. The whole arm's safety is captured by where the configuration point sits relative to the forbidden region.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** It implies a straight joint move between them would drive a link through the obstacle, so the planner must find a detour — a curved path through C_free around the C-obstacle. Whether a path exists at all depends on the connectivity of the free space: if the C-obstacle separates the start's free region from the goal's (disconnects C_free), no collision-free path exists, and one must move the obstacle, change the task, or use a different IK branch to open a route.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Thinking only about the gripper (a C-obstacle includes every colliding link pose).
- Expecting the C-obstacle to look like the workspace obstacle (the nonlinear map distorts it).
- Assuming free endpoints imply a free path; treating C-space as abstract math.
