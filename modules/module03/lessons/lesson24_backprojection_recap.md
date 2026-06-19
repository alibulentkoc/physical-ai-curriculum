---
module: 03
unit: 06
lesson: 6.4
title: Back-Projection — Unit 6 Recap
core_idea: "A pixel is a ray; depth selects the point. Back-projection inverts the camera to a 3D camera-frame point — ready to be carried into the world."
estimated_time: 20
difficulty: Review
prerequisites: [6.1, 6.2, 6.3]
learning_objectives:
  - Consolidate ray construction, depth, and deprojection.
  - State the back-projection formula compactly.
  - Bridge to placing the point in the world (Unit 7).
tags:
  - physical-ai
  - perception
  - back-projection
  - recap
---

# Lesson 6.4 — Back-Projection (Unit 6 Recap)

*A short synthesis — no new mathematics. It ties Unit 6 together and points toward the world.*

---

## From pixel to 3D point

Unit 6 inverted the camera, as far as the camera frame:

> **A pixel back-projects to a ray $(x_n,y_n,1)$ via $K^{-1}$; depth $Z$ selects the point $\mathbf{P}_c = Z(x_n,y_n,1)$.**

Direction from the lens math, distance from a depth measurement — together a 3D camera-frame point.

## What Unit 6 established

| Lesson | Point |
|---|---|
| 6.1 A Pixel Is a Ray | Inverse of a pixel is a ray (many-to-one projection); direction $(x_n,y_n,1)$; depth unknown from one image. |
| 6.2 Adding Depth Recovers a Point | $\mathbf{P}_c = Z(x_n,y_n,1)$; depth from RGB-D / stereo / geometry. |
| 6.3 Back-Projection in Code | Vectorized deprojection, depth filtering, point clouds, round-trip verification. |

## Why this matters

The point $\mathbf{P}_c$ is in the **camera frame** — useful, but the robot acts in the **world/arm frame**. **Unit 7** carries $\mathbf{P}_c$ across the extrinsics chain from Module 2 ($T_{\text{world}\leftarrow\text{cam}}$) to get the fruit's world position. **Unit 8** runs the entire round trip end to end — detect, undistort, deproject, transform, reach — the module capstone. Back-projection is the inverse half's engine; Unit 7 connects it to where the robot lives.

## Visual Explanation

`[Visual: the inverse pipeline — pixel → undistort → K⁻¹ ray → +depth → camera-frame point — with a dashed arrow forward to "world frame (Unit 7)"]`

**Diagram Specification**
- **Objective:** consolidate back-projection and point to Unit 7.
- **Scene:** flow pixel → "undistort (Unit 5)" → "K⁻¹ → ray" → "+ depth Z" → camera-frame point P_c; a dashed arrow labeled "× T(world←cam) — Unit 7" toward a world frame with a tomato.
- **Labels:** "ray (x_n,y_n,1)," "P_c = Z(x_n,y_n,1)," "still camera frame," "next: into the world."
- **Form:** SVG (faux-3D).

## Interactive Demonstration

Unit 6 in one tool: project a 3D point to a pixel, then back-project with the same depth and recover it exactly.

## Coding Exercise

A short consolidation: deproject a couple of pixels with depth to camera-frame points, verify round-trips, and note that the points are not yet in the world frame.

## Knowledge Check

A brief consolidation quiz across Unit 6 (formative — unlimited attempts).

## Key Takeaways

- Pixel → ray $(x_n,y_n,1)$ via $K^{-1}$; **depth** selects the point.
- $\mathbf{P}_c = Z(x_n,y_n,1)$; verify with a round-trip to the pixel.
- The result is in the **camera frame**.
- Next: **Unit 7** transforms $\mathbf{P}_c$ to the world via Module 2 extrinsics.

---

## AI Learning Companion

Copy any prompt below into ChatGPT, Claude, or another AI assistant.

**Tutor prompt** — explain it another way
```
Summarize Unit 6 of Module 3: a pixel back-projects to a ray (x_n,y_n,1) via K⁻¹, and depth Z selects the camera-frame point P_c = Z(x_n,y_n,1). Note the point is still in the camera frame.
```

**Practice prompt** — generate more exercises
```
Give me a 10-question review of back-projection: rays, depth, deprojection, point clouds, and round-trip checks. Include answers.
```

**Explore prompt** — connect it to the real world
```
Show me how back-projection feeds the extrinsics chain to put a fruit detection into the robot's world frame.
```

## Global Learning Support

Need this lesson explained in another language? Copy one of the prompts below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

**Español**
```
I just completed Lesson 6.4 (Module 3) — Back-Projection (Unit 6 Recap).
Explain this lesson in Spanish. Keep robotics and mathematical terminology in English when appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

**中文 (Simplified Chinese)**
```
I just completed Lesson 6.4 (Module 3) — Back-Projection (Unit 6 Recap).
Explain this lesson in Simplified Chinese. Keep mathematical notation unchanged.
Then provide: a summary, three practice questions, and one challenge problem.
```

**Türkçe**
```
I just completed Lesson 6.4 (Module 3) — Back-Projection (Unit 6 Recap).
Explain this lesson in Turkish. Keep robotics terminology in English where commonly used.
Then provide: a summary, three practice questions, and one challenge problem.
```

---

*Next: Unit 7 — From Pixels to the Robot.*
