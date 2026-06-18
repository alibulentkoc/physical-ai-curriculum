---
module: 7
unit: 8
lesson: 1
type: answer_key
title: "Answer Key — The Complete Workflow: Plan → Parameterize → Validate → Execute"
audience: coaches
---

# Answer Key 8.1 — The Complete Workflow: Plan → Parameterize → Validate → Execute

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** Plan → Parameterize → Validate → Execute.

**Q2 — B.** PLAN → collision-free path; PARAMETERIZE → timed trajectory.

**Q3 — B.** Each stage is an earlier unit (Plan=U6, Param=U2-5, Validate=U7, Execute=U7→M8).

**Q4 — B.** Execute in Module 7 = open-loop playback + handoff (tracking is Module 8).

**Q5 — B.** Each stage consumes the previous stage's output — clean composition.

---

**Q6 — model answer.** PLAN produces a collision-free geometric path (from the task's start and goal, around obstacles). PARAMETERIZE produces a timed trajectory by assigning a time scaling that respects the velocity/acceleration limits. VALIDATE produces a validated reference (or a rejection) by running the complete check suite. EXECUTE produces motion by discretizing and handing off the validated reference — in Module 7 this is open-loop playback plus delivery to Module 8, which does the closed-loop tracking.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** PLAN is Unit 6 (configuration space, collision checking, RRT, smoothing). PARAMETERIZE is Units 2-5 (polynomial/spline time scaling and the feasibility time-scaling that respects limits). VALIDATE is Unit 7 (the complete validation suite). EXECUTE is the Unit 7 boundary work — discretizing the reference (7.4) and handing it off (7.3) — with the actual closed-loop tracking belonging to Module 8. So the capstone is the wiring of units already built.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** PLAN: IK the start and pre-grasp tool poses to configurations, then RRT + smoothing find a collision-free path around the canopy. PARAMETERIZE: time each segment to its minimum feasible duration, producing q(t), q̇(t), q̈(t) within the limits. VALIDATE: run the suite — endpoints, continuity, limits, collision-free, reachable — and certify VALID. EXECUTE: discretize the validated reference and hand it off (open-loop playback in Module 7). Module 7 ends exactly at delivering the validated reference; Module 8 begins by tracking it on the real arm.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Skipping a stage (a planned path isn't executable until parameterized and validated).
- Reordering stages (validate the timed trajectory; execute only after validation passes).
- Thinking 'Execute' means feedback control (it's open-loop handoff in Module 7).
