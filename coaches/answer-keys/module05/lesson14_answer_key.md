# Answer Key — Lesson 4.2: The Local Linear Map: the FK Jacobian (for Solving)

**Coaches only.** Formative.

1. **The Jacobian is** — the matrix of partial derivatives ∂p/∂θ; the local linear map Δp ≈ J Δθ.
2. **Each column** — the gripper motion from twitching one joint (column j = ∂p/∂θⱼ).
3. **Used only as the solver's local linear map in Module 5** — True (velocity/singularity theory is Module 6).
4. **When is Δp ≈ J Δθ accurate (short).** For small joint changes; error grows with step size, so the solver steps small and re-evaluates J.

**Challenge rubric.** Full credit: applying a large Δθ₂ = 45°, the linear prediction JΔθ noticeably diverges from the true FK change because the forward map curves; the quadratic (and higher) terms the linearization drops grow with step size — hence many small steps, each with a fresh J. Partial: notes the mismatch without the "dropped higher-order terms / re-linearize" reasoning.
