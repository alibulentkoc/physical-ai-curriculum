# Module 3 — Camera Geometry and Robotic Perception
## Completion Report

**Status:** ✅ COMPLETE
**Theme:** Greenhouse Harvesting Robot — turning what the camera sees into where the fruit is.

---

## Summary

Module 3 builds the **perception spine** of the harvesting robot: the full, verifiable path from a camera image to a 3D world position the arm can reach. It develops the forward camera model (world → pixels) and then inverts it (pixels → world), closing the loop with Module 2's spatial transforms and setting up Module 4's kinematics.

The module is organized as a forward half (Units 1–5: how a 3D world becomes a 2D image) and an inverse half (Units 6–7: how an image, plus depth and the camera's pose, becomes a 3D world position), capped by an integrative mini-project (Unit 8).

---

## Unit arc

| Unit | Title | Contribution |
|---|---|---|
| 1 | Why Perception | A single image discards depth; perception must recover 3D from 2D. |
| 2 | The Pinhole Camera | Projection keeps direction and divides by Z (x = fX/Z). |
| 3 | Camera Intrinsics K | Metric rays → pixels via K (focal lengths, principal point). |
| 4 | Projection in Practice (Midpoint) | The full forward pipeline world→pixel, OpenCV-verified. |
| 5 | Lens Distortion | Real lenses bend; radial (k1,k2,k3) + tangential (p1,p2) model, applied before K; undistortion (iterative) restores ideal pinhole geometry. |
| 6 | Back-Projection: Pixels to 3D | A pixel is a ray (K⁻¹); depth selects the point, P_c = Z·(x_n,y_n,1). |
| 7 | From Pixels to the Robot | Camera-frame point → world frame via the Module 2 extrinsics chain T(world←cam)=T(world←arm)·T(arm←cam). |
| 8 | Mini Project: See the Fruit, Place It in the World | End-to-end, verified pixel→world capstone integrating all of Module 3 with Module 2. |

---

## The central pipeline

The whole module reduces to one verifiable computation:

> **pixel → undistort → back-project (+depth) → transform → verify → world position**
>
> P̃_w = T(world←cam) · [ Z · K⁻¹ · undistort(u, v) ]

with three acceptance checks: **re-projection** (≤ ~1 px), **distance preservation** (rigid invariant ‖P_c‖ = ‖P_w − t‖), and **workspace plausibility**.

**Canonical worked example** (used as a regression reference throughout): undistorted pixel (480, 160); K with f = 800, principal point (320, 240); depth Z = 0.3; T(arm←cam) translation (0,0,0.1); T(world←arm) translation (1.0,0.5,0); identity rotations → **P_c = (0.06, −0.03, 0.3)**, **P_w = (1.06, 0.47, 0.4)**, ‖P_c‖ ≈ 0.307 m preserved.

---

## Deliverables

| Asset | Count |
|---|---|
| Lessons (module03/lesson01–32) | 32 |
| Static diagrams (assets/diagrams/m03-l1…l32) | 32 |
| Jupyter notebooks (execute clean; OpenCV cross-checks degrade gracefully to NumPy) | 32 |
| Quizzes (formative; mc/tf/match/short) | 32 |
| Interactive demos | 4 |
| Coach answer keys (coaches/answer-keys/module03) | 32 |
| Assessments | midpoint (after Unit 4) + Unit 8 mini-project capstone |

**Interactive demos:** lesson07 perspective projection · lesson13 projection pipeline · lesson21 back-projection ray · lesson29 *See the Fruit, Place It in the World* (flagship capstone: live P_c/P_w readout with three PASS/FAIL acceptance-check badges and a frame-error toggle).

All pages carry the "You are here" context header (Module → Unit → Lesson); `mkdocs build --strict` passes; the validator confirms every published Visual Explanation resolves to an injected figure with no leaked `[Visual:]` placeholders.

---

## Key insights established

- **Projection is lossy and not invertible alone** — it collapses 3D→2D and discards depth; recovering 3D requires extra information (depth) and the camera's pose.
- **Distortion lives before K** and grows with radius; modeling and removing it is the gate to clean back-projection.
- **A pixel is a ray; depth is the missing scalar** that turns the ray into a point.
- **Perception output is camera-frame** — correct numbers in the wrong frame; Module 2's extrinsics chain carries it to the world.
- **Verification is part of the pipeline** — re-projection, distance preservation, and workspace checks make the result trustworthy enough to drive an arm, and their failure signatures localize faults (frame vs depth vs intrinsics).

---

## Bridges

- **Backward to Module 2:** the extrinsics transform T(world←cam) is a Module 2 SE(3) pose; the world-placement chain is reused in the perception direction.
- **Forward to Module 4:** Module 3 *assumed* the arm's pose T(world←arm) was available. **Module 4 — Forward Kinematics using Denavit–Hartenberg Parameters** computes T(world←arm) from the robot's joint angles, supplying exactly the transform this module leaned on. Perception (Module 3) + kinematics (Module 4) connect *seeing* to *reaching*.

---

*Module 3 complete. Forward and inverse camera geometry, lens distortion, back-projection, and the perception→world pipeline are built, verified, and integrated with Module 2. Next: Module 4 — Forward Kinematics using Denavit–Hartenberg Parameters.*
