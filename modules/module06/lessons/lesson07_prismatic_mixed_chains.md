---
module: 06
unit: 02
lesson: 2.3
title: "Prismatic Joints, Mixed Chains, and the Full 6×n Jacobian"
core_idea: "A prismatic joint contributes a pure translation along its axis, giving the column [z; 0]; mixing revolute and prismatic columns by joint type assembles the complete 6×n geometric Jacobian for any serial chain."
estimated_time: "40 min"
difficulty: "Intermediate"
prerequisites:
  - "M6 L2.2 — The revolute Jacobian column"
  - "M6 L1.3 — Twists and rigid-body velocity"
  - "M2 — Prismatic vs revolute joint kinematics"
learning_objectives:
  - "Derive the prismatic-joint column [z; 0] and explain its zero angular part."
  - "Assemble a mixed-chain Jacobian by selecting the column form per joint type."
  - "Read the full 6×n geometric Jacobian for an arbitrary serial manipulator."
  - "Use the Jacobian Column Explorer to connect columns to end-effector motion."
tags:
  - geometric-jacobian
  - prismatic
  - mixed-chains
  - demo
---

# Lesson 2.3 — Prismatic Joints, Mixed Chains, and the Full 6×n Jacobian

## 1. Why This Matters
Most real arms are all-revolute, but gantries, SCARA arms, and many specialized
manipulators include **prismatic** (sliding) joints. To build Jacobians for any
serial chain, we need the prismatic column and a rule for combining the two joint
types. The payoff is a single procedure that produces the complete $6\times n$
geometric Jacobian for *any* manipulator — the workhorse object for the rest of
Module 6. This lesson also carries the Installment A interactive demo, where you can
watch columns redraw as you drag the arm.

## 2. Physical Intuition
Slide a prismatic joint and freeze the rest. The whole outboard arm translates
bodily along the joint's axis — it does not rotate at all. So the end-effector picks
up a pure linear velocity equal to the joint's axis (per unit rate) and *zero*
angular velocity. Contrast this with a revolute joint, which contributes both a
rotation (its axis) and the lever-arm linear term. Two joint types, two column
shapes; everything else about the construction is identical.

## 3. Mathematical Foundations
For a **prismatic** joint $i$ sliding along axis $\mathbf{z}_{i-1}$ at unit rate, the
end-effector translates with velocity $\mathbf{z}_{i-1}$ and has no angular velocity:

$$\boxed{\;J_i^{\text{(pris)}} = \begin{bmatrix} \mathbf{z}_{i-1} \\ \mathbf{0} \end{bmatrix} \in \mathbb{R}^6.\;}$$

Compare with the revolute column from Lesson 2.2:

$$J_i^{\text{(rev)}} = \begin{bmatrix} \mathbf{z}_{i-1}\times(\mathbf{o}_n-\mathbf{o}_{i-1}) \\ \mathbf{z}_{i-1} \end{bmatrix}.$$

The **mixed-chain rule** is simply: for each joint $i$, choose the column form by its
type, with $\mathbf{z}_{i-1}$ and $\mathbf{o}_{i-1}$ taken in the base frame from
$T_0^{i-1}$. Assemble:

$$J(\mathbf{q}) = \big[\,J_1\;\;J_2\;\;\cdots\;\;J_n\,\big]\in\mathbb{R}^{6\times n},
\quad J_i = \begin{cases} [\mathbf{z}_{i-1}\times(\mathbf{o}_n-\mathbf{o}_{i-1});\,\mathbf{z}_{i-1}] & \text{revolute}\\[2pt] [\mathbf{z}_{i-1};\,\mathbf{0}] & \text{prismatic.} \end{cases}$$

Note a prismatic joint contributes nothing to the angular block $J_\omega$ — a fact
we will exploit when analyzing which task directions a manipulator can rotate in
(singularities, Unit 5).

## 4. Visual Explanation
`[Visual: side-by-side comparison of a revolute column (axis + lever-arm linear term, with angular part) and a prismatic column (pure translation along axis, zero angular part)]`
**Diagram Specification**

- Left panel: revolute joint — axis $\mathbf{z}$, lever arm to $\mathbf{o}_n$, linear
  term $\mathbf{z}\times(\mathbf{o}_n-\mathbf{o})$, and angular part $\mathbf{z}$;
  column $[\,\cdot\,;\mathbf{z}]$.
- Right panel: prismatic joint — axis $\mathbf{z}$, end-effector sliding along it,
  angular part $\mathbf{0}$; column $[\mathbf{z};\mathbf{0}]$.
- Caption: "Revolute = rotate (axis + lever arm); prismatic = slide (axis only, no
  rotation). Pick the column by joint type."

## 5. Engineering Example
A SCARA arm has two revolute joints (about parallel vertical axes) for planar
positioning and a prismatic joint for vertical insertion. Its Jacobian has two
revolute columns and one prismatic column $[\hat{z};\mathbf{0}]$ for the vertical
slide. Because the prismatic column adds no angular velocity, the SCARA's
orientation is governed solely by the revolute joints — which is exactly why SCARA
arms are prized for fast, orientation-stable vertical placement.

