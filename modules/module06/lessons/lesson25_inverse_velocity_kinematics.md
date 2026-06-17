---
module: 06
unit: 07
lesson: 7.1
title: "Inverse Velocity Kinematics: From Desired Twist to Joint Rates"
core_idea: "Forward velocity kinematics asked 'given joint rates, how does the tool move?'; the inverse question — 'to move the tool this way, what joint rates do I need?' — is answered by inverting the velocity map, q̇ = J⁻¹ξ for a non-redundant arm, which is geometrically just un-stretching the manipulability ellipsoid."
estimated_time: "35 min"
difficulty: "Intermediate"
prerequisites:
  - "M6 L2.1 — Forward velocity kinematics ξ = J q̇"
  - "M6 L6.1 — The SVD / ellipsoid anatomy"
  - "M6 L5.1 — Singularity = non-invertible direction"
learning_objectives:
  - "State the inverse velocity problem: find q̇ producing a desired tool twist ξ."
  - "Solve it for a square, non-singular Jacobian via q̇ = J⁻¹ξ."
  - "Interpret the inverse geometrically as un-stretching the ellipsoid."
  - "Recognize that invertibility fails exactly at singularities."
tags:
  - inverse-velocity-kinematics
  - jacobian-inverse
  - velocity-layer
  - capability
---

# Lesson 7.1 — Inverse Velocity Kinematics: From Desired Twist to Joint Rates

## 1. Why This Matters
Everything so far ran *forward*: joints move, the tool responds. But control runs the
other way — you know how you want the **tool** to move and must find the **joint** rates
that produce it. That is inverse velocity kinematics, and it is the doorway to making a
robot actually follow a commanded motion. For a non-redundant arm away from
singularities, the answer is a clean matrix inverse; the rest of Unit 7 handles the cases
where it is not.

## 2. Physical Intuition
You want the tool to slide right at a chosen speed. Which joints, and how fast? The
forward map turned joint rates into tool motion by combining per-joint pushes (Unit 2);
the inverse map runs that backwards — it finds the unique blend of joint rates whose
pushes add up to exactly the tool motion you asked for. When the arm is healthy (the
ellipsoid is full, no collapsed axis), there is exactly one such blend and it is easy to
find. When the arm is near a singularity, the direction you want may be the one the
ellipsoid has nearly lost — and the inverse strains (the next lessons handle that).

## 3. Visual Explanation
`[Visual: the forward map drawn as joint-rate circle → tool-velocity ellipse, and the inverse map drawn as the desired tool velocity → the joint rates that produce it (un-stretching the ellipse back to the circle)]`
**Diagram Specification (multi-panel)**

- **Panel 1 — forward:** unit joint-rate circle → ellipse (via $J$), labeled "Unit 2."
- **Panel 2 — inverse:** a chosen desired tool velocity $\boldsymbol{\xi}$ inside the
  ellipse, mapped back (via $J^{-1}$) to the joint rates $\dot{\mathbf{q}}$ that produce it
  — "un-stretching" the ellipse to the circle.
- Caption: "Inverse velocity kinematics = run the ellipsoid backwards: desired tool
  motion → the joint rates that make it."

## 4. Mathematical Foundations
*In words first:* solve the linear system "Jacobian times unknown joint rates equals
desired tool twist."

Given a desired tool twist $\boldsymbol{\xi}_d$, find $\dot{\mathbf{q}}$ with
$J(\mathbf{q})\dot{\mathbf{q}}=\boldsymbol{\xi}_d$. For a **square, non-singular** Jacobian
($n$ joints, $n$ task dimensions, $\det J\neq 0$):

$$\boxed{\,\dot{\mathbf{q}} = J(\mathbf{q})^{-1}\,\boldsymbol{\xi}_d.\,}$$

This is the unique joint-rate vector producing $\boldsymbol{\xi}_d$. In SVD terms,
$J^{-1}=V\Sigma^{-1}U^\top$ — un-rotate, divide by the gains, un-rotate — which is exactly
"un-stretching" the ellipsoid (Lesson 6.1). Two caveats set up the rest of Unit 7:

- **Redundant arms** ($n>$ task dimension): $J$ is not square, so there is no plain
  inverse — many solutions exist (Lesson 7.2, the pseudoinverse).
- **Singularities:** $\det J=0$, so $J^{-1}$ does not exist; $\Sigma^{-1}$ has a $1/0$
  (Lessons 7.3, the damped inverse).

*Back to motion:* away from those cases, inverse velocity kinematics is one matrix solve —
the desired tool twist in, the joint rates out.

