# Answer Key — Lesson 3.1: Closed-Form Solution of the 2-Link Arm

**Coaches only.** Formative.

1. **Closed-form elbow angle** — θ₂ = ±arccos((x²+y²−L₁²−L₂²)/(2L₁L₂)).
2. **The ± gives two solutions** — True (elbow-up / elbow-down).
3. **cos θ₂ outside [−1,1]** — target is unreachable (no solution); the range check is the reachability test.
4. **Why FK-verify (short).** Forward kinematics confirms the angles actually land the gripper on the target, catching algebra/quadrant slips.

**Challenge rubric.** Full credit: rewrite θ₂ = atan2(±√(1−cos²θ₂), cos θ₂); the atan2 form is more accurate near cos θ₂ = ±1 because arccos has infinite slope there (small input errors blow up), while atan2 stays well-conditioned. Partial: gives the atan2 form without the conditioning reason.
