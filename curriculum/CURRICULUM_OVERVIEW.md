# Physical AI Curriculum — Overview
*Phase 3 — Release Packaging · Release Manager · 2026-06 · companion to the completion reports*

EXECUTIVE SUMMARY

**Status:** Packaged. This is the single-document overview of the complete ten-module Physical AI curriculum, intended as the entry point for instructors, contributors, and reviewers.

**Findings:** The curriculum is one coherent system built capability-by-capability on a single running example (a greenhouse harvesting robot), closing with a digital twin. It comprises 10 modules, 80 units, 325 lessons, 50 interactive demos, 326 diagrams, 325 quizzes, 325 answer keys, and 9 midpoint assessments.

**Issues:** None. (Hygiene items are tracked in the release audit report.)

**Recommendations:** Use this document as the curriculum's front door and the basis for the published landing page.

**Next:** Phase 4 (Translation Readiness) and Phase 5 (Publication Plan).

---

## 1. Curriculum vision

Most robotics material teaches topics in isolation — a chapter on kinematics, a chapter on control — and leaves the student to imagine how they fit together. This curriculum takes the opposite stance: **build one complete Physical AI system, one capability at a time, and never lose sight of the whole.** A single running example — a planar 2-link arm (L₁ = 0.4, L₂ = 0.3) harvesting a row of tomatoes in a greenhouse — carries through all ten modules. Each module adds exactly one stage to a single growing pipeline, hands a concrete artifact to the next module, and the final module mirrors the entire system in a digital twin.

The result is that a student finishes not with ten separate skills but with one understanding: **how mathematics becomes a robot that sees, reaches, moves, runs as an integrated system, and watches and steers itself.**

The arc in one line:

> **represent → perceive → reach → move → integrate → twin**

## 2. Module roadmap

| # | Module | Adds | Lessons |
|---|---|---|---:|
| 1 | Mathematical Foundations | the language: vectors & linear algebra | 33 |
| 2 | Spatial Transformations and SE(3) | coordinate frames & rigid motion | 36 |
| 3 | Camera Geometry and Robotic Perception | seeing: pixels → 3-D positions | 32 |
| 4 | Forward Kinematics (Denavit–Hartenberg) | where the arm is: angles → pose | 32 |
| 5 | Inverse Kinematics | how to reach: pose → angles | 32 |
| 6 | Jacobians and Differential Motion | shaping the reach: the velocity layer | 32 |
| 7 | Trajectory Generation and Motion Planning | planning the motion: the reference layer | 32 |
| 8 | Feedback Control and Real-Time Execution (ROS 2) | moving reliably: the control layer | 32 |
| 9 | Physical AI System Integration | one self-healing harvester | 32 |
| 10 | Digital Twin Capstone | mirror, simulate, monitor, predict, adapt | 32 |

## 3. Layer architecture

The middle-to-late modules each produce a named software layer, and each layer consumes the previous one. This is the structural spine of the curriculum:

```
  M6 velocity layer  →  M7 reference layer  →  M8 control layer  →  M9 integrated system  →  M10 digital twin
  (Jacobian/DLS)        reference(t)→q,q̇,q̈     tracking controller    harvest_row(world)        twin-in-the-loop
```

- **Module 9** wires the *real* layers of M3–M8 into one harvester along the workflow spine **Perceive → Understand → Plan → Execute → Track → Recover**, exposed in a single call `harvest_row(world)`.
- **Module 10** wraps that finished system in a digital twin along the spine **Model → Mirror → Simulate → Monitor → Predict → Adapt**, with reality and the twin represented separately and an explicit sim-to-real gap.

Two disciplines hold across the integration and capstone modules: **wrap, do not redefine** (each stage calls a real existing layer) and **no new theory** (integration is composition; the twin reuses the existing system). The intelligence lives in the composition — the stage order, the seam contracts, the detection guards, the recovery loop, and the twin-in-the-loop cycle.

## 4. Learning outcomes

On completing the curriculum, a learner can:

- Represent positions, directions, and poses with vectors, matrices, and SE(3) transforms, and reason across camera / robot / world frames.
- Turn camera input into estimated 3-D target positions (perception).
- Compute forward and inverse kinematics for a serial arm and shape motion with the Jacobian (manipulability, singularities, damped least squares).
- Generate smooth, feasible trajectories and execute them reliably under feedback on an imperfect plant.
- Integrate perception, planning, and control into one self-healing system that detects, localises, and recovers from failures with graceful degradation.
- Build a digital twin that mirrors, simulates, monitors, predicts, and adapts — closing a twin-in-the-loop that improves the real system's behaviour.
- Articulate the whole pipeline end to end (the "one tomato through ten modules" synthesis) and place each module in one coherent Physical AI system.

## 5. Module summaries

