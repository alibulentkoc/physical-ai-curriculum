---
module: 03
unit: 06
lesson: 6.3
title: Back-Projection in Code
core_idea: "Deprojecting a detected pixel with depth gives a camera-frame point in code; doing it for many pixels yields a point cloud — the practical inverse of projection."
estimated_time: 45
difficulty: Core
prerequisites: [6.2]
learning_objectives:
  - Implement deprojection cleanly and vectorized.
  - Build a small point cloud from a depth image.
  - Verify back-projection against forward projection.
tags:
  - physical-ai
  - perception
  - back-projection
  - code
  - depth
---

# Lesson 6.3 — Back-Projection in Code

## 1. Why This Matters

The deprojection formula becomes a few lines of code that the robot runs constantly: turn a detected pixel (plus its depth) into a camera-frame 3D point, or turn a whole depth image into a **point cloud**. This lesson makes back-projection concrete and verifiable — and the verification (back-project then re-project) is how you trust the result before commanding an arm.

## 2. Physical Intuition

A depth image is a grid where each pixel carries a distance instead of (or alongside) a color. Back-projecting every pixel with its depth scatters those measurements into 3D space — a cloud of points that traces the visible surfaces. For perception we usually only need the few pixels on the detected fruit, but the same operation, applied to all pixels, reconstructs the scene's geometry. It's the inverse of "flattening 3D to an image": we're inflating the image back into 3D using the depth channel.

## 3. Mathematical Foundations

For one undistorted pixel $(u,v)$ with depth $Z$ and intrinsics $K$:

$$X = (u - c_x)\,Z/f_x, \quad Y = (v - c_y)\,Z/f_y, \quad \mathbf{P}_c = (X, Y, Z).$$

Vectorized over a set of pixels with per-pixel depths $Z_i$: stack $(u_i, v_i, Z_i)$ and apply the formula element-wise — no loops needed. Validity: only deproject pixels with a **valid depth** ($Z_i > 0$; depth sensors mark missing returns as 0 or NaN, which must be filtered). A round-trip check confirms correctness: deproject $(u,v,Z)$ to $\mathbf{P}_c$, then project $\mathbf{P}_c$ with $K$ (Unit 4) — you must recover $(u,v)$. This forward/back consistency is the test every implementation should pass. OpenCV has no single "deproject" call, but the formula is one line of NumPy; some stacks provide `rs2_deproject_pixel_to_point` (RealSense) doing exactly this.

## 4. Visual Explanation

`[Visual: a small depth image whose valid pixels are deprojected into a 3D point cloud, with invalid (zero-depth) pixels skipped]`

**Diagram Specification**
- **Objective:** show many pixels + depth → point cloud.
- **Scene:** left, a small grid (depth image) with most cells holding a Z value and a couple marked "no depth"; arrow "deproject each valid pixel"; right, a faux-3D scatter of points forming a surface; the no-depth cells absent from the cloud.
- **Labels:** "depth image (Z per pixel)," "P_c = ((u-c_x)Z/f_x, (v-c_y)Z/f_y, Z)," "skip Z≤0 / NaN," "point cloud."
- **Form:** SVG.

## 5. Engineering Example

The robot's RGB-D pipeline back-projects the depth pixels inside the fruit's detection mask, averages them into a single stable camera-frame point (robust to a few noisy depths), and passes that to the extrinsics chain (Unit 7). For mapping or collision-checking, it back-projects the whole frame into a cloud. The round-trip check runs in tests: if a deprojected-then-reprojected pixel drifts, the intrinsics or the depth alignment is wrong.

## 6. Worked Example

Pixels and depths: $(480,160,0.3)$ and $(320,240,0.5)$, $K$ ($f_x=f_y=800$, principal point $(320,240)$).
- $(480,160,0.3)$: $X=(160)(0.3)/800=0.06$, $Y=(-80)(0.3)/800=-0.03$, $\mathbf{P}_c=(0.06,-0.03,0.3)$.
- $(320,240,0.5)$: $X=0$, $Y=0$, $\mathbf{P}_c=(0,0,0.5)$ (principal-point pixel → straight ahead at its depth).
Round-trip: projecting $(0.06,-0.03,0.3)$ → $(480,160)$ ✓; projecting $(0,0,0.5)$ → $(320,240)$ ✓.

## 7. Interactive Demonstration

**Guided prediction.** For pixels $(480,160,0.3)$ and $(320,240,0.5)$ with the $K$ above, predict each $\mathbf{P}_c$. Predict what happens to a pixel whose depth reads 0 (sensor miss). Confirm the round-trip recovers the original pixels.

## 8. Coding Exercise

Implement vectorized `deproject_many(pixels, depths, K)` returning an $N\times3$ array; filter $Z>0$; build a tiny point cloud from a synthetic depth grid; assert the round-trip (deproject → project) recovers the input pixels to tolerance.

## 9. Knowledge Check

A check on the deprojection formula in code, depth validity filtering, and the round-trip verification.

## 10. Challenge Problem

A deprojected fruit point reprojects to a pixel 12 px away from the original detection. List the likely causes (wrong $K$, depth/color misalignment, distortion not removed) and the order you'd check them.

## 11. Common Mistakes

- Deprojecting invalid-depth pixels (0/NaN) into garbage points.
- Skipping undistortion, so the ray direction is wrong.
- Not verifying with a round-trip before trusting the 3D point.

## 12. Key Takeaways

- Deproject in code: $\mathbf{P}_c = ((u-c_x)Z/f_x,\ (v-c_y)Z/f_y,\ Z)$; vectorize over pixels.
- Filter invalid depths ($Z>0$); many pixels → a **point cloud**.
- **Round-trip check** (deproject → project) verifies correctness.
- $\mathbf{P}_c$ is camera-frame; Unit 7 takes it to the world.

---

## AI Learning Companion

Copy any prompt below into ChatGPT, Claude, or another AI assistant.

**Tutor prompt** — explain it another way
```
Explain Lesson 6.3 (Module 3) — Back-Projection in Code — as inflating a depth image into a point cloud. Show the vectorized deprojection, depth filtering, and the round-trip check (deproject then project).
```

**Practice prompt** — generate more exercises
```
Give me 6 coding-style exercises deprojecting pixels+depth into camera-frame points and verifying round-trips, including invalid-depth handling. Include answers.
```

**Explore prompt** — connect it to the real world
```
Show me how an RGB-D robot back-projects a detection mask into a stable 3D point and uses round-trip checks in tests.
```

## Global Learning Support

Need this lesson explained in another language? Copy one of the prompts below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

**Español**
```
I just completed Lesson 6.3 (Module 3) — Back-Projection in Code.
Explain this lesson in Spanish. Keep robotics and mathematical terminology in English when appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

**中文 (Simplified Chinese)**
```
I just completed Lesson 6.3 (Module 3) — Back-Projection in Code.
Explain this lesson in Simplified Chinese. Keep mathematical notation unchanged.
Then provide: a summary, three practice questions, and one challenge problem.
```

**Türkçe**
```
I just completed Lesson 6.3 (Module 3) — Back-Projection in Code.
Explain this lesson in Turkish. Keep robotics terminology in English where commonly used.
Then provide: a summary, three practice questions, and one challenge problem.
```

---

*Next lesson: 6.4 — Back-Projection (Unit 6 recap).*
