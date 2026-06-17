# Module 6 — Jacobians and Differential Motion

*Part of the Physical AI Curriculum. Theme: the greenhouse harvesting robot.*

Module 5 found *which joint angles* reach a target pose, $T_0^n(\boldsymbol\theta) = T_{\text{desired}}$. Module 6 answers the next question a moving robot must solve:

> **How does a little bit of joint motion turn into a little bit of end-effector motion — and when does that relationship break down?**

This is **differential (velocity) kinematics**, and its central object is the **Jacobian** $J(\mathbf q)$, the matrix that maps joint rates to the end-effector twist: $\boldsymbol\xi = J(\mathbf q)\,\dot{\mathbf q}$. Module 5 used the Jacobian only as the local linear step inside a numerical solver (D-054); here it becomes the subject. You'll build the geometric Jacobian column by column, validate it numerically, distinguish the analytic Jacobian and representation maps, and then read the *geometry* of $J$ — its manipulability ellipsoid, its singular values via the **SVD**, the four fundamental subspaces, rank and null space, and the singularities where the arm loses the ability to move in some direction. The module closes by inverting the relationship — resolved-rate motion, redundancy resolution, and damped least squares — producing the **velocity layer** Module 7 will plan on top of.

What this module is *not* (yet): trajectory generation and motion planning (Module 7), or dynamics and control — forces, torques, and feedback (Module 8). Module 6 is strictly the first-order (velocity) relationship and its geometry; it does not plan paths or close a control loop.

## How to use this module

Each lesson follows the same five layers: **physical intuition → visual understanding → mathematical formulation → computational implementation → system integration.** Read the lesson, study the diagram and any interactive demo, run the notebook (every notebook executes to "All checks passed."), and take the formative quiz (unlimited attempts).

## Structure

- `topic_map.md` — the units and lessons
- `learning_objectives.md` — what you'll be able to do
- `assessments.md` — quizzes, recaps, and checkpoints
- `lessons/`, `notebooks/`, `demos/`, `quizzes/` — the materials

## Prerequisites

Module 5 complete — especially the local linear map $\Delta\mathbf p \approx J\,\Delta\boldsymbol\theta$ used inside the numerical solver, and singularity *recognition* (det $J = 0$). Module 4 (forward kinematics, DH) and Module 2 (SE(3), frames, the cross product and skew-symmetric operator) are essential. Linear algebra — matrix rank, eigen/singular values, orthogonal subspaces — is used throughout.

## Tooling

No new heavy tooling. NumPy and Matplotlib throughout; `numpy.linalg` for SVD, rank, pseudoinverse, and condition number. SymPy is used where a symbolic Jacobian clarifies a derivation. Notebooks run without internet.

*Status: complete (Installments A–D approved; module signed off).*
