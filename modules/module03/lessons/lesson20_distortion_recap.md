---
module: 03
unit: 05
lesson: 5.4
title: Lens Distortion — Unit 5 Recap
core_idea: "Real lenses distort; a small coefficient model captures it, and undistortion restores the ideal pinhole geometry the rest of the pipeline assumes."
estimated_time: 20
difficulty: Review
prerequisites: [5.1, 5.2, 5.3]
learning_objectives:
  - Consolidate the distortion model and undistortion.
  - Place distortion correctly in the pipeline.
  - Bridge to back-projection (Unit 6).
tags:
  - physical-ai
  - perception
  - distortion
  - recap
---

# Lesson 5.4 — Lens Distortion (Unit 5 Recap)

*A short synthesis — no new mathematics. It ties Unit 5 together and points into back-projection.*

---

## Real lenses bend; we model it and undo it

Unit 5 closed the gap between the ideal pinhole and a real camera:

> **Distortion acts on normalized coordinates before $K$ (radial $k_1,k_2,k_3$ + tangential $p_1,p_2$); undistortion inverts it iteratively so a measured pixel maps back to ideal pinhole geometry.**

After undistortion, every Unit 4 tool is exact again.

## What Unit 5 established

| Lesson | Point |
|---|---|
| 5.1 Why Straight Lines Bend | Distortion = deviation from the pinhole; grows with radius; barrel (outward) vs pincushion (inward). |
| 5.2 Radial and Tangential Distortion | Model: ×(1+k1 r²+k2 r⁴+k3 r⁶) + tangential (p1,p2); distCoeffs=(k1,k2,p1,p2,k3); zeros = ideal. |
| 5.3 Undistortion | Recover the ideal point from a measured pixel; iterative (no closed form); `cv2.undistortPoints`/`undistort`. |

## Why this matters

The full forward map is now complete and *realistic*: world → extrinsics → normalized projection → **distortion** → $K$ → pixel. **Unit 6** runs the pipeline backward — starting from an (undistorted) pixel, treat it as a **ray**, and add depth to recover a 3D point. **Unit 7** carries that point into the world via Module 2's extrinsics. Undistortion is the gate: back-projection assumes clean pinhole geometry, which is exactly what undistortion provides.

## Visual Explanation

`[Visual: the realistic forward map with distortion inserted, and a note that undistortion reverses the distortion box to restore the ideal pinhole for back-projection]`

**Diagram Specification**
- **Objective:** place distortion in the pipeline and show undistortion as its inverse.
- **Scene:** flow world → extrinsics → normalized (x_n,y_n) → [distortion box] → K → pixel; a dashed return arrow over the distortion box labeled "undistortion (iterative)" pointing back to clean normalized coords.
- **Labels:** "distortion: radial+tangential," "undistortion restores ideal pinhole," "needed before back-projection."
- **Form:** SVG.

## Interactive Demonstration

Unit 5 in one tool: set k₁, then switch between the distorted image and the undistorted (corrected) one and watch straight lines return.

## Coding Exercise

A short consolidation: distort a grid of points, undistort them, and confirm the round-trip returns the originals; show the center is unaffected and edges are corrected most.

## Knowledge Check

A brief consolidation quiz across Unit 5 (formative — unlimited attempts).

## Key Takeaways

- Distortion model: radial $(k_1,k_2,k_3)$ + tangential $(p_1,p_2)$, applied to normalized coords before $K$.
- **Undistortion** recovers ideal pinhole points (iterative; OpenCV helpers).
- Pipeline: world → extrinsics → projection → distortion → $K$ → pixel.
- Next: **back-projection** — from an undistorted pixel (a ray) plus depth to a 3D point.

---

## AI Learning Companion

Copy any prompt below into ChatGPT, Claude, or another AI assistant.

**Tutor prompt** — explain it another way
```
Summarize Unit 5 of Module 3: lens distortion (radial k1,k2,k3 + tangential p1,p2) applied before K, and undistortion (iterative) that restores the ideal pinhole. Show where distortion sits in the pipeline.
```

**Practice prompt** — generate more exercises
```
Give me a 10-question review of lens distortion: barrel vs pincushion, the coefficient model, and undistortion round-trips. Include answers.
```

**Explore prompt** — connect it to the real world
```
Show me why undistortion must happen before back-projection in a harvesting robot's perception pipeline.
```

## Global Learning Support

Need this lesson explained in another language? Copy one of the prompts below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

**Español**
```
I just completed Lesson 5.4 (Module 3) — Lens Distortion (Unit 5 Recap).
Explain this lesson in Spanish. Keep robotics and mathematical terminology in English when appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

**中文 (Simplified Chinese)**
```
I just completed Lesson 5.4 (Module 3) — Lens Distortion (Unit 5 Recap).
Explain this lesson in Simplified Chinese. Keep mathematical notation unchanged.
Then provide: a summary, three practice questions, and one challenge problem.
```

**Türkçe**
```
I just completed Lesson 5.4 (Module 3) — Lens Distortion (Unit 5 Recap).
Explain this lesson in Turkish. Keep robotics terminology in English where commonly used.
Then provide: a summary, three practice questions, and one challenge problem.
```

---

*Next: Unit 6 — Back-Projection: Pixels to 3D.*
