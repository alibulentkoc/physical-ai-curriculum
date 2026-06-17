# Module 4 — Topic Map: Forward Kinematics using Denavit–Hartenberg Parameters

**Theme:** Greenhouse Harvesting Robot — move the arm that reaches the fruit.
**Central question:** Given the joint angles, where is the gripper?
**Structure:** 8 units × 4 lessons = 32 lessons. The `.4` lesson of each unit is a short recap. Midpoint checkpoint after Unit 4; multi-DOF mini-project capstone in Unit 8.

Numbering restarts: `module04/lessonNN`, diagrams `m04-lNN-*`, notebooks `M04_U0U_*`.

---

## Unit 1 — Why Kinematics (Joints, Links, and Pose)
*From "the fruit is at P_w" to "make the gripper go there" — the arm as a chain.*
- 1.1 The Arm Has to Move (lesson01)
- 1.2 Links and Joints (lesson02)
- 1.3 Configuration vs. Pose (lesson03)
- 1.4 Unit 1 recap (lesson04)

## Unit 2 — One Joint at a Time
*A single revolute joint; its transform; the gripper's pose as a function of one angle.*
- 2.1 A One-Joint Arm (lesson05)
- 2.2 The Joint Transform (lesson06)
- 2.3 Where Is the Tip? (lesson07)
- 2.4 Unit 2 recap (lesson08)

## Unit 3 — Chaining Transforms (Two and Three Links)
*Composition down the chain — forward kinematics as a matrix product (Module 2 reused).*
- 3.1 Adding a Second Joint (lesson09)
- 3.2 Composing the Chain (lesson10)
- 3.3 A Planar 2-/3-Link Arm (lesson11)
- 3.4 Unit 3 recap (lesson12)

## Unit 4 — The Forward Kinematics Map (Midpoint)
*Generalize to n joints: T_0^n(θ); position and orientation of the end-effector; OpenCV/NumPy build. Midpoint checkpoint.*
- 4.1 The General Chain T_0^n(θ) (lesson13)
- 4.2 Position and Orientation of the Gripper (lesson14)
- 4.3 Forward Kinematics in Code (lesson15)
- 4.4 Unit 4 recap · Midpoint (lesson16)

## Unit 5 — Denavit–Hartenberg Parameters
*The four DH parameters; why a consistent per-joint convention; frame assignment rules.*
- 5.1 Why a Convention (lesson17)
- 5.2 The Four DH Parameters (lesson18)
- 5.3 Assigning Frames (lesson19)
- 5.4 Unit 5 recap (lesson20)

## Unit 6 — Building and Using a DH Table
*From a robot to its DH table; each link transform from its four parameters; the product gives forward kinematics.*
- 6.1 The DH Link Transform (lesson21)
- 6.2 Reading a Robot into a Table (lesson22)
- 6.3 DH Forward Kinematics in Code (lesson23)
- 6.4 Unit 6 recap (lesson24)

## Unit 7 — Pose, Workspace, and Back to Perception
*Interpreting the end-effector pose; the reachable workspace; connecting T_0^n to the Module 3 T(world←arm).*
- 7.1 Reading the End-Effector Pose (lesson25)
- 7.2 The Reachable Workspace (lesson26)
- 7.3 Closing the Loop with Perception (lesson27)
- 7.4 Unit 7 recap (lesson28)

## Unit 8 — Mini Project: From Joints to the Fruit
*Capstone: build a multi-DOF arm's DH table, compute and verify the gripper pose, and place a perceived fruit target in the arm's frame — integrating Modules 2, 3, 4.*
- 8.1 The Project: Joints to Gripper (lesson29)
- 8.2 Building the Arm's DH Model (lesson30)
- 8.3 Verifying the Forward Kinematics (lesson31)
- 8.4 Wrap-Up and the Road to Inverse Kinematics (lesson32)

---

_Educational boundary (held): inverse kinematics, Jacobians, velocity kinematics, control, and motion planning are deferred to Modules 5–7. Module 4 is strictly the forward map: configuration → pose._

_Canonical running example (to be used across lessons/notebooks/demos for a consistent reference): a planar 2-link arm with link lengths L1, L2 and joint angles θ1, θ2, plus a 3-DOF extension for the capstone. Reference numbers defined in the Unit 2–3 lessons and reused through Unit 8._
