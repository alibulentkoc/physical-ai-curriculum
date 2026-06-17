---
module: 6
unit: 6
lesson: 24
type: answer_key
title: "Answer Key — Pseudoinverse and Damped Least Squares"
audience: coaches
---
# Answer Key 6.4
**Q1 B · Q2 B · Q3 B · Q4 B · Q5 B.**
**Q6.** J⁺ = VΣ⁺Uᵀ with Σ⁺ = diag(1/σᵢ) on nonzero σ; the gain 1/σ_min → ∞ as σ_min → 0, causing the joint-rate blow-up.
**Q7.** g(σ)=σ/(σ²+λ²): ≈ 1/σ when σ≫λ (no harm in easy directions), → 0 as σ→0 (no blow-up), peak 1/(2λ) at σ=λ.
**Q8.** It is exactly the damped inverse M5 used inside its numerical IK solver — introduced there as a fix, derived here from the SVD (the geometry explains why it works).
### Watch for: using the raw pseudoinverse near singularities; treating λ as cost-free; forgetting the two DLS forms are identical.
