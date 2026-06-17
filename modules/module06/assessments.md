---
title: Module 6 — Assessment Plan
module: 06
status: complete
---

# Module 6 — Assessment Plan

Assessment continues the established model: **formative and low-stakes**, oriented to readiness rather than grading. Three layers — per-lesson checks, per-unit recaps, and module-level checkpoints — plus the integrative capstone.

## 1. Per-lesson knowledge checks (formative)

- One interactive quiz per lesson (`modules/module06/quizzes/lessonNN_quiz.html`): five multiple-choice plus three short-answer items, unlimited attempts, immediate feedback, does not affect any grade.
- One answer key per lesson in `coaches/answer-keys/module06/` (kept out of learner folders), with the correct options, short-answer model responses, and grading notes.
- Emphasis on the signals that matter for differential kinematics: can the student *build and validate* a Jacobian; *read* the manipulability ellipsoid and condition number; *recognize and classify* a singularity; and *invert* the velocity map robustly near one.

## 2. Per-unit recaps

- Each unit consolidates before the next. Unit boundaries follow the build: motion/twists → Jacobian → geometry → inversion → capstone.

## 3. Module 6 checkpoints

- **Midpoint checkpoint** (after Unit 4, "Rank, Manipulability & the Ellipsoid"): a readiness check that the student can (a) build and numerically validate the geometric Jacobian, (b) distinguish geometric/analytic/representation Jacobians, and (c) interpret rank, null space, and the manipulability ellipsoid. Stored in `assessments/module06_midpoint_assessment.md` with a coaches' key (`coaches/answer-keys/module06/midpoint_answer_key.md`). **Placement rationale:** Unit 4 is the seam between *constructing* the Jacobian (Units 1–3) and *reading its geometry / inverting it* (Units 5–8).
- **Module 6 completion assessment:** centered on the Unit 8 capstone (below) plus a short mixed review across twists, Jacobian construction, manipulability, singularity classification, the SVD, and resolved-rate inversion.

## 4. Capstone (Unit 8) — the centerpiece

**The Velocity Layer.** Built in four parts: (I) a **manipulability & singularity analyzer** that reports $w$, the condition number, and singular directions for a configuration; (II) a **resolved-rate tracker** that drives the tool along a commanded twist; (III) an **integration** step adding scheduled damping and redundancy resolution for robustness near singularities; and (IV) packaging the result as the **velocity layer** Module 7 plans on top of. Deliverables: notebooks that pass assert-based checks ("All checks passed."), and a short written explanation of how damping was scheduled and how redundancy was used.

Assessed on: correct Jacobian construction and validation, correct geometric reading (ellipsoid/SVD/condition number), sound singularity handling (damped least squares), and a working, documented velocity layer — not on coding polish.

## 5. Readiness signals (what "ready for trajectory generation" looks like)

- Can build, validate, and frame-convert a Jacobian for a given arm.
- Can read what the arm can/cannot do from rank, null space, the ellipsoid, and the SVD.
- Can recognize, classify, and robustly handle singularities (DLS), and explain joint-rate blow-up.
- Can map a desired twist to joint rates, resolve redundancy, and run resolved-rate motion.
- Understands what is still missing (path/trajectory planning, dynamics and control) and where it comes next.

## 6. Usage policy (inherited from prior modules)

Assessments are placed in the curriculum as **readiness checkpoints**. Whether any becomes required, graded, optional, or self-assessment is a downstream instructor decision; production does not block on completion.
