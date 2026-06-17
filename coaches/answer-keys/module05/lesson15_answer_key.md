# Answer Key — Lesson 4.3: The Iteration Idea: Guess, Measure Error, Step

**Coaches only.** Formative.

1. **The loop** — measure e = p_target − f(θ); Δθ = J⁺e; θ ← θ + αΔθ; stop when |e| < tol.
2. **The seed determines** — which solution you converge to (and whether you converge).
3. **Too-large a step can diverge** — True.
4. **Why re-evaluate J each iteration (short).** J is only local; after each step the configuration changes, so the next step needs a fresh J.

**Challenge rubric.** Full credit: when J is non-invertible (a special configuration), J⁻¹e is undefined/huge, so the bare step explodes or stalls; the damped step J⁰(JJᵀ+λ²I)⁻¹e stays bounded because λ²I keeps the inverse well-defined, trading a little accuracy for stability — which is why Unit 5 introduces it. Partial: says the bare step "fails" without naming the damping mechanism. (Full singularity theory is Module 6 — not required here.)
