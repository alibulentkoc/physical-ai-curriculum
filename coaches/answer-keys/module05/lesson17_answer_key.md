# Answer Key — Lesson 5.1: Newton's Method for IK (Jacobian Pseudoinverse)

**Coaches only.** Formative.

1. **Newton step** — θ ← θ + α J⁺ e.
2. **Pseudoinverse returns** — the least-norm joint move achieving the desired gripper change.
3. **Fast near a well-conditioned solution** — True (roughly quadratic; error squares each step).
4. **Why fragile near det J = 0 (short).** J is ill-conditioned, so J⁺ has huge entries and the step blows up; damped least squares (5.2) fixes it.

**Challenge rubric.** Full credit: det J = L₁L₂ sin θ₂ = 0 at θ₂ = 0° (arm straight) and 180° (folded); there the columns of J align (rank 1), so the radial gripper direction can't be produced and J⁻¹ is undefined — the Newton step diverges. Partial: finds the angles without the geometric "arm straight/folded, radial direction lost" explanation. (Recognition only — full theory is 6.1 / Module 6.)
