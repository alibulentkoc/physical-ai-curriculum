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

## D-019 — Unit 1 Approved; Pipeline & Standards Locked · APPROVED
Unit 1 approved as baseline quality standard. Length band: typical 1,200–1,600 words, intro/synthesis up to 2,200, target 35–45 min. Math intensity increases naturally through the module (U2 vectors → U3 frames → U4 matrices → U5 linear algebra → U6 trig). **Notebook timing = PER-UNIT**: generate unit notebooks immediately after each unit is approved. Official pipeline: Unit Lessons → Review → Approved → Generate Unit Notebooks → Next Unit. Required new doc `curriculum/notebook_strategy.md` before large-scale notebook generation.

## D-020 — Notebook Strategy + Unit 2 Generated · DELIVERED (awaiting review)
Created `curriculum/notebook_strategy.md` (purpose, standards, lesson-to-notebook mapping, tooling, visualization conventions, assessment integration). Generated Unit 2 lessons 2.1–2.9 (vectors): what-is-a-vector, representation, addition, subtraction, magnitude/direction, unit vectors, dot product, cross product, distance. Avg ≈ 1,220 words/lesson, all within band. Unit 2 explicitly bridges to coordinate frames (Unit 3). Awaiting architect review.

## D-021 — Lesson 1.1 Full Prototype (student experience) · DELIVERED
Built the complete student experience for Lesson 1.1 as the reference pattern for all lessons:
- **Notebook:** `modules/module01/notebooks/lesson01_*.ipynb` — runnable (validated JSON, 12 cells), position→distance→reachability + "trace the loop", self-check asserts.
- **Diagram:** `assets/diagrams/m01-l1-perception-action-loop.svg` (also copied to `site_src/assets/` for the site).
- **Visual asset requirements:** `modules/module01/assets/lesson01_visual_requirements.md` (L1-V1..V3, specs, briefs, status).
- **Quiz:** `modules/module01/quizzes/lesson01_quiz.yaml` (learner-facing, formative) + answer key/rubric in `coaches/answer-keys/module01/lesson01_answer_key.md`.
- **Interactive demo spec:** `modules/module01/demos/lesson01_trace_the_loop_spec.md`.
- **MkDocs integration:** `mkdocs.yml` (Material theme, arithmatex math, admonitions), `requirements-docs.txt`, `site_src/index.md`, `site_src/module01/lesson01.md`. Site **builds successfully** with `mkdocs build --strict`. Build output `/site/` gitignored.

**Architecture note for review:** `site_src/` is the presentation layer; `modules/` holds authoring sources. The 1.1 student page was authored directly (one-off). Before scaling to 66 lessons, adopt a single-source approach (MkDocs `pymdownx.snippets` include or a sync script) so the site and source lessons don't drift.

---

### Pending architect decisions (none blocking)
- Architect review of (a) the four representative lessons (content review, in progress) and (b) the Lesson 1.1 full prototype. Key prototype decision: approve the `site_src/` presentation-layer architecture and the single-source plan before scaling. Notebook sequencing for Units 1–2 still deferred to the architect.

## D-022 — Role Expansion; Claude Owns All Asset Production · APPROVED
Gemini removed from the workflow. Claude now owns: lesson generation, SVG diagrams, Mermaid diagrams, interactive HTML demos, Jupyter notebooks, MkDocs site generation, and all lesson visual assets. Per-lesson deliverable set is now: lesson markdown + diagram specification + rendered SVG asset + notebook + quiz assets, all in-repo and immediately renderable. Lesson template §4 updated (Gemini brief → Diagram Specification + produced assets).

## D-023 — Lesson 1.1 Production-Quality Build · DELIVERED
Upgraded Lesson 1.1 to production quality with all assets produced and verified renderable:
- **SVGs:** `m01-l1-perception-action-loop.svg`, `m01-l1-software-vs-physical-ai.svg`.
- **Mermaid:** pixels→frames→angles pipeline embedded on the site page.
- **Interactive HTML demo:** `modules/module01/demos/lesson01_trace_the_loop.html` — self-contained vanilla JS + SVG, draggable/keyboard-accessible tomato, live readout, reach slider, perceive→reason→act stepper. No dependencies, no browser storage.
- **Notebook + quiz + answer key:** retained from D-021.
- **MkDocs:** Mermaid enabled (superfences custom fence); page embeds both SVGs, the Mermaid diagram, and the demo via iframe. **`mkdocs build --strict` passes**; verified mermaid block, both SVGs, demo, and iframe present in built HTML.
This is the production reference pattern for every lesson's complete student experience.

## D-024 — Interactive Knowledge-Check Widget · DELIVERED
The Lesson 1.1 knowledge check is now an **interactive HTML widget** (`modules/module01/quizzes/lesson01_quiz.html`), fulfilling the formative/immediate-feedback policy (D-015): multiple-choice and true/false give instant correct-incorrect feedback with explanations; the matching item is checkable; short-answer items reveal a model answer for self-assessment. Unlimited attempts, nothing stored, not graded. Embedded on the site page via iframe; replaces the previous static question list. JS validated; `mkdocs build --strict` passes. The `lesson01_quiz.yaml` remains the question source; the interactive feedback lives in the widget (formative self-check), while graded answer keys stay in `coaches/`.

