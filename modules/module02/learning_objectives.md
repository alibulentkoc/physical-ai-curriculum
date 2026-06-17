---
title: Module 2 — Learning Objectives
module: 02
status: proposed
---

# Module 2 — Learning Objectives

Measurable objectives per unit. Each is phrased as something a student can *do*; together they define "ready for kinematics" without requiring kinematics here.

## Module-level objectives

On completing Module 2, a student can:

1. Explain why a robot needs a single, composable representation for position **and** orientation together (pose).
2. Use **homogeneous coordinates** to express translation (and rotation+translation) as a single matrix.
3. Define and apply **SE(2)** and **SE(3)** rigid-body transformations to points and frames.
4. **Compose** transformations into chains, apply their **inverses**, and reason about order.
5. Represent a robot's **pose** as an SE(2)/SE(3) element and update it as the robot moves.
6. Carry a detection through the **camera → robot → world** chain as composed transforms.
7. Complete a **perception-to-pose** mini project end to end (no full kinematics).

## Per-unit objectives

**Unit 1 — Why Transformations Matter**
- Describe the robot's recurring "perceive here, act there" problem in physical terms.
- Explain why position and orientation must travel together as a single pose.
- State the Module 1 limitation (translation wasn't a matrix) that homogeneous coordinates will fix.

**Unit 2 — Homogeneous Coordinates**
- Write a 2D/3D point in homogeneous form and explain the role of the extra (w) coordinate.
- Distinguish points (w = 1) from directions (w = 0).
- Express translation, and rotation+translation, as a single matrix multiplication.

**Unit 3 — SE(2) Transformations**
- Define a rigid-body transformation (preserves distances and angles).
- Build and apply a 3×3 SE(2) transform to points and shapes.
- Compute and use the inverse of an SE(2) transform.

**Unit 4 — SE(3) Transformations**
- Extend rigid motion to 3D: 3D rotation + translation as a 4×4 SE(3) transform.
- Describe 3D rotation intuitively (axis + angle) using faux-3D visuals.
- Apply SE(3) to 3D points and compute inverses.

**Unit 5 — Transformation Composition**
- Chain multiple transforms and predict the combined effect.
- Explain how order and inversion interact in a chain.
- Compose along a path of frames and reverse it by inversion.

**Unit 6 — Robot Pose Representation**
- Define a pose as position + orientation, and represent it as an SE(2)/SE(3) element.
- Interpret a pose as a transformation between two frames (e.g. base→world).
- Update a stored pose as the robot moves.

**Unit 7 — Camera-to-Robot Transformations**
- Represent the camera→robot→world chain as composed SE(3) transforms.
- Explain camera **extrinsics** as the camera's pose on the robot.
- Convert a frame-relative detection into a world-frame target (concept level).

**Unit 8 — Mini Project: Perception-to-Pose Pipeline**
- Assemble a transform chain that takes a detected tomato (camera frame) to a world pose.
- Verify the result numerically (notebook) and visually (demo).
- Articulate what remains for a future kinematics module.

## Out of scope (explicit, for continuity)

- Full **robot kinematics** (joint angles → end-effector pose, Jacobians, IK) — later module.
- Camera **intrinsics / projection** (focal length, distortion, pixels→rays) — later vision module; Module 2 treats the camera's *pose* (extrinsics) only.
- Dynamics, control, and trajectory planning — later modules.
