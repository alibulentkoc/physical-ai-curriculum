---
module: 6
unit: 1
lesson: 4
type: answer_key
title: "Answer Key — Transforming Twists Between Frames"
audience: coaches
---

# Answer Key 1.4 — Transforming Twists Between Frames

**Q1 — B.** Rotate components by $R$; shift the reference point via $\boldsymbol{\omega}\times\mathbf{d}$.

**Q2 — B.** The $-R^\top S(\mathbf{d})$ block is the reference-point shift.

**Q3 — B.** With $\mathbf{d}=0$ the transform is $\text{diag}(R^\top,R^\top)$.

**Q4 — C.** Invariance of physical point velocities is the correctness criterion (the matrix is *not* orthogonal in general, so A/B/D are wrong tests).

**Q5 — B, $(0,0,0)$.** $\mathbf{v}_B=\mathbf{v}_A+\boldsymbol{\omega}_A\times\mathbf{d}=(1,0,0)+(-1,0,0)=(0,0,0)$. B's origin is the instantaneous center (matches Lesson 1.3's stationary point). *Common wrong answer A=(2,0,0) flips the sign of the lever-arm term.*

**Q6 — model.** $\boldsymbol{\omega}$ is a property of the whole body, identical at every point; only its *coordinates* change with the frame's orientation, hence a pure rotation. The reference point affects only where you "stand" to measure linear velocity. *Full credit for "shared by all points."*

**Q7 — model.** $R=I$ leaves orientation alone, so the transform shifts only the linear part by $\boldsymbol{\omega}\times\mathbf{d}$; $\boldsymbol{\omega}_B=\boldsymbol{\omega}_A$. *Full credit.*

**Q8 — model.** The base-frame Jacobian outputs the end-effector twist in world coordinates; applying the twist transform with the gripper's pose $(R,\mathbf{d})$ re-expresses it in the tool frame, so no separate model/derivation is needed. *Full credit for "apply the transform to the base-frame result."*

### Watch for
- Rotating but forgetting the lever arm (or vice versa).
- Memorizing $R$ vs $R^\top$ instead of verifying via the invariance test.
- The sign slip on $\boldsymbol{\omega}\times\mathbf{d}$ (the Q5 distractor).
