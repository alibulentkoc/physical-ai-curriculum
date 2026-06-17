---
title: Module 4 — Midpoint Assessment (Readiness Checkpoint)
position: After Unit 4 (The Forward Kinematics Map)
covers: [Unit 1 why kinematics, Unit 2 one-joint transform, Unit 3 chaining transforms, Unit 4 general T_0^n + position/orientation + FK in code]
excludes: [Denavit-Hartenberg parameters, DH tables, workspace, perception bridge, the mini project]
format: formative readiness checkpoint; unlimited attempts; not graded
---

# Module 4 — Midpoint Assessment (Readiness Checkpoint)

**Placement:** after Unit 4. The first half of Module 4 builds forward kinematics from the ground up — one joint, then a chain, then the general $SE(3)$ product $T_0^n(\boldsymbol{\theta})$ — and makes it runnable. This checkpoint confirms a student can compute a serial arm's gripper pose before the second half introduces the **DH convention** that standardizes how each factor is written. It is formative — a readiness signal, not a grade.

**The readiness signal:** given an arm's joint transforms and a configuration, can the student form $T_0^n$, read out the gripper's position and orientation, and reconcile the matrix result with the planar closed form? If yes, they are ready for Units 5–8.

---

## Part A — Concept checks (short answer)

1. Distinguish *configuration* (joint space) from *pose* (task space). Which one does forward kinematics take as input?
2. Why is forward kinematics single-valued in the forward direction but generally many-to-one? Give a one-line example.
3. For a serial arm, how many degrees of freedom does it have, and how does that relate to the number of joints?
4. Write the general forward-kinematics product for an $n$-joint arm. Why must the factors be multiplied base→tip, and why does order matter?
5. In the end-effector pose $T_0^n$, where do you find the gripper's position, and where its orientation? What do the columns of the rotation block represent?

## Part B — Build and apply

6. One-joint planar arm, $L=0.5$. Give the gripper position and orientation at $\theta = 120°$.
7. Two-link planar arm, $L_1=0.4, L_2=0.3$. Compute the gripper position and orientation at $(\theta_1,\theta_2) = (30°, 60°)$ using the accumulated-angle formula.
8. Show that the matrix product $T_0^1(30°)\,T_1^2(60°)$ gives the same translation column as your answer to Q7. (You may describe the steps rather than multiply by hand.)
9. Three-link planar arm, $L_1=0.4, L_2=0.3, L_3=0.2$, angles $(30°, 60°, -30°)$. Compute the gripper position and orientation.
10. For a 6-DOF arm, how many $SE(3)$ factors does $T_0^6$ have? If you change only $\theta_6$, does the gripper position generally change? Does $\theta_1$ changing affect the orientation?

## Part C — Reasoning

11. Explain why forward kinematics is "evaluate a function" (easy) while inverse kinematics is "solve an equation" (hard, Module 5). 
12. Two configurations place the gripper at the same point with different orientations. Explain how a redundant arm uses this, and why orientation (not just position) matters for grasping fruit.

---

## What "ready" looks like

A student ready for Units 5–8 can:

- compute the gripper pose of a planar 2-/3-link arm by the accumulated-angle formula **and** by the matrix product, and confirm they agree;
- form the general $SE(3)$ product $T_0^n(\boldsymbol{\theta})$ and extract position (translation column) and orientation (rotation block, columns = gripper axes);
- explain configuration vs pose and why FK is many-to-one;
- articulate why forward is easy and inverse is hard.

If any of these is shaky, revisit: Unit 2 (one-joint transform), Unit 3 (chaining as a product), or Unit 4.3 (FK in code) before starting the DH convention.

*Answer key: `coaches/answer-keys/module04/midpoint_answer_key.md` (coaches only).*
