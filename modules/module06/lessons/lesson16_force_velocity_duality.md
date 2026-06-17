---
module: 06
unit: 04
lesson: 4.4
title: "Force and Velocity Duality: τ = JᵀF and the Force Ellipsoid"
core_idea: "The same Jacobian that maps joint rates to tool velocity maps tool forces back to joint torques through its transpose, τ = JᵀF — and the consequence is a beautiful trade-off: the directions a robot moves most easily are exactly the directions it can push least hard."
estimated_time: "35 min"
difficulty: "Intermediate"
prerequisites:
  - "M6 L4.2 — The manipulability (velocity) ellipsoid"
  - "M6 L2.1 — ξ = J q̇"
  - "Work/energy: force·velocity, torque·joint-rate"
learning_objectives:
  - "Derive τ = JᵀF from the equivalence of work in joint space and task space."
  - "Picture the force ellipsoid as the dual of the velocity ellipsoid (reciprocal axes)."
  - "Explain the easy-to-move / hard-to-push trade-off geometrically."
  - "Keep the treatment about capability, not statics machinery."
tags:
  - force-velocity-duality
  - jacobian-transpose
  - force-ellipsoid
  - capability
---

# Lesson 4.4 — Force and Velocity Duality: τ = JᵀF and the Force Ellipsoid

## 1. Why This Matters
So far the Jacobian has been about motion. But the very same matrix governs *force*:
the joint torques needed to hold a tool force are $\boldsymbol{\tau}=J^\top\mathbf{F}$.
This is not a new model — it is the transpose of the one we already have — and it yields
one of the most useful intuitions in robotics: a robot's easy-to-move directions are its
weak-to-push directions, and vice versa. We keep this geometric and capability-focused;
the goal is the trade-off picture, not a statics course.

