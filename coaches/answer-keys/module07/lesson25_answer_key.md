---
module: 7
unit: 7
lesson: 1
type: answer_key
title: "Answer Key — What Makes a Trajectory Good? Quality Metrics"
audience: coaches
---

# Answer Key 7.1 — What Makes a Trajectory Good? Quality Metrics

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Quality is a ranking among feasible trajectories (feasibility is pass/fail).

**Q2 — B.** Peak jerk is the rate of change of acceleration — smoothness.

**Q3 — B.** Metrics trade off; best depends on a task-specific weighting.

**Q4 — B.** Duration, peak speed, peak acceleration, peak jerk, path length.

**Q5 — C.** Not energy/dynamics — those need the robot's mass/inertia (Module 8+).

---

**Q6 — model answer.** Duration (total time — faster vs slower); peak speed and peak acceleration (how hard the motion pushes the velocity/acceleration limits); peak jerk (the rate of change of acceleration — smoothness, with low jerk meaning gentle motion); and Cartesian path length (how far the tool actually travels — efficiency of the route). Together they let you compare feasible trajectories objectively rather than by feel.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** Both pass the feasibility gates, but they differ on the metrics. A smooth quintic over a longer duration has low peak jerk (gentle) but takes more time; a faster trapezoidal motion finishes sooner but spikes jerk at the ramp corners. For delicate fruit handling you weight jerk heavily and prefer the smooth one; for a fast empty-gripper reposition you weight duration heavily and prefer the fast one. Same start and goal, both feasible — the ranking flips with the task's priority.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** Each metric is computed purely from the trajectory's shape and timing — positions, their time-derivatives, and the tool's path length — none of which require knowing the robot's mass, inertia, or motor torques. Energy and actuator effort, by contrast, depend on dynamics (force = mass times acceleration, torque-inertia relationships), which is Module 8 and beyond. By measuring only the motion's geometry and timing, the quality metrics stay within Module 7's deliberate no-dynamics scope.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Treating quality as pass/fail (it's a ranking among feasible options).
- Assuming faster is always better (shorter time raises jerk/acceleration).
- Ignoring jerk, or confusing quality metrics with energy/effort (which need dynamics).
