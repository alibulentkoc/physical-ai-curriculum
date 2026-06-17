---
title: Module 5 — Learning Objectives
module: 05
status: proposed
---

# Module 5 — Learning Objectives

Measurable objectives per unit. Each is phrased as something a student can *do*; together they define "can command the arm to a target" — the inverse problem only, without the velocity/planning/control that come later.

## Module-level objectives

On completing Module 5, a student can:

1. State the inverse-kinematics problem precisely as solving $T_0^n(\boldsymbol\theta) = T_{\text{desired}}$, and contrast it with the forward map (evaluate vs solve).
2. Determine whether a target pose is **reachable**, and relate reachability to the Module 4 workspace.
3. Explain and identify **solution multiplicity** (0 / 1 / many; elbow-up vs elbow-down; redundancy).
4. Solve the **planar 2-link arm analytically** in closed form, producing *both* solutions, using the law of cosines and `atan2`.
5. Explain **why a general arm needs a numerical method**, and implement an **iterative IK solver** (Jacobian pseudoinverse / transpose / damped least squares).
6. **Recognize a singularity** as the place IK degrades (lost directions, ill-conditioning) — at the recognition level, deferring the full theory to Module 6.
7. **Choose among solutions** using joint limits and proximity to the current configuration.
8. **Verify** any candidate configuration by evaluating the Module 4 forward map.
9. Complete a **reach-the-fruit** mini project: from a perceived grasp pose to a chosen, verified joint configuration (no path planning, no control).

## Per-unit objectives

**Unit 1 — The Inverse Problem**
- Describe inverse kinematics as inverting the forward map, in physical terms.
- Explain why the inverse problem is nonlinear and can have 0, 1, or many solutions.
- Decide whether a target lies in the reachable workspace.

**Unit 2 — Inverse Kinematics of One and Two Joints**
- Solve a one-joint arm's IK by inspection.
- Describe the planar 2-link arm's solution geometrically (the triangle the links form to the target).
- Identify and name the elbow-up and elbow-down solutions.

**Unit 3 — Analytical (Closed-Form) Inverse Kinematics**
- Derive the closed-form joint angles of the 2-link arm with the law of cosines.
- Use `atan2` to recover angles unambiguously across quadrants.
- Explain (concept level) how a wrist-partitioned arm decouples into position then orientation.

**Unit 4 — From Geometry to Numerical IK (Midpoint)**
- Explain when closed form is unavailable (general arms, redundancy).
- Identify the FK **Jacobian** as the local linear map that relates small joint changes to small pose changes — *for solving only*.
- Describe the iterative loop: guess → measure error → step → repeat.

**Unit 5 — Numerical Inverse Kinematics in Practice**
- Implement Newton's method for IK using the Jacobian pseudoinverse.
- Implement and contrast the Jacobian-transpose and damped-least-squares updates.
- Diagnose convergence behavior, step-size effects, and common failure modes.

**Unit 6 — Singularities and Solution Selection**
- Recognize a singularity from its symptoms (a direction the arm can't move; huge joint steps).
- Reject solutions that violate joint limits.
- Select a solution that is near the current configuration and avoids unnecessary flips.

**Unit 7 — Verifying and Connecting to Perception**
- Verify a candidate $\boldsymbol\theta$ by checking $T_0^n(\boldsymbol\theta) \approx T_{\text{desired}}$ with the Module 4 FK.
- Convert a perceived fruit's grasp pose into a target pose for the solver.
- Trace the full loop: perceive (M3) → place in arm frame (M2/M4) → solve (M5).

**Unit 8 — Mini Project: Reach the Fruit**
- Assemble an IK solver (analytical where possible, numerical otherwise) for the 3-DOF capstone arm.
- Handle multiplicity and the no-solution case explicitly, and verify the chosen configuration.
- Articulate what remains for differential motion (Module 6) and planning (Module 7).

## Out of scope (explicit, for continuity)

- **Velocity / differential kinematics** and the full Jacobian/singularity theory (manipulability, singular-value analysis) — **Module 6**. The Jacobian appears here only as the local linear step in a solver.
- **Trajectory generation / motion planning** (smooth, collision-free paths between configurations) — **Module 7**. Module 5 finds a target configuration, not the path to it.
- **Control** (torques, feedback, actuation) — **Module 8**.
- **Dynamics** (forces, inertia) — later modules.
