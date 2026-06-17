---
module: 6
unit: 3
lesson: 12
type: answer_key
title: "Answer Key — Representation vs Kinematic Singularity"
audience: coaches
---

# Answer Key 3.4 — Representation vs Kinematic Singularity

**Q1 — B.** $\det B=0$. **Q2 — B.** $\operatorname{rank}J$ drops. **Q3 — B.** Robot still moves; description breaks. **Q4 — B.** Kinematic. **Q5 — B.** Representation singularity.

**Q6 — model.** Representation: $\det B(\boldsymbol{\phi})=0$ — the angle map breaks (gimbal lock). Kinematic: $\operatorname{rank}J(\mathbf{q})$ drops — the robot loses a motion direction. *Credit for both matrices.*

**Q7 — model.** It is a physical property of the manipulator geometry (the tool genuinely cannot move in some direction); coordinates only relabel, they cannot restore lost mobility. *Credit for "physical, not bookkeeping."*

**Q8 — model.** Check whether the blow-up tracks the orientation representation (pitch→90°, $\det B\to0$) or a collapsing smallest singular value of $J$. The former is a harmless representation issue (switch representation); the latter is a real kinematic singularity needing damping/path change. *Credit for "diagnose which matrix degenerates."*

### Watch for
- Calling gimbal lock a robot singularity; trying to fix a kinematic singularity with coordinates; inspecting the wrong matrix.
