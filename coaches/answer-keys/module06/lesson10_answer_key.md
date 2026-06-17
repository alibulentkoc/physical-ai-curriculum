---
module: 6
unit: 3
lesson: 10
type: answer_key
title: "Answer Key — The Representation Map B(φ)"
audience: coaches
---

# Answer Key 3.2 — The Representation Map B(φ)

**Q1 — B.** $\boldsymbol{\omega}=B(\boldsymbol{\phi})\dot{\boldsymbol{\phi}}$. **Q2 — B.** Unit-dial angular velocity. **Q3 — B.** $J_\omega=B J_\phi$. **Q4 — B.** Pose-dependent. **Q5 — B.** Loses rank.

**Q6 — model.** Angle-rates measure how fast bookkeeping dials spin; angular velocity is the body's true axis-and-rate. They coincide only through the pose-dependent map $B$. *Credit for bookkeeping vs physical.*

**Q7 — model.** $B$ becomes singular, so $B^{-1}$ blows up; commanded angle-rates explode for an ordinary desired turn (gimbal lock). *Credit for "B singular → angle-rates blow up."*

**Q8 — model.** $J_\omega=B(\boldsymbol{\phi})J_\phi$ (and $J_\phi=B^{-1}J_\omega$); lets you convert between angle-rate and physical-twist Jacobians. *Credit for relation + conversion use.*

### Watch for
- Treating $B$ as constant; inverting it near gimbal lock; convention mismatch.
