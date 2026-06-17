---
module: 6
unit: 2
lesson: 5
type: answer_key
title: "Answer Key — Forward Velocity Kinematics"
audience: coaches
---

# Answer Key 2.1 — Forward Velocity Kinematics

**Q1 — B.** $\boldsymbol{\xi}=J(\mathbf{q})\dot{\mathbf{q}}$. (A is position FK; C is the inverse problem, Unit 7.)

**Q2 — B.** Each column is one joint's unit-rate tool twist.

**Q3 — C.** Nonlinear in $\mathbf{q}$ (entries depend on pose), linear in $\dot{\mathbf{q}}$.

**Q4 — B.** $6\times n = 6\times 6$.

**Q5 — C.** Linear velocity on top (D-057).

**Q6 — model.** The tool twist is the rate-weighted sum of the per-joint columns: each joint "pushes" the tool, and $J\dot{\mathbf{q}}$ adds those pushes. *Full credit for sum-of-columns.*

**Q7 — model.** The columns (pushes) depend on the arm's geometry, which changes with pose; at a fixed pose the map is a constant matrix, but that matrix is different at every configuration. *Full credit for distinguishing pose-dependence of entries from linearity in rates.*

**Q8 — model.** It is the same matrix: M5 used $J$ as the local linear step generator ($\Delta\mathbf{p}\approx J\Delta\boldsymbol{\theta}$); here the same $J$ is read as the continuous velocity map $\boldsymbol{\xi}=J\dot{\mathbf{q}}$. *Full credit for "same matrix, now the velocity map."*

### Watch for
- Calling $J$ constant.
- Swapping the linear/angular blocks (D-057 fixes linear on top).
