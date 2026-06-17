---
module: 06
unit: 01
lesson: 1.4
title: "Transforming Twists Between Frames"
core_idea: "The same physical motion looks like different velocity numbers to different observers; converting between them takes just two intuitive moves — rotate the arrows into the new frame, and shift the linear part by the lever-arm term ω × d — while every real point velocity stays the same."
estimated_time: "40 min"
difficulty: "Intermediate"
prerequisites:
  - "M6 L1.3 — The twist ξ = [v; ω] and v = ω × r"
  - "M2 — Homogeneous transforms (R, d) between frames"
  - "Cross product and the skew operator"
learning_objectives:
  - "Explain, as a change of observer, why a twist's numbers depend on the frame and reference point."
  - "Apply the two physical moves — rotate components, shift reference point — that make up the transform."
  - "Assemble those moves into the 6×6 twist transform."
  - "Verify a transform by checking that physical point velocities are unchanged."
tags:
  - twist-transform
  - frames
  - velocity-kinematics
  - base-frame
---

# Lesson 1.4 — Transforming Twists Between Frames

## 1. Why This Matters
A robot's Jacobian (Unit 2) reports the gripper's twist in the **base/world frame**
(locked by D-057). But a task often speaks a different language: "push along the
tool's own axis," "track the part in the camera frame." Translating one observer's
velocity numbers into another's is the twist transform. Get it right and the
tool-frame Jacobian of Lesson 2.4 falls out in one line; get it wrong and a robot
that looks still at the wrist drives its tool off course.

## 2. Physical Intuition
Watch a spinning bicycle wheel. Standing on the curb, you write down its velocity one
way. Sitting in a car rolling past, you write down *different* numbers for the *same*
wheel — it now appears to drift backward and its center seems to move. The wheel
didn't change; your description did.

Changing observers does exactly two things to the velocity numbers:

1. **You turned your head** — your axes are oriented differently, so both the linear
   and angular arrows get re-expressed in the new orientation (multiply by $R$).
2. **You stood somewhere else** — you now measure the linear velocity *of a different
   point*, so it picks up the lever-arm term $\boldsymbol{\omega}\times\mathbf{d}$ from
   Lesson 1.3. The angular arrow, shared by the whole body, does not change.

The figure shows the same motion as seen by observer A and observer B. The transform
is just these two moves, stacked — nothing more.

## 3. Mathematical Foundations
*In words first:* re-express the arrows in the new frame ($\times R$), and move the
reference point ($+\,\boldsymbol{\omega}\times\mathbf{d}$). Now write it down.

