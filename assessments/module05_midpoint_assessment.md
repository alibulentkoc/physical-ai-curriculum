---
title: Module 5 — Midpoint Assessment (Readiness Checkpoint)
position: After Unit 4 (From Geometry to Numerical IK)
covers: [Unit 1 the inverse problem and reachability, Unit 2 one- and two-joint IK, Unit 3 closed-form 2-link + atan2 + decoupling, Unit 4 closed form runs out + FK Jacobian + the iteration idea]
excludes: [numerical solver variants (transpose, damped least squares), singularity recognition, solution selection, perception bridge, the mini project]
format: formative readiness checkpoint; unlimited attempts; not graded
---

# Module 5 — Midpoint Assessment (Readiness Checkpoint)

**Placement:** after Unit 4. The first half of Module 5 frames the inverse problem and solves it **analytically** — the inverse equation and reachability (Unit 1), one- and two-joint arms by geometry (Unit 2), the closed-form 2-link solution with `atan2` discipline and the decoupling idea (Unit 3) — then crosses the seam to **numerical** methods, introducing the FK Jacobian as a local linear map and the guess–measure–step loop (Unit 4). This checkpoint confirms a student owns the analytical half and understands *why* and *where* numerical methods take over, before Unit 5 makes the solver robust. It is formative — a readiness signal, not a grade.

**The readiness signal:** given a planar 2-link arm and a target, can the student decide reachability, solve the closed form producing **both** solutions, verify them by forward kinematics, and explain why a general arm needs iteration and what the Jacobian provides? If yes, they are ready for Units 5–8.

---

## Part A — Concept checks (short answer)

1. State the inverse-kinematics problem as an equation. How does it differ from *evaluating* forward kinematics?
2. Why is the inverse problem nonlinear? Name the three solution cases and the geometric condition for each (for the planar 2-link arm).
3. Define the reachable workspace. Why is a reachability check done *before* solving?
4. Explain why `atan2(y, x)` is used throughout analytical IK instead of `arctan(y/x)`. Give one target where they disagree.
5. What does "decoupling position and orientation" mean, and what arm feature makes it possible?

## Part B — Build and apply

Use $L_1 = 0.4,\ L_2 = 0.3$ throughout.

6. Is the target $(0.6, 0.0)$ reachable? Show the reasoning (compute $r$ and compare to the annulus bounds).
7. Solve the closed-form inverse kinematics for $(0.6, 0.0)$. Give **both** $(\theta_1, \theta_2)$ solutions in degrees.
8. Verify **one** of your Q7 solutions by forward kinematics — show the gripper lands on $(0.6, 0.0)$.
9. Classify the number of solutions for $(0.7, 0.0)$, $(0.3, 0.0)$ via the inner radius, and $(0.9, 0.0)$. Explain each.
10. Write (symbolically) the $2\times2$ Jacobian of the planar 2-link arm, and state what its two columns mean physically.

## Part C — Reasoning

11. Explain why a planar 3-link arm reaching a 2D point has infinitely many solutions, while the 2-link arm has only two. What does this imply about closed-form solvability?
12. Describe the guess–measure–step loop. What roles do the seed, the step size, and the tolerance play? In this module, what is the Jacobian used for — and what is deliberately *not* covered until Module 6?

---

## What "ready" looks like

A student ready for Units 5–8 can:

- state the inverse problem $T_0^n(\boldsymbol\theta) = T_{\text{desired}}$, decide reachability, and explain the 0/1/many cases;
- solve the planar 2-link arm in closed form — **both** solutions — using the law of cosines and `atan2`, and verify by forward kinematics;
- explain what breaks closed form (general geometry, redundancy, coupled orientation) and why iteration is the general fix;
- describe the FK Jacobian as the **local linear map** $\Delta\mathbf p \approx J\,\Delta\boldsymbol\theta$ and how the guess–measure–step loop uses it — while recognizing that the Jacobian's velocity meaning, singularity theory, manipulability, and SVD analysis belong to Module 6.

If any of these is shaky, revisit: Unit 1 (problem statement / reachability), Unit 3.1–3.2 (closed form, `atan2`), or Units 4.2–4.3 (the Jacobian and the iteration loop) before starting Unit 5.

---

*A coaches' answer key is available in `coaches/answer-keys/module05/midpoint_answer_key.md`.*
