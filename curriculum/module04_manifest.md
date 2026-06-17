---
title: Module 4 — Manifest
module: 04
title_full: Forward Kinematics using Denavit–Hartenberg Parameters
status: IN PRODUCTION
theme: Greenhouse Harvesting Robot (continuous with Modules 1–3)
prerequisite: Module 3 (Camera Geometry and Robotic Perception) complete; Module 2 (SE(3)) essential
tooling_introduced: none new (NumPy, Matplotlib, SymPy; SymPy used for symbolic DH tables)
---

# Module 4 — Manifest: Forward Kinematics using Denavit–Hartenberg Parameters

## What this module is

Module 3 ended on an explicit promise it could not keep alone: the perception pipeline produced a fruit's world position **only because it assumed the arm's pose** $T_{w\leftarrow a}$ was available. Where does that transform come from? Not from the camera — from the **robot's own joints and links**. **Module 4 keeps that promise.** It answers the foundational robotics question:

> **Given the joint angles, where is the end-effector (the gripper) — and what is its full pose in the world?**

This is **forward kinematics**. The arc:

- **Module 1:** the math substrate (frames, vectors, matrices).
- **Module 2:** rigid transforms and SE(3) — the language of pose.
- **Module 3:** the camera — turning fruit into a world position, *given* the arm's pose.
- **Module 4:** the arm itself — composing per-joint transforms down the kinematic chain to compute the gripper's pose from joint angles, supplying exactly the $T_{w\leftarrow a}$ Module 3 assumed.

By the end, a student can build a **Denavit–Hartenberg (DH) parameter table** for a serial manipulator, form each link's transform $T_{i-1}^{i}(\theta_i)$, multiply them into the full forward-kinematics map $T_0^n(\boldsymbol{\theta})$, and compute the end-effector pose for any joint configuration — then connect that pose back to the perception and transform machinery of Modules 2–3.

## The one new idea that unlocks the module

A robot arm is a **chain of rigid links connected by joints**. Each joint contributes one rigid transform (a rotation or a translation) that depends on its single variable. **Forward kinematics is just Module 2 composition applied down the chain:** multiply the per-joint SE(3) transforms in order, and the product maps the base frame to the end-effector frame. The **DH convention** is a disciplined, minimal way (four parameters per joint) to write each of those transforms consistently, so any serial robot's kinematics reduces to a table and a matrix product.

## Educational stance (unchanged)

Five-layer flow on every lesson: **Physical Intuition → Visual Understanding → Mathematical Formulation → Computational Implementation → System Integration.** Lead with the physical arm — joints bending, the gripper moving — *not* with the DH matrix. Build a one-joint arm, then two, then generalize; introduce the four DH parameters only once the need for a consistent per-joint convention is felt. The greenhouse-harvesting-robot narrative continues — now we move the arm that reaches the fruit Module 3 located.

## Scope and deferrals

**In scope:** rigid links and joints (revolute/prismatic); the kinematic chain; per-joint transforms; the four DH parameters ($\theta, d, a, \alpha$) and how to assign frames; building a DH table for a serial arm; the forward-kinematics product $T_0^n(\boldsymbol{\theta})$; computing end-effector **position and orientation** for a given configuration; the **workspace** swept by forward kinematics; and connecting the computed $T_{w\leftarrow a}$ back to the Module 3 perception pipeline. A multi-DOF arm capstone (compute and verify the gripper pose, and place a perceived fruit target in the arm's reach).

**Deferred to later modules (educational boundary — held firm):**
- **Inverse kinematics** (joint angles for a desired pose) → Module 5.
- **Jacobians and differential/velocity kinematics** → Module 6.
- **Control** (torques, feedback) → later modules.
- **Trajectory generation / motion planning** → Module 7.

Module 4 is strictly the **forward** map: configuration → pose. We never solve for joint angles from a target here; we only go joints → gripper.

## Notation conventions

- Joint variables: $\boldsymbol{\theta} = (\theta_1,\dots,\theta_n)$ (revolute) or $d_i$ (prismatic).
- Link transform from frame $i-1$ to frame $i$: $T_{i-1}^{i}$ (a function of the joint variable).
- Forward kinematics: $T_0^n(\boldsymbol{\theta}) = T_0^1 T_1^2 \cdots T_{n-1}^n$.
- DH parameters per joint $i$: $\theta_i$ (joint angle about $z_{i-1}$), $d_i$ (offset along $z_{i-1}$), $a_i$ (link length along $x_i$), $\alpha_i$ (link twist about $x_i$). **Standard (distal) DH convention** used throughout; noted explicitly because the modified convention orders the factors differently.
- The arm's base frame is the world/robot-base frame from Modules 2–3; the end-effector pose in the world is $T_{w\leftarrow a} \equiv T_0^n$.

## Numbering and assets

Numbering **restarts** for Module 4: lessons `module04/lesson01…`, diagrams `m04-l01…`, notebooks `M04_U0Y_*`. Generator wired by adding `"04"` to `MODULES`, `MODULE_TITLES["04"]`, and `UNIT_TITLES` for the M4 units; nav added manually (Module → Unit → Lesson). All existing production standards, the lesson template, the design system, and the validator apply unchanged.

## Bridges

- **Backward to Modules 2–3:** each DH link transform is a Module 2 SE(3) element; the forward-kinematics product is Module 2 composition; the resulting end-effector pose is precisely the $T_{w\leftarrow a}$ that Module 3's perception pipeline assumed.
- **Forward to Module 5:** forward kinematics is the function we will *invert* in Module 5 (inverse kinematics) — knowing $T_0^n(\boldsymbol{\theta})$ is the prerequisite for asking which $\boldsymbol{\theta}$ reaches a target.
