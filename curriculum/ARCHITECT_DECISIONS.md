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

## D-029 — Embedded-Visual Robustness · FIXED
Hardened the generator's asset embedding so interactive demos/quizzes render reliably on lesson pages:
- Guaranteed blank-line separation around every injected HTML block.
- Clarified the two path rules: **iframes** (raw HTML, browser-resolved against the output URL) use `../../demos|quizzes/`; **Markdown links** (MkDocs-rewritten, source-relative) use `../demos|quizzes/`.
- Added a validated Markdown **"Open in a new tab"** fallback link under every demo/quiz, so `mkdocs build --strict` now *validates* every asset path (a broken path fails the build) and students always have a working entry even if an iframe is cached blank.
- Verified: all 20 iframes + 20 fallback links resolve to existing files; `--strict` passes with no warnings. "Embedded not working" locally is a stale-page/browser-cache symptom — fix by re-running the generator and hard-refreshing.

## D-030 — Unit 2 Approved; Recap Built; Unit 3 Authorized (Plan) · DELIVERED
- **Unit 2 APPROVED** as production complete (flagship review of 2.3/2.7/2.8 passed).
- **Unit 2 recap built:** Lesson 2.10 "Vectors in Physical AI" (lesson16) — short synthesis lesson answering "why do robots need vectors?", with a summary SVG (the toolkit in one reach), a capstone notebook (all ops together, executes clean), a recap quiz + answer key, and the two standard sections. In nav; `mkdocs build --strict` passes. Generator anchors generalized to accept unnumbered section headings so shorter lessons embed assets correctly.
- **Unit 3 AUTHORIZED.** Topic map 3.1–3.7 (Coordinate Systems and Reference Frames). Intuition-first; "the same tomato has different coordinates depending on who is looking"; **no matrices in Unit 3** (frames/transforms taught conceptually).
- **Plan delivered:** `curriculum/unit3_production_plan.md` — topic map, per-lesson asset plan, three required demo specs (3.5 viewpoint switcher, 3.6 conceptual transform, 3.7 flagship tri-frame pick), asset inventory, sequencing, and pre-production recommendations.
- **PAUSE:** production not started; awaiting architect confirmation of the plan/recommendations before Unit 3 production.

Module 1 now: 16 lessons produced (1.1–1.6, 2.1–2.9, 2.10 recap), 17 SVGs, 16 notebooks, 16 quizzes, 16 answer keys, 5 demos.

## D-031 — Unit 3 Installment 1 · DELIVERED (3.1, 3.5, 3.7)
Intuition cornerstones produced to standard; **PAUSE for review** before remaining Unit 3 lessons (per architect).
- **3.1 Why Coordinate Frames Matter** (lesson17): lesson + SVG (one tomato, two observers, two readings) + notebook + quiz + answer key. Signature insight foregrounded: *the tomato has not moved; only the observer changed.*
- **3.5 Local and Global Frames** (lesson21): lesson + SVG (three labeled frames, three readings) + notebook + quiz + answer key + **required demo** `lesson21_frames_viewpoint.html` (World/Robot/Camera switcher; drag the robot; tomato fixed; world reading never changes).
- **3.7 Robot and Camera Frames** (lesson23, flagship): lesson + SVG (camera→robot→world chain) + notebook + quiz + answer key + **required demo** `lesson23_robot_camera_frames.html` (tri-frame pick; step perceive→act→remember; all three readouts live; world stays fixed).
- No matrices (offsets/conceptual only), per the confirmed boundary. Faux-3D not needed for these three (2D top-down suffices); isometric SVG reserved for 3.4/3.7-style 3D when 3.2–3.4 are produced.
- Generator fix: lesson file glob broadened to `lesson[0-9][0-9]_*.md` so Unit 3 files (lesson20+) publish; section anchors already accept unnumbered headings.
- `mkdocs build --strict` passes; all three notebooks execute clean; all cornerstone embeds + fallback links resolve. Nav now has a "Unit 3" section with 3.1/3.5/3.7.
- **Remaining Unit 3 (Installment 2, after review):** 3.2 Cartesian, 3.3 2D, 3.4 3D, 3.6 Conceptual Transformations (+ required demo), then 3.8 recap "Coordinate Frames in Physical AI."

Module 1 now: 19 lessons produced (1.1–1.6, 2.1–2.10, 3.1, 3.5, 3.7), 20 SVGs, 19 notebooks, 19 quizzes, 19 answer keys, 7 demos.

## D-032 — Unit 3 COMPLETE (Installment 2 delivered) · PAUSE before Unit 4
Installment 2 produced to standard; Unit 3 (Coordinate Systems & Reference Frames) is now production-complete.
- **3.2 Cartesian Coordinates** (lesson18), **3.3 2D Coordinate Systems** (lesson19), **3.4 3D Coordinate Systems** (lesson20, faux-3D isometric SVG + right-hand rule), **3.6 Conceptual Frame Transformations** (lesson22) — each lesson + SVG + notebook + quiz + answer key.
- **3.6 required demo** `lesson22_frame_transform.html`: offset (dx, dy) + rotation θ sliders; one fixed point read live in frame A and frame B; offset-only (θ=0) reduces to subtraction; the conceptual bridge to Unit 4 matrices — no matrices shown.
- **3.8 recap** `lesson24` "Coordinate Frames in Physical AI": short synthesis answering "why can the same tomato have multiple correct coordinates?"; capstone notebook (world/robot/camera + a frame conversion); recap SVG; quiz + answer key. Sets up Unit 4.
- Through-line kept visible: Unit 2 = "how do we describe position?"; Unit 3 = "who is describing it?"
- No matrices anywhere in Unit 3 (offset + rotation, hand-rolled helpers). faux-3D isometric for 3.4 (no WebGL), per architect.
- `mkdocs build --strict` passes; all Unit 3 notebooks execute clean; all embeds + fallback links resolve. Nav has the full Unit 3 section (3.1–3.8).
- **PAUSE for review before Unit 4 production** (architect directive). Unit 4 = matrix transformations (the offset+rotation packaged as one matrix).

Module 1 totals: 24 lessons produced (1.1–1.6, 2.1–2.10, 3.1–3.8), 25 SVGs, 24 notebooks, 24 quizzes, 24 answer keys, 8 demos.

## D-033 — Unit 3 Approved; Midpoint Assessment + Unit 4 Plan · DELIVERED (production paused)
- **Unit 3 APPROVED** (no revisions). Signature insight operationalized; strong bridge to Unit 4.
- **Module 1 Midpoint Assessment** created (`assessments/module01_midpoint_assessment.md`) — readiness checkpoint positioned between Unit 3 and Unit 4. Covers Unit 1 physical quantities, Unit 2 vectors, Unit 3 coordinate frames; **no matrix mathematics**. Mixed format (MC/TF/short/applied); the applied item is the camera→robot→world chain. Key + readiness rubric in `coaches/answer-keys/module01/midpoint_assessment_key.md` (the readiness signal is whether the student can explain *why the same point has multiple correct coordinates*).
- **Unit 4 AUTHORIZED.** Topic map 4.1–4.8 "Matrices as Transformations" — positioned as **"Transformations of Space," not linear algebra**. Central idea: *a matrix is an action applied to space, not a table of numbers.* Geometry first (rotation/scaling/reflection/composition) before algebra.
- **Plan delivered:** `curriculum/unit4_production_plan.md` — topic map, per-lesson asset plan, three required demo specs (4.4 identity = do-nothing; 4.5 rotation slider 0°→360°; 4.8 flagship composition scale→rotate→translate with order-matters), asset inventory, geometry-first sequencing, and pre-production recommendations (incl. how to handle translation without 3×3 homogeneous matrices yet, and a recommended 4.9 recap).
- **PAUSE:** Unit 4 lesson production not started; awaiting architect confirmation of the plan/recommendations.

Module 1 totals unchanged: 24 lessons, 25 SVGs, 24 notebooks, 24 quizzes, 24 answer keys, 8 demos, + the midpoint assessment.

## D-034 — Unit 4 Installment 1 · DELIVERED (4.1, 4.4, 4.5, 4.6)
Operator-intuition cornerstones produced to standard; **PAUSE for review** before remaining Unit 4 lessons.
- **4.1 Matrices as Operators** (lesson25): lesson + SVG (matrix-as-machine: points in → moved points out; columns = images of unit arrows) + notebook + quiz + answer key. Frames the unit: a matrix is an action, not a table.
- **4.4 The Identity Matrix** (lesson28): lesson + SVG (pass-through) + notebook + quiz + key + **required demo** `lesson28_identity.html` (apply identity → nothing moves; toggle a non-identity to contrast). identity = do nothing.
- **4.5 Rotation Matrices** (lesson29): lesson + SVG (rotate about origin, ghost original, distance circle) + notebook + quiz + key + **required demo** `lesson29_rotation.html` (single slider 0°→360°; matrix shown live; distance preserved). rotation as geometry first.
- **4.6 Scaling Transformations** (lesson30): lesson + SVG (stretch along axes, area note) + notebook + quiz + key + **required demo** `lesson30_scaling.html` (sx, sy sliders; uniform vs non-uniform; live area factor).
- Boundaries honored: 2D; geometry-first; no homogeneous matrices; translation stays conceptual (will appear as an action in the 4.8 composition demo). Through-line visible: Unit 3 "who describes the position?" → Unit 4 "what can we do to it?"
- `mkdocs build --strict` passes; all four notebooks execute clean; all embeds + fallback links resolve. Nav now has a "Unit 4" section (4.1/4.4/4.5/4.6).
- **Remaining Unit 4 (Installment 2, after review):** 4.7 Reflection, 4.2 Matrix Addition, 4.3 Matrix Multiplication, 4.8 Composition (+ required flagship demo), then 4.9 recap "Transformations in Physical AI."

Module 1 now: 28 lessons produced, 29 SVGs, 28 notebooks, 28 quizzes, 29 answer keys (incl. midpoint), 11 demos, + midpoint assessment.

## D-035 — Unit 4 COMPLETE (Installment 2 delivered) → MODULE 1 COMPLETE · PAUSE before Module 2
Installment 2 produced to standard; Unit 4 (Matrices as Transformations) and **Module 1** are now production-complete.
- **4.7 Reflection** (lesson31): lesson + SVG (mirror across axis, backwards-Я handedness flip) + notebook + quiz + key. det = −1, reflect-twice = identity.
- **4.2 Matrix Addition** (lesson26, lightweight): entry-wise; explicitly NOT composition. SVG + notebook + quiz + key.
- **4.3 Matrix Multiplication** (lesson27): geometry-first — "do A, then B = apply BA"; first action on the right; not commutative. SVG + notebook + quiz + key.
- **4.8 Composition** (lesson32, flagship): order matters (scale→rotate ≠ rotate→scale) + **flagship demo** `lesson32_composition.html` (drag-reorder scale/rotate/translate, reverse-order button, live result + tracked point). Translation included as an action conceptually (homogeneous form deferred to Module 2).
- **4.9 recap** (lesson33) "Transformations in Physical AI": consolidates identity/rotation/scaling/reflection/composition; answers "what can a matrix do to space?"; capstone notebook; bridges to Module 2 (homogeneous coords, SE(3)).
- Through-line kept: Unit 3 "the same point can have different coordinates" → Unit 4 "the same point can be transformed in different ways." Core belief reinforced: a matrix is an action, not a table.
- `mkdocs build --strict` passes; all Unit 4 notebooks execute clean; all embeds + fallback links resolve. Nav has the full Unit 4 section (4.1–4.9).
- **MODULE 1 COMPLETE:** Units 1–4 + the Module 1 Midpoint Assessment.
- **PAUSE for review before Module 2 production** (architect directive). Module 2 = homogeneous coordinates / SE(3) / kinematics.

Module 1 totals: 33 lessons produced (1.1–1.6, 2.1–2.10, 3.1–3.8, 4.1–4.9), 34 SVGs, 33 notebooks, 33 quizzes, 34 answer keys (incl. midpoint), 14 demos, + midpoint assessment.

