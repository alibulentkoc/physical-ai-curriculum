---
module: 7
unit: 8
lesson: 2
type: answer_key
title: "Answer Key — Plan and Parameterize: From Task to Timed Trajectory"
audience: coaches
---

# Answer Key 8.2 — Plan and Parameterize: From Task to Timed Trajectory

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** PLAN = what route (geometry); PARAMETERIZE = how fast along it (timing).

**Q2 — B.** PLAN = RRT + smoothing; PARAMETERIZE = time scaling + polynomial/spline timing.

**Q3 — B.** Plan-then-time keeps each step tractable and reusable.

**Q4 — B.** Fusing them is kinodynamic planning (harder, out of scope).

**Q5 — B.** Re-parameterizing leaves the path unchanged and lowers the peaks.

---

**Q6 — model answer.** First, with a map, you trace the route — which roads and turns, avoiding the closed bridge — pure geometry, no speeds yet (PLAN: RRT finds a collision-free path, smoothing straightens it). Then you schedule it — decide how fast to drive each segment so you don't speed or dawdle (PARAMETERIZE: time each segment to the velocity/acceleration limits with a polynomial/spline timing). Route first, schedule second. You'd never compute the exact speed for every meter while still discovering the route; separating them keeps each manageable.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** Decoupling lets the planner solve a pure geometry problem (no derivatives, no limits) and the parameterizer solve a closed-form timing problem on a fixed curve — each simple, well-understood, and independently swappable, and the same path can be re-timed without replanning. The harder alternative is kinodynamic planning, which searches over path and velocities/accelerations jointly under coupled constraints; it's heavier and reserved for cases that truly need it. Module 7 deliberately uses plan-then-time and keeps kinodynamic planning out of scope.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** Same path, different timing. For the gentle loaded grasp, parameterize with a smooth profile and longer segment durations to minimize jerk and keep accelerations low. For the fast empty reposition, parameterize with the fastest-feasible (trapezoidal) timing to minimize duration, accepting higher jerk — both stay within the limits. You only go back to PLAN if no timing can make the path feasible — i.e. a geometric problem like an unreachable point or a collision (which timing can't fix); a mere too-fast trajectory is a parameterize fix (slow down), not a re-plan.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Mixing timing into planning (don't solve the kinodynamic problem unless you must).
- Timing a segment below its minimum feasible duration; re-planning to fix a too-fast trajectory.
- Forgetting to re-collision-check a smoothing spline.