- **M1 — Mathematical Foundations.** Measurement, vectors, coordinate systems, and the linear-algebra language underpinning everything later. 33 lessons, 12 demos, midpoint.
- **M2 — Spatial Transformations and SE(3).** Rotations, translations, SE(3), transformation chains, and frames-as-a-graph. 36 lessons, 6 demos, midpoint.
- **M3 — Camera Geometry and Robotic Perception.** Pinhole geometry, intrinsics/extrinsics, distortion, and back-projection to 3-D. 32 lessons, midpoint + capstone mini-project.
- **M4 — Forward Kinematics (DH).** DH parameters, building/using a DH table, the forward chain to tool pose. 32 lessons, midpoint + capstone.
- **M5 — Inverse Kinematics.** The inverse problem, analytic/iterative solutions, the Reach-the-Fruit capstone. 32 lessons, midpoint + capstone.
- **M6 — Jacobians and Differential Motion.** Geometric Jacobian, manipulability (w = ∏σᵢ), singularities, damped least squares from the SVD — the velocity layer. 32 lessons, midpoint + 4-part capstone.
- **M7 — Trajectory Generation and Motion Planning.** Time-parameterisation, cubic/quintic & trapezoidal/S-curve profiles, the reference layer. 32 lessons, midpoint + harvest-cycle capstone.
- **M8 — Feedback Control and Real-Time Execution (ROS 2).** Tracking error, PID, stability/tuning, feedforward+feedback, actuators, and conceptual ROS 2 — the control layer. 32 lessons, midpoint.
- **M9 — System Integration.** The six-stage self-healing harvester (Perceive → … → Recover), failure taxonomy, localisation, recovery, `harvest_row`. 32 lessons, 4 flagship demos.
- **M10 — Digital Twin Capstone.** The twin (mirror/simulate/monitor/predict/adapt), the twin-in-the-loop, the Self-Improving Greenhouse Harvest, and the curriculum close. 32 lessons, 4 flagship demos, midpoint.

## 6. Artifact inventory (repo-verified)

| Artifact | Count |
|---|---:|
| Modules | 10 |
| Units | 80 |
| Lessons | 325 |
| Canonical notebooks (one per lesson) | 325 |
| Diagrams (SVG) | 326 |
| Interactive demos | 50 |
| Quizzes | 325 |
| Answer keys (+ midpoint keys) | 325 |
| Midpoint assessments | 9 |
| Published site (`mkdocs --strict`) | 325 lesson pages, exit 0 |

**Repository layout (authoring → published):**
- Lessons: `modules/moduleNN/lessons/lessonNN_slug.md`
- Notebooks: `modules/moduleNN/notebooks/` · Quizzes: `modules/moduleNN/quizzes/` · Demos: `modules/moduleNN/demos/`
- Diagrams: `assets/diagrams/mNN-lN-slug.svg`
- Answer keys: `coaches/answer-keys/moduleNN/` · Assessments: `assessments/`
- Generator: `tools/generate_site_pages.py` → published `site_src/` → `mkdocs build --strict` → `site/`
- Reusable build helpers: `tools/_m9_nbbuild.py`, `tools/_m9_quizbuild.py`
- Tracking: `curriculum/PROJECT_STATE.md`, `curriculum/master_progress.md`, `curriculum/ARCHITECT_DECISIONS.md`
- Reports: per-module installment + completion reports, plus the curriculum completion report, all in `curriculum/`.

Every lesson follows a 12-section template with an AI Learning Companion and four-language Global Learning Support (English · Español · 中文 · Türkçe).

## 7. Release history

Production ran module by module, each module delivered in Architect-approved installments, recorded as decisions **D-001 … D-078** in `ARCHITECT_DECISIONS.md`:

- Modules 1–8 — foundations through control, completed in sequence (control layer = the M9 handoff).
- **Module 9 — System Integration:** Installments A–D = D-071…D-074. *Module 9 complete.*
- **Module 10 — Digital Twin Capstone:** Installments A–D = D-075…D-078. *Module 10 complete; curriculum complete.*

Locked conventions held curriculum-wide: twist ordering ξ = [v; ω]; geometric Jacobian primary; base/world frame primary; manipulability w = ∏σᵢ; damped least squares from the SVD; canonical arm L₁ = 0.4, L₂ = 0.3.

## 8. Future maintenance guidance

- **Regeneration is deterministic.** After any lesson/diagram/quiz/demo edit, run `python3 tools/generate_site_pages.py` then `mkdocs build --strict`. The strict build is the gate; treat any non-zero exit as a release blocker.
- **One figure per lesson.** A lesson with a Visual Explanation section but no injected figure fails the strict validator — keep exactly one `mNN-lN-*.svg` per lesson.
- **Notebooks must self-verify.** Each ends with "All checks passed."; re-run under Restart-and-Run-All after edits.
- **Recap lessons** require both a `## Coding Exercise` and a `## Knowledge Check` heading for the generator to inject the notebook tip and quiz.
- **No emoji in SVGs** (surrogate pairs break XML validation); use text labels and HTML entities for special characters.
- **Adding content** means editing the authoring sources under `modules/` and `assets/`, never the generated `site_src/` or `site/`.
- **Hygiene before a tag:** clear orphan notebooks and stale flat `site_src` copies (see the release audit report), then rebuild `--strict`.
- **Tooling:** Python with MkDocs + Material theme; reusable builders `tools/_m9_nbbuild.py` and `tools/_m9_quizbuild.py`.

*Phase 3 complete.*