## D-036 — Module 1 Signed Off; Module 2 Authorized (Planning) · DELIVERED
- **Module 1 APPROVED & signed off** (no revisions). All objectives achieved across Units 1–4.
- **Module 1 completion report** created: `curriculum/module01_completion_report.md` — objectives, full lesson/asset/demo/notebook/assessment inventories, lessons learned, recommendations. Archival record.
- **Module 2 AUTHORIZED** = "Spatial Transformations and SE(3)" (highest-priority workstream). Teaches how transformations are represented and composed in robotics: homogeneous coordinates, rigid-body transforms, rotation matrices, translation vectors, transformation chains, SE(2), SE(3) — NOT full kinematics yet.
- **Module 2 scaffolding created:** `modules/module02/` with README.md, learning_objectives.md, topic_map.md, assessments.md, and lessons/ notebooks/ assets/ demos/ quizzes/ dirs. Manifest at `curriculum/module02_manifest.md`; production plan (roadmap + demo + asset + risks) at `curriculum/module02_production_plan.md`.
- **Topic map (proposed, 8 units):** 1 Why Transformations Matter · 2 Homogeneous Coordinates · 3 SE(2) · 4 SE(3) · 5 Composition · 6 Robot Pose · 7 Camera-to-Robot · 8 Mini Project (Perception-to-Pose). Refinements flagged: per-unit recaps; Unit 7 concept-level (extrinsics yes, intrinsics deferred); inverses introduced in SE(2); faux-3D isometric for 3D; mini project = assessment centerpiece; numbering restart per module (module02/lesson01…, m02-l01…).
- **Production cadence:** intuition-first; lead Module 2 with physical movement (Unit 1) before homogeneous-coordinate algebra; installments A(U1+U2) → B(U3+U4) → C(U5+U6) → D(U7+U8) with pause-for-review between, mirroring Module 1.
- **PAUSE:** no Module 2 lessons generated; awaiting review of manifest/topic map/plans before lesson production.

Open decisions for architect: confirm topic-map refinements (recaps, Unit 7 boundary, inverse placement, 3D approach, numbering); confirm midpoint-checkpoint placement (after Unit 4 vs Unit 5); confirm rubric weighting carry-over.

