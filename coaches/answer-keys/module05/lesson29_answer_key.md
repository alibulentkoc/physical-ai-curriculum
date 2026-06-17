# Answer Key — Lesson 8.1: The Project: From Target Pose to Joint Angles

**Coaches only.** Formative.

1. **Reach the Fruit produces** — a verified, feasible, selected joint configuration (or a clear no-solution reason).
2. **Match** — perceive → Module 3; place in base frame → Module 2/4; inverse kinematics → Module 5.
3. **Analytical where possible, numerical where needed** — True.
4. **Modules integrated (short).** Modules 2 (frames), 3 (perception), 4 (forward kinematics), 5 (inverse kinematics).

**Challenge rubric.** Full credit: for the planar 2-link arm the closed form always applies, so the numerical fallback would only run for a *variation* — e.g. adding a third joint for obstacle avoidance (redundant, no closed form) or requiring a full-pose grasp with orientation the 2-link can't independently set — and it slots into the "solve" stage as the fallback branch, seeded from the current pose, with downstream verify/filter/select unchanged. Partial: names a variation without placing the numerical solver in the flow.
