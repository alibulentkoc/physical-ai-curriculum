---
title: Module 6 — Learning Objectives
module: 06
status: complete
---

# Module 6 — Learning Objectives

Measurable objectives per unit. Each is phrased as something a student can *do*; together they define "can relate joint motion to tool motion, read what the arm can do, and command it at the velocity level" — the first-order relationship only, without the planning and control that come later.

## Module-level objectives

On completing Module 6, a student can:

1. Decompose a small rigid-body motion into a differential translation and rotation, and express angular velocity with the skew-symmetric operator $S(\boldsymbol\omega)$.
2. Define the **twist** $\boldsymbol\xi = [\mathbf v;\boldsymbol\omega]$ and transform it between frames.
3. Build the **geometric Jacobian** $J(\mathbf q)$ column by column for revolute, prismatic, and mixed chains, and **validate** it against finite differences.
4. Distinguish the **analytic Jacobian** and the representation map $B(\boldsymbol\phi)$ from the geometric Jacobian, and relate base-frame and tool-frame Jacobians.
5. Interpret **rank, range, and null space** of $J$ as what the tool can, cannot, and internally do; picture them as the **manipulability ellipsoid** and summarize with the **Yoshikawa measure** $w=\sqrt{\det(JJ^\top)}$.
6. Explain **force/velocity duality** ($\boldsymbol\tau = J^\top\mathbf F$) and the force ellipsoid.
7. Define a **singularity** as lost motion (ellipsoid collapse), distinguish boundary vs internal singularities, explain joint-rate blow-up, and classify shoulder/elbow/wrist singularities — upgrading M5 *recognition* to full theory.
8. Use the **SVD** $J = U\Sigma V^\top$ to read the ellipsoid's axes, the **condition number**, and the **four fundamental subspaces**, and derive the **pseudoinverse** and **damped least squares** from it.
9. Solve **inverse velocity kinematics** (desired twist → joint rates), resolve **redundancy** via null-space motion, and implement **singularity-robust resolved-rate motion** — the open-loop velocity layer Module 7 builds on.

## Per-unit objectives

- **Unit 1 (Differential Motion & Twists):** linearize a small motion; write $R \approx I + S(\delta\boldsymbol\theta)$; explain why differential rotations commute and add; assemble and transform twists.
- **Unit 2 (Geometric Jacobian):** state $\boldsymbol\xi = J\dot{\mathbf q}$; construct revolute/prismatic columns; assemble the full $6\times n$ Jacobian; verify numerically.
- **Unit 3 (Analytic Jacobian & Representations):** differentiate a pose representation; build $B(\boldsymbol\phi)$; convert between base and tool frames; separate representation from kinematic singularities.
- **Unit 4 (Manipulability, Midpoint):** compute rank/range/null space; draw and read the manipulability ellipsoid; compute $w$; explain force/velocity duality.
- **Unit 5 (Singularity Theory):** identify and classify singularities; explain joint-rate blow-up; describe loci and workspace boundaries.
- **Unit 6 (SVD):** compute and interpret $U,\Sigma,V$; the condition number; the four subspaces; pseudoinverse and DLS from the SVD.
- **Unit 7 (Inverse Velocity & Resolved Rate):** map a desired twist to joint rates; resolve redundancy; apply damped least squares near singularities; run resolved-rate motion.
- **Unit 8 (Capstone):** build an analyzer, a resolved-rate tracker, scheduled damping with redundancy, and package the velocity layer for Module 7.
