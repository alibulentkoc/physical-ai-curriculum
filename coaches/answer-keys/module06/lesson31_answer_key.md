---
module: 6
unit: 8
lesson: 31
type: answer_key
title: "Answer Key — Capstone Integration"
audience: coaches
---
# Answer Key 8.3
**Q1 B · Q2 B · Q3 B · Q4 B · Q5 B.**
**Q6.** λ²=(1−(σ_min/ε)²)λ_max² inside the band (σ_min<ε), else 0 — damping grows smoothly as the arm nears a singularity, bounding joint rates; zero damping far away preserves accuracy.
**Q7.** The null-space projector (I−J⁺J) maps into the Jacobian null space, so J·(null term)=0 — joint self-motion that produces no tool velocity.
**Q8.** Damping trades a little tracking accuracy in the dying direction for bounded, feasible joint rates — the command is followed as well as the (near-singular) geometry permits.
### Watch for: thinking damping makes tracking exact — it deliberately accepts small error for safety.
