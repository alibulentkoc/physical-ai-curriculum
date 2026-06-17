# Answer Key — Lesson 7.1: Reading the End-Effector Pose

**Coaches only.** Formative.

1. **The end-effector pose answers** — where the gripper is and which way it points.
2. **The approach axis is** — ẑ_g, the third column of the rotation block.
3. **A grasp target is a full pose (position + approach), not just a point** — True.
4. **When can the arm "grasp now" (short)?** When T_0^n ≈ T_grasp in both position and approach orientation.

**Challenge rubric.** Full credit: a grasp-readiness score combines a position term (distance ‖p − p_target‖) and an orientation term (angle between current and desired approach axes); both must be present because a correct position with the wrong approach would knock the fruit off (and vice-versa). Weighting position only ignores orientation and can crush or miss the fruit. Partial: combines both terms without explaining the failure of position-only weighting.