---

### Open architecture item (carried)
- Single-source plan for `site_src/` vs `modules/` before scaling the site to 66 lessons (recommend pymdownx.snippets include or a sync script).

*Append new decisions below as `D-0NN — Title · APPROVED` with a date.*

## D-025 — Full Unit 1 Production + Standards + Design System · DELIVERED
Produced all of Unit 1 to the proven 1.1 standard, plus the governing documents:
- **Production contract:** `curriculum/production_standards.md` (Definition of Done, SVG/diagram/notebook/quiz standards, accessibility, MkDocs validation, demo policy).
- **Design system:** `assets/design-system/{colors,typography,svg_standards,diagram_standards}.md`.
- **Per lesson 1.2–1.6:** rendered SVG, runnable notebook (all six Unit 1 notebooks **executed headless — pass**), interactive HTML quiz (JS validated), answer key in `coaches/`, MkDocs site page in nav.
- **Mermaid** added to 1.4 (error taxonomy). **Interactive demo** added to 1.5 only (accuracy/precision sliders) — the lesson where manipulation clearly helps; others SVG-only per demo policy.
- Lesson §4 updated for 1.2–1.6 (Gemini brief → produced-asset reference).
- **`mkdocs build --strict` passes**; verified 6 pages, 7 SVGs, 6 quizzes, 2 demos served.
- Note: Unit 2 lesson files (2.1–2.9) still carry legacy "Gemini" §4 wording — to be updated during Unit 2 production.

## D-027 — Single-Source Generator + core_idea + Unit 2 Launch · IN PROGRESS
- **Generator (approved option b):** `tools/generate_site_pages.py` builds every `site_src/` page from the **authoritative canonical lesson** markdown, injecting assets at fixed anchors (SVG → §4, demo → §7, notebook tip → §8, quiz → §9; Mermaid passes through), and copies assets into `site_src/`. Pages with no assets are held back (not published) to keep `--strict` clean. Eliminates the double-maintenance that bit us repeatedly. Run: `python3 tools/generate_site_pages.py`.
- **core_idea:** added to all 15 lesson frontmatters (Unit 1 + Unit 2) for Companion/Global generation, search, and analytics.
- **Gemini fully removed** from all Unit 2 lessons (§4 → Diagram Specification / produced-asset reference). Residual-reference check: NONE.
- **Two standard sections** (AI Companion + Global Learning Support) added to all 9 Unit 2 lessons.
- **Unit 2 produced so far (2.1–2.3):** SVG + executed notebook + interactive quiz each; **2.3 Vector Addition interactive demo** (drag two vectors tip-to-tail, live resultant + magnitude, b+a swap) — the architect-required demo. Pages generated + in nav. `mkdocs build --strict` passes.
- **Remaining Unit 2 (next installment):** assets for 2.4–2.9 (SVGs, notebooks, quizzes), and the two remaining required demos — **2.7 Dot Product** (alignment angle → dot value) and **2.8 Cross Product** (normal vector + parallelogram area).

## D-028 — Unit 2 Complete · DELIVERED
All of Unit 2 (2.1–2.9) produced to the Unit 1 standard:
- **2.4–2.9:** SVG + executed notebook + interactive quiz + answer key (`coaches/`) each. All Unit 2 notebooks execute headless clean.
- **Required interactive demos delivered:** 2.3 Vector Addition (tip-to-tail resultant), **2.7 Dot Product** (drag b / angle slider → live dot value, aligned/perpendicular/opposed, gripper-alignment framing), **2.8 Cross Product** (drag a & b → parallelogram area + signed normal toward/away).
- **Answer keys for all 15 lessons** present in `coaches/answer-keys/module01/` (added 2.1–2.3 keys for consistency).
- **Diagram Specification kept in canonical, hidden from site** (architect decision): generator strips the spec, `[Visual:]`, and maintainer notes from student pages while canonical retains them as production source.
- Nav lists 1.1–2.9 (15 lessons). `mkdocs build --strict` passes; 15 pages, 9 Unit 2 SVGs, 5 demos served.
- **PAUSE FOR REVIEW** before Unit 3 (architect): review flagship lessons 2.3/2.7/2.8 and overall student experience; authorize Unit 3 only if a student can learn vectors through intuition→visual→math→computation without losing the robotics connection.

## D-026 — AI Learning Companion + Global Learning Support + i18n · DELIVERED
Two new standard lesson sections added curriculum-wide (after Key Takeaways, before Next lesson):
- **AI Learning Companion** — lesson-specific Tutor / Practice / Explore prompts (≤50 words each, copy/paste ready).
- **Global Learning Support** — per-language explanation prompts (Español, 中文 Simplified, Türkçe), generated from the lesson title; English authoritative.
Applied to all six Unit 1 lessons (canonical + site pages). Template updated with both as standard components. Created `curriculum/internationalization_strategy.md` (English authoritative; AI-assisted multilingual workflow; Phase 1 prompts → Phase 2 MkDocs selector → Phase 3 human-reviewed; terminology-preservation rules; supported-language roadmap). `mkdocs build --strict` passes; sections (incl. CJK) render.
