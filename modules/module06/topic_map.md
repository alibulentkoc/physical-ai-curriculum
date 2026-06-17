# Module 6 — Topic Map: Jacobians and Differential Motion

**Theme:** Greenhouse Harvesting Robot — relate joint motion to tool motion, and read what the arm can and cannot do.
**Central question:** How does a little bit of joint motion become a little bit of end-effector motion — and where does that map degrade?
**Structure:** 8 units × 4 lessons = 32 lessons. The `.4` lesson of each unit consolidates or recaps. Midpoint checkpoint after Unit 4; a four-part capstone in Unit 8.

Numbering: `module06/lessonNN`, diagrams `m06-lN-*` (N un-padded), notebooks `lessonNN_*`.

**Through-line:** Module 5 inverted the *position* map (pose → θ) and used the Jacobian only as solver machinery. Module 6 makes the Jacobian the subject: differential motion and twists → the geometric Jacobian → its geometry (manipulability, SVD, subspaces, singularities) → inverting it (resolved-rate, redundancy, damped least squares) → a reusable velocity layer for Module 7.

---

## Unit 1 — Differential Motion & Twists
*A small rigid-body motion linearizes into a differential translation plus a differential rotation; package linear and angular velocity together as a twist.*
- 1.1 From Finite to Infinitesimal: Differential Translation and Rotation (lesson01)
- 1.2 Angular Velocity and the Skew Operator (lesson02)
- 1.3 The Twist: Linear and Angular Velocity Together (lesson03)
- 1.4 Transforming Twists Between Frames (lesson04)

## Unit 2 — Geometric Jacobian & Forward Velocity Kinematics
*Define the Jacobian as the velocity map and build it column by column for revolute, prismatic, and mixed chains; validate against finite differences.*
- 2.1 Forward Velocity Kinematics: Defining the Jacobian (lesson05)
- 2.2 The Geometric Jacobian by Column Construction: Revolute Joints (lesson06)
- 2.3 Prismatic Joints, Mixed Chains, and the Full 6×n Jacobian (lesson07)
- 2.4 Numerical Validation: Geometric J vs Finite Differences (lesson08)

## Unit 3 — Analytic Jacobian, Frames & Representations
*The analytic Jacobian differentiates a pose representation; the representation map B(φ) links angular velocity to angle rates; base vs tool frame; representation vs kinematic singularities.*
- 3.1 The Analytic Jacobian: Differentiating Forward Kinematics (lesson09)
- 3.2 The Representation Map B(φ): Linking ω to Angle Rates (lesson10)
- 3.3 Base-Frame vs Tool-Frame Jacobian (lesson11)
- 3.4 Representation Singularities vs Kinematic Singularities (lesson12)

## Unit 4 — Rank, Manipulability & the Ellipsoid (Midpoint)
*What the tool can and cannot do — rank, range, null space — pictured as the manipulability ellipsoid and summarized by the Yoshikawa measure; force/velocity duality. Midpoint checkpoint.*
- 4.1 What the Tool Can and Cannot Do: Rank, Range, and Null Space (lesson13)
- 4.2 The Manipulability Ellipsoid: A Picture of What the Robot Can Do (lesson14)
- 4.3 Putting a Number on It: The Yoshikawa Manipulability Measure (lesson15)
- 4.4 Force and Velocity Duality: τ = JᵀF and the Force Ellipsoid (lesson16)

## Unit 5 — Singularity Theory
*Singularity as lost motion when the ellipsoid collapses; boundary vs internal singularities and joint-rate blow-up; classifying shoulder/elbow/wrist; loci and workspace boundaries — from M5 recognition to full theory.*
- 5.1 When the Ellipsoid Collapses: Singularity as Lost Motion (lesson17)
- 5.2 Boundary vs Internal Singularities, and Joint-Rate Blow-Up (lesson18)
- 5.3 Classifying Singularities: Shoulder, Elbow, and Wrist (lesson19)
- 5.4 Singularity Loci and Workspace Boundaries; from M5 Recognition to Full Theory (lesson20)

## Unit 6 — SVD & Geometry of the Jacobian
*The SVD is the ellipsoid's anatomy (U, Σ, V); singular values and the condition number; the four fundamental subspaces; pseudoinverse and damped least squares derived from the SVD.*
- 6.1 The SVD as the Ellipsoid's Anatomy: U, Σ, V Explain the Picture (lesson21)
- 6.2 Singular Values and the Condition Number (lesson22)
- 6.3 The Four Fundamental Subspaces of the Jacobian (lesson23)
- 6.4 Pseudoinverse and Damped Least Squares via the SVD (lesson24)

## Unit 7 — Inverse Velocity Kinematics & Resolved-Rate Motion
*Invert the velocity map: desired twist → joint rates; redundancy resolution and null-space motion; singularity-robust damped least squares; the open-loop resolved-rate velocity layer.*
- 7.1 Inverse Velocity Kinematics: From Desired Twist to Joint Rates (lesson25)
- 7.2 Redundancy Resolution: The Pseudoinverse and Null-Space Motion (lesson26)
- 7.3 Singularity-Robust Resolved Rates: Damped Least Squares in Action (lesson27)
- 7.4 Resolved-Rate Motion: The Open-Loop Velocity Layer (lesson28)

## Unit 8 — Capstone: Analyzer → Resolved-Rate Tracker
*Integrate the module into a working velocity layer: a manipulability/singularity analyzer, a resolved-rate tracker, scheduled damping with redundancy, and the velocity layer handed forward to Module 7.*
- 8.1 Capstone I — The Manipulability & Singularity Analyzer (lesson29)
- 8.2 Capstone II — The Resolved-Rate Tracker (lesson30)
- 8.3 Capstone III — Integration: Scheduled Damping and Redundancy (lesson31)
- 8.4 Capstone IV — The Velocity Layer for Module 7 (lesson32)

---

_Educational boundary (held): trajectory generation and motion planning are Module 7; dynamics, forces/torques, and feedback control are Module 8. Module 6 is the first-order (velocity) relationship and its geometry — it does not plan paths or close a control loop. Resolved-rate motion here is open-loop (a velocity layer), explicitly handed to Module 7._

_Canonical running example: the planar 2-link arm continued from Modules 4–5 (L1 = 0.4 m, L2 = 0.3 m), extended to a 3-DOF/redundant chain where redundancy and null-space motion are needed. The M5 damped-least-squares damping introduced numerically is re-derived from the SVD in Unit 6._
