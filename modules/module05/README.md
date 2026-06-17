# Module 5 — Inverse Kinematics

*Part of the Physical AI Curriculum. Theme: the greenhouse harvesting robot.*

Module 4 gave you forward kinematics: plug in the joint angles, get the gripper's pose, $T_0^n(\boldsymbol\theta)$. Module 5 answers the question a harvesting robot actually has to solve before it can grasp anything:

> **Given a desired end-effector pose, what joint angles achieve it?**

This is **inverse kinematics**. Forward kinematics is a function you *evaluate* — always defined, one answer. Inverse kinematics is an equation you *solve*: $T_0^n(\boldsymbol\theta) = T_{\text{desired}}$. It is harder on purpose. The equation is nonlinear, and a target can have **no solution, one, or many** (elbow-up vs elbow-down). You'll learn both ways to crack it: **analytical (closed-form)** IK — writing the angles directly with geometry and trigonometry for simple arms, which reveals *all* the solutions — and **numerical (iterative)** IK — starting from a guess and stepping toward the target, which works for *any* arm. You'll learn when each applies, how to **choose** among multiple solutions (joint limits, staying near the current pose), how to recognize a **singularity**, and to **verify** every answer by pushing it back through the Module 4 forward map.

What this module is *not* (yet): velocity / differential kinematics and the full Jacobian theory (Module 6), trajectory generation and motion planning (Module 7), or control (Module 8). Module 5 finds *which joint angles reach the target* — it doesn't plan the path there or drive the motors.

## How to use this module

Each lesson follows the same five layers: **physical intuition → visual understanding → mathematical formulation → computational implementation → system integration.** Read the lesson, play with the diagram and any interactive demo, run the notebook (every notebook executes to "All checks passed."), and take the formative quiz (unlimited attempts).

## Structure

- `topic_map.md` — the units and lessons
- `learning_objectives.md` — what you'll be able to do
- `assessments.md` — quizzes, recaps, and checkpoints
- `lessons/`, `notebooks/`, `demos/`, `quizzes/` — the materials

## Prerequisites

Module 4 complete — especially the forward map $T_0^n(\boldsymbol\theta)$, reading position and orientation off a pose, and the reachable workspace. Module 2 (SE(3) and inverses) is essential, and the planar 2-link arm from Module 4 is the running example here. If "forward kinematics evaluates a function; inverse kinematics solves an equation" and "a point in the plane can be reached two ways — elbow-up or elbow-down" feel natural, you're ready.

## Tooling

No new heavy tooling. NumPy, Matplotlib, and SymPy throughout (SymPy for closed-form derivations and symbolic verification). SciPy is optional for the numerical track and is imported defensively (`try/except`) so notebooks run with or without it — the same policy Module 3 used for OpenCV.

*Status: planning (launch package). Lessons are produced unit by unit with architect review between installments.*
