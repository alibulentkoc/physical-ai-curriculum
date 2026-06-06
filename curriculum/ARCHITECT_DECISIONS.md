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
