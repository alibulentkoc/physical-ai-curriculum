---
module: 03
unit: 07
lesson: 7.4
title: From Pixels to the Robot — Unit 7 Recap
core_idea: "A camera-frame point becomes a world-frame target by composing Module 2 extrinsics. Perception and transforms now connect end to end."
estimated_time: 20
difficulty: Review
prerequisites: [7.1, 7.2, 7.3]
learning_objectives:
  - Consolidate the camera→world transform step.
  - State the full pixel-to-world pipeline.
  - Set up the Unit 8 mini project.
tags:
  - physical-ai
  - perception
  - extrinsics
  - recap
---

# Lesson 7.4 — From Pixels to the Robot (Unit 7 Recap)

*A short synthesis — no new mathematics. It ties Unit 7 together and sets up the capstone.*

---

## Perception meets transforms

Unit 7 closed the loop between Module 3 and Module 2:

> **A back-projected point is in the camera frame; the Module 2 extrinsics chain $T_{w\leftarrow c}=T_{w\leftarrow a}T_{a\leftarrow c}$ carries it to the world frame — the fruit's actionable position.**

## What Unit 7 established

| Lesson | Point |
|---|---|
| 7.1 The Camera-Frame 3D Point | $\mathbf{P}_c$ is correct but in the camera frame; not actionable until transformed. |
| 7.2 Bridging to Module 2 | $T_{w\leftarrow c}$ is an SE(3) pose; compose camera→arm→world (right-to-left). |
| 7.3 Estimating the Fruit's World Position | Full pipeline: undistort → back-project (+depth) → transform; sanity-check. |

## The full pipeline (Module 3 in one line)

$$\tilde{\mathbf{P}}_w = T_{w\leftarrow c}\,\big[\,Z\cdot K^{-1}\,\text{undistort}(u,v)\,\big].$$

Forward (Units 1–5) turned world into pixels; inverse (Units 6–7) turns pixels back into the world, given depth and the camera's pose.

## Why this matters

**Unit 8** runs this end to end as the module **mini project**: detect a fruit, undistort, back-project with depth, transform to the world, verify, and visualize — the capstone integrating Module 3 (perception) with Module 2 (transforms). It also names the open question that launches **Module 4**: where does $T_{w\leftarrow a}$ come from? From the robot's joints, via **forward kinematics** — the next module.

## Visual Explanation

`[Visual: the complete forward+inverse picture — world→pixel (projection) on top, pixel→world (undistort, back-project, transform) on the bottom, meeting at the fruit]`

**Diagram Specification**
- **Objective:** consolidate the round trip world↔pixel.
- **Scene:** top arrow world → projection (extrinsics, distortion, K) → pixel; bottom arrow pixel → undistort → K⁻¹ ray + depth → P_c → T(world←cam) → P_w; both ends at the same tomato.
- **Labels:** "forward: Units 1–5," "inverse: Units 6–7," "next: Unit 8 capstone; Module 4 supplies T(world←arm)."
- **Form:** SVG.

## Coding Exercise

A short consolidation: run `pixel_to_world` on the worked example, confirm $\mathbf{P}_w=(1.06,0.47,0.4)$, distance preservation, and re-projection.

## Knowledge Check

A brief consolidation quiz across Unit 7 (formative — unlimited attempts).

## Key Takeaways

- $\mathbf{P}_c$ (camera) → $\mathbf{P}_w$ (world) via $T_{w\leftarrow c}$, composed from Module 2 poses.
- Full Module 3 pipeline: undistort → back-project (+depth) → transform.
- Next: **Unit 8** capstone end-to-end; **Module 4** supplies $T_{w\leftarrow a}$ via forward kinematics.

---

## AI Learning Companion

Copy any prompt below into ChatGPT, Claude, or another AI assistant.

**Tutor prompt** — explain it another way
```
Summarize Unit 7 of Module 3: a camera-frame point P_c becomes a world-frame target via T(world←cam) from Module 2. State the full pixel→world pipeline and preview the Unit 8 capstone and Module 4 (forward kinematics).
```

**Practice prompt** — generate more exercises
```
Give me a 10-question review of camera→world transforms and the full pixel-to-world pipeline. Include answers.
```

**Explore prompt** — connect it to the real world
```
Show me how perception (Module 3) and transforms (Module 2) combine in a real harvesting robot, and what forward kinematics (Module 4) adds.
```

## Global Learning Support

Need this lesson explained in another language? Copy one of the prompts below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

**Español**
```
I just completed Lesson 7.4 (Module 3) — From Pixels to the Robot (Unit 7 Recap).
Explain this lesson in Spanish. Keep robotics and mathematical terminology in English when appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

**中文 (Simplified Chinese)**
```
I just completed Lesson 7.4 (Module 3) — From Pixels to the Robot (Unit 7 Recap).
Explain this lesson in Simplified Chinese. Keep mathematical notation unchanged.
Then provide: a summary, three practice questions, and one challenge problem.
```

**Türkçe**
```
I just completed Lesson 7.4 (Module 3) — From Pixels to the Robot (Unit 7 Recap).
Explain this lesson in Turkish. Keep robotics terminology in English where commonly used.
Then provide: a summary, three practice questions, and one challenge problem.
```

---

*Next: Unit 8 — Mini Project: See the Fruit, Place It in the World.*
