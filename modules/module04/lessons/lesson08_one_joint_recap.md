---
module: 04
unit: 02
lesson: 2.4
title: One Joint at a Time — Unit 2 Recap
core_idea: "A single joint is one SE(3) transform of one variable; the gripper pose is read from its columns. Chaining these transforms is forward kinematics."
estimated_time: 20
difficulty: Review
prerequisites: [2.1, 2.2, 2.3]
learning_objectives:
  - Consolidate the one-joint pose and joint transform.
  - State the position/orientation extraction.
  - Set up chaining (Unit 3).
tags:
  - physical-ai
  - kinematics
  - recap
---

# Lesson 2.4 — One Joint at a Time (Unit 2 Recap)

*A short synthesis — no new mathematics. It ties Unit 2 together and points into chaining.*

---

## The atom of forward kinematics

Unit 2 built the single-joint case completely:

> **One joint = one $SE(3)$ transform of one variable ($R_z(\theta)\,G$ or $\text{Trans}_z(d)\,G$); the gripper pose is read from its translation column (position) and rotation block (orientation).**

## What Unit 2 established

| Lesson | Point |
|---|---|
| 2.1 A One-Joint Arm | Gripper position $(L\cos\theta, L\sin\theta)$, orientation $\theta$; pose $T_0^1(\theta)$. |
| 2.2 The Joint Transform | Each joint = variable motion ∘ fixed link geometry, one $SE(3)$ factor. |
| 2.3 Where Is the Tip? | Position = translation column; orientation = rotation block; matches trig. |

## Why this matters

A real arm has several joints. Because each is one transform, the gripper's pose for the whole arm is the **product** of the per-joint transforms — and that product *is* forward kinematics. **Unit 3** does exactly this: add a second (then third) joint and **compose** the transforms (Module 2 composition), reading the gripper pose off the product. **Unit 4** generalizes to $n$ joints, and **Units 5–6** introduce the DH convention so each factor comes from four numbers. We are one composition away from a general arm.

## Visual Explanation

`[Visual: a single joint transform as one factor, with a hint of more factors to the right forming a product T_0^n — "chaining is next"]`

**Diagram Specification**
- **Objective:** consolidate the single factor and preview the product.
- **Scene:** T_0^1(θ1) as one boxed factor; faded boxes T_1^2(θ2), …, T_{n-1}^n to the right with "×" between them; under it "gripper pose = product of joint transforms."
- **Labels:** "one joint = one factor," "forward kinematics = product," "Unit 3: chain them."
- **Form:** SVG.

## Interactive Demonstration

Unit 2 in one tool: swing the one-joint arm and watch the single transform T₀¹ carry both its position and orientation.

## Coding Exercise

A short consolidation: build `pose_one_joint(theta, L)`, extract position and orientation, and confirm against trig for two angles — the routine that will be applied to each factor of the chain.

## Knowledge Check

A brief consolidation quiz across Unit 2 (formative — unlimited attempts).

## Key Takeaways

- One joint = **one $SE(3)$ transform** of one variable (revolute or prismatic).
- Read **position** (translation column) and **orientation** (rotation block) from the pose.
- Forward kinematics for many joints is the **product** of per-joint transforms.
- Next: **Unit 3** — chaining two and three links.

---

## AI Learning Companion

Copy any prompt below into ChatGPT, Claude, or another AI assistant.

**Tutor prompt** — explain it another way
```
Summarize Unit 2 of Module 4: a single joint is one SE(3) transform of one variable; read position (translation column) and orientation (rotation block) from the pose; forward kinematics for many joints is the product of these factors.
```

**Practice prompt** — generate more exercises
```
Give me a 10-question review of the one-joint arm: pose formula, joint transform, and position/orientation extraction. Include answers.
```

**Explore prompt** — connect it to the real world
```
Show me how a multi-joint arm's gripper pose is the product of single-joint transforms, building on the one-joint case.
```

## Global Learning Support

Need this lesson explained in another language? Copy one of the prompts below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

**Español**
```
I just completed Lesson 2.4 (Module 4) — One Joint at a Time (Unit 2 Recap).
Explain this lesson in Spanish. Keep robotics and mathematical terminology in English when appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

**中文 (Simplified Chinese)**
```
I just completed Lesson 2.4 (Module 4) — One Joint at a Time (Unit 2 Recap).
Explain this lesson in Simplified Chinese. Keep mathematical notation unchanged.
Then provide: a summary, three practice questions, and one challenge problem.
```

**Türkçe**
```
I just completed Lesson 2.4 (Module 4) — One Joint at a Time (Unit 2 Recap).
Explain this lesson in Turkish. Keep robotics terminology in English where commonly used.
Then provide: a summary, three practice questions, and one challenge problem.
```

---

*Next: Unit 3 — Chaining Transforms (Two and Three Links).*
