# Answer Key — Lesson 6.1: Singularities: Where IK Breaks Down (Recognition)

**Coaches only.** Formative.

1. **Singularity** — a configuration where J drops rank; a direction of gripper motion is lost.
2. **2-link det J = L₁L₂ sin θ₂ = 0 at** — θ₂ = 0° (straight) or 180° (folded) — the workspace boundaries.
3. **Tangential motion remains, radial is lost** — True.
4. **Why the pseudoinverse misbehaves (short).** det J → 0 makes J⁻¹/J⁺ entries huge, so the joint step explodes; damping is required.

**Challenge rubric.** Full credit: at θ₂ = 0, sin θ₂ = 0 so column 2 = [−L₂ sin θ₁₂, L₂ cos θ₁₂] becomes parallel to part of column 1 (both point along the arm), giving rank 1; the gripper can still move *perpendicular* to the arm (tangential) but not *along* it (radial) — and this is exactly where the elbow-up/elbow-down solutions merge into one at the workspace boundary (Lesson 2.3). Partial: states rank 1 without linking to the merged solutions. **Scope:** recognition only — singular values, manipulability, and the velocity meaning are Module 6.