Let frame $B$ sit at offset $\mathbf{d}$ and orientation $R$ relative to $A$ (both in
$A$'s coordinates). The two moves give:

- **Move 1 — shift the reference point** (still in $A$'s axes): the linear velocity of
  the body point at $B$'s origin is $\mathbf{v}_A + \boldsymbol{\omega}_A\times\mathbf{d}$;
  the angular part is unchanged.
- **Move 2 — rotate into $B$'s axes:** multiply both parts by $R^\top$.

Stacking the two moves is the 6×6 twist transform:

$$\begin{bmatrix} \mathbf{v}_B \\ \boldsymbol{\omega}_B \end{bmatrix}
= \begin{bmatrix} R^\top & -R^\top S(\mathbf{d}) \\ \mathbf{0} & R^\top \end{bmatrix}
\begin{bmatrix} \mathbf{v}_A \\ \boldsymbol{\omega}_A \end{bmatrix},$$

since $-S(\mathbf{d})\boldsymbol{\omega}_A = \boldsymbol{\omega}_A\times\mathbf{d}$. The
two special cases are the two moves in isolation: with $\mathbf{d}=\mathbf{0}$ (same
origin) the matrix is block-diagonal $\text{diag}(R^\top,R^\top)$ — Move 2 only; with
$R=I$ (same axes) only the linear part shifts — Move 1 only. *Back to motion:* the
matrix is bookkeeping for "turn your head, then stand somewhere else." In screw theory
this 6×6 is the adjoint; we use only the geometric form, per D-057.

## 4. Visual Explanation
`[Visual: a two-panel view of one rigid-body motion — observer A and observer B writing different twist numbers for the same wheel — linked by the rotate-and-shift transform]`
**Diagram Specification (multi-panel)**

- **Panel A — "observer A":** the moving body (e.g., a wheel) with frame $A$;
  $\boldsymbol{\xi}_A=[\mathbf{v}_A;\boldsymbol{\omega}_A]$ drawn as arrows.
- **Panel B — "observer B":** the *same* body and motion with frame $B$ offset by
  $\mathbf{d}$ and rotated by $R$; $\boldsymbol{\xi}_B=[\mathbf{v}_B;\boldsymbol{\omega}_B]$
  drawn as different arrows.
- **Between panels:** a labeled transform arrow — "rotate arrows by $R$, shift linear
  part by $\boldsymbol{\omega}\times\mathbf{d}$."
- A small annotation that one chosen world point has the **same** physical velocity in
  both panels.
- Caption: "Different observers, different twist numbers — same motion. Two moves
  convert one to the other."

## 5. Engineering Example
A peg-in-hole routine wants to command "advance the peg 2 mm/s along the tool's own
axis." The base-frame Jacobian gives the gripper twist in world coordinates, so the
controller applies the twist transform with $(R,\mathbf{d})$ = the gripper's current
pose to read the motion in the *tool* frame, command it there, and transform the
result back. Same Jacobian, two observers — no second kinematic model. This is the
everyday reason the transform exists.

## 6. Worked Example
Frame $B$ has $R=I$ (axes aligned) and offset $\mathbf{d}=(0,0.5,0)$ from $A$. A body
twist in $A$ is $\boldsymbol{\xi}_A=[(1,0,0);(0,0,2)]$. Since $R=I$, only the
reference-point move acts:

$$\mathbf{v}_B = \mathbf{v}_A + \boldsymbol{\omega}_A\times\mathbf{d}
= (1,0,0) + (0,0,2)\times(0,0.5,0) = (1,0,0) + (-1,0,0) = (0,0,0),$$

$\boldsymbol{\omega}_B = (0,0,2)$. The origin of $B$ is **instantaneously at rest** —
it sits exactly at the point we found stationary in Lesson 1.3's worked example (the
same body motion). There the forward slide of $A$'s origin and the rotational
lever-arm term cancel: $B$'s origin lies on the instantaneous axis of rotation. The
two lessons describe one motion from two reference points.

## 7. Interactive Demonstration
*(Embedded demo is Lesson 2.3. Guided prediction here.)*

**Predict, then check.** Use the worked-example setup.

1. **Predict** $\mathbf{v}_B$ if $\mathbf{d}$ is doubled to $(0,1,0)$.
2. **Predict** what happens to $\mathbf{v}_B$ if instead $\boldsymbol{\omega}_A=0$
   (pure translation — which move switches off?).
3. **Check** in the notebook, then verify the physical velocity of a fixed world point
   is identical whether computed via $\boldsymbol{\xi}_A$ or $\boldsymbol{\xi}_B$.

## 8. Coding Exercise
In the companion notebook:

1. Implement `twist_transform(R, d)` as the two stacked moves.
2. **Invariance test (the real check):** pick a body motion and a world point $P$;
   compute $\mathbf{v}_P$ via $\boldsymbol{\xi}_A$ and via $\boldsymbol{\xi}_B$, and
   assert they agree.
3. Confirm the special cases: $\mathbf{d}=0$ → block-diagonal (Move 2 only); $R=I$ →
   linear shift only (Move 1 only).

Prints `All checks passed.`

## 9. Knowledge Check
1. Name the two physical moves of a twist transform and what each one does.
2. Which block of the 6×6 encodes the reference-point shift?
3. What stays invariant under any transform, and why is that the correct test?
4. What does the transform reduce to when the two observers share an origin?

## 10. Challenge Problem
Show the transform composes: $A\!\to\!B$ then $B\!\to\!C$ equals the direct
$A\!\to\!C$ transform from the composed pose $(R_{AC},\mathbf{d}_{AC})$. This is what
lets us chain frames freely along a manipulator in Unit 2.

## 11. Common Mistakes
- **Doing one move and forgetting the other.** Both act unless $\mathbf{d}=0$ or $R=I$.
- **Memorizing $R$ vs $R^\top$.** Don't — verify with the invariance test; the physics
  tells you the direction.
- **Treating the 6×6 as block-diagonal in general.** The off-diagonal
  $-R^\top S(\mathbf{d})$ block *is* the reference-point move.

## 12. Key Takeaways
- A twist's numbers depend on the observer (frame + reference point); the motion does
  not.
- The transform is two moves: rotate the arrows by $R$, shift the linear part by
  $\boldsymbol{\omega}\times\mathbf{d}$ (the $-R^\top S(\mathbf{d})$ block).
- Special cases isolate each move: $\mathbf{d}=0$ → rotate only; $R=I$ → shift only.
- Correctness = invariance of physical point velocities — and this is what turns the
  base-frame Jacobian into the tool-frame Jacobian in Lesson 2.4.

---

### AI Learning Companion

- **Tutor (re-explain):** "Explain the twist transform as two observer moves — turn
  your head, stand somewhere else — then quiz me on the two special cases."
- **Practice (generate exercises):** "Generate three twist-transform problems,
  including one invariance check. Withhold answers until I respond."
- **Explore (connect to the real world):** "Why does a peg-in-hole controller convert a
  world-frame twist to the tool frame? Give other examples of re-expressing velocity
  between observers."

### Global Learning Support

- **English (authoritative):** "Explain how a twist transforms between frames as two
  moves (rotate arrows + shift reference point), forming a 6×6 matrix, at
  robotics-course level."
- **Español:** "Explica cómo se transforma un twist entre marcos como dos movimientos
  (rotar vectores + cambiar punto de referencia), formando una matriz 6×6, a nivel de
  robótica."
- **中文（简体）：** "用机器人学课程的水平，把旋量的坐标系变换解释为两步动作（旋转箭头 +
  平移参考点），并组装成 6×6 矩阵。"
- **Türkçe:** "Bir twist'in çerçeveler arası dönüşümünü iki hareket olarak (okları
  döndür + referans noktasını kaydır) ve 6×6 matris kurulumunu robotik ders düzeyinde
  açıkla."

---

*Next lesson: 2.1 — Forward Velocity Kinematics: Defining the Jacobian.*
