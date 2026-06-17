---
module: 6
unit: 1
lesson: 2
type: answer_key
title: "Answer Key — Angular Velocity and the Skew Operator"
audience: coaches
---

# Answer Key 1.2 — Angular Velocity and the Skew Operator

**Q1 — B.** Direction = instantaneous axis, magnitude = rate. (D conflates spatial and body.)

**Q2 — B.** $\dot R = S(\boldsymbol{\omega}_s)R$ (spatial, left-multiplication). Right-multiplication (A) is the body form.

**Q3 — B, skew-symmetric.** From $\dot R R^\top + R\dot R^\top = 0$, $\dot R R^\top = -(\dot R R^\top)^\top$.

**Q4 — B.** $\boldsymbol{\omega}_s = R\,\boldsymbol{\omega}_b$.

**Q5 — B.** Vee extracts the vector from a skew matrix; it inverts `skew`.

**Q6 — model.** Differentiate $RR^\top=I$: $\dot R R^\top + R\dot R^\top = 0$, so $\dot R R^\top = -(R\dot R^\top) = -(\dot R R^\top)^\top$. A matrix equal to minus its transpose is skew-symmetric. *Full credit for the differentiation + the transpose identity.*

**Q7 — model.** $S(\boldsymbol{\omega}_s)=\begin{bmatrix}0&-3&0\\3&0&0\\0&0&0\end{bmatrix}$, and $\dot R(0)=S(\boldsymbol{\omega}_s)\,I = S(\boldsymbol{\omega}_s)$. *Full credit for correct skew matrix and recognizing $\dot R(0)=S$ since $R(0)=I$.*

**Q8 — model.** $\dot R R^\top$ yields a clean three-vector valid for any orientation, whereas Euler-angle rates blow up or become ill-conditioned near representation singularities (gimbal lock). *Accept any mention of gimbal lock / representation singularity.*

### Watch for
- Students putting the multiplication on the wrong side (mixing spatial/body forms).
- Treating $\boldsymbol{\omega}$ as $\dot{\boldsymbol{\phi}}$ (Euler rates) — flagged for Lesson 3.2.