## 2. Physical Intuition
Lean on a long fishing rod near the tip: it moves easily but you can barely resist a
force there — small effort, big motion, little strength. Now hold it near the base: hard
to move, but very strong. Robots feel the same trade-off pose-by-pose. In a direction
where the tool moves fast for little joint effort (the ellipsoid's long axis), the arm
can resist only a small force; in a stiff, hard-to-move direction (the short axis), it can
push hard. Velocity capability and force capability are two sides of one coin, traded by
the geometry.

## 3. Visual Explanation
`[Visual: the velocity ellipsoid and the force ellipsoid drawn together, sharing axes but with reciprocal lengths — long velocity axis lines up with short force axis and vice versa]`
**Diagram Specification (multi-panel)**

- **Panel 1 — velocity ellipsoid:** long axis = easy-to-move direction (large $\sigma$),
  short axis = hard-to-move.
- **Panel 2 — force ellipsoid (overlaid or beside):** same axis directions, but lengths
  $1/\sigma$ — long where velocity was short. Arrows show "easy to move here = weak to
  push here."
- Caption: "Force ellipsoid = velocity ellipsoid with reciprocal axes. Move easily one
  way, push hard the other."

## 4. Mathematical Foundations
*In words first:* power must match whether you compute it at the joints or at the tool;
equating the two gives the transpose relationship.

The mechanical power delivered is the same measured in joint space or task space:
$\boldsymbol{\tau}^\top\dot{\mathbf{q}} = \mathbf{F}^\top\boldsymbol{\xi}
= \mathbf{F}^\top J\dot{\mathbf{q}}$ for all $\dot{\mathbf{q}}$. Hence

$$\boxed{\,\boldsymbol{\tau} = J^\top\mathbf{F}.\,}$$

The Jacobian *transpose* maps a tool force/wrench $\mathbf{F}$ to the joint torques that
balance it. Geometrically, the **force ellipsoid** (joint torques of unit norm, mapped to
achievable tool forces) shares the velocity ellipsoid's axis directions but has
**reciprocal** semi-axes: where velocity has length $\sigma_i$, force has length
$1/\sigma_i$. So:

- long velocity axis (easy to move) ⇔ short force axis (weak to push);
- short velocity axis (hard to move) ⇔ long force axis (strong to push);
- at a singularity a velocity axis $\to 0$, so the dual force axis $\to\infty$: the arm
  can resist arbitrarily large force in the lost direction (it is "braced"), while being
  unable to move there at all.

*Back to motion (and force):* one Jacobian, two capabilities, locked in inverse
proportion by the geometry.

## 5. Engineering Example
A robot deburring an edge must *move* fast along the edge but *press* firmly into it. The
two requirements pull in opposite directions on the ellipsoid: a posture that makes
sliding easy makes pressing weak. Designers choose an arm posture that balances the two —
often deliberately keeping the press direction along a shorter velocity axis so the arm
can exert force there. Recognizing the trade-off is what turns "the arm feels mushy when
pressing" into a posture/redundancy fix.

## 6. Worked Example
For a planar 2R arm at a generic pose, compute the velocity ellipse axes (singular values
$\sigma_1,\sigma_2$) and the force ellipse axes ($1/\sigma_1,1/\sigma_2$) along the same
directions. The notebook confirms the force ellipsoid's semi-axes are exactly the
reciprocals of the velocity ellipsoid's, so the easy-to-move direction is the weak-to-push
direction. As the arm approaches straight, the collapsing velocity axis ($\sigma\to 0$)
becomes a diverging force axis ($1/\sigma\to\infty$).

## 7. Interactive Demonstration
*(The L17 flagship demo toggles the dual force ellipsoid alongside the velocity ellipsoid.
Guided prediction here.)*

**Predict, then check.**

1. **Predict** how the force ellipse axes relate to the velocity ellipse axes.
2. **Predict** what happens to the force ellipse as the arm nears a singularity.
3. **Check** in the notebook by comparing singular values of $J$ and of $J^{-\top}$.

## 8. Coding Exercise
In the companion notebook:

1. For a planar 2R arm, compute velocity-ellipse semi-axes ($\sigma_i$) and force-ellipse
   semi-axes (singular values of $J^{-\top}$).
2. Confirm the force semi-axes equal $1/\sigma_i$ along the same directions.
3. Show the reciprocal blow-up near a singular pose.

Prints `All checks passed.`

## 9. Knowledge Check
1. Derive $\boldsymbol{\tau}=J^\top\mathbf{F}$ from power equivalence.
2. How do the force-ellipsoid axes relate to the velocity-ellipsoid axes?
3. State the easy-to-move / hard-to-push trade-off in one sentence.
4. What happens to the force ellipsoid at a singularity, and what does it mean physically?

## 10. Challenge Problem
Using $J=U\Sigma V^\top$, show the force ellipsoid (image of the unit torque ball under
$J^{-\top}$ for square $J$) has the same axis directions $U$ as the velocity ellipsoid but
semi-axes $1/\sigma_i$. Then interpret the singular limit $\sigma\to 0$: why can the arm
resist unbounded force in a direction it cannot move?

## 11. Common Mistakes
- **Turning this into a full statics course.** The point is the duality picture, not free-
  body diagrams.
- **Forgetting the transpose.** Motion uses $J$; force uses $J^\top$.
- **Expecting force and velocity to be "good" in the same direction.** They are inverse —
  easy-to-move is weak-to-push.

## 12. Key Takeaways
- $\boldsymbol{\tau}=J^\top\mathbf{F}$: the Jacobian transpose maps tool force to joint
  torque (from power equivalence).
- The force ellipsoid shares the velocity ellipsoid's axes with reciprocal lengths
  ($1/\sigma_i$).
- Easy-to-move directions are weak-to-push directions, and vice versa.
- At a singularity, a vanishing velocity axis becomes a diverging force axis — strong but
  immobile.

---

### AI Learning Companion

- **Tutor (re-explain):** "Explain $\boldsymbol{\tau}=J^\top\mathbf{F}$ and the
  velocity/force ellipsoid duality with the fishing-rod intuition. Then quiz me."
- **Practice (generate exercises):** "Give me three problems on force/velocity duality and
  the force ellipsoid, including one near a singularity. Hold solutions."
- **Explore (connect to the real world):** "How does the easy-to-move/hard-to-push
  trade-off shape posture choice in pressing, deburring, and assembly tasks?"

### Global Learning Support

- **English (authoritative):** "Explain $\boldsymbol{\tau}=J^\top\mathbf{F}$ and the
  force/velocity ellipsoid duality (reciprocal axes), at robotics-course level."
- **Español:** "Explica $\boldsymbol{\tau}=J^\top\mathbf{F}$ y la dualidad de elipsoides
  fuerza/velocidad (ejes recíprocos), a nivel de robótica."
- **中文（简体）：** "用机器人学课程的水平，解释 $\boldsymbol{\tau}=J^\top\mathbf{F}$ 以及
  力/速度椭球的对偶性（互为倒数的轴）。"
- **Türkçe:** "$\boldsymbol{\tau}=J^\top\mathbf{F}$'yi ve kuvvet/hız elipsoidi dualitesini
  (resiprokal eksenler) robotik ders düzeyinde açıkla."

---

*Next: Midpoint Assessment (Units 1–4), then Unit 5 — Singularity Theory. (Installment C)*
