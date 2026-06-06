---
title: Module 2 — Assessment Plan
module: 02
status: proposed
---

# Module 2 — Assessment Plan

Assessment continues Module 1's model: **formative and low-stakes**, oriented to readiness rather than grading. Three layers — per-lesson checks, per-unit recaps, and module-level checkpoints — plus the integrative mini project.

## 1. Per-lesson knowledge checks (formative)

- One interactive quiz per lesson (`modules/module02/quizzes/lessonNN_quiz.html`): MC / TF / match / short, unlimited attempts, immediate feedback, does not affect any grade.
- One answer key per lesson in `coaches/answer-keys/module02/` (kept out of learner folders), with a short rubric for the short-answer and challenge items.
- Emphasis on *conceptual* signals: can the student explain why translation needs homogeneous coordinates; why a pose is one object; why inverses reverse a frame.

## 2. Per-unit recaps

- Each unit ends with a short synthesis lesson + recap quiz (mirrors Module 1's 2.10 / 3.8 / 4.9), consolidating before the next unit.

## 3. Module 2 checkpoints

- **Midpoint checkpoint** (after Unit 4, SE(3)): a readiness check that the student can build and apply SE(2)/SE(3) transforms and inverses — analogous to Module 1's midpoint assessment. Stored in `assessments/module02_midpoint_assessment.md` with a coaches' key.
- **Module 2 completion assessment:** centered on the Unit 8 mini project (below) plus a short mixed review across homogeneous coordinates, SE(2)/SE(3), composition, inverses, and pose.

## 4. Mini project (Unit 8) — the centerpiece

**Perception-to-Pose Pipeline (no kinematics).** Given:
- a detected tomato expressed in the **camera frame**,
- the camera's **pose on the robot** (extrinsics, an SE(3) transform),
- the robot's **pose in the world** (an SE(3) transform),

the student composes the transform chain to produce the tomato's **world pose**, and verifies it. Deliverables:
- a notebook that builds the chain, applies it, and passes assert-based checks ("All checks passed.");
- a short written explanation of the chain and the role of each transform;
- (provided) an interactive demo to visualize the chain.

Assessed on: correct composition order, correct use of inverses where needed, and a clear explanation of *why* each transform appears — not on coding polish.

## 5. Readiness signals (what "ready for kinematics" looks like)

- Can move a point/pose between frames using SE(3) transforms and their inverses, in the right order.
- Can represent and update a robot pose.
- Can explain the camera→robot→world chain as composed rigid transforms.
- Understands what is still missing (joint kinematics, camera intrinsics) and where it comes next.

## 6. Usage policy (inherited from Module 1)

Assessments are placed in the curriculum as **readiness checkpoints**. Whether any becomes required, graded, optional, or self-assessment is a downstream instructor decision; production does not block on completion.

## Open questions for the architect

1. Confirm the **midpoint checkpoint after Unit 4** (SE(3)) placement, or prefer it after Unit 5 (composition)?
2. Confirm the **mini project as the module assessment centerpiece** (perception-to-pose, no kinematics).
3. Any desired **rubric weighting** (Module 1 used Coding 40 / Knowledge 25 / Challenge 15 / Mini Project 20) — keep, or adjust for a transforms-heavy module?
