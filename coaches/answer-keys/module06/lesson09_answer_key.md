---
module: 6
unit: 3
lesson: 9
type: answer_key
title: "Answer Key — The Analytic Jacobian"
audience: coaches
---

# Answer Key 3.1 — The Analytic Jacobian

**Q1 — B.** Rates of a pose representation. **Q2 — B.** Identical position rows. **Q3 — B.** Angle-rates. **Q4 — B.** The orientation representation. **Q5 — B.** Angle-coordinate commands/errors.

**Q6 — model.** Position velocity is independent of how orientation is described, so $J_p=J_v$ regardless of the angle convention. *Credit for representation-independence of position.*

**Q7 — model.** $J_a=\partial\mathbf{x}/\partial\mathbf{q}=[J_p;J_\phi]$ with $\mathbf{x}=[\mathbf{p};\boldsymbol{\phi}]$; top block position velocity, bottom block angle-rates. *Credit for derivative form + blocks.*

**Q8 — model.** A teleop/orientation controller commanding roll-pitch-yaw rates (error in angle coordinates) maps them to joint rates via the analytic Jacobian. *Accept any angle-coordinate command example.*

### Watch for
- Feeding $\boldsymbol{\omega}$ to an angle-rate controller or vice versa.
- Believing in a single canonical Jacobian (geometric is representation-free; analytic is not).
