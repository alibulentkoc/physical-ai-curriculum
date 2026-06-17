---
module: 6
unit: 3
lesson: 11
type: answer_key
title: "Answer Key — Base-Frame vs Tool-Frame Jacobian"
audience: coaches
---

# Answer Key 3.3 — Base-Frame vs Tool-Frame Jacobian

**Q1 — B.** Rotation of both blocks only. **Q2 — B.** $\mathbf{d}=\mathbf{0}$. **Q3 — B.** $\mathrm{blkdiag}((R^n_0)^\top,(R^n_0)^\top)J_{\text{base}}$. **Q4 — B.** Same reference point. **Q5 — B.** Twist invariance.

**Q6 — model.** Both Jacobians measure the velocity of the same point (the tool origin), so there is no reference-point shift; only the axes differ, giving a pure rotation. *Credit for "same point ⇒ no shift."*

**Q7 — model.** If the Jacobian is moved to a *different* reference point (e.g., the fingertip offset by $\mathbf{r}$), the lever-arm term $\boldsymbol{\omega}\times\mathbf{r}$ reappears. *Credit for reference-point change.*

**Q8 — model.** Tool frame: pressing/sliding along the tool's approach axis (surface finishing, peg insertion). Base frame: gravity-direction reasoning, world-referenced moves. *Accept reasonable examples.*

### Watch for
- Adding a lever-arm term for base↔tool; rotating only one block; stale $R^n_0$.