## 5. Engineering Example
A 6-DOF arm asked to translate its tool along a weld seam at constant speed converts that
desired tool twist into joint rates every control cycle with $\dot{\mathbf{q}}=J^{-1}\boldsymbol{\xi}_d$,
recomputing $J$ at the current pose. This is the heart of the velocity layer: a steady
stream of "here's how I want the tool to move" turned into "here's how to drive the
joints." The seam-tracking itself (where the seam is, how fast to go) is a *trajectory*
question for Module 7; here we only resolve a given desired velocity into joint rates.

## 6. Worked Example
For a planar 2R arm at a non-singular pose, pick a desired tool velocity (say
$\boldsymbol{\xi}_d=(0.3,-0.2)$) and solve $\dot{\mathbf{q}}=J^{-1}\boldsymbol{\xi}_d$. Feeding
that $\dot{\mathbf{q}}$ back through the forward map returns exactly $\boldsymbol{\xi}_d$ — the
inverse is verified by the round trip. The notebook does this and confirms
$J\dot{\mathbf{q}}=\boldsymbol{\xi}_d$ to machine precision.

## 7. Interactive Demonstration
*(The capstone Analyzer/Tracker demo at L29 brings inverse velocity kinematics to life.
Guided prediction here.)*

**Predict, then check.**

1. **Predict** whether $J^{-1}\boldsymbol{\xi}_d$ reproduces $\boldsymbol{\xi}_d$ through the
   forward map.
2. **Predict** what happens to $J^{-1}$ as the arm nears a singularity.
3. **Check** in the notebook (round-trip + near-singular conditioning).

## 8. Coding Exercise
In the companion notebook:

1. For a non-singular planar 2R pose, solve $\dot{\mathbf{q}}=J^{-1}\boldsymbol{\xi}_d$ and
   confirm $J\dot{\mathbf{q}}=\boldsymbol{\xi}_d$.
2. Show $J^{-1}=V\Sigma^{-1}U^\top$ matches the direct inverse.
3. Move toward a singular pose and watch the conditioning of $J^{-1}$ degrade.

Prints `All checks passed.`

## 9. Knowledge Check
1. State the inverse velocity problem.
2. Give the solution for a square, non-singular Jacobian.
3. Interpret the inverse in SVD / ellipsoid terms.
4. Name the two cases where the plain inverse fails.

## 10. Challenge Problem
Show that $J^{-1}=V\Sigma^{-1}U^\top$ for a square non-singular $J=U\Sigma V^\top$, and
explain why the inverse "un-stretches" the ellipsoid. What does the largest entry of
$\Sigma^{-1}$ ($=1/\sigma_{\min}$) tell you about the joint-rate cost of the hardest
direction?

## 11. Common Mistakes
- **Using $J^{-1}$ for a redundant arm.** It is not square; use the pseudoinverse (Lesson
  7.2).
- **Ignoring singularities.** $J^{-1}$ does not exist there; damp (Lesson 7.3).
- **Forgetting $J$ depends on $\mathbf{q}$.** Recompute it at the current pose each cycle.

## 12. Key Takeaways
- Inverse velocity kinematics: find $\dot{\mathbf{q}}$ with $J\dot{\mathbf{q}}=\boldsymbol{\xi}_d$.
- Square non-singular case: $\dot{\mathbf{q}}=J^{-1}\boldsymbol{\xi}_d=V\Sigma^{-1}U^\top\boldsymbol{\xi}_d$ —
  un-stretch the ellipsoid.
- Redundant arms and singularities need the pseudoinverse / damping (next lessons).
- This is the core of the velocity layer: desired tool twist → joint rates.

---

### AI Learning Companion

- **Tutor (re-explain):** "Explain inverse velocity kinematics and q̇ = J⁻¹ξ as un-stretching
  the ellipsoid. Then quiz me."
- **Practice (generate exercises):** "Give me three problems solving for joint rates from a
  desired tool twist, including a near-singular case. Hold solutions."
- **Explore (connect to the real world):** "How does the velocity layer turn a desired tool
  motion into joint commands each control cycle?"

### Global Learning Support

- **English (authoritative):** "Explain inverse velocity kinematics, q̇ = J⁻¹ξ, and its SVD
  form, at robotics-course level."
- **Español:** "Explica la cinemática inversa de velocidad, q̇ = J⁻¹ξ, y su forma SVD, a
  nivel de robótica."
- **中文（简体）：** "用机器人学课程的水平，解释逆速度运动学 q̇ = J⁻¹ξ 及其 SVD 形式。"
- **Türkçe:** "Ters hız kinematiğini, q̇ = J⁻¹ξ'yi ve SVD biçimini robotik ders düzeyinde
  açıkla."

---

*Next lesson: 7.2 — Redundancy Resolution: The Pseudoinverse and Null-Space Motion.*
