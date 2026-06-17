# Answer Key — Lesson 1.1: From Forward to Inverse

**Coaches only.** Formative.

1. **Inverse kinematics is...** — solving T₀ⁿ(θ) = T_desired for θ (not evaluating it; that is forward kinematics).
2. **Forward evaluates, inverse solves** — True.
3. **One-joint angle for (x,y)** — atan2(y, x).
4. **Why a robot must solve IK (short).** Perception delivers a target *pose*; the motors need *joint angles*. IK is the step that converts the desired pose into the angles that achieve it — without it, a perceived target is never acted on.

**Challenge rubric.** Full credit: adding a second joint lets the arm reach the same point with the elbow bent either way (two configurations), so the tidy one-to-one map of the single joint breaks — multiple joint vectors map to one position. Partial: states "more than one solution" without tying it to the extra joint's freedom.
