---
module: 7
unit: 6
lesson: 4
type: answer_key
title: "Answer Key — From Safe Path to Feasible Trajectory: Smoothing and Time Scaling"
audience: coaches
---

# Answer Key 6.4 — From Safe Path to Feasible Trajectory: Smoothing and Time Scaling

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** A raw RRT path is jagged and untimed — a route, not a trajectory.

**Q2 — B.** Shortcut smoothing replaces a sub-path with a collision-free direct segment.

**Q3 — B.** Time scaling makes the trajectory respect velocity and acceleration limits.

**Q4 — B.** Obstacle → Constraint → Safe Path → Feasible Trajectory.

**Q5 — B.** Smoothing changes geometry (recheck); time scaling changes only the clock.

---

**Q6 — model answer.** Step 1 — smooth: repeatedly test a straight C-space segment between two points of the path; if it's collision-free, replace the wandering sub-path with that direct segment. After several shortcuts the path is much shorter and more direct, still entirely collision-free. Step 2 — time-scale: treat the smoothed waypoints as via-points, build a synchronized blended trajectory, and stretch its duration until every joint's velocity and acceleration peak fits under the limits (Unit 5). The result is smooth in space, gentle in time, and executable open-loop.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** Obstacle (workspace) → Constraint: the C-obstacle / forbidden region in configuration space (6.1, using the collision check of 6.2) → Safe Path: a collision-free path found by RRT (6.3) and shortened by shortcut smoothing (6.4) → Feasible Trajectory: the smoothed path time-scaled to respect velocity/acceleration limits (6.4, using Unit 5). Each stage reuses earlier machinery, and the design deliberately decouples planning the path from timing it (plan-then-time, not kinodynamic).
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** Smoothing changes the geometry: replacing waypoints with a fitted C² spline can make the curve bulge away from the original segments, and that bulge may clip an obstacle even though the shortcut segments were clear — so any smoothing that alters the path must be re-collision-checked (and a waypoint re-inserted if it fails). Time scaling, by contrast, changes only the clock (s(t)), leaving the path identical; since the geometry is untouched, it can never introduce a collision and needs no re-check for collisions (only the limit check).
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Running the raw RRT path (jagged, untimed) instead of smoothing + timing it.
- Forgetting to re-collision-check after spline smoothing (a spline can bulge into an obstacle).
- Time-scaling before smoothing; assuming the timed path is automatically reachable/limit-safe (run the 5.4 audit).
