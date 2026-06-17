---
title: Module 5 — Assessment Plan
module: 05
status: proposed
---

# Module 5 — Assessment Plan

Assessment continues the established model: **formative and low-stakes**, oriented to readiness rather than grading. Three layers — per-lesson checks, per-unit recaps, and module-level checkpoints — plus the integrative mini project.

## 1. Per-lesson knowledge checks (formative)

- One interactive quiz per lesson (`modules/module05/quizzes/lessonNN_quiz.html`): MC / TF / match / short, unlimited attempts, immediate feedback, does not affect any grade.
- One answer key per lesson in `coaches/answer-keys/module05/` (kept out of learner folders), with a short rubric for the short-answer and challenge items.
- Emphasis on the signals that matter for IK: can the student explain *why* a target has two solutions; *when* closed form applies vs when iteration is needed; *what* a singularity looks like; and *why* every solution must be verified by forward kinematics.

## 2. Per-unit recaps

- Each unit ends with a short synthesis lesson + recap quiz (mirrors Modules 1–4), consolidating before the next unit.

## 3. Module 5 checkpoints

- **Midpoint checkpoint** (after Unit 4, "From Geometry to Numerical IK"): a readiness check that the student can (a) state the inverse problem and its multiplicity, (b) solve the planar 2-link arm in closed form producing both solutions, and (c) explain why a general arm needs a numerical method and what the FK Jacobian provides. Stored in `assessments/module05_midpoint_assessment.md` with a coaches' key. **Placement rationale:** Unit 4 is the natural seam — analytical IK is complete (Units 1–3) and numerical IK is about to begin (Units 5–6), so the midpoint confirms the closed-form half before the iterative half, exactly as M3/M4 placed their midpoints at the forward/whole-pipeline seam.
- **Module 5 completion assessment:** centered on the Unit 8 mini project (below) plus a short mixed review across reachability, the 2-link closed form, the numerical solver, singularity recognition, solution selection, and verification.

## 4. Mini project (Unit 8) — the centerpiece

**Reach the Fruit.** Given:
- a perceived fruit's **grasp pose** expressed in the arm's base frame (the output of the Module 3 → Module 4 bridge),
- the arm's **DH model** (the 3-DOF capstone arm from Module 4),
- joint **limits**,

the student computes a joint configuration that places the gripper on the fruit, and verifies it. Deliverables:
- a notebook that **solves** the IK (analytically for the planar reach where possible; numerically for the full target), **enumerates** the solutions, **selects** a feasible one (joint limits, nearest to a given current pose), handles the **no-solution / unreachable** case gracefully, and **verifies** the chosen $\boldsymbol\theta$ by evaluating the Module 4 forward map ($T_0^n(\boldsymbol\theta) \approx T_{\text{desired}}$) — passing assert-based checks ("All checks passed.");
- a short written explanation of which method was used and why, and what each solution means physically (elbow-up/down);
- (provided) an interactive demo to visualize the solver landing the gripper on the target.

Assessed on: correct reachability reasoning, correct solutions (and *both* where they exist), sound solution selection, explicit handling of the unreachable case, and verification against FK — not on coding polish.

## 5. Readiness signals (what "ready for differential motion" looks like)

- Can decide reachability and explain solution multiplicity for a given target.
- Can solve the planar 2-link arm in closed form, producing both solutions, and pick the right one.
- Can run and debug a numerical IK solver on a general arm, and recognize when it is near a singularity.
- Can verify any solution with forward kinematics, and connect a perceived grasp pose to an executable configuration.
- Understands what is still missing (velocities/Jacobian theory, path planning, control) and where it comes next.

## 6. Usage policy (inherited from prior modules)

Assessments are placed in the curriculum as **readiness checkpoints**. Whether any becomes required, graded, optional, or self-assessment is a downstream instructor decision; production does not block on completion.

## Open questions for the architect

1. Confirm the **midpoint checkpoint after Unit 4** placement (analytical/numerical seam), or prefer after Unit 5 (once one numerical method is in hand)?
2. Confirm the **capstone concept** ("Reach the Fruit": target grasp pose → chosen, verified configuration; analytical + numerical; multiplicity + no-solution handling).
3. Confirm the **Jacobian boundary** — introduced in Module 5 only as the local linear solver step, with full velocity/differential-motion and singularity theory reserved for Module 6.
4. Any desired **rubric weighting** for an IK-heavy module (prior modules used Coding 40 / Knowledge 25 / Challenge 15 / Mini Project 20) — keep or adjust?
