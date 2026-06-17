---
module: 6
type: midpoint_assessment
title: "Module 6 Midpoint Assessment — Units 1–4"
covers: "Differential motion & twists · the Jacobian & velocity kinematics · analytic Jacobian, frames & representations · rank, manipulability & duality"
estimated_time: "60–75 min"
---

# Module 6 — Midpoint Assessment (Units 1–4)

You are halfway through Module 6. The first half built the Jacobian *as the subject*:
from differential motion, to the velocity map, to the analytic/geometric distinction
and frames, to what the robot can and cannot do. This assessment checks that arc.
Sections A–D mirror the four units; Section E is integrative. Computational items can be
answered with the lesson notebooks.

---

## Section A — Differential Motion and Twists (Unit 1)

**A1.** Write the differential approximation of a rotation by $\delta\boldsymbol{\theta}$
and explain in one sentence why differential rotations commute but finite ones do not.

**A2.** State the law of motion relating $\dot R$ to angular velocity, and explain the
difference between spatial ($\boldsymbol{\omega}_s$) and body ($\boldsymbol{\omega}_b$)
angular velocity.

**A3.** A rigid body has $\mathbf{v}=(1,0,0)$ and $\boldsymbol{\omega}=(0,0,2)$. Find the
point along $+y$ that is instantaneously at rest, and state which twist block changes if
you re-report the twist about that point.

## Section B — The Jacobian and Velocity Kinematics (Unit 2)

**B1.** Write forward velocity kinematics and explain the "sum-of-pushes"
interpretation of the columns of $J$.

**B2.** Give the geometric Jacobian column for (i) a revolute joint and (ii) a prismatic
joint, and explain why the prismatic column's angular block is zero.

**B3.** Describe how to validate a Jacobian by finite differences — including how the
*angular* part is obtained — and state the expected convergence order.

## Section C — Analytic Jacobian, Frames, Representations (Unit 3)

**C1.** Distinguish the analytic Jacobian from the geometric Jacobian. Which rows are
identical, and which differ?

**C2.** Write the relationship $\boldsymbol{\omega}=B(\boldsymbol{\phi})\dot{\boldsymbol{\phi}}$
and the link $J_\omega=B J_\phi$. What is the physical meaning of one column of $B$?

**C3.** A controller logs exploding commanded joint rates. Explain how you decide whether
this is a **representation** singularity or a **kinematic** singularity, naming the matrix
you inspect in each case.

## Section D — Capability: Rank, Manipulability, Duality (Unit 4)

**D1.** Name the three capability buckets the Jacobian sorts motion into, and give the
linear-algebra object behind each.

**D2.** Describe the manipulability ellipsoid as a picture: what are its long axis, short
axis, and a collapsed axis? Then write the Yoshikawa measure $w$ and state what it equals
in terms of singular values — and one thing it cannot capture.

**D3.** State $\boldsymbol{\tau}=J^\top\mathbf{F}$ and the force/velocity ellipsoid
duality. In which direction is a robot easy to move but weak to push?

**D4 (intuition — answer in words, no equations).** A robot slides a heavy block
across a tabletop (top-down view). In its current posture the tool moves easily
forward/back but only sluggishly left/right.
(a) Describe the manipulability ellipse: which way is it long, which way short?
(b) If the task suddenly demanded fast left/right motion in this posture, what would
happen to the joint speeds, and what configuration is this posture approaching?
(c) Using force/velocity duality, in which direction can the robot shove the block most
forcefully — and why is that the *opposite* of the easy-motion direction?

## Section E — Integrative Problem

A planar 2R arm ($L_1=L_2=1$) is commanded to move its tool in a straight world line that
passes *through* the fully extended (straight-arm) configuration.

**E1.** Using the capability picture, explain what happens to the manipulability ellipsoid
as the arm approaches full extension, and which tool-velocity direction becomes
impossible.

**E2.** Compute the Yoshikawa measure $w(\theta_2)$ symbolically and identify where it
vanishes.

**E3.** Using force/velocity duality, explain what happens to the arm's ability to *exert
force* along the impossible direction at that configuration.

**E4.** Connect back to Module 5: the same matrix you are analyzing here was used as what,
inside the M5 numerical IK solver? In one sentence, state how Module 6 has reframed it.
