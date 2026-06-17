---
module: 6
unit: 2
lesson: 8
type: answer_key
title: "Answer Key — Numerical Validation of the Jacobian"
audience: coaches
---

# Answer Key 2.4 — Numerical Validation: Geometric J vs Finite Differences

**Q1 — B.** Central difference: $[\mathbf{p}(+)-\mathbf{p}(-)]/2\varepsilon$. (A is the first-order forward difference.)

**Q2 — B.** Form $R(+)R(-)^\top \approx I + S(2\varepsilon\boldsymbol{\omega})$ and apply vee.

**Q3 — B.** Second order, $\varepsilon^2$.

**Q4 — B.** Round-off floor: below it, error grows again.

**Q5 — B.** Sweep many configurations; errors hide near specific geometries.

**Q6 — model.** Perturb joint $i$ by $+\varepsilon$ and $-\varepsilon$, record the tool pose each time, and divide the change by $2\varepsilon$; that is column $i$, measured rather than derived. *Full credit for the perturb-measure-divide description.*

**Q7 — model.** A difference of rotation matrices is not itself a rotation or an angular velocity; the correct angular rate comes from the relative rotation $R(+)R(-)^\top$ read through the vee operator (Lesson 1.2). *Full credit for "matrix subtraction isn't angular velocity."*

**Q8 — model.** It is cheap, model-agnostic, and catches sign/off-by-one/axis errors before the robot moves — comparing predicted columns to measured tool motion across configurations. *Full credit for "catches silent errors before motion."*

### Watch for
- Subtracting rotation matrices directly for the angular part.
- Forward instead of central differences when second-order accuracy is wanted.
- Validating at only one pose; driving $\varepsilon$ below the round-off floor.
