# Module 2 — Spatial Transformations and SE(3)

*Part of the Physical AI Curriculum. Theme: the greenhouse harvesting robot.*

Module 1 gave you vectors, coordinate frames, and transformations understood as **actions on space**. Module 2 answers the next question a real robot must solve:

> **How are transformations represented and composed in robotics?**

You'll learn the representation that makes robot motion computable: **homogeneous coordinates** (which let translation become a matrix too), **rigid-body transformations** (rotation and translation together), and the groups **SE(2)** and **SE(3)** that describe rigid motion in the plane and in 3D. You'll chain transformations the way a robot does — camera to robot to world — and represent a robot's **pose**.

What this module is *not* (yet): full robot kinematics (joint angles → end-effector motion). Module 2 builds the representational backbone; kinematics comes later.

## How to use this module

Each lesson follows the same five layers: **physical intuition → visual understanding → mathematical formulation → computational implementation → system integration.** Read the lesson, play with the diagram and any interactive demo, run the notebook (every notebook executes to "All checks passed."), and take the formative quiz (unlimited attempts).

## Structure

- `topic_map.md` — the units and lessons
- `learning_objectives.md` — what you'll be able to do
- `assessments.md` — quizzes, recaps, and checkpoints
- `lessons/`, `notebooks/`, `demos/`, `quizzes/` — the materials

## Prerequisites

Module 1 complete — especially Unit 3 (coordinate frames) and Unit 4 (transformations as actions; composition and order). If "the tomato has not moved, only the observer changed" and "a matrix is an action, not a table" feel natural, you're ready.

*Status: planning. Lessons are being produced unit by unit with architect review between installments.*
