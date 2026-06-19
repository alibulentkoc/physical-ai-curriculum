---
title: "Physical AI Curriculum — Final Completion Report"
status: COMPLETE
scope: Modules 1–10 (the full curriculum)
decisions: D-001 … D-078
date: 2026-06
---

# Physical AI Curriculum — Final Completion Report

**10 of 10 modules complete.** The curriculum is finished.

## What the curriculum is

A ten-module course that builds a complete **Physical AI system** one capability at a time, using a single running example throughout — a **greenhouse harvesting robot** (a planar 2-link arm, L₁ = 0.4, L₂ = 0.3, picking a row of tomatoes). Each module adds one stage to a single growing pipeline, and the final module mirrors the whole thing in a digital twin. The arc, in one line:

> **represent → perceive → reach → move → integrate → twin**

Nothing in the course is a standalone topic. Every module's output is the next module's input, so a student finishes not with ten separate skills but with one coherent understanding: how mathematics becomes a robot that sees, reaches, moves, runs as an integrated system, and watches and steers itself through a twin.

## The through-line, module by module

- **Module 1 — Mathematical Foundations.** The language: vectors, matrices, and linear algebra to represent positions, directions, and transformations. Everything later rests on this.
- **Module 2 — Spatial Transformations and SE(3).** Coordinate frames and rigid motion: placing and moving points between camera, robot, and world frames.
- **Module 3 — Camera Geometry and Robotic Perception.** Seeing: turning pixels into estimated 3-D positions of fruit in the world frame.
- **Module 4 — Forward Kinematics (Denavit–Hartenberg).** Knowing where the arm is: joint angles → tool pose.
- **Module 5 — Inverse Kinematics.** Knowing how to reach: a target position → the joint angles that get there.
- **Module 6 — Jacobians and Differential Motion.** Shaping the reach: relating joint rates to tool motion, manipulability, singularities, damped least squares — the **velocity layer**.
- **Module 7 — Trajectory Generation and Motion Planning.** Planning the motion: a time-parameterised **reference layer** `reference(t) → (q_d, q̇_d, q̈_d)`.
- **Module 8 — Feedback Control and Real-Time Execution (ROS 2).** Moving reliably: tracking the reference under disturbance on an imperfect plant — the **control layer**.
- **Module 9 — Physical AI System Integration.** Making the layers cooperate as one self-healing harvester along **Perceive → Understand → Plan → Execute → Track → Recover**, runnable in one call, `harvest_row`.
- **Module 10 — Digital Twin Capstone.** Mirroring the finished system in a twin that follows **Model → Mirror → Simulate → Monitor → Predict → Adapt** — closing the twin-in-the-loop and the curriculum.

The capstone (Module 10, Lessons 8.3–8.4) makes the through-line explicit: one tomato is traced through all ten modules, and the course closes by naming the arc from mathematics to a digital twin.

## The governing philosophy

Three disciplines held across all ten modules and define the curriculum's character:

- **Build one system, not ten topics.** A single robot and a single example carry through every module; each module hands a concrete artifact to the next (M6 velocity layer → M7 reference layer → M8 control layer → M9 integrated system → M10 twin).
- **Intuition and composition over new formalism.** The later modules deliberately *compose* earlier layers rather than introduce heavier theory. Integration wraps the real layers; the twin wraps the integrated system. The intelligence lives in the composition — the stage order, the seam contracts, the detection guards, the recovery loop, the twin-in-the-loop cycle.
- **Honest, stated scope boundaries.** The course stays with kinematics and geometric reasoning (no formal manipulator dynamics), intuitive feedback control (no Laplace/transfer-function machinery), reading-and-coordination for integration (no fault-diagnosis or new estimation), and twin-based decision-making (no machine learning, RL, or optimization). These boundaries are taught as the deliberate **edges of a foundation**, each with a named next course that attaches to the pipeline — not as gaps to apologise for.

## Locked conventions (held curriculum-wide)

Twist ordering ξ = [v; ω] (linear on top); geometric Jacobian primary; base/world frame primary; manipulability w = ∏σᵢ (product of singular values); damped least squares derived from the SVD; the canonical arm L₁ = 0.4, L₂ = 0.3. Every lesson follows a 12-section template with an AI Learning Companion and four-language Global Learning Support (English · Español · 中文 · Türkçe).

## Totals (repo-verified)

| | Count |
|---|---:|
| Modules | **10 (all complete)** |
| Units | 80 |
| Lessons | **325** |
| Self-verifying notebooks | one per lesson (all "All checks passed.") |
| Diagrams (SVG) | 326 |
| Interactive demos | **50** |
| Quizzes | 325 |
| Answer keys | 325 + midpoint keys |
| Midpoint assessments | 9 |
| Site (`mkdocs build --strict`) | **325 lesson pages, exit 0** |

Per-module lessons: M1 = 33, M2 = 36, M3–M10 = 32 each. The published site builds clean under `mkdocs --strict`; every lesson page carries its figure, notebook tip, and quiz, and each module's flagship demos are injected on their designated lessons only.

## Verification standard

Every module was delivered in installments, each Architect-approved before the next began. Across the curriculum: all lesson notebooks execute clean under Restart-and-Run-All, every diagram is XML-valid with exactly one figure per lesson, every demo is self-contained with no browser storage, and each module closed with `mkdocs build --strict` green and a milestone/completion report. Module 10's final regression re-executed all 32 of its notebooks; the full site stands at 325 lesson pages.

## Close

The curriculum delivers what it set out to: a student who finishes can take a robot from a mathematical representation of the world all the way to a self-improving, twin-in-the-loop physical system. The greenhouse harvester is one instance; the same pipeline picks parts off a line, places components on a board, or guides a tool to a workpiece. The application changes; the through-line — represent, perceive, reach, move, integrate, twin — does not.

**The Physical AI curriculum is COMPLETE: 10 of 10 modules signed off. Paused at full curriculum completion; no new module production remains.**
