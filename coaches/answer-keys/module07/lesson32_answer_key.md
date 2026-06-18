---
module: 7
unit: 8
lesson: 4
type: answer_key
title: "Answer Key — Capstone Integration: The Greenhouse Harvest Cycle"
audience: coaches
---

# Answer Key 8.4 — Capstone Integration: The Greenhouse Harvest Cycle

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** A harvest cycle is a sequence of motions, each the full workflow.

**Q2 — B.** Legs meet at rest poses, so the chained cycle is continuous.

**Q3 — B.** Module 7 delivers the validated reference cycle; Module 8 tracks it.

**Q4 — B.** Module 8 adds feedback control, dynamics, and actuator control.

**Q5 — B.** Replan per leg because the scene/payload changes (fruit held on retreat).

---

**Q6 — model answer.** Picking an apple is a little sequence: reach toward it avoiding branches, close your hand around it, pull back without snagging — three motions flowing into one action, each planned as you go (the route back with the apple differs from the route in). The harvester does the same explicitly: leg 1 (reach) plans a clear route to a pre-grasp pose, times it, validates; leg 2 (grasp) a short careful move; leg 3 (retreat) plans a route back out with the fruit as payload. Each leg runs the full workflow and produces a validated reference; the legs meet at rest poses so the chained cycle is continuous.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** U1: path vs trajectory and smoothness. U2: polynomial time scaling and the smooth-vs-fast trade. U3: joint-space trajectories (per-joint, synchronized, via-points, splines). U4: Cartesian-space trajectories (straight-line, orientation/SLERP, screw motion). U5: feasibility — velocity/acceleration limits, time scaling, fastest-feasible timing, whole-trajectory checks. U6: motion planning — configuration space, collision checking, RRT, smoothing. U7: trajectory quality, validation, tracking prerequisites, reference representation. U8: the capstone workflow (Plan → Parameterize → Validate → Execute) producing the reference trajectory layer.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** Module 7 delivers a validated reference for the entire cycle: the chained, continuous sequence of reference layers (reach, grasp, retreat), each giving q_d, q̇_d, q̈_d, feasible, collision-free, and certified — an open-loop reference the controller can step through. Module 8 must build the tracker that actually follows this reference on the real arm: computing tracking error, applying feedback control, accounting for the robot's dynamics, and commanding the actuators to reject disturbances. Module 7 decides and certifies the motion; Module 8 executes it under closed-loop control — none of which (feedback, dynamics, actuators) is in Module 7.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Treating the task as one motion (a cycle is legs; run the workflow per leg and chain).
- Ignoring per-leg world/payload changes; chaining without rest joins.
- Thinking the capstone tracks the motion (Module 7 delivers the reference; Module 8 tracks).
