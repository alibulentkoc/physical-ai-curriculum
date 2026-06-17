# Mathematical Prerequisites

> **Scope:** Entry competencies for **Module 1** (Mathematical Foundations).
> **Authority:** Module 1 manifest §5; Architect Decision **D-008**.
> **Purpose:** State exactly what a student is assumed to know *before* Unit 1, provide a self-check diagnostic, and route students who need refreshers — without turning Module 1 into a remedial course.

This document is **not a lesson**. It is an entry contract and diagnostic.

---

## 1. What is assumed (entry competencies)

A student beginning Module 1 should already be comfortable with:

| Area | Specifically |
|---|---|
| **Algebra** | Manipulating expressions, solving linear equations, working with exponents, substitution. |
| **Functions & graphs** | Reading/plotting `y = f(x)`; slope and intercept; interpreting a graph. |
| **Basic trigonometry** | Sine, cosine, tangent in a right triangle; degrees vs. radians at a basic level. |
| **Geometry** | Points, lines, angles, distance in the plane; the Pythagorean theorem. |
| **Numeracy** | Units, ratios, percentages; basic estimation. |

## 2. What is helpful but NOT required

- Prior programming experience (Python is taught at the level needed in Unit 8).
- Any prior linear algebra (built from scratch in Units 4–5).
- Calculus (intuitive notions are reinforced where used; no formal prerequisite).

## 3. What is explicitly NOT assumed

- Matrices, vectors-as-objects, or coordinate transformations — these are *taught*, not assumed.
- Robotics, ROS, simulation, or perception background.
- Familiarity with the Greenhouse Harvesting Robot narrative.

---

## 4. Self-check diagnostic

A short, honest self-assessment. These are **diagnostic prompts, not graded items** — they tell a student whether to start at Unit 1 directly or do a quick refresher first. (Full solutions live in `coaches/answer-keys/`, not here.)

**Algebra**
1. Solve for x: `3x − 7 = 11`.
2. Simplify: `2(a + 3) − 4a`.

**Functions & graphs**
3. For `y = 2x + 1`, what are the slope and y-intercept?
4. Sketch (mentally) where `y = x²` is increasing.

**Trigonometry**
5. In a right triangle, the side opposite a 30° angle is 5. What relationship gives the hypotenuse?
6. Convert 180° to radians.

**Geometry / numeracy**
7. Distance between points (0, 0) and (3, 4)?
8. A measurement reads 12.0 cm ± 0.2 cm. What does the ± mean?

### Interpreting your results
- **Comfortable with all eight →** start at Unit 1.
- **Shaky on 1–2 →** skim the relevant refresher (below) and proceed.
- **Shaky on 3+ in one area →** complete that area's refresher before Unit 1.

---

## 5. Refresher routing

Module 1 does not teach the prerequisites, but points to where to shore them up. Recommended free resources will be listed in `docs/` (resource list maintained separately so it can be updated without touching this contract):

| If shaky on… | Refresh before… |
|---|---|
| Algebra / functions | Unit 1 |
| Trigonometry | Unit 6 (but basic trig helps from Unit 3 onward) |
| Geometry / distance | Unit 2 |
| Units & uncertainty | Unit 1 (this is also taught early in Unit 1) |

---

## 6. Mapping prerequisites to Module 1 units

This shows where each assumed skill first gets *used*, so students know how soon a gap will matter.

| Prerequisite | First load-bearing in |
|---|---|
| Algebra | Unit 1 |
| Units / measurement sense | Unit 1 |
| Distance / Pythagoras | Unit 2 (vector magnitude) |
| Functions & graphs | Unit 2 (visualization) |
| Basic trigonometry | Unit 3 (frames), heavily in Unit 6 |
| Right-triangle geometry | Unit 6 |

A student who clears the diagnostic in §4 has everything needed to reach the Unit 9 mini project without mathematical remediation.
