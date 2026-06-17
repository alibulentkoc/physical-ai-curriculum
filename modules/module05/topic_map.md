# Module 5 — Topic Map: Inverse Kinematics

**Theme:** Greenhouse Harvesting Robot — compute the joint angles that put the gripper on the fruit.
**Central question:** Given a desired end-effector pose, what joint angles achieve it?
**Structure:** 8 units × 4 lessons = 32 lessons. The `.4` lesson of each unit is a short recap. Midpoint checkpoint after Unit 4; multi-DOF mini-project capstone in Unit 8.

Numbering restarts: `module05/lessonNN`, diagrams `m05-lNN-*`, notebooks `M05_U0U_*`.

**Through-line:** Module 4 evaluated the forward map θ → pose. Module 5 *inverts* it: pose → θ. The difficulty grows deliberately — one joint (trivial) → planar 2-link in closed form (two visible solutions) → why a general arm needs iteration → the numerical solver → choosing among solutions and verifying → capstone reach.

---

## Unit 1 — The Inverse Problem
*From "where is the gripper?" to "what angles put it there?" — why inverting the map is hard, and what "hard" means concretely.*
- 1.1 From Forward to Inverse (lesson01)
- 1.2 Why It's Hard: Nonlinear, and 0/1/Many Solutions (lesson02)
- 1.3 Reachability and the Workspace (lesson03)
- 1.4 Unit 1 recap (lesson04)

## Unit 2 — Inverse Kinematics of One and Two Joints
*The simplest IK by geometry — one joint is trivial; the planar 2-link arm is the workhorse, where two solutions are visible and namable.*
- 2.1 One Joint: Solve by Inspection (lesson05)
- 2.2 The Planar Two-Link Arm — Geometry of the Solution (lesson06)
- 2.3 Elbow-Up and Elbow-Down: the Two Solutions (lesson07)
- 2.4 Unit 2 recap (lesson08)

## Unit 3 — Analytical (Closed-Form) Inverse Kinematics
*Write the joint angles directly with trigonometry. Law of cosines + atan2; when closed form exists; the wrist-decoupling idea (position then orientation) at concept level.*
- 3.1 Closed-Form Solution of the 2-Link Arm (lesson09)
- 3.2 The atan2 Tool and Choosing the Right Quadrant (lesson10)
- 3.3 Decoupling Position and Orientation (Wrist-Partitioned Arms, concept) (lesson11)
- 3.4 Unit 3 recap (lesson12)

## Unit 4 — From Geometry to Numerical IK (Midpoint)
*Closed form runs out: general arms, redundancy, no clean trig. The local linear map FK already gives us — the Jacobian — as the bridge to iteration. Midpoint checkpoint.*
- 4.1 When Closed Form Runs Out (lesson13)
- 4.2 The Local Linear Map: the FK Jacobian (for solving only) (lesson14)
- 4.3 The Iteration Idea: Guess, Measure Error, Step (lesson15)
- 4.4 Unit 4 recap · Midpoint (lesson16)

## Unit 5 — Numerical Inverse Kinematics in Practice
*The iterative solver built for real: Newton / Jacobian-transpose / damped least squares; step size, convergence, and what makes it stall.*
- 5.1 Newton's Method for IK (Jacobian Pseudoinverse) (lesson17)
- 5.2 The Jacobian-Transpose and Damped Least Squares (lesson18)
- 5.3 Convergence, Step Size, and Failure Modes (lesson19)
- 5.4 Unit 5 recap (lesson20)

## Unit 6 — Singularities and Solution Selection
*Where IK degrades and how to choose well. Singularities as lost directions (recognition only — full theory is Module 6); joint limits; staying near the current pose; avoiding flips.*
- 6.1 Singularities: Where IK Breaks Down (recognition) (lesson21)
- 6.2 Joint Limits and Feasible Solutions (lesson22)
- 6.3 Choosing Among Solutions (nearest, smooth, limit-safe) (lesson23)
- 6.4 Unit 6 recap (lesson24)

## Unit 7 — Verifying and Connecting to Perception
*Trust nothing unverified: push every candidate θ back through the Module 4 forward map. Then connect a perceived fruit's grasp pose to an executable configuration.*
- 7.1 Verifying a Solution with Forward Kinematics (lesson25)
- 7.2 From a Fruit's Grasp Pose to a Target Configuration (lesson26)
- 7.3 Closing the Loop: Perceive → Place → Solve (lesson27)
- 7.4 Unit 7 recap (lesson28)

## Unit 8 — Mini Project: Reach the Fruit
*Capstone: from a perceived target pose to a chosen, verified joint configuration the arm can execute — integrating Modules 2, 3, 4, and 5. Analytical where possible, numerical where needed, multiplicity handled, every solution verified.*
- 8.1 The Project: From Target Pose to Joint Angles (lesson29)
- 8.2 Building the Solver (analytical + numerical) (lesson30)
- 8.3 Verifying, Selecting, and Handling No-Solution Cases (lesson31)
- 8.4 Wrap-Up and the Road to Differential Motion (lesson32)

---

_Educational boundary (held): velocity / differential kinematics and the full Jacobian/singularity theory are Module 6; trajectory generation and motion planning are Module 7; control is Module 8. Module 5 is strictly the inverse position/orientation problem: desired pose → joint configuration. The Jacobian appears here only as the local linear step inside a numerical solver._

_Canonical running example (used across lessons/notebooks/demos for a consistent reference): the planar 2-link arm continued from Module 4 (L1 = 0.4 m, L2 = 0.3 m), with target points inside the annulus |L1−L2| ≤ r ≤ L1+L2 and the two named solutions elbow-down / elbow-up; a 3-DOF extension (matching the Module 4 capstone DH table) for the numerical track and the Unit 8 capstone. Reference numbers fixed in Unit 2 and reused through Unit 8._
