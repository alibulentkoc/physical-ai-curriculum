---
module: 6
unit: 1
lesson: 1
type: answer_key
title: "Answer Key — From Finite to Infinitesimal"
audience: coaches
---

# Answer Key 1.1 — Differential Translation and Rotation

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** A differential motion is a small translation $d\mathbf{p}$ plus a small
rotation $\delta\boldsymbol{\theta}$. (A describes a generic finite motion; C is a
specific parameterization; D omits rotation.)

**Q2 — C.** $R \approx I + S(\delta\boldsymbol{\theta})$. Option A drops the
identity (so it isn't near a rotation); B has the wrong sign; D is second-order.

**Q3 — C, quarters.** The error scales as $\delta\phi^2$, so halving the angle
divides the error by four. (Confirmed numerically in the notebook: slope $\approx 2$
on log–log axes.)

**Q4 — B.** Differential rotations commute to first order because the cross term
$S_aS_b$ is second-order and drops; finite rotations generally do not commute.

**Q5 — B.** $S(\mathbf{v})\mathbf{u} = \mathbf{v}\times\mathbf{u}$. Note $S$ is
skew ($S^\top=-S$), so C is false, and $S$ is singular (rank 2), so D is false.

---

**Q6 — model answer.** Near the solution the joint update $\Delta\boldsymbol{\theta}$
and pose error $\Delta\mathbf{p}$ are small, so the forward kinematics is well
approximated by its first-order (linear) term, $\Delta\mathbf{p} \approx
J\,\Delta\boldsymbol{\theta}$. That linearization *is* differential motion: $J$ maps
a differential joint motion to a differential end-effector motion.
*Grading: full credit for connecting "small change" → "first-order/linear" → "$J$
is the local linear map." Accept mention of quadratic convergence as a bonus.*

**Q7 — model answer.** Applying $\delta\boldsymbol{\theta}_1$ then
$\delta\boldsymbol{\theta}_2$ gives, to first order,
$$(I+S(\delta\boldsymbol{\theta}_2))(I+S(\delta\boldsymbol{\theta}_1)) \approx I + S(\delta\boldsymbol{\theta}_1 + \delta\boldsymbol{\theta}_2),$$
so the rotation vectors simply **add**. *Grading: full credit for the summed
argument $\delta\boldsymbol{\theta}_1+\delta\boldsymbol{\theta}_2$ and the
statement that order doesn't matter at first order.*

**Q8 — model answer (accept any valid example).** Examples: the final corrections
of a numerical IK solver; a visual-servoing controller nudging the tool toward a
target each frame; jogging a robot a tiny step in tool coordinates. A finite-motion
description would force full nonlinear rotation composition (non-commuting,
matrix-valued) where a simple additive linear update suffices.
*Grading: full credit for a plausible small-motion scenario plus a one-line reason
the linear/differential view is simpler.*

---

### Common misconceptions to watch for
- Students writing $\delta\boldsymbol{\theta}$ as roll/pitch/yaw — flag that this
  is an axis-times-angle vector, not Euler angles (revisited in Lesson 3.4).
- Claiming finite rotations commute "if the angles are equal." They don't, unless
  the axes coincide.
- Treating $S(\delta\boldsymbol{\theta})$ as a full rotation rather than the
  *linear part* near the identity.
