---
module: 6
unit: 2
lesson: 6
type: answer_key
title: "Answer Key — Geometric Jacobian (Revolute)"
audience: coaches
---

# Answer Key 2.2 — Geometric Jacobian by Column Construction (Revolute)

**Q1 — B.** $[\mathbf{z}\times(\mathbf{o}_n-\mathbf{o}_{i-1}); \mathbf{z}]$. (A is prismatic.)

**Q2 — B.** Joint $i$ turns about $\mathbf{z}_{i-1}$.

**Q3 — C.** From joint $i$'s frame origin $\mathbf{o}_{i-1}$ to the end-effector origin $\mathbf{o}_n$.

**Q4 — C.** Base/world frame (D-057).

**Q5 — B.** The lever arm is longer, so $\mathbf{z}\times(\mathbf{o}_n-\mathbf{o}_{i-1})$ is larger.

**Q6 — model.** From the forward-kinematics transforms $T_0^{i-1}$: $\mathbf{z}_{i-1}$ is the third column of its rotation block, $\mathbf{o}_{i-1}$ its translation. *Full credit for "read off $T_0^{i-1}$."*

**Q7 — model.** Using $\mathbf{z}_i$ instead of $\mathbf{z}_{i-1}$ (off-by-one). It corrupts that column and hence the whole Jacobian, producing wrong velocities everywhere. *Full credit for the off-by-one + "corrupts the Jacobian."*

**Q8 — model.** Moving joint $i$ rotates only the links outboard of it (including the tool); inboard links don't move, so only the outboard geometry (the lever arm to $\mathbf{o}_n$) enters the column. *Full credit for "inboard links don't move."*

### Watch for
- Lever arm to the next joint instead of to $\mathbf{o}_n$.
- Axes expressed in local frames instead of the base frame.
