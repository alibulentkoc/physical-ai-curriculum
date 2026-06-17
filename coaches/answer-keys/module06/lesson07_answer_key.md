---
module: 6
unit: 2
lesson: 7
type: answer_key
title: "Answer Key — Prismatic Joints and Mixed Chains"
audience: coaches
---

# Answer Key 2.3 — Prismatic Joints, Mixed Chains, the Full 6×n Jacobian

**Q1 — B.** $[\mathbf{z}; \mathbf{0}]$.

**Q2 — C.** Zero — sliding produces no rotation.

**Q3 — B.** Pick each column's form by the joint's actual type.

**Q4 — B.** Revolute joints only; the prismatic column adds no angular velocity.

**Q5 — B.** Nearly parallel — the tool loses a direction of motion (a singularity preview).

**Q6 — model.** A prismatic joint translates the outboard arm bodily along its axis without rotating it, so the end-effector gains linear velocity ($\mathbf{z}$) but zero angular velocity. *Full credit for "translation, no rotation."*

**Q7 — model.** For each joint, use $[\mathbf{z}\times(\mathbf{o}_n-\mathbf{o}_{i-1});\mathbf{z}]$ if revolute and $[\mathbf{z};\mathbf{0}]$ if prismatic, with base-frame axes/origins, then place the columns side by side. *Full credit for type-selected columns.*

**Q8 — model.** The two revolute columns became nearly parallel, so the spanned tool-velocity directions collapsed toward a line — foreshadowing kinematic singularities (Unit 5). *Full credit for "columns align → lost direction → singularity."*

### Watch for
- Giving a prismatic joint a nonzero angular part.
- Reusing the revolute lever-arm term for prismatic joints.
