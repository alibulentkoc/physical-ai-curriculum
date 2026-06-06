---
title: Module 2 — Topic Map
module: 02
status: proposed (for architect review/refinement)
---

# Module 2 — Topic Map: Spatial Transformations and SE(3)

Eight units, following the architect's proposed sequence (refinements noted inline). Intuition-first throughout; matrix algebra is never the entry point. Lesson counts are planning estimates to be confirmed per-unit at production time.

## Unit 1 — Why Transformations Matter  *(motivation / re-grounding)*
Re-enter the problem physically: a robot must move a point between camera, gripper, and world, again and again. Why a *single, composable representation* is needed — and why Module 1's 2×2 matrices weren't enough (they couldn't translate).
- 1.1 The Robot's Constant Problem (perceive here, act there)
- 1.2 Why Position + Orientation Must Travel Together (pose)
- 1.3 The Limit We Hit in Module 1 (rotation was a matrix; translation wasn't)
- 1.4 Recap / bridge into homogeneous coordinates

## Unit 2 — Homogeneous Coordinates  *(the key device)*
The trick that makes translation a matrix multiply: add a coordinate.
- 2.1 The Idea: One Extra Coordinate
- 2.2 Points vs Directions (the w-coordinate: 1 vs 0)
- 2.3 Translation as a Matrix (at last)
- 2.4 Rotation + Translation in One Matrix
- 2.5 Recap "Homogeneous Coordinates in Physical AI"

## Unit 3 — SE(2) Transformations  *(rigid motion in the plane)*
Rigid-body transforms in 2D: rotate + translate, no distortion.
- 3.1 What "Rigid" Means (distances/angles preserved)
- 3.2 The SE(2) Transformation (3×3 homogeneous form)
- 3.3 Applying SE(2) to Points and Shapes
- 3.4 Inverse Transformations (undo a move; go back a frame)
- 3.5 Recap "Rigid Motion in the Plane"

## Unit 4 — SE(3) Transformations  *(rigid motion in 3D)*
Lift to 3D: rotation in 3D + a translation vector, as a 4×4 homogeneous transform.
- 4.1 From 2D to 3D Rigid Motion (the third axis returns)
- 4.2 3D Rotation (intuition: axis + angle; faux-3D visuals)
- 4.3 The SE(3) Transformation (4×4 homogeneous form)
- 4.4 Translation Vectors in 3D
- 4.5 Applying SE(3); Inverses in 3D
- 4.6 Recap "Rigid Motion in 3D"

## Unit 5 — Transformation Composition  *(chaining)*
Compose transforms into chains; order and inversion in a rigid-motion setting.
- 5.1 Chaining Transforms (a then b then c)
- 5.2 Order Matters, Revisited (now with translation in the matrix)
- 5.3 Frames as a Graph (compose along a path; invert to reverse)
- 5.4 Recap "Composing Rigid Motions"

## Unit 6 — Robot Pose Representation  *(pose = where + which way)*
Represent a robot's (and its parts') pose as an SE(2)/SE(3) element.
- 6.1 What Is a Pose? (position + orientation as one object)
- 6.2 A Pose Is a Transformation (base→world, gripper→base)
- 6.3 Reading and Writing Poses (and updating as the robot moves)
- 6.4 Recap "Pose in Physical AI"

## Unit 7 — Camera-to-Robot Transformations  *(the applied payoff)*
The classic chain made rigorous: camera frame → robot frame → world frame, now as SE(3) transforms.
- 7.1 The Camera→Robot→World Chain as Transforms
- 7.2 Extrinsics: the Camera's Pose on the Robot
- 7.3 Turning a Detection into a World-Frame Target
- 7.4 Recap "From Pixels-in-a-Frame to a World Pose" (concept-level; full intrinsics/projection deferred)

## Unit 8 — Mini Project: Perception-to-Pose Pipeline  *(integration)*
A capstone that wires the module together (no full kinematics): given a detected tomato in the camera frame and the camera's pose on the robot and the robot's pose in the world, compute the tomato's world pose and the move the robot must represent — as a composed chain of SE(3) transforms, verified in a notebook and visualized in a demo.
- 8.1 Project Brief & Scaffolding
- 8.2 Building the Transform Chain
- 8.3 Verifying and Visualizing the Result
- 8.4 Module 2 Wrap / bridge to kinematics (next module)

## Proposed refinements (for architect)

1. **Each unit ends with a short recap** (mirrors Module 1's 2.10/3.8/4.9 pattern). Confirm.
2. **Unit 7 stays concept-level** on camera geometry — extrinsics (the camera's pose) yes; full camera *intrinsics*/projection (focal length, pixels→rays) flagged as a later vision module, to keep Module 2 about rigid transforms. Confirm boundary.
3. **Inverses introduced in SE(2) (3.4) and reused in SE(3)/composition** — needed for "go back a frame" and the mini project. Confirm placement.
4. **3D via faux-3D isometric + interactive demos** (no WebGL), consistent with Module 1. Confirm.
5. **Mini project (Unit 8) is the module assessment's centerpiece** — integrative, not new theory. Confirm scope (perception-to-pose, no kinematics).
6. **Numbering:** Module 2 = `module02/lesson01…` restarting per module, diagrams `m02-l01…`. Confirm (vs continuing Module 1's running count).