## 6. Worked Example
A 2-DOF planar arm with a revolute base joint (axis $\hat{z}$, link length $1$)
followed by a **prismatic** extension along the arm's current $x$-axis, at extension
$d=0.5$, base angle $\theta=0$. Then $\mathbf{o}_n=(1.5,0,0)$,
$\mathbf{z}_0=(0,0,1)$ (revolute), $\mathbf{z}_1=(1,0,0)$ (prismatic slide
direction).

- Column 1 (revolute): $[\mathbf{z}_0\times(\mathbf{o}_n-\mathbf{o}_0);\mathbf{z}_0]
  = [(0,0,1)\times(1.5,0,0);(0,0,1)] = [(0,1.5,0);(0,0,1)]$.
- Column 2 (prismatic): $[\mathbf{z}_1;\mathbf{0}] = [(1,0,0);(0,0,0)]$.

The revolute column sweeps the tool in $+y$; the prismatic column slides it in $+x$
with no rotation — exactly the two motions you'd expect.

## 7. Interactive Demonstration
**Jacobian Column Explorer.** Drag the joints of a planar arm and watch each
Jacobian column render as an arrow at the end-effector — the instantaneous tool
velocity that joint would produce at unit rate. Toggle joints, switch the third
joint between revolute and prismatic, and observe how the columns (and their sum)
change with configuration. Watch what happens to the columns as the arm approaches a
straight, fully extended pose — a preview of singularities in Unit 5.

*(Embedded widget: `lesson07_jacobian_column_explorer.html`. The student page injects
it here.)*

What to notice:

- Each colored arrow is one column of $J_v$ — one joint's contribution.
- The total tool velocity is the (rate-weighted) sum of the columns.
- Near full extension the two revolute columns become nearly parallel: the arm loses
  the ability to move radially. Hold that thought for Unit 5.

## 8. Coding Exercise
In the companion notebook:

1. Extend `geometric_jacobian(q, joint_types)` to handle both joint types, choosing
   $[\mathbf{z};\mathbf{0}]$ for prismatic and the revolute form otherwise.
2. Build the Jacobian for a mixed revolute–prismatic chain and confirm the prismatic
   column has zero angular part.
3. Verify the full $6\times n$ Jacobian against finite differences (preview of
   Lesson 2.4).

Prints `All checks passed.`

## 9. Knowledge Check
1. Write the prismatic-joint column and explain why its angular block is zero.
2. State the rule for assembling a mixed-chain Jacobian.
3. Why does a SCARA arm's orientation depend only on its revolute joints?
4. In the demo, what happened to the revolute columns near full extension?

## 10. Challenge Problem
A 3-DOF chain is revolute–prismatic–revolute. Write the symbolic form of each column
in terms of the base-frame axes and origins, and identify which columns contribute to
the angular block $J_\omega$. Then argue how many independent angular directions the
end-effector can be commanded in, and what that implies about orientation control.

## 11. Common Mistakes
- **Giving a prismatic joint an angular part.** Sliding produces no rotation; the
  bottom block is $\mathbf{0}$.
- **Reusing the lever-arm term for prismatic joints.** That term is revolute-only.
- **Type/column mismatch.** Always select the column form from the *actual* joint
  type, not position in the chain.

## 12. Key Takeaways
- Prismatic column: $[\mathbf{z}_{i-1};\mathbf{0}]$ — pure translation, no rotation.
- Mixed chains: pick the column form per joint type; assemble side by side.
- The result is the full $6\times n$ geometric Jacobian for any serial manipulator.
- The demo makes columns tangible — and foreshadows singularity loss of mobility.

---

### AI Learning Companion

- **Tutor (re-explain):** "Explain the prismatic column $[\mathbf{z};\mathbf{0}]$ and
  the mixed-chain assembly rule, then quiz me on why prismatic joints add no angular
  velocity."
- **Practice (generate exercises):** "Generate three mixed revolute/prismatic chain
  Jacobian problems. Hold solutions until I answer."
- **Explore (connect to the real world):** "Why are SCARA and gantry arms built with
  prismatic joints? Connect the column structure to their strengths."

### Global Learning Support

- **English (authoritative):** "Explain the prismatic Jacobian column
  $[\mathbf{z};\mathbf{0}]$ and assembling a mixed-chain $6\times n$ Jacobian."
- **Español:** "Explica la columna prismática $[\mathbf{z};\mathbf{0}]$ y el ensamble
  de un jacobiano $6\times n$ de cadena mixta a nivel de robótica."
- **中文（简体）：** "用机器人学课程的水平，解释移动关节列 $[\mathbf{z};\mathbf{0}]$
  以及如何组装混合链的 $6\times n$ 雅可比矩阵。"
- **Türkçe:** "Prizmatik sütun $[\mathbf{z};\mathbf{0}]$'yi ve karışık zincirli
  $6\times n$ Jacobian'ın kurulumunu robotik ders düzeyinde açıkla."

---

*Next lesson: 2.4 — Numerical Validation: Geometric J vs Finite Differences.*
