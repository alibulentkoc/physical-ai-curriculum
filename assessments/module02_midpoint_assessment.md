---
title: Module 2 — Midpoint Assessment (Readiness Checkpoint)
position: After Unit 5 (Transformation Composition)
covers: [Unit 1 why transformations, Unit 2 homogeneous coordinates, Unit 3 SE(2), Unit 4 SE(3), Unit 5 composition]
excludes: [robot pose representation, camera extrinsics, the mini project]
format: formative readiness checkpoint; unlimited attempts; not graded
---

# Module 2 — Midpoint Assessment (Readiness Checkpoint)

**Placement:** after Unit 5. Composition is the conceptual heart of the module, so this checkpoint confirms a student can *build, apply, compose, and invert* rigid transforms before moving on to pose, camera extrinsics, and the mini project. It is formative — a readiness signal, not a grade.

**The readiness signal:** can the student carry a point between frames through a *composed chain* of SE(2)/SE(3) transforms, in the correct order, and reverse it with inverses? If yes, they are ready for Units 6–8.

---

## Part A — Concept checks (short answer)

1. Why did Module 1's $2\times2$ matrices fail to represent a frame change, and what does the homogeneous "1" fix?
2. State, in one sentence each, what it means for a transformation to be **rigid** and why robot motion is rigid.
3. Read off an SE(3) matrix: where is the orientation, where is the position, and what is the bottom row?
4. Explain why $T_2 T_1 \neq T_1 T_2$ in general, with a one-line physical example.
5. Given camera→arm and arm→world transforms, write the camera→world transform and its inverse (world→camera).

## Part B — Build and apply

6. Write the SE(2) matrix for a robot at position $(2, 1)$ heading $90°$.
7. Apply it to the point $(1, 0)$; show the result is a rigid move (state one distance preserved).
8. Write the SE(3) matrix for a gripper at $(0.4, 0.3, 0.9)$ with no rotation; then describe what changes if it is rolled $90°$ about $z$.
9. For a 3D point $(x,y,z,1)$ and a direction $(x,y,z,0)$ under the same SE(3): which one picks up the translation, and why?

## Part C — Compose and invert

10. $T_1$ rotates $90°$; $T_2$ translates $(2,0)$. Compute "apply $T_1$ then $T_2$" to $(1,0)$ two ways — step by step, and as the product $T_2 T_1$ — and confirm they match.
11. For the same $T_1, T_2$, show "apply $T_2$ then $T_1$" gives a *different* point, and say which part of the product matrix differs.
12. Given a camera→arm→world chain, the robot needs a world-frame goal expressed in the camera frame. Write the transform that does this in terms of the two edges and their inverses, and state which edge is undone first.

## Part D — Reasoning (short answer)

13. A robot's arm reaches confidently to empty air near a detected tomato. Name two transform-handling errors (from this module) that could cause this, and how you would check each.
14. Two different paths in the frame graph both claim to give camera→world but disagree. What does that tell you about the data?

---

## Readiness rubric (for coaches)

- **Ready:** correctly builds SE(2)/SE(3) from pose numbers; applies them and recognizes rigidity; composes in the right order; uses inverses to reverse a path; explains non-commutativity.
- **Needs review — homogeneous coordinates / rigidity:** shaky on why the extra coordinate enables translation, or on points vs directions → revisit Units 2–3.
- **Needs review — composition:** builds single transforms but mis-orders products or mishandles inverses → revisit Unit 5 (the heart of the module) before Units 6–8.

Full solutions: `coaches/answer-keys/module02/midpoint_assessment_key.md`.
