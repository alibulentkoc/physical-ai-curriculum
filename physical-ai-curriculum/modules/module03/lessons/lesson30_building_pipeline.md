---
module: 03
unit: 08
lesson: 8.2
title: "Building the Perception → World Pipeline"
core_idea: "Implement the capstone end to end: undistort, back-project with depth, compose extrinsics, and transform — one clean function from pixel to world position."
estimated_time: 55
difficulty: Project
prerequisites: [8.1]
learning_objectives:
  - Implement each stage as a tested function.
  - Compose the stages into a single pixel-to-world call.
  - Reproduce the canonical reference result.
tags:
  - physical-ai
  - perception
  - project
  - implementation
---

# Lesson 8.2 — Building the Perception → World Pipeline

## 1. Why This Matters

A pipeline you can't run isn't a capability. This lesson turns the 8.1 contract into working code: small, tested stage functions, composed into one `see_fruit_place_in_world` call. Building it stage-by-stage (each verified before the next) is how robust perception code is actually written — and how you debug it when a number looks wrong.

## 2. Physical Intuition

Think of an assembly line. Station 1 cleans the pixel (undistort). Station 2 turns it into a 3D point using depth (back-project). Station 3 carries that point into the world (transform). Each station has one job and a check at its output, so if the final position is wrong you know which station to inspect. We assemble the line, then run the canonical part through it and confirm it comes out where 8.1 said it should.

## 3. Mathematical Foundations

The stages, each a function:

- `undistort(u,v,K,dist) → (x_n,y_n)` — iterative inversion of the distortion model (Unit 5).
- `deproject(x_n,y_n,Z) → P_c = Z(x_n,y_n,1)` (Unit 6).
- `se3(R,t) → 4×4 T`; `compose(T_wa,T_ac) → T_wc` (Module 2).
- `transform(T_wc, P_c) → P_w` via homogeneous coordinates (Unit 7).

Composed:

$$\mathbf{P}_w = \text{transform}\big(T_{w\leftarrow a}T_{a\leftarrow c},\ \text{deproject}(\text{undistort}(u_d,v_d,K,\text{dist}),\ Z)\big).$$

Each stage is independently testable (identity distortion = passthrough; identity extrinsics ⇒ $\mathbf{P}_w=\mathbf{P}_c$; etc.), and the composition must reproduce the canonical $\mathbf{P}_w=(1.06,0.47,0.4)$.

## 4. Visual Explanation

`[Visual: the implemented pipeline as four function blocks with their inputs/outputs and a unit-test check under each]`

**Diagram Specification**
- **Objective:** show the code structure as tested stages.
- **Scene:** four blocks: undistort → deproject → compose extrinsics → transform; each with a small "✓ test" tag (identity passthrough, identity extrinsics, etc.); final output P_w.
- **Labels:** "one job per stage," "test each output," "compose into see_fruit_place_in_world."
- **Form:** SVG.

## 5. Engineering Example

Production perception nodes are built exactly this way: composable transforms (often via `tf2`), a deprojection helper, and an undistortion step, each unit-tested, then wired together. Keeping stages separate means a depth-alignment fix or a recalibration only touches one stage. The canonical reference doubles as a regression test that runs in CI.

## 6. Worked Example

Run the canonical inputs through the implemented stages: `undistort(480,160,...)` → $(0.2,-0.1)$ (no distortion in the canonical case); `deproject(...,0.3)` → $(0.06,-0.03,0.3)$; `compose(T_wa,T_ac)` → $T_{w\leftarrow c}$ with translation $(1.0,0.5,0.1)$, identity rotation; `transform(...)` → $(1.06,0.47,0.4)$. Output matches 8.1 ✓. Add a nonzero $k_1$ and confirm undistortion changes only the first stage's output, propagating predictably.

## 7. Interactive Demonstration

**Guided prediction.** Predict the output of each stage for the canonical inputs before running. Predict which stage's output changes if you set $T_{a\leftarrow c}$ rotation to a 90° yaw. Confirm by running the cells.

## 8. Coding Exercise

Implement the four stage functions and `see_fruit_place_in_world`; unit-test each stage (identity cases); assert the composition yields $(1.06,0.47,0.4)$; add a distortion case and confirm only the undistort stage's output shifts.

## 9. Knowledge Check

A check on the stage decomposition, the composition formula, and per-stage testing.

## 10. Challenge Problem

Refactor `transform` to accept and return *batches* of points (an $N\times3$ array) so the pipeline can place many detected fruits at once. What shape conventions keep the matrix multiply correct?

## 11. Common Mistakes

- Composing extrinsics in the wrong order (right-to-left: $T_{w\leftarrow a}T_{a\leftarrow c}$).
- Forgetting homogeneous coordinates in `transform`.
- Testing only the whole pipeline (test each stage so failures localize).

## 12. Key Takeaways

- Build the capstone as tested stages: undistort → deproject → compose → transform.
- Composition: $\mathbf{P}_w=\text{transform}(T_{w\leftarrow a}T_{a\leftarrow c},\text{deproject}(\text{undistort}(\cdot),Z))$.
- Reproduce the canonical $\mathbf{P}_w=(1.06,0.47,0.4)$.
- Per-stage tests localize bugs; the reference doubles as a regression test.

---

## AI Learning Companion

Copy any prompt below into ChatGPT, Claude, or another AI assistant.

**Tutor prompt** — explain it another way
```
Explain Lesson 8.2 (Module 3) — Building the Perception→World Pipeline — as composable, individually-tested stages (undistort, deproject, compose extrinsics, transform) that reproduce P_w=(1.06,0.47,0.4).
```

**Practice prompt** — generate more exercises
```
Give me 5 implementation tasks building and testing pixel-to-world pipeline stages, including identity-case tests. Include answers.
```

**Explore prompt** — connect it to the real world
```
Show me how production perception nodes structure deprojection + transforms with tf2 and unit tests, and why per-stage testing matters.
```

## Global Learning Support

Need this lesson explained in another language? Copy one of the prompts below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

**Español**
```
I just completed Lesson 8.2 (Module 3) — Building the Perception→World Pipeline.
Explain this lesson in Spanish. Keep robotics and mathematical terminology in English when appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

**中文 (Simplified Chinese)**
```
I just completed Lesson 8.2 (Module 3) — Building the Perception→World Pipeline.
Explain this lesson in Simplified Chinese. Keep mathematical notation unchanged.
Then provide: a summary, three practice questions, and one challenge problem.
```

**Türkçe**
```
I just completed Lesson 8.2 (Module 3) — Building the Perception→World Pipeline.
Explain this lesson in Turkish. Keep robotics terminology in English where commonly used.
Then provide: a summary, three practice questions, and one challenge problem.
```

---

*Next lesson: 8.3 — Verifying and Visualizing.*
