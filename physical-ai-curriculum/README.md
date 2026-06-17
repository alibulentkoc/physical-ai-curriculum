<div align="center">

# Physical AI Curriculum

**A comprehensive, open curriculum in Physical AI, Robotics, Computer Vision, Mechatronics, and Digital Twins — built around a single running system: a greenhouse harvesting robot.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
![Status](https://img.shields.io/badge/status-foundation-blue.svg)

</div>

---

## Overview

This repository hosts an open, GitHub-based curriculum that takes learners from physical intuition all the way to a working **digital twin** of a robotic system. Rather than treating robotics as a pile of disconnected subjects, every module advances one concrete system — a **Greenhouse Harvesting Robot** — so that each new piece of mathematics or code has an obvious reason to exist.

By the end, students can trace a complete **perception-to-action** pipeline: see a fruit, estimate where it is, transform that into the robot's frame, solve the kinematics to reach it, plan a safe motion, send the command, drive the motors, and validate the whole thing in a simulated twin.

## Who this is for

- **Agricultural Engineering** students applying robotics to real crops
- **Mechatronics Engineering** students bridging mechanical, electrical, and software domains
- **Robotics Engineering** students who want a unified, system-level view
- **Mechanical Engineering** students extending into perception and control
- **STEM learners** seeking a rigorous but intuition-first path into Physical AI

## Educational philosophy

Each topic is taught in five deliberate layers, in this order:

1. **Physical intuition** — what is actually happening in the world
2. **Visual understanding** — seeing it as a picture or diagram
3. **Mathematical formulation** — the equations that describe it
4. **Computational implementation** — turning the math into running code
5. **System integration** — connecting it back into the full robot

The goal is that students understand not just *how* an equation works, but *why it matters* in a real robotic system.

## The core narrative: a Greenhouse Harvesting Robot

Every module contributes one capability to the same robot. As the curriculum progresses, students incrementally build the models required to:

- perceive fruit
- estimate position
- transform coordinate frames
- compute kinematics
- plan motion
- communicate commands
- actuate motors
- construct a digital twin

## Curriculum roadmap

| #  | Module                                                                 | Focus |
|----|------------------------------------------------------------------------|-------|
| 01 | Mathematical Foundations for Physical AI, Robotics, and Digital Twins   | Vectors, matrices, calculus, and probability for robotics |
| 02 | Spatial Transformations and SE(3)                                       | Rotations, translations, and rigid-body motion |
| 03 | Camera Geometry and Robotic Perception                                  | Pinhole model, projection, and detecting fruit |
| 04 | Forward Kinematics using Denavit–Hartenberg Parameters                  | From joint angles to end-effector pose |
| 05 | Inverse Kinematics                                                       | From a target pose back to joint angles |
| 06 | Jacobians and Differential Motion                                       | Velocities, singularities, and differential control |
| 07 | Trajectory Generation and Motion Planning                               | Smooth, safe paths to the fruit |
| 08 | Robot Communication, Embedded Systems, and Control                      | Commands, protocols, and driving motors |
| 09 | Physical AI System Integration                                          | Assembling the full perception-to-action loop |
| 10 | Digital Twin Capstone Project                                           | Building and validating a digital twin |

## Standard topic template

To keep the experience consistent, **every topic** follows the same 12-part structure:

1. Why This Matters
2. Physical Intuition
3. Mathematical Foundations
4. Visual Explanation
5. Engineering Example
6. Worked Example
7. Interactive Demonstration
8. Coding Exercise
9. Knowledge Check
10. Challenge Problem
11. Common Mistakes
12. Key Takeaways

## Repository structure

```
physical-ai-curriculum/
├── docs/          # Project documentation, authoring guides, philosophy, glossary
├── curriculum/    # Roadmap, per-module manifests, learning objectives, sequencing
├── modules/       # The teaching content: lessons, notebooks, demos, exercises
├── assets/        # Diagrams, animations, storyboards, figures, branding
├── coaches/       # Instructor guides, AI tutor prompts, rubrics, answer keys
├── projects/      # Greenhouse robot integration + Digital Twin capstone
├── README.md      # You are here
├── CONTRIBUTING.md # How to contribute
├── LICENSE        # MIT
└── TODO.md        # Build plan and current status
```

Each top-level folder contains its own `README.md` explaining what belongs there.

## How this curriculum is built

Authoring is a collaboration between tools, each playing to its strengths:

| Tool            | Role |
|-----------------|------|
| **ChatGPT**     | Curriculum architect — learning objectives, topic sequencing, quizzes, engineering intuition |
| **Claude Code** | Markdown lessons, Jupyter notebooks, interactive demos, repository generation |
| **Gemini**      | Diagrams, animation storyboards, visual assets |
| **GitHub**      | Integration hub — version control, review, and distribution |

## Project status

🚧 **Foundation stage.** The repository scaffold and supporting documents are in place. Lesson content has **not** yet been written.

**Next deliverable:** `curriculum/module01_manifest.md` — the manifest for Module 1.

See [`TODO.md`](TODO.md) for the detailed build plan.

## Getting started

1. **Browse the roadmap** above to see where the curriculum is headed.
2. **Read each folder's `README.md`** to understand the structure.
3. **Check [`TODO.md`](TODO.md)** for what is being built next.
4. **Want to help?** Read [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Contributing

Contributions are welcome — content, code, diagrams, fixes, and ideas. Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a pull request.

## License

Released under the [MIT License](LICENSE). You are free to use, adapt, and share this material; attribution is appreciated.
