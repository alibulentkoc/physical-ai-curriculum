---
module: 7
unit: 6
lesson: 3
type: answer_key
title: "Answer Key — Finding a Safe Path: Sampling-Based Planning (RRT)"
audience: coaches
---

# Answer Key 6.3 — Finding a Safe Path: Sampling-Based Planning (RRT)

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Sample → nearest → steer → collision-check → try to connect to goal.

**Q2 — B.** Goal bias occasionally samples the goal to pull the tree toward finishing.

**Q3 — B.** It probes free space with samples instead of enumerating the huge space.

**Q4 — B.** RRT returns a jagged feasible path (smoothed in 6.4).

**Q5 — B.** Basic RRT can't prove infeasibility; 'not found' ≠ 'impossible'.

---

**Q6 — model answer.** From the doorway you repeatedly: pick a random spot in the room (sample), walk from your nearest already-explored point a short step toward it (nearest + steer), and if the step doesn't hit furniture keep it (collision-check). Your explored tree grows outward, bending around furniture because you can't step through it. Every so often you aim at the far corner (goal bias); once you're close and the way is clear, you connect and trace your hops back to the door for a route. That's RRT: sample, nearest, step, check, connect.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** A 6- or 7-joint arm has a 6- or 7-dimensional configuration space; gridding it (or building the full C-obstacle) needs exponentially many cells — hopeless. Sampling-based planners never enumerate the space: they draw random configurations, call the cheap collision check only where they look, and connect the safe ones into a tree (or roadmap) reaching from start to goal. They discover free space by probing it, so cost scales with problem difficulty, not with the dimension's exponential volume.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** A narrow corridor of free space is a small target: the chance that a random sample plus a step lands inside it (and the connecting edge stays collision-free) is low, so the tree rarely grows through it and planning takes many iterations. Probabilistic completeness guarantees it's found eventually, just slowly. Practical remedies without invoking optimization: more samples / iterations, a smaller step size near clutter, or biasing samples toward the corridor or goal region. (If no path exists, basic RRT simply never returns one — it can't prove infeasibility.)
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Expecting a clean/short path (RRT is jagged; smoothing follows).
- Forgetting the goal bias, or skipping the edge collision check.
- Assuming failure means no path exists (basic RRT can't prove infeasibility).
