---
module: 6
unit: 7
lesson: 28
type: answer_key
title: "Answer Key — Resolved-Rate Motion (Velocity Layer)"
audience: coaches
---
# Answer Key 7.4
**Q1 B · Q2 B · Q3 B · Q4 B · Q5 B.**
**Q6.** Each cycle: q̇ = J⁺_λ(q) ξ_d; q ← q + q̇ Δt; recompute J(q); repeat.
**Q7.** Because J q̇ = J J⁺ ξ_d = ξ_d for a full-rank Jacobian — the resolved rates reproduce the command instantaneously.
**Q8.** Not trajectory generation (the command ξ_d is an input — M7), not feedback control (no sensed-error correction — M8), not dynamics (no forces/masses).
### Watch for: adding an error-feedback term (makes it M8); treating ξ_d as something to plan (M7); forgetting to recompute J each cycle.
