---
module: 04
unit: 06
lesson: 6.4
title: Building and Using a DH Table — Unit 6 Recap
core_idea: "A DH table becomes forward kinematics by building each row's four-factor transform and multiplying them. One function, any arm; verified against closed forms; symbolic via SymPy."
estimated_time: 20
difficulty: Review
prerequisites: [6.1, 6.2, 6.3]
learning_objectives:
  - Consolidate the DH transform and table-to-FK pipeline.
  - State the verification against closed forms.
  - Set up pose, workspace, and the perception bridge (Unit 7).
tags:
  - physical-ai
  - kinematics
  - denavit-hartenberg
  - recap
---

# Lesson 6.4 — Building and Using a DH Table (Unit 6 Recap)

*A short synthesis — no new mathematics. It ties Unit 6 together and points toward pose, workspace, and perception.*

---

## From table to gripper pose

Unit 6 closed the loop from description to computation:

> **Each DH row becomes a link transform $T_{i-1}^i = \mathrm{Rot}_z(\theta)\,\mathrm{Trans}_z(d)\,\mathrm{Trans}_x(a)\,\mathrm{Rot}_x(\alpha)$; multiply the rows to get $T_0^n(\boldsymbol{\theta})$. One function computes forward kinematics for any arm, verified against the planar closed form and available symbolically via SymPy.**

## What Unit 6 established

| Lesson | Point |
|---|---|
| 6.1 The DH Link Transform | One fixed four-factor formula per joint; reduces to the planar transform when $d=0,\alpha=0$. |
| 6.2 Reading a Robot into a Table | A procedure: number joints → assign frames → read $\theta,d,a,\alpha$; the 3-DOF capstone table. |
| 6.3 DH FK in Code | `dh_fk(table, config)` — build per-row transforms, multiply, extract; verify vs closed form; SymPy symbolic. |

## Why this matters

We can now take any serial arm, write its DH table, and compute the gripper pose. The remaining question is **interpretation and connection**: what does the pose tell us, what set of poses can the arm reach, and how does this plug back into perception? **Unit 7** answers all three — reading the end-effector pose, the reachable **workspace**, and **closing the loop** by identifying $T_0^n = T_{w\leftarrow a}$, the arm pose Module 3 assumed. Then **Unit 8** is the capstone: build the 3-DOF arm's DH model, compute and verify the gripper pose, and place a perceived fruit target in the arm's frame.

## Visual Explanation

`[Visual: DH table → dh_fk → T_0^n → (position, orientation), with arrows forward to "workspace" and "T(world←arm) = perception bridge" (Unit 7)]`

**Diagram Specification**
- **Objective:** consolidate table→FK and preview Unit 7.
- **Scene:** "DH table + config" → "dh_fk" → "T_0^n" → "position + orientation"; two forward arrows to "reachable workspace" and "T_0^n = T(world←arm) → perception."
- **Labels:** "any arm = a table," "verified + symbolic," "Unit 7: pose, workspace, back to perception."
- **Form:** SVG.

## Interactive Demonstration

Unit 6 in one tool: drive the 3-DOF arm and watch the live DH table feed the forward kinematics that places the gripper.

## Coding Exercise

A short consolidation: given the 3-DOF DH table, compute $T_0^3$ at one configuration with `dh_fk`, extract position and orientation, and confirm the in-plane reach matches `fk_planar`.

## Knowledge Check

A brief consolidation quiz across Unit 6 (formative — unlimited attempts).

## Key Takeaways

- A DH row → a **four-factor link transform**; multiply rows → $T_0^n(\boldsymbol{\theta})$.
- **One function** computes FK for any arm; verify against the planar closed form.
- **SymPy** gives the symbolic end-effector pose from a symbolic table.
- Next: **Unit 7** — interpret the pose, the workspace, and reconnect to perception.

---

## AI Learning Companion

Copy any prompt below into ChatGPT, Claude, or another AI assistant.

**Tutor prompt** — explain it another way
```
Summarize Unit 6 of Module 4: each DH row becomes the four-factor link transform; multiply rows to get T_0^n; one dh_fk function works for any arm, verified against the planar closed form and available symbolically via SymPy.
```

**Practice prompt** — generate more exercises
```
Give me a 10-question review of building and using a DH table: the link transform, table-building procedure, and DH FK in code. Include answers.
```

**Explore prompt** — connect it to the real world
```
Show me how going from a robot's DH table to its gripper pose works end to end, and how this becomes the T(world←arm) perception needs.
```

## Global Learning Support

Need this lesson explained in another language? Copy one of the prompts below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

**Español**
```
I just completed Lesson 6.4 (Module 4) — Building and Using a DH Table (Unit 6 Recap).
Explain this lesson in Spanish. Keep robotics and mathematical terminology in English when appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

**中文 (Simplified Chinese)**
```
I just completed Lesson 6.4 (Module 4) — Building and Using a DH Table (Unit 6 Recap).
Explain this lesson in Simplified Chinese. Keep mathematical notation unchanged.
Then provide: a summary, three practice questions, and one challenge problem.
```

**Türkçe**
```
I just completed Lesson 6.4 (Module 4) — Building and Using a DH Table (Unit 6 Recap).
Explain this lesson in Turkish. Keep robotics terminology in English where commonly used.
Then provide: a summary, three practice questions, and one challenge problem.
```

---

*Next: Unit 7 — Pose, Workspace, and Back to Perception.*
