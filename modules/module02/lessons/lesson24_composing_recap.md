---
module: 02
unit: 05
lesson: 5.4
title: Composing Rigid Motions — Unit 5 Recap
core_idea: "Chaining transforms is matrix multiplication: order matters, inverses reverse edges, and frames-as-a-graph turns any pose query into a composed path."
estimated_time: 20
difficulty: Review
prerequisites: [5.1, 5.2, 5.3]
learning_objectives:
  - Consolidate composition, order-dependence, and frames-as-a-graph.
  - Explain why composition is the conceptual heart of the module.
  - Bridge to robot pose representation in Unit 6.
tags:
  - physical-ai
  - transformations
  - composition
  - recap
---

# Lesson 5.4 — Composing Rigid Motions (Unit 5 Recap)

*A short synthesis — no new mathematics. It ties Unit 5 together and points into pose.*

---

## The heart of the module

Units 3–4 built single rigid motions (SE(2), SE(3)). Unit 5 is where they become a system:

> **Chain transforms by multiplying them — mind the order, invert to go backward, and treat frames as a graph so any pose query is a composed path.**

This is the conceptual heart of Module 2: everything a robot does spatially is a composition of rigid motions.

## What Unit 5 established

| Lesson | Point |
|---|---|
| 5.1 Chaining Transforms | Doing transforms in sequence = multiplying them; the chain collapses into one matrix ($T_2 T_1$, apply $T_1$ first). |
| 5.2 Order Matters | Composition is non-commutative: $T_2 T_1 \neq T_1 T_2$; "rotate then move" ≠ "move then rotate." |
| 5.3 Frames as a Graph | Frames are nodes, transforms are edges; relate any two by composing along the path, inverting backward edges. |

A chain of rigid motions is itself rigid, so every composed path is a valid SE(2)/SE(3) transform.

## Why this matters

The camera→robot→world pipeline is a path through the frame graph, composed into one transform. Get the **order** right and the gripper lands on the fruit; get it wrong and it reaches empty air. Need the reverse direction? Invert the path. Composition + inversion + the graph view are the complete toolkit for moving any quantity between any two frames.

## Visual Explanation

`[Visual: Unit 5 in one picture — a frame graph with a highlighted composed path (product of edges), a side note that order matters, and an inverse arrow for the reverse direction]`

**Diagram Specification**
- **Objective:** consolidate chaining, order, and the graph path.
- **Scene:** a small frame graph (camera, arm, world) with a highlighted path and its product T2·T1; an inset showing T·R ≠ R·T (two different endings); a dashed inverse arrow for the reverse path.
- **Labels:** "compose along the path," "order matters," "invert to reverse."
- **Form:** SVG.

## Coding Exercise

A short capstone: build two SE(3) edges, compose them along a path (camera→world), show that swapping the order changes the result, and invert the path to recover world→camera.

## Knowledge Check

A brief consolidation quiz across Unit 5 (formative — unlimited attempts).

## Key Takeaways

- **Composition = matrix multiplication**; the chain is one matrix ($T_2 T_1$, $T_1$ first).
- **Order matters**: $T_2 T_1 \neq T_1 T_2$ in general.
- **Frames as a graph**: relate any two by composing the path; **invert** backward edges.
- This is the heart of the module and the backbone of the perception-to-pose pipeline (Units 7–8). Next: **robot pose** (Unit 6).

---

## AI Learning Companion

Copy any prompt below into ChatGPT, Claude, or another AI assistant.

**Tutor prompt** — explain it another way
```
Summarize Unit 5 of Module 2 as one story: chaining transforms by multiplication, why order matters, and frames-as-a-graph where any pose query is a composed path (with inverses for backward edges).
```

**Practice prompt** — generate more exercises
```
Give me a 10-question mixed review of composition: chaining as a product, non-commutativity, and composing along a frame-graph path with inverses. Include answers.
```

**Explore prompt** — connect it to the real world
```
Show me how a robot composes the camera→world transform along a frame-graph path and why order and inverses are critical to getting the gripper to the right place.
```

## Global Learning Support

Need this lesson explained in another language? Copy one of the prompts below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

**Español**
```
I just completed Lesson 5.4 (Module 2) — Composing Rigid Motions (Unit 5 Recap).
Explain this lesson in Spanish. Keep robotics and mathematical terminology in English when appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

**中文 (Simplified Chinese)**
```
I just completed Lesson 5.4 (Module 2) — Composing Rigid Motions (Unit 5 Recap).
Explain this lesson in Simplified Chinese. Keep mathematical notation unchanged.
Then provide: a summary, three practice questions, and one challenge problem.
```

**Türkçe**
```
I just completed Lesson 5.4 (Module 2) — Composing Rigid Motions (Unit 5 Recap).
Explain this lesson in Turkish. Keep robotics terminology in English where commonly used.
Then provide: a summary, three practice questions, and one challenge problem.
```

---

*Next: the Module 2 Midpoint Checkpoint, then Unit 6 — Robot Pose Representation.*