## D-037 — Module 2 Installment A DELIVERED (Unit 1 + Unit 2) · PAUSE before Installment B
Installment A produced to standard; Module 2 Units 1–2 are production-complete. Numbering restarted per module (module02/lessonNN, m02-lN); per-unit recaps included.
- **Unit 1 — Why Transformations Matter (4):** 1.1 The Robot's Constant Problem (lesson01) · 1.2 Position + Orientation Together / pose (lesson02) · 1.3 The Limit We Hit in Module 1 — 2×2 can't translate (lesson03) · 1.4 recap (lesson04). Intuition/motivation-first; no matrix algebra at the open.
- **Unit 2 — Homogeneous Coordinates (5):** 2.1 One Extra Coordinate / lift to (x,y,1) (lesson05) · 2.2 Points vs Directions / w=1 vs w=0 (lesson06) · 2.3 Translation as a Matrix (lesson07) · 2.4 Rotation + Translation in One Matrix / block form [[R,t],[0,1]] (lesson08) · 2.5 recap (lesson09).
- **Required demo:** `modules/module02/demos/lesson07_translation_matrix.html` — the module "aha": toggle 2×2 (can't move the origin) vs homogeneous 3×3 (slides the point); drag the offset, watch the last column and point move together; a direction (w=0) stays fixed. JS validated.
- Per lesson: SVG + notebook + quiz + answer key + the two standard sections + core_idea. 9 SVGs (incl. faux-3D isometric "lift to height-1" for 2.1; block-form matrix for 2.4). 9 notebooks execute "All checks passed." 9 quizzes + 9 answer keys (new coaches/answer-keys/module02/).
- **Generator extended for multi-module** (MODULES=["01","02"]; quizzes/demos namespaced site_src/{quizzes,demos}/moduleMM/ to avoid lesson01 collisions; SVGs flat with m01-/m02- prefixes). Module 1 re-verified strict-clean.
- `mkdocs build --strict` passes; all 9 Module 2 notebooks execute clean; all 10 Module 2 embeds + fallback links resolve. Nav has a Module 2 section (Unit 1 1.1–1.4, Unit 2 2.1–2.5).
- Through-line kept: M1-U3 "different observers, different coordinates" → M1-U4 "transformations change space" → M2 "how transformations are represented and composed." Boundaries: 2D so far; translation now a matrix via homogeneous coords; SE(2)/SE(3) named but not yet formalized (Units 3–4).
- **PAUSE for review before Installment B** (architect directive). Installment B = Unit 3 (SE(2), with inverses) + Unit 4 (SE(3)).

Module 2 so far: 9 lessons, 9 SVGs, 9 notebooks, 9 quizzes, 9 answer keys, 1 demo.

## D-038 — UX FIXES: visual embedding + navigation hierarchy + page-header context (production pause)
Addressed the UX review (Issues 1–3). Module 2 lesson production paused per directive until visuals + nav verified — both now done.
- **Issue 1 (missing visuals) — ROOT CAUSE:** source/build were correct for 1.1,1.2,1.3,2.1,2.2,2.4 (SVG present, embed identical to working Module 1 pattern, anchor correct; a clean build resolves every img). The genuinely-broken pages were the two recaps (1.4, 2.5) whose lighter structure omitted the "Visual Explanation"/"Knowledge Check" anchors — fixed earlier (D-037 follow-up). Remaining user-visible gaps trace to a STALE build being tested (recurring sync issue). MkDocs rewrites the source-relative `../assets/` to output-relative `../../assets/` under use_directory_urls — confirmed resolving.
  - **Hardening:** generator now has a VALIDATOR that aborts the build if any published page has a "Visual Explanation" heading without an injected `<figure>/<img>`, or if a `[Visual: …]` placeholder leaks to a student page. Placeholder-only visual sections can no longer ship.
- **Issue 2 (navigation hierarchy) — ROOT CAUSE:** Module 1 nav was inconsistent — Units 3–4 were grouped under named "Unit —" subsections but Units 1–2 listed lessons flat under the module. **Fix:** restructured mkdocs.yml so every unit (M1 U1–U4, M2 U1–U2) is a named "Unit Y — Title" subsection → Module → Unit → Lesson everywhere. Nav labels already include lesson titles.
- **Issue 3 (context-free titles):**
  - **Page-header standard (implemented):** generator injects a "You are here" admonition above every H1: **Module X — Title · Unit Y — Title · Lesson Y.Z — Title** (driven by frontmatter module/unit/lesson + a MODULE_TITLES/UNIT_TITLES map in the generator).
  - **Notebook naming standard (PROPOSED, awaiting confirm before mass-rename):** `M{MM}_U{UU}_L{lesson}_{Title}.ipynb`, e.g. `M01_U02_L01_What_Is_A_Vector.ipynb`. Executing requires updating the generator's notebook glob + renaming 42 files; proposed as a dedicated follow-up pass once the convention is confirmed (architect allowed "or equivalent").
- **Verification:** `mkdocs build --strict` passes; generator validator passes for all 42 pages; automated check across both modules: 43 images, 0 broken paths, 0 "Visual Explanation" sections without an image → ALL VISUALS RENDER. Module 1 fully re-verified.

No new lessons produced. Module 2 lesson production remains paused pending architect review of these UX fixes (and the notebook-naming confirmation).

## D-039 — Curriculum-wide UX fixes applied globally (Issues 1–4)
Applied across Module 1 + Module 2 (no new lesson content). Existing standards (ARCHITECT_DECISIONS, production_standards, lesson_template, internationalization_strategy) remain in force.
- **Issue 1 (demo/visual sections student-facing):** removed ALL maintainer/production commentary and future-demo references from "Interactive Demonstration" sections curriculum-wide. Stripped note variants ("*(Conceptual; notebook version later.)*", "*(Conceptual; runnable version in the notebook track.)*", "*(Snippet — full implementation in the notebook track…)*"). Lessons WITHOUT a demo (Mode B) now carry a self-contained **guided-prediction / visual-reasoning activity** using the lesson's own figure or worked example — no references to other lessons/units/future demos. Lessons WITH a demo (Mode A, e.g. 3.6) keep an embedded demo + intro. Generator validator already blocks placeholder-only visual sections.
- **Issue 2 (nav hierarchy):** mkdocs.yml restructured so every unit is a named "Unit Y — Title" subsection → consistent Module → Unit → Lesson across M1 (U1–U4) and M2 (U1–U2); labels include lesson titles. (Done D-038; in force.)
- **Issue 3 (page identity):** generator injects a "You are here" banner above every H1 — **Module X — Title · Unit Y — Title · Lesson Y.Z — Title** — on all 42 pages. (Done D-038; verified.)
- **Issue 4 (notebook identity):** every notebook now opens with a Module/Unit/Lesson/Title markdown header cell, and all 42 notebooks renamed to the standard **M{MM}_U{UU}_L{lesson}_{Title}.ipynb** (e.g. M02_U02_L2_3_Translation_As_A_Matrix.ipynb). Generator notebook discovery updated to the new names (with legacy fallback); notebook tips link to the new filenames. Sampled renamed notebooks still execute "All checks passed."
- **Verification:** `mkdocs build --strict` passes; generator validator passes for all 42 pages; cross-module scan = 42 pages, 42 context headers, 43 images, 0 broken paths, 0 visual-sections-without-image; section-7 maintainer-reference scan clean (the only remaining "interactive demo" mention is a Mode-A same-page self-reference in 3.6). 42/42 notebooks match the naming standard.
No Module 2 Installment B produced; awaiting approval after UX verification.

## D-040 — Module 2 Unit 3 (SE(2)) DELIVERED
- Lessons 3.1–3.5 (lesson10–14): What "Rigid" Means · The SE(2) Transformation · Applying SE(2) · Inverse Transformations (geometric, "rotate back then move back"; SE(2) inverse is itself SE(2)) · Unit 3 recap.
- 5 SVGs (m02-l10..l14), 5 notebooks (M02_U03_*; execute "All checks passed."), 5 quizzes + 5 answer keys, required demo `lesson12_se2_playground.html` (θ/tx/ty sliders, live 3×3, tracked edge-length proving rigidity, Apply-inverse returns shape). Nav Unit 3 subsection added.
- build --strict PASS; all Unit 3 embeds + headers resolve. Proceeding to Unit 4 (SE(3)) to complete Installment B before pausing.

## D-041 — Module 2 Unit 4 (SE(3)) DELIVERED · Installment B COMPLETE
- Lessons 4.1–4.6 (lesson15–20): From 2D to 3D Rigid Motion · 3D Rotation (axis+angle; Rx/Ry/Rz) · The SE(3) Transformation (4×4) · Translation Vectors in 3D (points w=1 vs directions w=0) · Applying SE(3); Inverses in 3D (rotate back, then move back; inverse is itself SE(3)) · Unit 4 recap.
- 6 faux-3D isometric SVGs (m02-l15..l20, no WebGL, single viewpoint), 6 notebooks (M02_U04_*; execute "All checks passed."), 6 quizzes + 6 answer keys, required demo `lesson17_se3_viewer.html` (axis/angle + tx/ty/tz, live 4×4, rigid frame). Nav Unit 4 subsection added.
- build --strict PASS; all Unit 4 embeds + headers resolve.
- **Installment B (Unit 3 SE(2) + Unit 4 SE(3)) COMPLETE.** Module 2 now: 20 lessons, 20 SVGs, 20 notebooks, 20 quizzes, 20 answer keys, 3 demos (Units 1–4 done; Units 5–8 remain).
- PAUSE at Installment-B milestone for review. Next: Installment C = Unit 5 (Composition) + Unit 6 (Robot Pose); midpoint checkpoint AFTER Unit 5.

## D-042 — Module 2 Unit 5 (Composition) + Midpoint Checkpoint DELIVERED
- Lessons 5.1–5.4 (lesson21–24): Chaining Transforms (product, right-to-left) · Order Matters, Revisited (non-commutativity) · Frames as a Graph (compose along path, invert backward edges) · Unit 5 recap.
- 4 SVGs (m02-l21..l24), 4 notebooks (M02_U05_*; "All checks passed."), 4 quizzes + 4 answer keys, required demo `lesson21_composition_chain.html` (chain two SE(2), toggle order, live combined matrix). Nav Unit 5 subsection added.
- **Midpoint checkpoint placed AFTER Unit 5** per D-036: `assessments/module02_midpoint_assessment.md` + `coaches/answer-keys/module02/midpoint_assessment_key.md` (covers Units 1–5; readiness signal = build/apply/compose/invert rigid transforms; excludes pose/extrinsics/mini-project).
- build --strict PASS; all Unit 5 embeds + headers resolve. Proceeding to Unit 6 (Robot Pose) to complete Installment C.

## D-043 — Module 2 Unit 6 (Robot Pose) DELIVERED · Installment C COMPLETE
- Lessons 6.1–6.4 (lesson25–28): What Is a Pose? (position+orientation = one SE(2)/SE(3) element) · A Pose Is a Transformation (pose = frame-to-frame transform; poses compose/invert like transforms) · Reading and Writing Poses (read t/R; update by composing motion, right vs left multiply) · Unit 6 recap.
- 4 SVGs (m02-l25..l28; pose = little coordinate frame), 4 notebooks (M02_U06_*; "All checks passed."), 4 quizzes + 4 answer keys, recommended demo `lesson27_pose_explorer.html` (x/y/θ sliders, live SE(2), "Move in robot frame" composes a motion). Nav Unit 6 subsection added.
- build --strict PASS (one transient I/O flake on first attempt; clean on retry); all Unit 6 embeds + headers resolve.
- **Installment C (Unit 5 Composition + Unit 6 Pose) COMPLETE**, midpoint checkpoint placed after Unit 5.
- Module 2 now: 28 lessons, 28 SVGs, 28 notebooks, 28 quizzes, 28 answer keys (+ midpoint assessment & key), 5 demos. Units 1–6 done; Units 7–8 remain (Installment D).
- PAUSE at Installment-C milestone. Next: Installment D = Unit 7 (Camera-to-Robot, extrinsics only) + Unit 8 (Mini Project: Perception-to-Pose).

## D-044 — Module 2 Unit 7 (Camera-to-Robot, extrinsics only) DELIVERED
- Lessons 7.1–7.4 (lesson29–32): The Camera Sees Its Own World (detections in camera frame) · Camera Extrinsics (camera's pose on robot, SE(3); vs intrinsics deferred to M3) · Building the Transformation Chain (camera→world = arm-pose · extrinsics; convert in one multiply; inverse chain) · Unit 7 recap ("how does a detected object become a robot pose?").
- Scope honored: extrinsics/coordinate-relationships/pose-interpretation/chains ONLY; intrinsics, projection, image formation, CV math deferred to Module 3 (stated explicitly in lessons).
- 4 faux-3D SVGs (m02-l29..l32), 4 notebooks (M02_U07_*; "All checks passed."), 4 quizzes + 4 answer keys. Nav Unit 7 subsection added.
- build --strict PASS; all Unit 7 embeds + headers resolve. Proceeding to Unit 8 capstone (Mini Project: Perception-to-Pose).

## D-044 — Module 2 Installment D (Units 7 & 8) DELIVERED · MODULE 2 COMPLETE
- **Unit 7 — Camera-to-Robot Transformations** (7.1–7.4, lesson29–32): the camera sees its own world · camera extrinsics (camera's pose) · building the transformation chain (camera→arm→world) · recap. Extrinsics ONLY; intrinsics/projection deferred to Module 3. (Lessons/SVGs/notebooks/quizzes/keys were already present from a prior session; verified complete.)
- **Unit 8 — Mini Project: Perception-to-Pose Pipeline** (8.1–8.4, lesson33–36): from detection to reach · building the pipeline · verifying and visualizing · wrap-up and the road to kinematics. Built this session: 2 missing SVGs (m02-l35 verify, m02-l36 module-arc), 4 notebooks (M02_U08_*; execute "All checks passed."), 4 quizzes + 4 answer keys, and the flagship demo `lesson33_perception_to_pose.html` (faux-3D scene, sliders for detection/extrinsics/arm pose, live composed world target + verification view: inverse round-trip + distance preservation). Unit 7 & 8 nav subsections added.
- Capstone equation T(world←tomato)=T(world←arm)·T(arm←cam)·T(cam←tomato); worked example (detection (0,0,0.3), extrinsics (0,0,0.1), arm (1.0,0.5,0)) → world (1.0,0.5,0.4); verified by inverse round-trip + 0.3 m distance preservation, consistent across lessons, notebooks, and demo.
- build --strict PASS; all Units 7–8 embeds + "You are here" headers resolve.
- **MODULE 2 COMPLETE:** 36 lessons, 36 SVGs, 36 notebooks, 36 quizzes, 36 answer keys, 6 demos, midpoint assessment + key. Completion report at `curriculum/module02_completion_report.md`.
- PAUSE for Module 2 review. After review: Module 3 (kinematics; camera intrinsics/projection/perception) + the parked asset-hardening audit pass.

## D-045 — Module 3 begun; manifest + scaffold + Installment A (Units 1–2) DELIVERED
- **Module 3 = "Camera Geometry and Robotic Perception"** (roadmap D-004): how a camera turns world→pixels and back; perceive fruit + estimate position. Absorbs the perception stack deferred from Module 2 (intrinsics, projection, image formation, distortion, back-projection). **OpenCV introduced in this module (Unit 4).** Central idea: projection is NOT rigid and NOT invertible alone — it collapses 3D→2D, discarding depth; recovering 3D needs extra info (depth).
- Created: `curriculum/master_progress.md` (10-module tracker, architect-requested), `curriculum/module03_manifest.md`, `modules/module03/topic_map.md`, scaffold dirs, `coaches/answer-keys/module03/`. Generator wired: `MODULES=["01","02","03"]`, `MODULE_TITLES["03"]`, all 8 M3 `UNIT_TITLES`. Numbering restarts (lesson01…, m03-l01…, M03_U0Y_*).
- **Planned 8 units** (topic_map): U1 Why Perception · U2 The Pinhole Camera Model · U3 Camera Intrinsics (K) · U4 Projection in Practice (OpenCV intro; **midpoint checkpoint after U4**) · U5 Lens Distortion · U6 Back-Projection (pixels→3D) · U7 From Pixels to the Robot (bridge to M2 extrinsics) · U8 Mini Project (See the Fruit, Place It in the World capstone).
- **Installment A built (Units 1–2, lessons 01–08):** 8 lessons, 8 SVGs (XML-valid, rendered; pinhole diagram visually verified), 8 notebooks (execute "All checks passed."; standard f=800 px), 8 quizzes + 8 answer keys, and the perspective-projection demo `lesson07_perspective_projection.html` (sliders X/Z/f, live x=fX/Z). Nav added for U1+U2.
- Key formulas taught: image=2D pixel array (direction not position); forward many-to-one loses depth, inverse needs depth; projection keeps direction (X/Z,Y/Z), discards depth, apparent size ∝1/Z; pinhole x=fX/Z (similar triangles); f=center-of-projection-to-image-plane distance, FOV=2·arctan(w/f) trades off with magnification ∝f; divide-by-Z = perspective vs orthographic.
- build --strict PASS; all M3 1.1–2.4 embeds + "You are here" headers resolve.
- Continue per standing production directive: next Installment B = U3 Camera Intrinsics (K) + U4 Projection in Practice (OpenCV intro; midpoint checkpoint after U4). Pause only at unit/module/milestone or for the 5 escalation reasons.

## D-046 — Module 3 Installment B (Units 3 & 4) DELIVERED · Module 3 midpoint reached
- **Unit 3 — Camera Intrinsics** (3.1–3.4, lesson09–12): from metric image coordinates to pixels (f_x = f_m/s_x) · the intrinsic matrix K = [[f_x,0,c_x],[0,f_y,c_y],[0,0,1]] (project = K·(X,Y,Z) then ÷Z; u = f_x·X/Z + c_x) · principal point (≈ center, where the optical axis hits) and focal length in pixels as image scale (calibration finds f_x,f_y,c_x,c_y) · recap. K depends only on the camera, not its pose.
- **Unit 4 — Projection in Practice** (4.1–4.4, lesson13–16): the full pipeline world → (extrinsics T(cam←world), rigid, Module 2) → camera frame → (intrinsics K, ÷Z) → pixel · projecting many points (per-point ÷Z; validity = in front Z>0 AND in frame 0≤u<W,0≤v<H; behind-camera Z≤0 invalid) · **OpenCV introduced** (cv2.projectPoints = our exact pipeline; same K; rvec/tvec ≡ (R,t) via Rodrigues; distCoeffs=0 = ideal pinhole) · recap = **Module 3 midpoint checkpoint** (readiness list).
- **OpenCV is the first new library in Module 3.** Documented in `modules/module03/software_environment_module3.md` (install into venv; opencv-python-headless OK). Notebook policy: NumPy is the asserted ground truth, OpenCV a confirmation inside try/except import cv2, so notebooks execute headless with or without cv2. Verified: cv2 4.13.0 present in sandbox; projectPoints matches the hand-built pipeline.
- Canonical worked example throughout: K f_x=f_y=800, principal point (320,240); point (0.06,-0.03,0.3) → pixel (480,160); any (0,0,Z) → principal point (320,240).
- Built this session: 8 lessons, 8 SVGs (m03-l9..l16; XML-valid, rendered; matrix-K diagram visually verified), 8 notebooks (M03_U03_*, M03_U04_*; execute "All checks passed."), 8 quizzes + 8 answer keys (module03 keys now total 16), the projection-pipeline demo `modules/module03/demos/lesson13_projection_pipeline.html` (sliders world X/Y/Z, camera tx + yaw, focal f; shows camera-frame coords, pixel, and in-frame/out-of-frame/behind-camera badge), and `assessments/module03_midpoint_assessment.md` (Parts A concept / B build-apply / C pipeline+OpenCV + instructor key; placement after Unit 4). Nav subsections for U3 + U4 added.
- build --strict PASS (60 s); all M3 3.1–4.4 embeds + "You are here" headers resolve; lesson13 also carries the demo. No placeholder leaks.
- **Module 3 status: Units 1–4 of 8 complete; midpoint reached** (forward map world→pixel done, runnable, OpenCV-verified). Continue per standing directive: Installment C = U5 Lens Distortion + U6 Back-Projection (pixels→3D). Pause only at unit/module/milestone or for the 5 escalation reasons.

## D-047 — Module 3 Installment C (Units 5–6) delivered
**Date:** 2026-06 · **Status:** Accepted
Module 3 Units 5 (Lens Distortion) and 6 (Back-Projection: Pixels to 3D) complete: lessons 17–24, 8 SVGs (m03-l17..l24), 8 notebooks (M03_U05_*, M03_U06_*), 8 quizzes + 8 answer keys, 1 demo (lesson21 back-projection ray). Strict build PASS. Distortion model (radial k1,k2,k3 + tangential p1,p2, before K) and undistortion (iterative) taught; back-projection (pixel→ray via K⁻¹, depth→point P_c=Z(x_n,y_n,1)) taught, point remains in camera frame pending Unit 7. NumPy in-place aliasing bug in the 5.4 notebook (`xn += ...` mutating an input array) found and fixed to non-in-place copy updates. SVG cosmetic items (barrel/pincushion approximations; flat ray schematics) logged to future_roadmap, not blocking. Next: Installment D — Units 7 (From Pixels to the Robot) and 8 (Mini Project capstone), then Module 3 completion report.

## D-048 — Module 3 Installment D (Units 7–8) delivered; MODULE 3 COMPLETE
**Date:** 2026-06 · **Status:** Accepted
Module 3 Units 7 (From Pixels to the Robot) and 8 (Mini Project: See the Fruit, Place It in the World) complete: lessons 25–32, 8 SVGs (m03-l25..l32), 8 notebooks (M03_U07_*, M03_U08_*, all execute clean), 8 quizzes + 8 answer keys, and the flagship capstone demo lesson29_see_fruit_place_world.html (live P_c/P_w readout + three PASS/FAIL acceptance-check badges + frame-error toggle). Unit 7 connects back-projection to Module 2 extrinsics (T(world←cam)=T(world←arm)·T(arm←cam)); Unit 8 assembles, verifies (re-projection / distance preservation / workspace), and visualizes the full pixel→world pipeline. Canonical capstone result P_w=(1.06,0.47,0.4) reproduced across lessons, notebooks, and demo.

**MODULE 3 COMPLETE.** Totals: 32 lessons / 32 notebooks / 32 SVGs / 32 quizzes / 4 demos / 32 answer keys / midpoint + Unit-8 mini-project capstone. `mkdocs build --strict` passes (101 pages); validator clean; site cleared. Completion report at curriculum/module03_completion_report.md. Module explicitly hands off to Module 4: it assumed T(world←arm); Module 4 (Forward Kinematics, DH parameters) computes it from joint angles.

**Next:** Module 4 — Forward Kinematics using Denavit–Hartenberg Parameters (manifest, topic map, scaffold, lessons, notebooks, quizzes, answer keys, SVGs, demos; wire generator MODULES+="04", titles, nav; numbering restarts module04/lesson01…, m04-l01…, M04_U0Y_*). Kinematics now permitted. Pause at Module 4 completion.

## D-049 — Module 4 launched; Installment A (Units 1–2) delivered
**Date:** 2026-06 · **Status:** Accepted
Module 4 — Forward Kinematics using Denavit–Hartenberg Parameters — opened (its designated module per roadmap D-004; kinematics now permitted). Setup: manifest (curriculum/module04_manifest.md), topic map (modules/module04/topic_map.md, 8 units × 4 lessons = 32), scaffold dirs, generator wired (MODULES += "04", MODULE_TITLES["04"], 8 UNIT_TITLES, manual nav). Numbering restarts: module04/lessonNN, m04-lNN, M04_U0U_*. Educational boundary held: inverse kinematics (M5), Jacobians/velocity (M6), control, trajectory/motion planning (M7) all deferred; M4 is strictly the forward map configuration → pose.

**Installment A — Units 1–2 (lessons 01–08) complete:** 8 lessons, 8 SVGs (m04-l1..l8, XML-valid + rendered), 8 notebooks (M04_U01_*, M04_U02_*, all execute "All checks passed."), 1 demo (lesson05_one_joint_arm.html, JS-validated), 8 quizzes + 8 answer keys. Unit 1 (Why Kinematics): FK maps θ → gripper pose T_0^n ∈ SE(3) = the T(world←arm) Module 3 assumed; serial arm = links + joints; revolute (θ)/prismatic (d); DOF = joint count; configuration (joint space) vs pose (task space), many-to-one. Unit 2 (One Joint at a Time): one-joint planar arm pose T_0^1(θ) = [[c,−s,Lc],[s,c,Ls],[0,0,1]], position (Lcosθ, Lsinθ), orientation θ; joint transform = variable motion (R_z(θ) or Trans_z(d)) ∘ fixed link geometry G; read position (translation column) and orientation (rotation block) off the pose; FK for many joints = product of per-joint transforms. `mkdocs build --strict` passes (109 pages); validator clean; site cleared.

**Next:** Installment B — Units 3 (Chaining Transforms, lessons 09–12) and 4 (The Forward Kinematics Map T_0^n(θ) + midpoint, lessons 13–16). Then C (Units 5–6 DH parameters, lessons 17–24), D (Units 7–8 capstone From Joints to the Fruit, lessons 25–32). Pause at Module 4 completion.

## D-050 — Module 4 Installment B (Units 3–4) delivered; midpoint reached
**Date:** 2026-06 · **Status:** Accepted
Module 4 Installment B — Units 3 (Chaining Transforms, lessons 09–12) and 4 (The Forward Kinematics Map, lessons 13–16, with midpoint) — complete. 8 lessons, 8 SVGs (m04-l9..l16, XML-valid + rendered), 8 notebooks (M04_U03_*, M04_U04_*, all execute "All checks passed." incl. SymPy symbolic FK), 1 demo (lesson09_two_link_arm.html, JS-validated), midpoint assessment (assessments/module04_midpoint_assessment.md) + key, 8 quizzes + 8 answer keys (lessons 09–16).

Unit 3 (Chaining Transforms): second joint lives in the first's moving frame; 2-link gripper position (L1cosθ1+L2cos(θ1+θ2), L1sinθ1+L2sin(θ1+θ2)), orientation θ1+θ2; FK = base→tip matrix product T_0^2 = T_0^1 T_1^2 (Module 2 composition, adds angles, non-commutative); planar closed form = sum of link reaches at accumulated angles φk = Σθ≤k, orientation φn; running example planar 2-/3-link arm (L1=0.4,L2=0.3,(30°,60°)→(0.346,0.5) orient 90°; +L3=0.2,(30°,60°,−30°)→(0.446,0.673) orient 60°). Unit 4 (The FK Map): general SE(3) product T_0^n(θ)=∏T_{i-1}^i; position = translation column, orientation = rotation block (columns = gripper x/y/z axes, one is approach direction); FK in code (build factors → multiply → extract; one function per arm; fresh arrays to avoid aliasing; SymPy symbolic p(θ),R(θ) verified against the planar closed form); midpoint at 4.4.

Nav added (Units 3–4 under "Module 4"); generated (117 pages; M4 3.1–4.4 show [SVG, notebook, quiz], 3.1/lesson09 also demo); `mkdocs build --strict` passes (117 pages); validator clean, no leaks; site cleared.

**Next:** Installment C — Units 5 (Denavit–Hartenberg Parameters, lessons 17–20) and 6 (Building and Using a DH Table, lessons 21–24). Then D (Units 7–8: Pose/Workspace/back-to-perception, lessons 25–28; Mini Project From Joints to the Fruit, lessons 29–32). Pause at Module 4 completion.

## D-051 — Module 4 Installment C (Units 5–6) delivered
**Date:** 2026-06 · **Status:** Accepted
Module 4 Installment C — Units 5 (Denavit–Hartenberg Parameters, lessons 17–20) and 6 (Building and Using a DH Table, lessons 21–24) — complete. 8 lessons, 8 SVGs (m04-l17..l24, XML-valid + rendered), 8 notebooks (M04_U05_*, M04_U06_*, all execute "All checks passed." incl. symbolic DH FK via SymPy), 1 demo (lesson18_dh_parameters.html, interactive four-parameter DH transform explorer, JS-validated), 8 quizzes + 8 answer keys (lessons 17–24).

Unit 5 (DH Parameters): frame placement is a choice → arbitrary frames give inconsistent transforms → the DH convention is a shared standard reducing six free choices to four parameters (not new physics); the four parameters θ (rotate about z), d (slide along z), a (length along x), α (twist about x), with two about the joint axis and two about the link; joint variable = θ (revolute) or d (prismatic); frame-assignment rules (z along joint axis, x along common normal, y right-handed); parallel axes → α=0, intersecting → a=0, perpendicular → α=±90°; the DH table is the robot's kinematic identity. Unit 6 (Building/Using a DH Table): the DH link transform T_{i-1}^i = Rot_z(θ)·Trans_z(d)·Trans_x(a)·Rot_x(α) (four-factor product = expanded closed form; d=0,α=0 → planar transform); reading a robot into a table (procedure; 3-DOF capstone arm table: row1 (θ1,d=0.1,a=0,α=90°), row2 (θ2,0,0.4,0), row3 (θ3,0,0.3,0)); DH FK in code (dh_fk(table,config): fill variable → build per-row transform → multiply → extract; one function any arm; verify in-plane reach vs planar formula; SymPy symbolic DH); recap (table → dh_fk → T_0^n → pose, forward to workspace + perception bridge).

Nav added (Units 5–6 under "Module 4"); generated (125 pages; M4 5.1–6.4 show [SVG, notebook, quiz], 5.2/lesson18 also demo); `mkdocs build --strict` passes (125 pages, clean); validator clean, no leaks; site cleared.

**Next:** Installment D — Units 7 (Pose, Workspace, and Back to Perception, lessons 25–28) and 8 (Mini Project: From Joints to the Fruit, lessons 29–32, flagship capstone demo). Then Module 4 COMPLETION (completion report, totals, pause checkpoint).

## D-052 — Module 4 Installment D (Units 7–8) delivered; MODULE 4 COMPLETE
**Date:** 2026-06 · **Status:** Accepted
Module 4 Installment D — Units 7 (Pose, Workspace, and Back to Perception, lessons 25–28) and 8 (Mini Project: From Joints to the Fruit, lessons 29–32) — complete, and with it **all of Module 4**. 8 lessons, 8 SVGs (m04-l25..l32, XML-valid + rendered), 8 notebooks (M04_U07_*, M04_U08_*, all execute "All checks passed."; lesson 7.1 grasp-readiness assert corrected — a z-rotation leaves the approach axis along base z=(0,0,1), so the desired-approach vector was fixed to (0,0,1); 8.3 runs the five-check verification suite incl. SymPy), 1 flagship capstone demo (lesson29_from_joints_to_fruit.html: side-view 3-DOF arm, sliders θ2/θ3 + fruit r/h, reachable shell, live gripper/fruit/reachability/move-vector; JS-validated), 8 quizzes + 8 answer keys (lessons 25–32).

Unit 7 (Pose, Workspace, Perception): read the end-effector pose (position = translation column, approach axis = ẑ_g = 3rd column of R; grasping compares full poses T_0^n ≈ T_grasp); the reachable workspace (image of FK over joint ranges; planar annulus outer L1+L2 inner |L1−L2|; sample to find; base swivel revolves into a shell; joint limits shrink it); closing the loop with perception (T_0^n with base mount = T(world←arm) that Module 3 assumed; P_base = T_base^cam·P_cam; fruit rel gripper = (T_0^n)⁻¹·P_base; eye-in-hand variant config-dependent); recap. Unit 8 (Capstone "From Joints to the Fruit"): the project (perceive→bridge→FK→report; integrates M2+M3+M4; NOT IK); build the arm's DH model (capstone(cfg,P_cam,T_base_cam,table) via dh_fk + frame bridge → move vector; reachability gate); verify FK (5 independent checks: zero-config, planar reduction vs fk_planar, θ1-sweep revolution, SymPy=numeric, RᵀR=I & det R=1; corrupting α1 caught by diverse checks); wrap-up + forward (evaluate, one answer) vs inverse (solve T_0^n(θ)=T_desired; 0/1/many) → Module 5.

Nav added (Units 7–8 under "Module 4"); generated (133 pages; M4 7.1–8.4 show [SVG, notebook, quiz], 8.1/lesson29 also demo); `mkdocs build --strict` passes (133 pages, clean, 266s); validator clean, no leaks; site cleared.

**MODULE 4 COMPLETE.** 32 lessons / 32 notebooks / 32 SVGs / 4 demos (lesson05, lesson09, lesson18, lesson29) / 32 quizzes / 32 answer keys / midpoint + capstone. Completion report at curriculum/module04_completion_report.md. Educational boundary held: forward kinematics only — inverse kinematics deferred to Module 5, velocity/Jacobians to Module 6, control/planning to Module 7. The forward map T_0^n(θ) = ∏ DH-generated factors is the foundation Module 5 (inverse kinematics) will invert; T_0^n = T(world←arm) closes the loop with Module 3 perception.

**Curriculum totals after Module 4:** 4 of 10 modules complete · 133 lessons · 133 notebooks · 134 SVGs · 26 demos · 133 quizzes · 134 answer keys · 7 assessments.

**Next:** Module 5 — Inverse Kinematics (pending architect launch decision).

## D-053 — Module 5 launch package APPROVED; Installment A (Units 1–2) delivered
**Date:** 2026-06 · **Status:** Accepted
Architect approved the Module 5 (Inverse Kinematics) launch package with all four confirmations: (a) midpoint after Unit 4, (b) Jacobian-as-solver-step boundary — use the Jacobian as a numerical IK tool only, deferring velocity interpretation, differential motion, manipulability, singularity theory, and SVD-based analysis to Module 6, (c) "Reach the Fruit" capstone (Unit 8), (d) the 8-unit topic map. Minor refinement applied: Unit 4 retitled **"From Geometry to Numerical IK"** (was "Why We Need Numerical Methods") across manifest, topic_map, learning_objectives, assessments. No architectural blockers identified.

Generator wired: `MODULES` now `["01","02","03","04","05"]`; `MODULE_TITLES["05"]="Inverse Kinematics"`; all 8 Module 5 `UNIT_TITLES` registered.

**Installment A — Units 1 (The Inverse Problem, lessons 01–04) and 2 (IK of One and Two Joints, lessons 05–08) — complete.** 8 lessons (12-section template + 2 standard components), 8 SVGs (m05-l1..l8, XML-valid + key ones rendered; l6 triangle layout fixed after first render), 8 notebooks (M05_U01_*, M05_U02_*, all execute "All checks passed." — shared fk_two_link/ik_two_link/reachable helpers; boundary-merge tolerance set to 1e-6 so outer/inner-boundary targets correctly return one solution), 1 required demo (lesson07_two_solution_explorer.html — drag/keyboard-accessible target, live elbow-up + elbow-down arms, 2→1→0 transition across the annulus; IK logic JS-validated against the notebook helper and FK-verified), 8 quizzes (byte-identical reference renderer, per-lesson questions JSON) + 8 answer keys (lessons 01–08).

Unit 1 (The Inverse Problem): forward **evaluates** T_0^n(θ); inverse **solves** T_0^n(θ)=T_desired for θ (nonlinear, angles via sin/cos); a target has 0/1/many solutions by location relative to the reachable annulus; the 2-link "many" case is elbow-up/elbow-down; the workspace is the image of FK and a target is solvable iff inside it (planar annulus |L1−L2| ≤ r ≤ L1+L2); reachability is tested first so "unreachable" is a clean answer; recap. Unit 2 (IK of One and Two Joints): one joint by inspection (θ = atan2(y,x), valid only on the radius-L circle, one solution); the planar two-link arm as the base–elbow–target triangle (law of cosines cos θ2 = (r²−L1²−L2²)/(2L1L2); shoulder θ1 = atan2(y,x) − β); elbow-up/elbow-down (θ2 = ±arccos(...), two solutions that merge at the workspace boundary; each elbow sign has its own θ1 because β flips with θ2) — the demo lesson; recap (geometry solved both small arms with no iteration; Unit 3 will write closed-form formulas and add orientation decoupling). Running example: planar 2-link arm L1=0.4, L2=0.3.

Nav added (Units 1–2 under "Module 5 — Inverse Kinematics"); generated (**141 pages**; M5 1.1–2.4 show [SVG, notebook, quiz], 2.3/lesson07 also demo); `mkdocs build --strict` **passes** (141 pages, clean, exit 0); validator clean (no Visual-Explanation page lacks an image, no [Visual:] placeholder leaked); demo + 8 quizzes copied into site/.

Educational boundary held: analytical/geometric IK only in Units 1–2; numerical methods and the Jacobian-as-solver-step begin Unit 4 (Installment B+); velocity/differential-motion/singularity-theory remain Module 6.

**Next:** Installment B — Units 3 (Analytical Closed-Form IK, lessons 09–12) and 4 (From Geometry to Numerical IK + **midpoint**, lessons 13–16). Pausing at this installment milestone for architect review before Installment B.

## D-054 — Module 5 Installment B (Units 3–4) delivered; midpoint assessment in place
**Date:** 2026-06 · **Status:** Accepted
Architect approved Installment A (no revisions; progression FK→Inverse→Reachability→One-Joint→Two-Link→Elbow-up/down endorsed; intuition-first and greenhouse narrative preserved) and re-confirmed all four launch decisions: (a) midpoint after Unit 4, (b) Jacobian-as-numerical-solver-machinery only — defer velocity interpretation, differential motion, manipulability, singularity theory, SVD analysis to Module 6, (c) "Reach the Fruit" capstone, (d) 8-unit structure. Directive: proceed with Installment B (Units 3–4) including the midpoint assessment; maintain standards; pause at the Installment B milestone.

**Installment B — Units 3 (Analytical Closed-Form IK, lessons 09–12) and 4 (From Geometry to Numerical IK, lessons 13–16) — complete, with the module midpoint assessment.** 8 lessons (12-section template + 2 standard components), 8 SVGs (m05-l9..l16, XML-valid; l13 redundant-arm and l14 Jacobian-columns visually verified via cairosvg), 8 notebooks (M05_U03_*, M05_U04_*, all execute "All checks passed." — shared fk_two_link/ik_2link_closed/jacobian_2link/ik_numerical helpers; L4.2 includes a finite-difference Jacobian check; L4.3 the guess–measure–step loop with FK-verified convergence and two-seeds→two-solutions; L4.4 numerical matches analytical), 8 quizzes (reference renderer, titles 3.1–4.4) + 8 answer keys (lessons 09–16). **Midpoint assessment** authored at `assessments/module05_midpoint_assessment.md` (position: after Unit 4; Parts A concept / B build-and-apply / C reasoning; "What ready looks like"; remediation pointers) with a coaches' key at `coaches/answer-keys/module05/midpoint_answer_key.md`.

Unit 3 (Analytical Closed-Form IK): the boxed 2-link closed form — θ₂ = ±arccos((x²+y²−L₁²−L₂²)/(2L₁L₂)), θ₁ = atan2(y,x) − atan2(L₂sinθ₂, L₁+L₂cosθ₂) — returning both solutions with the cos-range as the built-in reachability test; the atan2 tool and quadrant discipline (atan2(y,x) keeps the quadrant from the two signs, arctan loses it and breaks at x=0; behind-the-base targets need it); decoupling position from orientation via a spherical wrist at concept level (wrist center p_w = p_d − d₆ R_d ẑ; arm sets position, wrist sets orientation R₃⁶ = (R₀³)⁻¹R_d) — why closed-form 6-DOF exists; recap (closed form is possible when structure separates into trig-solvable pieces). Unit 4 (From Geometry to Numerical IK): when closed form runs out (general geometry, redundancy → a solution manifold, coupled orientation; planar 3-link family exhibited); the FK Jacobian as the local linear map Δp ≈ J Δθ with an explicit 2×2 form and per-joint-motion columns — **introduced strictly as solver machinery**, with an in-lesson scope note deferring velocity/singularity/manipulability/SVD to Module 6; the guess–measure–step loop (e = p_target − f(θ); Δθ = J⁺e; θ += αΔθ; stop |e|<tol; seed/step-size/tolerance roles); recap + midpoint (analytical and numerical as two halves bridged by the Jacobian; the midpoint confirms the analytical half).

Nav added (Units 3–4 under "Module 5"); generated (**149 pages**; M5 3.1–4.4 show [SVG, notebook, quiz]); `mkdocs build --strict` **passes** (149 pages, clean, exit 0); validator clean (no Visual-Explanation page lacks an image, no [Visual:] placeholder leaked). DoD matrix re-checked across lessons 09–16; all 8 notebooks re-executed clean.

Educational boundary held: the Jacobian appears only as the numerical solver's local linear map; the deferred topics (velocity, differential motion, manipulability, singularity theory, SVD) remain Module 6, flagged explicitly in Lesson 4.2.

**Module 5 status after Installment B:** 16 of 32 lessons · 16 notebooks · 16 SVGs · 1 demo · 16 quizzes · 16 answer keys · 1 midpoint assessment (+ coaches' key).

**Next:** Installment C — Units 5 (Numerical IK in Practice, lessons 17–20; demo 5.1 convergence stepper) and 6 (Singularities & Solution Selection, lessons 21–24; demo 6.1 singularity visualizer). Pausing at the Installment B milestone for architect review.

## D-055 — Module 5 Installment C (Units 5–6) delivered; two demos added
**Date:** 2026-06 · **Status:** Accepted
Architect approved Installments A–B (no revisions; progression Inverse Problem → Reachability → Closed-Form IK → Multiple Solutions → Numerical IK Transition endorsed; midpoint-after-Unit-4 and the Jacobian boundary re-affirmed) and directed Installment C (Units 5–6) including the convergence stepper and singularity visualizer demos; maintain standards; pause at the Installment C milestone. The Jacobian boundary is re-confirmed: Jacobian as numerical-solver machinery only — defer velocity interpretation, differential motion, manipulability, singularity theory, and SVD analysis to Module 6.

**Installment C — Units 5 (Numerical IK in Practice, lessons 17–20) and 6 (Singularities and Solution Selection, lessons 21–24) — complete, with two demos.** 8 lessons (12-section template + 2 standard components), 8 SVGs (m05-l17..l24, XML-valid; l17 convergence, l19 outcomes, l21 singularity-lost-direction visually verified via cairosvg), 8 notebooks (M05_U05_*, M05_U06_*, all execute "All checks passed."), 8 quizzes (reference renderer, titles 5.1–6.4) + 8 answer keys (lessons 17–24), and **2 interactive demos**: `lesson17_convergence_stepper.html` (set target/seed/gain, advance the Newton step one click at a time, live error norm + arm + error-vs-iteration plot; near-singular falls back to damped least squares) and `lesson21_singularity_visualizer.html` (sweep θ₂, live det J = L₁L₂ sin θ₂ with a |det J|-across-θ₂ plot, the lost radial direction vs surviving tangential motion, and a well-conditioned/near-singular/singular badge). Both demos: design-system CSS vars, accessible SVG (role+aria-label), no browser storage; their FK/IK/det-J JS matches the notebook helpers and FK-verifies.

Unit 5 (Numerical IK in Practice): the Newton/pseudoinverse step θ ← θ + αJ⁺e (least-norm move; near-quadratic convergence when well-conditioned); the Jacobian-transpose step αJᵀe (gradient descent — always downhill, stable, slow) and damped least squares Jᵀ(JJᵀ+λ²I)⁻¹e (bounded everywhere; λ blends Newton↔transpose); convergence/step-size/failure handling (stop on |e|<tol + iteration cap; step-size speed/stability trade-off + line search; failure table — unreachable/divergence/singular-stall/wrong-solution/slow-crawl, each with a remedy — and a status return converged/max_iter/diverged); recap (one loop, three choices: step rule, step size, stop/fail). Unit 6 (Singularities and Solution Selection): singularities as **lost directions / rank drop**, recognition only — det J = L₁L₂ sin θ₂ = 0 at θ₂ = 0° (straight) and 180° (folded), the workspace boundaries; an explicit in-lesson scope note defers singular values, manipulability, the lost-subspace geometry, and the velocity meaning to Module 6; joint limits and feasibility filtering (θᵢ ∈ [min,max]; one/both/none feasible; limits shrink the effective workspace); choosing among solutions (nearest-to-current for least motion/smoothness, limit-safe margin, singularity-safe |det J| proxy, combined into a weighted cost); recap (solve → recognize/damp → filter limits → choose → command, a deployable solver).

Nav added (Units 5–6 under "Module 5"); generated (**157 pages**; M5 5.1/lesson17 and 6.1/lesson21 show [SVG, demo, notebook, quiz], others [SVG, notebook, quiz]); `mkdocs build --strict` **passes** (157 pages, clean, exit 0); 3 demos + 24 quizzes copied into site/; validator clean. DoD matrix re-checked across lessons 17–24; all 8 notebooks re-executed clean.

Implementation note (L5.3 status logic): for the bounded 2-link arm the pseudoinverse step cannot run to infinity, so too-large α produces *oscillation* (flagged `diverged` via a reachable-target-whose-error-grows test) while an *unreachable* target *plateaus* (flagged `max_iter`); the lesson and notebook state this explicitly so the failure-mode taxonomy stays honest.

Educational boundary held: the Jacobian remains the numerical solver's local linear map; singularities are recognized but not theorized; the deferred topics (velocity, differential motion, manipulability, singularity theory, SVD) remain Module 6, flagged in Lesson 6.1.

**Module 5 status after Installment C:** 24 of 32 lessons · 24 notebooks · 24 SVGs · 3 demos · 24 quizzes · 24 answer keys · 1 midpoint assessment (+ coaches' key).

**Next:** Installment D — Units 7 (Verifying & Connecting to Perception, lessons 25–28) and 8 (Mini Project "Reach the Fruit," lessons 29–32; flagship demo 8.1), then Module 5 completion. Pausing at the Installment C milestone for architect review.

## D-056 — Module 5 Installment D (Units 7–8) delivered; Module 5 COMPLETE
**Date:** 2026-06 · **Status:** Accepted
Architect approved Installment C and directed Installment D (Units 7–8) including the flagship capstone demo, to run **straight through to Module 5 completion with no further installment reviews** — pausing only at Module 5 completion (or a major architectural conflict, missing prerequisite, significant pedagogical concern, or build failure). Educational emphasis: Unit 7 = Solve → Verify with FK → Accept/Reject; Unit 8 = integrate perception + transforms + forward kinematics + inverse kinematics into one coherent workflow. The Jacobian boundary and singularity-recognition boundary remain re-confirmed (velocity, differential motion, manipulability, singularity theory, SVD → Module 6).

**Installment D — Units 7 (Verifying and Connecting to Perception, lessons 25–28) and 8 (Mini Project "Reach the Fruit," lessons 29–32) — complete, with the flagship capstone demo.** 8 lessons (12-section template + 2 standard components; 8.1 tagged Capstone, 8.4 the module wrap-up), 8 SVGs (m05-l25..l32, XML-valid; l27 pipeline, l28 loop, l29 capstone flow visually verified via cairosvg), 8 notebooks (M05_U07_*, M05_U08_*, all execute "All checks passed."), 8 quizzes (reference renderer, titles 7.1–8.4) + 8 answer keys (lessons 25–32), and the **flagship capstone demo** `lesson29_reach_the_fruit.html` (drag the fruit, set the camera offset and joint limits, and watch the full pipeline run live — base-frame target, candidate configurations, joint-limit filtering with a ghosted rejected arm, FK verification, selection, the arm reaching, or a clear failure message with the status taxonomy and a live pipeline checklist). Demo verified: design-system CSS vars, accessible SVG (role+aria-label), no browser storage; its FK/IK/reach_the_fruit JS mirrors the notebook helpers and returns ok / unreachable / no_feasible correctly with the chosen configuration FK-verified on the target.

Unit 7 (Verifying and Connecting to Perception): FK verification as the **solve → verify → accept/reject** discipline (accept iff ‖p_target − f(θ_c)‖ < tol; FK is exact, cheap, independent, and catches analytical, numerical, and selection errors); turning a perceived fruit's grasp pose into a base-frame IK target (p_base = T_base^cam · p_cam plus an approach orientation; frames, units, and tolerances must align end to end); and closing the loop into one pipeline (perceive → place → reachability gate → solve → filter limits → verify FK → select → configuration, with a clean failure exit at every gate); recap. Unit 8 (Mini Project: Reach the Fruit): the capstone problem statement and integrated flow (8.1, flagship demo) tagging each stage's source module (M2 frames, M3 perception, M4 FK, M5 IK); the solver core (8.2) — analytical closed form first (fast, all solutions), numerical fallback (seeded Newton/DLS) when needed, returning an unverified candidate list; completing the pipeline (8.3) — verify → filter → select with the status taxonomy ok / unreachable / no_solution / verification_failed / no_feasible (one executable θ⋆ with ok, or None with a reason — never silent, never invalid); and the module wrap-up (8.4) consolidating all 8 units and re-flagging the Module 6 handoff (the Jacobian returns as a velocity relationship — differential motion, manipulability, singularity theory, SVD).

Nav added (Units 7–8 under "Module 5"; 8.1/lesson29 marked demo); generated (**165 pages**; M5 8.1/lesson29 shows [SVG, demo, notebook, quiz], 4 demos total — lessons 07/17/21/29); `mkdocs build --strict` **passes** (165 pages, clean, exit 0); 4 demos + 32 quizzes copied into site/; validator clean. Full Module-5 DoD matrix (lessons 01–32) re-checked — all pass; all 32 M5 notebooks re-executed clean.

**Module 5 final totals:** 32 lessons · 32 notebooks · 32 SVGs · 4 demos · 32 quizzes · 32 answer keys · 1 midpoint assessment (+ coaches' key). `mkdocs build --strict` PASS at 165 pages. Educational boundaries held throughout: Jacobian as solver machinery only; singularities recognition-only; velocity/differential-motion/manipulability/singularity-theory/SVD deferred to Module 6; trajectory/planning → Module 7; control → Module 8. Capstone integrates Modules 2–5.

**Module 5 — Inverse Kinematics: COMPLETE.** This is the 5th of 10 modules signed off (after M1 D-036, M2 D-044, M3 D-048, M4 D-052). A Module 5 completion report has been delivered.

**Next:** Module 6 — Differential Kinematics. Not yet started; awaiting the architect's Module 6 launch package. Paused at Module 5 completion for review.

## D-057 — Module 6 launch package APPROVED; Installment A (Units 1–2) delivered
**Date:** 2026-06 · **Status:** Accepted
Architect approved the Module 6 (Jacobians and Differential Motion) launch package: (a) midpoint after Unit 4, (b) the 8-unit topic map (Differential Motion & Twists · Geometric Jacobian · Analytic Jacobian/Representations · Rank/Manipulability/Ellipsoid · Singularity Theory · SVD · Inverse Velocity & Resolved-Rate · Capstone), (c) the Jacobian — used in M5 only as the numerical solver's local linear map (D-054) — is now the subject: velocity interpretation, manipulability, singularity theory, and the SVD all come home here, and the M5 damped-least-squares damping introduced numerically is re-derived from the SVD in Unit 6, (d) the open-loop **velocity layer** is the deliverable Module 7 plans on top of (no path planning or feedback control — those remain M7/M8).

Generator wired: `MODULES` now includes `"06"`; `MODULE_TITLES["06"]="Jacobians and Differential Motion"`; all 8 Module 6 `UNIT_TITLES` registered. (Module 5 generation was also restored to the generator — `"05"` + titles re-registered — after an earlier merge had dropped it, so `mkdocs build --strict` resolves M5's served assets again.)

**Installment A — Units 1 (Differential Motion & Twists, lessons 01–04) and 2 (Geometric Jacobian & Forward Velocity Kinematics, lessons 05–08) — complete.** 8 lessons, 8 SVGs (m06-l1..l8), 8 notebooks, 1 demo (lesson07 Jacobian Column Explorer), 8 quizzes + 8 answer keys. Differential rotation $R \approx I + S(\delta\boldsymbol\theta)$, the twist $\boldsymbol\xi=[\mathbf v;\boldsymbol\omega]$ and its frame transforms; the Jacobian defined by $\boldsymbol\xi = J(\mathbf q)\dot{\mathbf q}$ and built column by column for revolute/prismatic/mixed chains, then validated against finite differences. Revision applied during review: L04 differential-rotation sign error caught by an assert and corrected; L02/L05 minor clarifications.

**Next:** Installment B — Units 3–4 + midpoint.

## D-058 — Module 6 Installment B (Units 3–4) delivered; midpoint assessment in place
**Date:** 2026-06 · **Status:** Accepted
**Installment B — Units 3 (Analytic Jacobian, Frames & Representations, lessons 09–12) and 4 (Rank, Manipulability & the Ellipsoid, lessons 13–16) — complete, with the module midpoint assessment.** 8 lessons, 8 SVGs (m06-l9..l16), 8 notebooks, 8 quizzes + 8 answer keys. The analytic Jacobian as the derivative of a pose representation; the representation map $B(\boldsymbol\phi)$ linking $\boldsymbol\omega$ to angle rates; base- vs tool-frame Jacobians; representation vs kinematic singularities. Then rank/range/null space as what the tool can/cannot/internally do, the manipulability ellipsoid, the Yoshikawa measure $w=\sqrt{\det(JJ^\top)}$, and force/velocity duality $\boldsymbol\tau=J^\top\mathbf F$. **Midpoint assessment** at `assessments/module06_midpoint_assessment.md` (after Unit 4 — the seam between constructing the Jacobian and reading its geometry) with a coaches' key at `coaches/answer-keys/module06/midpoint_answer_key.md`; the midpoint adds an intuition item (D4) on capability buckets.

**Module 6 status after Installment B:** 16 of 32 lessons · 16 notebooks · 16 SVGs · 1 demo · 16 quizzes · 16 answer keys · 1 midpoint assessment (+ key).

**Next:** Installment C — Units 5–6 (Singularity Theory; SVD), two demos.

## D-059 — Module 6 Installment C (Units 5–6) delivered; two demos added
**Date:** 2026-06 · **Status:** Accepted
**Installment C — Units 5 (Singularity Theory, lessons 17–20) and 6 (SVD & Geometry of the Jacobian, lessons 21–24) — complete, with two demos.** 8 lessons, 8 SVGs (m06-l17..l24), 8 notebooks, 8 quizzes + 8 answer keys, and 2 interactive demos: lesson17 Ellipsoid Collapse and lesson21 SVD Bars. Singularity as lost motion (ellipsoid collapse), boundary vs internal singularities and joint-rate blow-up, shoulder/elbow/wrist classification, loci and workspace boundaries — upgrading M5 *recognition* to full theory. Then the SVD $J=U\Sigma V^\top$ as the ellipsoid's anatomy, the condition number, the four fundamental subspaces, and the pseudoinverse and damped least squares derived from the SVD (closing the loop on M5's numerically-introduced DLS). Revision applied: L15 corrected — $w$ computed via $\prod\sigma_i$ (not $\sqrt{\det}$) to avoid a NaN at the singularity, and the worked example replaced with a genuine equal-$w$/different-$\kappa$ case ($\theta_2 = 0.6$ vs $\pi-0.6$: same $w$, $\kappa$ 8.1 vs 1.9).

**Module 6 status after Installment C:** 24 of 32 lessons · 24 notebooks · 24 SVGs · 3 demos · 24 quizzes · 24 answer keys · 1 midpoint assessment (+ key).

**Next:** Installment D — Units 7–8 + capstone, then Module 6 completion.

## D-060 — Module 6 Installment D (Units 7–8) delivered; Module 6 COMPLETE
**Date:** 2026-06 · **Status:** Accepted
**Installment D — Units 7 (Inverse Velocity Kinematics & Resolved-Rate Motion, lessons 25–28) and 8 (Capstone: Analyzer → Resolved-Rate Tracker, lessons 29–32) — complete, with the flagship capstone demo.** 8 lessons, 8 SVGs (m06-l25..l32), 8 notebooks, 8 quizzes + 8 answer keys, and the capstone demo lesson29 Resolved-Rate Tracker. Inverting the velocity map (desired twist → joint rates), redundancy resolution and null-space motion, singularity-robust damped least squares, and the open-loop resolved-rate velocity layer; the four-part capstone builds a manipulability/singularity analyzer, a resolved-rate tracker, scheduled damping with redundancy, and packages the **velocity layer for Module 7**. Revision applied: L30 test command drove the arm to full extension — corrected to an in-workspace command.

Nav added (8 units under "Module 6 — Jacobians and Differential Motion", demos marked on 2.3/5.1/6.1/8.1); generated (**197 lesson pages** across M1–M6); `mkdocs build --strict` **passes** (clean, exit 0); validator clean (every Visual-Explanation page carries an injected figure; no `[Visual:]` placeholder leaked). All 32 M6 quizzes converted to the module05 interactive-HTML format (5 MC + 3 short answer each, answers from the coaches' keys; MathJax added to the quiz template so the LaTeX renders).

**Module 6 final totals:** 32 lessons · 32 notebooks · 32 SVGs · 4 demos · 32 quizzes · 32 answer keys · 1 midpoint assessment (+ key). Educational boundaries held: M6 is the first-order (velocity) relationship and its geometry — no trajectory/path planning (M7), no dynamics/feedback control (M8); resolved-rate motion is open-loop and explicitly handed to M7.

**Module 6 — Jacobians and Differential Motion: COMPLETE.** This is the 6th of 10 modules signed off (after M1 D-036, M2 D-044, M3 D-048, M4 D-052, M5 D-056). A Module 6 completion report has been delivered (`curriculum/module06_completion_report.md`).

**Repo reconciliation (integration):** the Module 6 bundle was unzipped into `curriculum/module06/`; it has been relocated into the canonical layout (lessons/notebooks/demos/quizzes under `modules/module06/`, SVGs renamed to `assets/diagrams/m06-lN-*.svg`, answer keys under `coaches/answer-keys/module06/`, midpoint under `assessments/`, report under `curriculum/`). Lesson headings were normalized to the canonical numbered template (renumbered in place; `[Visual:]` lines backticked). The committed nested duplicate `physical-ai-curriculum/` (a stale pre-M5 snapshot) was removed, and the bundle's loose helper files (`MODULE6_NAV_SNIPPET.yml`, `README_PUSH.md`, `MANIFEST.txt`) were discarded. The three trackers, which the bundle had overwritten with stubs, were restored and then extended with the real Module 6 entries.

**Next:** Module 7 — Trajectory Generation and Motion Planning. Awaiting the architect's launch package.

## D-061 — Module 7 launch package APPROVED
**Date:** 2026-06 · **Status:** Accepted

**Module 7 — Trajectory Generation and Motion Planning — launch package APPROVED.** Module 7 answers "How do I move from here to there smoothly, safely, and efficiently?" — producing the time-parameterized reference trajectory the M6 velocity layer executes open-loop and that M8 will later track with feedback. All §9 architectural rulings accepted as proposed: **§9.1** planning depth = configuration space + collision checking + RRT + path smoothing (no deeper planning theory); **§9.2** joint-space (U3) / Cartesian (U4) balance maintained; **§9.3** SLERP + screw interpolation applied, no in-depth quaternion algebra; **§9.4** strict M7-defines-references / M8-tracks-references boundary; **§9.5** open-loop execution through the M6 velocity layer approved (demonstrate feasibility, never correct error); **§9.6** dynamics excluded (efficiency is a geometric/temporal proxy); **§9.7** demos at L07/L17/L21/L29; **§9.8** static obstacle only.

**Decision-id reconciliation (architect-ruled).** The launch package proposed **D-058**, but D-057–D-060 were already consumed by Module 6's installments (M6 A–D). The architect ruled the authoritative Module 7 mapping: **D-061 = Launch, D-062 = Installment A, continuing sequentially** → **B = D-063, C = D-064, D = D-065**. (An interim draft had bundled Launch+A under a single D-061; this is now split per the architect's ruling.) No content impact.

**Next:** Installment A — Units 1–2 [**D-062**].

## D-062 — Module 7 Installment A (Units 1–2) delivered and APPROVED
**Date:** 2026-06 · **Status:** Accepted

**Installment A — Units 1 (Motion, Paths, and Trajectories, lessons 01–04) and 2 (Time Parameterization and Smoothness, lessons 05–08) — complete, with the flagship demo.** 8 lessons (12-section template + AI Learning Companion + Global Learning Support in 4 languages), 8 SVGs (m07-l1..l8), 8 notebooks (all end "All checks passed." under Restart & Run All), 8 quizzes (5 MC + 3 short, module05 interactive-HTML format with MathJax), 8 answer keys (coaches' format with model answers + grading notes + common misconceptions), and 1 flagship interactive demo: **lesson07 Polynomial Profile Shaper** (toggle cubic↔quintic, drag duration T, live position/velocity/acceleration/jerk panels, accessible, no browser storage).

Unit 1 builds motion literacy: why smooth/safe/efficient motion matters (jerky vs smooth harvest), path q(s) vs trajectory q(t)=q(s(t)), the four quality criteria (smooth/feasible/safe/efficient) with the C⁰/C¹/C² ladder, and the plan → parameterize → execute-open-loop (M6) → track (M8) pipeline with both fences drawn. Unit 2 builds the timing toolkit: q(t)=q(s(t)) and its derivatives via the chain rule (incl. jerk), continuity classes and why C² means no force jumps, **cubic vs quintic** time scaling (the headline result — the cubic leaves a non-zero endpoint acceleration $\pm 6\Delta/T^2$ → only C¹, while the quintic zeros it → C², at the cost of higher mid-move peaks), and trapezoidal (time-optimal, C¹, jerk spikes) vs S-curve (jerk-limited, C²) velocity profiles.

**Key educational achievement:** the cubic→quintic acceleration-jump demonstration (C¹→C²) is shown three independent ways that agree numerically — the flagship demo, the m07-l7 SVG (red cubic endpoints "jump" vs green quintic zeros), and the L07 notebook/engine (cubic endpoint accel = 6·1.2/1.5² = 3.2 rad/s²; quintic = 0).

**Engine.** A reusable Module 7 engine is embedded in each notebook: the **M6 base imported verbatim** (`dh`, `forward_chain`, `geometric_jacobian`, `Jv_planar`, `fk_xy`, `analyze`, `dls`, `velocity_layer`) — the velocity layer is the execution backend, not reimplemented — plus new Unit 1–2 time utilities (`poly_eval`, `cubic_coeffs`, `quintic_coeffs`, `trapezoidal_profile`, `s_curve_profile`). Verified: cubic endpoint acceleration jump vs quintic zero; S-curve peak jerk bounded by j_max and total time ≥ the time-optimal trapezoid.

**Generator + site.** `tools/generate_site_pages.py` extended: `"07"` added to `MODULES`, module title registered, all 8 Unit titles registered (only U1–U2 have lessons so far). Generator run injected each lesson's SVG (after §4), the demo iframe (L07, after §7), the notebook tip (after §8), and the quiz iframe (after §9); the visual-embed validator passed (every Visual-Explanation page carries a figure; no `[Visual:]` placeholder leaked). Nav added to `mkdocs.yml` (Units 1–2 under "Module 7 — Trajectory Generation and Motion Planning", demo marked on 2.3). `mkdocs build --strict` **passes** (clean, exit 0) at **205 lesson pages** (197 M1–M6 + 8 M7).

**Educational boundaries held:** no feedback/closed-loop control and no dynamics anywhere in Installment A; open-loop execution is via the imported M6 velocity layer only, used to demonstrate feasibility. Running example: planar 2-link arm L1=0.4, L2=0.3 (engine is length-agnostic via the DH parameter table).

**Architect decision:** Installment A **APPROVED**. Cited as strong: motion-first framing, path vs trajectory distinction, cubic vs quintic comparison, continuity/jerk treatment, strict M7/M8 boundary; M6 velocity-layer reuse approved. Guidance for Units 3–4: **lead with motion** — students first see the path the robot follows, how different trajectory choices behave, and why Cartesian and joint-space motion differ, before interpolation mathematics.

**Module 7 status after Installment A:** 8 of 32 lessons · 8 notebooks · 8 SVGs · 1 demo · 8 quizzes · 8 answer keys.

**Next:** Installment B — Units 3 (Joint-Space Trajectories) and 4 (Cartesian-Space Trajectories) + the midpoint assessment (after Unit 4) [**D-063**].

## D-063 — Module 7 Installment B (Units 3–4) delivered; midpoint assessment in place
**Date:** 2026-06 · **Status:** Accepted

Architect approved Installment A and directed Installment B — Units 3 (Joint-Space Trajectories) and 4 (Cartesian-Space Trajectories) plus the midpoint assessment — with the guidance to **lead with motion**: students should first see the path the robot follows, how different trajectory choices behave, and why Cartesian and joint-space motion differ, before the interpolation mathematics. Per the launch demo schedule (§9.7: demos at L07/L17/L21/L29), **Installment B ships no new flagship demo**.

**Installment B — Units 3 (Joint-Space Trajectories, lessons 09–12) and 4 (Cartesian-Space Trajectories, lessons 13–16) — complete, with the module midpoint assessment.** 8 lessons (12-section template + AI Learning Companion + Global Learning Support in 4 languages), 8 SVGs (m07-l9..l16, XML-valid; l9 joint-vs-task-space, l13 joint-curve-vs-cartesian-line, l15 SLERP arc visually verified via cairosvg), 8 notebooks (all end "All checks passed." under Restart & Run All), 8 quizzes (5 MC + 3 short, module05 interactive-HTML format with MathJax, no browser storage), 8 answer keys (coaches' format with model answers + grading notes + common misconceptions).

Each lesson **leads with the motion** before the math: Unit 3 — per-joint polynomials with the tool path *shown* curved while the joint path is straight (3.1), synchronization with the slowest-limited joint setting the pace (3.2), via-points with the stop-vs-flow contrast seen first (3.3), and C² cubic-spline blending that flows through the via-points without stopping or jolting (3.4). Unit 4 — *why* Cartesian, with the straight tool path contrasted against the joint move's curve (4.1), straight-line position realized by the interpolate-then-IK loop with branch consistency and per-sample reachability (4.2), orientation by SLERP — shortest-arc, constant-rate, always valid (4.3), and unified position+orientation by screw motion / constant twist (4.4, with the Unit 4 recap). §9.3 honored: SLERP and screw interpolation are applied, with quaternion algebra kept light.

**Midpoint assessment** at `assessments/module07_midpoint_assessment.md` (after Unit 4 — the seam between *generating* trajectories in joint/Cartesian space and the *feasibility and planning* that follow in Units 5–6) with a coaches' key at `coaches/answer-keys/module07/midpoint_answer_key.md`. Sections A–D mirror Units 1–4 (motion literacy; time parameterization; joint-space; Cartesian-space); Section E is integrative (task-appropriate joint-vs-Cartesian choice, a full stow→via→approach design, and an M7/M8-boundary check).

**Engine.** The reusable Module 7 engine (M6 base imported verbatim + Unit 1–2 time utilities) was extended with Unit 3–4 utilities, all verified: closed-form planar 2R IK `ik_2link` (FK round-trip residual ~5e-17); synchronized multi-joint polynomial trajectories `joint_traj`/`sample_joint_traj`/`sync_duration` (e.g. [0,0]→[2,0.5] at vmax=1 gives T*=3.75 s); the C² natural cubic spline `cubic_spline_natural`/`eval_spline` (interpolates knots, continuous second derivative at via-points); straight-line Cartesian position with the IK-per-sample loop `cartesian_line`/`cartesian_traj_ik` (max perpendicular deviation from the straight line = 5e-17, every sample FK-verified, raises on an unreachable path point); orientation `slerp`/`slerp_angle`/`quat_axis_angle` (unit-norm throughout, shortest arc — 170°→−170° gives a +20° turn); and SE(2) screw interpolation `se2`/`screw_interp_se2` (endpoints exact, constant twist).

**Generator + site.** Generator auto-discovered L09–L16 and injected each lesson's SVG (after §4), the notebook tip (after §8), and the quiz iframe (after §9); the visual-embed validator passed (every Visual-Explanation page carries an injected figure; no `[Visual:]` placeholder leaked; the Diagram Specification is stripped from student pages). Nav added to `mkdocs.yml` (Units 3–4 under "Module 7 — Trajectory Generation and Motion Planning"; no demo markers on L09–L16). `mkdocs build --strict` **passes** (clean, exit 0) at **213 lesson pages** (205 + 8).

**Educational boundaries held:** no feedback/closed-loop control and no dynamics anywhere in Installment B; the trajectory is an open-loop **reference** that the imported M6 velocity layer executes (the midpoint E3 item explicitly tests this boundary — "correcting the arm back onto the path" is Module 8, not Module 7). Running example: planar 2-link arm L1=0.4, L2=0.3.

**Module 7 status after Installment B:** 16 of 32 lessons · 16 notebooks · 16 SVGs · 1 demo · 16 quizzes · 16 answer keys · 1 midpoint assessment (+ coaches' key). **Paused at the Installment B milestone for architect review.**

**Next:** Installment C — Units 5 (Feasibility: Velocity, Acceleration, and Limits) and 6 (Motion Planning and Collision Awareness), with the demos at L17 and L21 [**D-064**].

**Architect review — Module 7 midpoint assessment: APPROVED (no revisions required).** Rated quality Strong, coverage Appropriate, educational balance Excellent; cited as particularly strong: path vs trajectory, continuity/smoothness, joint-space vs Cartesian-space tradeoffs, IK branch consistency, and the explicit M7/M8 boundary checks — confirming the assessment evaluates motion-planning *literacy* rather than memorization. **Optional future enhancement (logged, not yet applied):** allow **"hybrid" trajectory choices** to appear in motion-selection discussions — i.e., beyond a binary joint-vs-Cartesian pick, recognize blended moves (e.g., a joint move for the gross repositioning handed off to a Cartesian straight-line final approach; or a path that is Cartesian near the endpoints and joint-space through the middle for efficiency). To be woven into the Installment C feasibility/planning motion-selection framing and, in a later pass, the midpoint's Section E1 (the approved midpoint is left unchanged for now). **Status remains: paused at the Installment B milestone as planned** — Installment C (Units 5–6, D-064) awaits the architect's go-ahead.

## D-064 — Module 7 Installment C (Units 5–6) delivered; 2 demos
**Date:** 2026-06 · **Status:** Accepted

Architect approved Installment B (and its midpoint) and directed Installment C — Units 5 (Feasibility: Velocity, Acceleration, and Limits) and 6 (Motion Planning and Collision Awareness) — with the demos L17 (Velocity & Acceleration Limit Explorer) and L21 (Configuration Space & Obstacle Visualizer). Guidance: **lead with physical feasibility** — why a trajectory may be impossible, why limits matter, why slowing down solves a problem, why obstacles create forbidden regions — before formal planning; present **configuration space as a way to understand motion constraints**, not abstract math; keep planning **practical and intuitive**; reach the objective **Obstacle → Constraint → Safe Path → Feasible Trajectory** before algorithm details. Boundary reminder: no advanced planning theory, no optimization planning, no kinodynamic planning, no feedback, no dynamics.

**Installment C — Units 5 (Feasibility, lessons 17–20) and 6 (Motion Planning, lessons 21–24) — complete, with 2 flagship demos.** 8 lessons (12-section template + AI Learning Companion + Global Learning Support in 4 languages), 8 SVGs (m07-l17..l24, XML-valid; l17 limit bars, l21 workspace‖C-space, l23 RRT tree visually verified via cairosvg), 8 notebooks (all end "All checks passed." under Restart & Run All), 8 quizzes (5 MC + 3 short, interactive-HTML with MathJax, no browser storage), 8 answer keys (coaches' format).

**Unit 5 leads with physical feasibility** exactly as directed: 5.1 *why* a smooth, goal-reaching trajectory can still be impossible (velocity/acceleration limits; peaks scale 1/T, 1/T²) with the **Limit Explorer** demo; 5.2 *slowing down* via uniform time scaling (path unchanged, peaks ÷k and ÷k²) as the universal fix; 5.3 the *fastest feasible* timing (trapezoidal/triangular, saturating limits) — explicitly distinguished from formal time-optimal optimization; 5.4 the *whole-trajectory* check (joint limits, velocity, acceleration, reachability at every point) with the **timing-fixable vs geometric** triage. **Unit 6 builds planning intuitively** toward the objective chain: 6.1 obstacles → forbidden regions / **configuration space** (robot = point, obstacle = region; presented as a way to *see* constraints, not abstract math) with the **C-space Visualizer** demo; 6.2 collision checking (link-geometry test + dense path sampling + tunneling); 6.3 finding a safe path with **RRT** (sample/nearest/steer/check/connect — basic RRT only); 6.4 **safe path → feasible trajectory** via shortcut smoothing + time scaling, completing **Obstacle → Constraint → Safe Path → Feasible Trajectory**.

**Demos.** L17 `lesson17_limit_explorer.html` (drag duration & displacement; peak-speed/acceleration bars against limit lines; turns red and reports the binding limit when crossed) and L21 `lesson21_cspace_visualizer.html` (drag the disk obstacle and watch the forbidden region redraw in the (q1,q2) C-space; drag the configuration point and watch the arm move and the point redden inside the C-obstacle). Both self-contained, accessible (role/aria-label/aria-live, keyboard, focus styles), no browser storage. This brings Module 7 to **3 demos** (L07, L17, L21).

**Engine.** Extended with verified Unit 5–6 utilities: `quintic_peaks` (peak |v|=15|Δq|/8T, |a|=(10/√3)|Δq|/T²), `is_feasible`/`feasible_duration` (min common feasible duration), `uniform_time_scale_factors` (1/k, 1/k²), `arm_points2`/`arm_hits_disk` (link-segment vs disk), `cspace_grid` (C-obstacle occupancy), `edge_collision_free`/`path_collision_free` (dense sampling), `rrt` (basic sampling-based planner), `shortcut_smooth`/`path_length`. Canonical Unit-6 scenario locked (disk center (0.5,0.05), r=0.06; start tool (0.45,0.25) → goal (0.45,−0.25), both elbow-up): direct C-space edge blocked, RRT solves 5/5 across seeds, smoothing shortens the path while keeping it collision-free.

**Generator + site.** Generator auto-discovered L17–L24 and injected each SVG (after §4), the **demo iframe** (after §7) for L17 and L21, the notebook tip (after §8), and the quiz (after §9); the validator passed (every Visual-Explanation page carries an injected figure; no `[Visual:]` leak; Diagram Specification stripped from student pages). Nav added to `mkdocs.yml` (Units 5–6, with "· demo" markers on 5.1 and 6.1). `mkdocs build --strict` **passes** (clean, exit 0) at **221 lesson pages** (213 + 8).

**Boundaries held:** no advanced/optimization/kinodynamic planning (basic RRT only; the plan-then-time decoupling is stated explicitly), no feedback, no dynamics (acceleration limits treated as given numbers, not derived from torque/inertia). The trajectory remains an open-loop **reference** the M6 velocity layer executes. Running example: planar 2-link arm L1=0.4, L2=0.3.

**Module 7 status after Installment C:** 24 of 32 lessons · 24 notebooks · 24 SVGs · **3 demos** · 24 quizzes · 24 answer keys · 1 midpoint assessment (+ coaches' key). **Paused at the Installment C milestone for architect review.**

**Next:** Installment D — Units 7 (Trajectory Quality, Validation, and Tracking Prerequisites) and 8 (Capstone: Plan → Parameterize → Validate → Execute), completing Module 7 [**D-065**].

## D-065 — Module 7 Installment D (Units 7–8, capstone) delivered; MODULE 7 COMPLETE
**Date:** 2026-06 · **Status:** Accepted

Architect approved Installment C and directed the final installment — Unit 7 (Trajectory Quality, Validation, and Tracking Prerequisites) and Unit 8 (Capstone: Plan → Parameterize → Validate → Execute), including the **L29 flagship Trajectory Studio demo**. Guidance: the capstone emphasizes **Plan ↓ Parameterize ↓ Validate ↓ Execute** as a complete motion-planning workflow; the final artifact clearly becomes the **reference trajectory layer consumed by Module 8**; maintain strict boundaries — **no feedback control, no dynamics, no actuator control** (all Module 8). **Pause at Module 7 completion; no further installment reviews within this module.**

**Installment D — Units 7 (lessons 25–28) and 8 (capstone, lessons 29–32) — complete, with the L29 flagship demo.** 8 lessons (12-section template + AI Learning Companion + Global Learning Support in 4 languages), 8 SVGs (m07-l25..l32, XML-valid; l29 workflow, l31 reference-layer handoff, l32 harvest cycle visually verified via cairosvg), 8 notebooks (all end "All checks passed." under Restart & Run All), 8 quizzes (5 MC + 3 short, MathJax, no browser storage), 8 answer keys.

**Unit 7 (Quality, Validation, Tracking Prerequisites).** 7.1 quality metrics rank feasible trajectories (duration, peak speed/acceleration, **jerk**, path length — geometric/temporal, never energy/dynamics). 7.2 the **complete validation suite** as one aggregated pass/fail gate (endpoints, rest, continuity, velocity, acceleration, collision-free, reachable) between planning and execution. 7.3 **tracking prerequisites** and the explicit **Module 7/Module 8 boundary** — the reference must provide q_d, q̇_d, q̈_d (feed-forward), continuous and feasible; Module 7 produces the reference, Module 8 tracks it; no error/torque/gain/motor command here. 7.4 **discretizing/representing** the reference at the control rate (time-axis tunneling if too coarse) and the reference data structure handed to execution.

**Unit 8 (Capstone: Plan → Parameterize → Validate → Execute).** 8.1 the complete **four-stage workflow** with the **Trajectory Studio** demo (each stage = an earlier unit; Execute = open-loop reference handoff). 8.2 **plan-then-time** in depth (PLAN = RRT + smoothing; PARAMETERIZE = time-scale to limits; decoupled, not kinodynamic). 8.3 **validate and hand off** — VALIDATE gates the handoff, then package the **reference trajectory layer** exposing `reference(t) → (q_d, q̇_d, q̈_d, info)` + metadata, the M8 handoff **bookending M6's velocity_layer**. 8.4 the **greenhouse harvest cycle** end-to-end (reach → grasp → retreat, each leg the full workflow, chained at rest), the **Module 7 recap** (8 units), and the **bridge to Module 8**.

**Trajectory Studio demo** (`lesson29_trajectory_studio.html`): drag the obstacle / start / goal on the greenhouse arm, then run the pipeline stage-by-stage — **Plan** draws the RRT route, **Parameterize** times it against the limit lines, **Validate** runs the checklist (green/red per check), **Execute** plays the validated reference and displays the reference signal (q̇_d, q̈_d) that hands off to Module 8. Self-contained, accessible (role/aria-label/aria-live, keyboard, focus), no browser storage; carries an explicit "Module 7 produces the reference; no feedback control" note. This brings Module 7 to **4 demos** (L07, L17, L21, L29).

**Engine.** Extended with verified Unit 7–8 utilities: `piecewise_quintic` (rest-to-rest C² segments → ref_fn), `sample_reference` (discretize at the control rate), `trajectory_metrics` (duration/peak speed/accel/jerk/Cartesian length), `validate_trajectory` (7-check suite + overall valid), `plan_parameterize` (PLAN+PARAMETERIZE), and the capstone **`reference_trajectory_layer`** (PLAN→PARAMETERIZE→VALIDATE → a validated `reference(t)→(q_d,q̇_d,q̈_d,info)` + metadata). Verified end-to-end on the canonical scenario (validated=True, all 7 checks pass, duration≈2.35 s, peak accel = the binding limit; the reference returns the feed-forward triple). This is the M8 handoff, the bookend to M6's velocity_layer.

**Generator + site.** Generator auto-discovered L25–L32 and injected each SVG (after §4), the **Trajectory Studio demo iframe** (after §7) for L29, the notebook tip (after §8), and the quiz (after §9); validator passed (no `[Visual:]` leak; Diagram Specification stripped). Nav added to `mkdocs.yml` (Units 7–8, "· demo" marker on 8.1). `mkdocs build --strict` **passes** (clean, exit 0) at **229 lesson pages** (221 + 8); all 4 demos copied into `site_src/demos/module07/`.

**Boundaries held throughout:** **no feedback control, no dynamics, no actuator control** — acceleration limits are given numbers, "Execute" is open-loop reference playback/handoff, and the reference layer is explicitly the *input* to Module 8's controller, not a controller. Running example: planar 2-link arm L1=0.4, L2=0.3.

**MODULE 7 COMPLETE.** Totals: **8 units · 32 lessons · 32 notebooks · 32 SVGs · 4 demos (L07, L17, L21, L29) · 32 quizzes · 33 answer keys (incl. midpoint) · 1 midpoint assessment.** `mkdocs build --strict` green at 229 pages. The module's arc: from "what is a trajectory?" to a validated **reference trajectory layer** for a complete task. **Paused at Module 7 completion — no further installment reviews within this module.**

**Next:** Module 8 — Feedback Control, which builds the tracker that consumes the reference trajectory layer produced here, adding closed-loop control, dynamics, and actuator control.

### D-065 addendum — capstone workflow framing
Per the architect's refined guidance, the Unit 8 capstone foregrounds the complete robotics workflow as the **artifact chain Goal → Path → Trajectory → Validation → Execution**, produced by the four **actions Plan → Parameterize → Validate → Execute**. Both framings are one pipeline (boxes = artifacts, arrows = actions); the artifact chain begins explicitly from the **Goal**. L29 (lesson + the m07-l29 diagram) now leads with Goal → Path → Trajectory → Validation → Execution, and the L32 recap names it as the assembly of the eight units. No engine/notebook/quiz changes were needed (all were already consistent with both framings); `mkdocs build --strict` re-verified green at 229 pages. Boundaries unchanged: Execution = open-loop reference handoff; feedback control, dynamics, and actuator control remain Module 8.
