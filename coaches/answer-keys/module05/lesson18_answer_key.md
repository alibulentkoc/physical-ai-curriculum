# Answer Key — Lesson 5.2: The Jacobian-Transpose and Damped Least Squares

**Coaches only.** Formative.

1. **Transpose step** — a gradient-descent step: always downhill (reduces ½|e|²), stable, slower.
2. **Damped least squares** — Δθ = Jᵀ(JJᵀ + λ²I)⁻¹ e.
3. **λ→0 ⇒ pseudoinverse; large λ ⇒ transpose-like** — True.
4. **Why DLS is the practical default (short).** It stays bounded everywhere via one damping factor — Newton-fast when well-conditioned, transpose-gentle near singularities.

**Challenge rubric.** Full credit: ∇_θ C = ∇_θ ½|p_target − f(θ)|² = −Jᵀ(p_target − f) = −Jᵀe, so Jᵀe is the negative gradient; a small enough step along it decreases C (descent lemma), guaranteeing error reduction; and as λ→∞, (JJᵀ+λ²I)⁻¹ ≈ (1/λ²)I, so DLS ≈ (1/λ²)Jᵀe — a scaled transpose step. Partial: shows the gradient identity but not the λ→∞ limit.
