# Architect Decisions — Source of Truth

> **Owner:** ChatGPT (Curriculum Architect).
> **Maintained by:** appended to whenever a major curriculum decision is approved.
> **Purpose:** Single authoritative record of approved decisions so contributors (ChatGPT, Claude Code, Gemini, humans) work from one consistent reference instead of reconstructing context from conversation history.

Each entry is dated and marked **APPROVED**. Implementation work cites the decision it depends on.

---

## D-001 — Curriculum Vision · APPROVED
A GitHub-based curriculum in Physical AI, Robotics, Computer Vision, Mechatronics, Digital Twins, and Perception-to-Action systems. All modules revolve around one running system: a **Greenhouse Harvesting Robot**.

## D-002 — Educational Philosophy · APPROVED
Five-layer progression for every topic: **physical intuition → visual understanding → mathematical formulation → computational implementation → system integration.** Students should understand not just how equations work, but why they matter in real robotic systems.

## D-003 — Audience · APPROVED
Agricultural Engineering, Mechatronics Engineering, Robotics Engineering, Mechanical Engineering, and STEM learners.

## D-004 — Module Roadmap (10 modules) · APPROVED
1. Mathematical Foundations · 2. Spatial Transformations and SE(3) · 3. Camera Geometry and Robotic Perception · 4. Forward Kinematics (DH parameters) · 5. Inverse Kinematics · 6. Jacobians and Differential Motion · 7. Trajectory Generation and Motion Planning · 8. Robot Communication, Embedded Systems, and Control · 9. Physical AI System Integration · 10. Digital Twin Capstone Project.

## D-005 — Standard Topic Template (12 parts) · APPROVED
Why This Matters · Physical Intuition · Mathematical Foundations · Visual Explanation · Engineering Example · Worked Example · Interactive Demonstration · Coding Exercise · Knowledge Check · Challenge Problem · Common Mistakes · Key Takeaways.

## D-006 — Repository Foundation · APPROVED
Repo `physical-ai-curriculum` initialized with `docs/`, `curriculum/`, `modules/`, `assets/`, `coaches/`, `projects/`, plus README, CONTRIBUTING, MIT LICENSE, TODO, .gitignore. Pushed to GitHub.

## D-007 — Sequencing Principle · APPROVED
The manifest defines the module; everything else supports the manifest. Supporting docs and lessons are written *after* the manifest, never before, to avoid documentation drift.

## D-008 — Module 1 Unit Structure (9 units) · APPROVED
1. Physical Quantities and Measurements · 2. Vectors and Geometric Thinking · 3. Coordinate Systems and Reference Frames · 4. Matrices as Transformations · 5. Linear Algebra for Robotic Systems · 6. Trigonometry for Motion and Perception · 7. Modeling Physical Systems · 8. Computational Mathematics with Python · 9. Mini Project — Greenhouse Robot Workspace.

## D-009 — Module 1 Software Stack · APPROVED
Python 3.12+, NumPy, Matplotlib, SymPy, Jupyter. **Explicitly excluded from Module 1:** OpenCV, ROS 2, Gazebo, Isaac Sim (these enter in later modules: OpenCV→M3, ROS 2→M8, Gazebo/Isaac→M9–10).

## D-010 — Module 1 Assessment Weights · APPROVED
Coding Exercises 40% · Knowledge Checks 25% · Challenge Problems 15% · Mini Project 20%.

## D-011 — Roles & Workflow · APPROVED
ChatGPT = Curriculum Architect (vision, objectives, sequencing, topic maps, quizzes, approvals). Claude Code = Implementation Engineer (markdown docs, notebooks, demos, repo generation). Gemini = Visual Assets (diagrams, storyboards, animations). GitHub = integration hub. Handoffs use the standardized ARCHITECT DECISION / IMPLEMENTATION REPORT format; only current-assignment context is passed, not full history.

## D-012 — Module 1 Supporting Docs · APPROVED
`software_environment.md`, `mathematical_prerequisites.md`, and `assessment_strategy.md` (with policy updates) approved. Mini-project scope (manifest §14), exit criteria (§16), and the competency framework approved.

## D-013 — Module 1 Scaffolding Authorized · APPROVED
Authorized to create `modules/module01/` scaffolding only: `README.md`, `learning_objectives.md`, `topic_map.md`, `assessments.md`, and empty `lessons/`, `notebooks/`, `assets/`. Populate learning objectives, topic map, and assessment alignment. No lessons, notebooks, or quizzes yet.

## D-014 — Module 1 Topic Granularity & Breakdown · APPROVED
Granularity = **option B** (sub-topic level). Each sub-topic is one lesson. **66 lessons** total across 9 units. Full authoritative breakdown recorded in `modules/module01/topic_map.md §2`. Rationale: one-lesson-per-unit is too coarse for a comprehensive Physical AI program.

## D-015 — Final Assessment Policy · APPROVED
Mastery thresholds: ≥85% Mastery · 70–84% Proficient · 50–69% Developing · <50% Beginning. Knowledge Checks = formative only (unlimited attempts, immediate feedback; participation credit only if LMS requires). Competency-based exit **overrides** numeric score; six required competencies: vector ops, coordinate frames, matrix transformations, trigonometric reasoning, Python computation, workspace modeling. A passing percentage alone is insufficient to enter Module 2.

## D-016 — Pilot Lesson & Generation Strategy · APPROVED
Philosophy and roadmap approved. Generation strategy: **pilot lesson → architect review → revise template → generate Unit 1 → review → continue unit-by-unit.** Do NOT generate all 66 lessons at once. Pilot lesson selected: **1.1 Physical AI and the Physical World**. Gemini greenlit for **storyboard briefs only** (no assets yet) for Priority-1 Units 2, 3, 4.

## D-017 — Pilot Approved; Lesson Standards Locked · APPROVED
Pilot 1.1 approved as canonical reference. Locked curriculum-wide standards:
- **Sections 7/8 (Units 1–7):** Interactive Demonstration = conceptual/guided; Coding Exercise = pseudocode/snippet/thought exercise. Full runnable implementations belong to the notebook track. Unit 8+ may include substantial executable content.
- **Section 9 vs 10:** §9 Knowledge Check = recall/understanding/immediate application, short-answer/MC. §10 Challenge = transfer/engineering reasoning/open-ended.
- **Metadata:** YAML frontmatter (module, unit, lesson, title, estimated_time, difficulty, prerequisites, learning_objectives, tags).
- **Visuals:** each lesson includes an inline `[Visual: ...]` placeholder + a Gemini Storyboard Brief (Objective/Scene/Labels/Animation Notes).
- **Template:** `templates/lesson_template.md` created; all future lessons reference it rather than copying a previous lesson.

## D-018 — Unit 1 Lessons Generated · DELIVERED (awaiting review)
Lessons 1.2–1.6 generated (1.2 Units and Dimensions, 1.3 Scalars and Physical Quantities, 1.4 Measurement Error, 1.5 Accuracy and Precision, 1.6 Engineering Estimation). Pilot 1.1 retrofitted to YAML + visual convention. Unit 1 average ≈ 1,400 words/lesson (1.1 longer as the orientation lesson). Awaiting architect review before Unit 2.

---

### Pending architect decisions (none blocking)
- Architect review of Unit 1 (lessons 1.2–1.6). On approval, Unit 2 (lessons 2.1–2.9, vectors) generation proceeds.

*Append new decisions below as `D-0NN — Title · APPROVED` with a date.*
