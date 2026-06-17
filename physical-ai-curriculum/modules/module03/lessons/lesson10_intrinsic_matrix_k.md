---
module: 03
unit: 03
lesson: 3.2
title: The Intrinsic Matrix K
core_idea: "The intrinsic matrix K packages focal length and principal point into one 3×3 matrix that maps a camera-frame direction to a pixel."
estimated_time: 45
difficulty: Core
prerequisites: [3.1]
learning_objectives:
  - Write the intrinsic matrix K from focal lengths and principal point.
  - Apply K to project a camera-frame point to a pixel (with the divide-by-Z).
  - Interpret each entry of K.
tags:
  - physical-ai
  - perception
  - intrinsics
  - matrix
---

# Lesson 3.2 — The Intrinsic Matrix K

## 1. Why This Matters

We now have all the pieces of the forward map in pixels: focal length in pixels ($f_x, f_y$) and the offset of the image center (the principal point). The **intrinsic matrix** $K$ collects them into one tidy $3\times3$ object, so projection becomes "multiply by $K$, then divide by $Z$." This is the form every vision library uses — OpenCV, calibration tools, your own code. Master $K$ and you can project any camera-frame point to the exact pixel a real camera would report.

## 2. Physical Intuition

Think of $K$ as the camera's personal "translator" from a *direction in space* to a *spot on its image*. Two facts define that translator: how much it magnifies (focal length in pixels — bigger means a given direction lands farther from center) and where the center of its image actually sits (the principal point — rarely the exact array corner). Package those into a small table and you can convert any incoming direction into the pixel that camera would record. Different cameras have different translators; calibration is how you learn a specific camera's $K$.

## 3. Mathematical Foundations

For a camera-frame point $\mathbf{P} = (X, Y, Z)$, form the homogeneous pixel vector

$$\tilde{\mathbf{p}} = K \begin{bmatrix} X \\ Y \\ Z \end{bmatrix}, \qquad K = \begin{bmatrix} f_x & 0 & c_x \\ 0 & f_y & c_y \\ 0 & 0 & 1 \end{bmatrix},$$

then **divide by the third entry** to get pixel coordinates:

$$\tilde{\mathbf{p}} = \begin{bmatrix} f_x X + c_x Z \\ f_y Y + c_y Z \\ Z \end{bmatrix} \;\Rightarrow\; u = \frac{f_x X + c_x Z}{Z} = f_x\frac{X}{Z} + c_x, \quad v = f_y\frac{Y}{Z} + c_y.$$

The divide-by-$Z$ is the same perspective division from Unit 2; $K$ just applies focal length and shifts by the principal point $(c_x, c_y)$. Entries: $f_x, f_y$ focal lengths in pixels; $c_x, c_y$ the principal point (image center, in pixels); the top-right-ish zero is the **skew** (assumed 0 for modern sensors — axes are perpendicular). $K$ is **upper-triangular** and depends only on the camera, not on where it is in the world (that's extrinsics, Module 2).

## 4. Visual Explanation

`[Visual: the 3×3 matrix K with f_x, f_y, c_x, c_y labeled, acting on (X,Y,Z) then divide-by-Z to land at pixel (u,v) on the image]`

**Diagram Specification**
- **Objective:** show K's structure and its action.
- **Scene:** the matrix $K$ with entries labeled ($f_x, f_y$ = focal length px; $c_x, c_y$ = principal point); an arrow "K·(X,Y,Z) then ÷Z" landing on a pixel $(u,v)$ in an image grid with the principal point marked near center.
- **Labels:** "f_x, f_y: focal length (px)," "c_x, c_y: principal point," "÷Z: perspective," "u = f_x X/Z + c_x."
- **Form:** SVG.

## 5. Engineering Example

When the robot's perception code projects a candidate 3D point or undistorts a detection, it uses this camera's $K$, loaded once from calibration. OpenCV's `projectPoints` and friends take exactly this $K$ (plus distortion, Unit 5). Because $K$ depends only on the camera, it's a fixed asset: calibrate once, reuse every frame. Getting $K$ right is what makes a pixel detection convertible into an accurate direction.

## 6. Worked Example

$K$ with $f_x = f_y = 800$, principal point $(c_x, c_y) = (320, 240)$ (center of a $640\times480$ image). Point $(X,Y,Z) = (0.06, -0.03, 0.3)$:
$$u = 800\cdot\frac{0.06}{0.3} + 320 = 160 + 320 = 480, \qquad v = 800\cdot\frac{-0.03}{0.3} + 240 = -80 + 240 = 160.$$
So the tomato images at pixel $(480, 160)$. The $(160, -80)$ from Unit 2 were offsets from center; adding $(c_x, c_y)$ turns them into absolute pixel coordinates. A point straight ahead $(0,0,Z)$ images exactly at the principal point $(320, 240)$.

## 7. Interactive Demonstration

**Guided prediction.** With $f_x = f_y = 800$ and principal point $(320, 240)$, predict the pixel for a point straight ahead $(0,0,0.5)$, then for $(0.06, -0.03, 0.3)$. Predict how $u$ changes if $c_x$ increases by 50. Confirm $u = f_x X/Z + c_x$.

## 8. Coding Exercise

Build $K$ from $f_x, f_y, c_x, c_y$; implement `project_K(P, K)` doing $K\mathbf{P}$ then divide-by-$Z$; verify the worked example gives $(480, 160)$ and that $(0,0,Z)$ maps to the principal point.

## 9. Knowledge Check

A check on the structure of $K$, applying it with the divide-by-$Z$, and interpreting $f_x, f_y, c_x, c_y$.

## 10. Challenge Problem

Show that any point with $X = Y = 0$ (on the optical axis) projects to the principal point regardless of $Z$. Then explain why $K$ alone cannot tell you *where the camera is* — only how it turns directions into pixels.

## 11. Common Mistakes

- Forgetting the divide-by-$Z$ after multiplying by $K$.
- Swapping $f$ and $c$ roles, or putting the principal point in the wrong entries.
- Thinking $K$ encodes camera position (that's extrinsics, not intrinsics).

## 12. Key Takeaways

- $K = \begin{bmatrix} f_x & 0 & c_x \\ 0 & f_y & c_y \\ 0 & 0 & 1\end{bmatrix}$ packages **focal length** and **principal point**.
- Projection in pixels: $\tilde{\mathbf p} = K(X,Y,Z)$, then **divide by $Z$** → $u = f_x X/Z + c_x$.
- $K$ depends only on the **camera** (intrinsics), not its pose (extrinsics).
- A point on the optical axis images at the **principal point**.

---

## AI Learning Companion

Copy any prompt below into ChatGPT, Claude, or another AI assistant.

**Tutor prompt** — explain it another way
```
Explain Lesson 3.2 (Module 3) — The Intrinsic Matrix K — as the camera's translator from a 3D direction to a pixel. Write K, show u = f_x·X/Z + c_x via K·(X,Y,Z) then divide-by-Z, and interpret each entry.
```

**Practice prompt** — generate more exercises
```
Give me 6 exercises building K and projecting camera-frame points to pixels with the divide-by-Z, including points on the optical axis. Include answers.
```

**Explore prompt** — connect it to the real world
```
Show me how OpenCV uses the intrinsic matrix K, why it's calibrated once and reused, and why it depends only on the camera, not its pose.
```

## Global Learning Support

Need this lesson explained in another language? Copy one of the prompts below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

**Español**
```
I just completed Lesson 3.2 (Module 3) — The Intrinsic Matrix K.
Explain this lesson in Spanish. Keep robotics and mathematical terminology in English when appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

**中文 (Simplified Chinese)**
```
I just completed Lesson 3.2 (Module 3) — The Intrinsic Matrix K.
Explain this lesson in Simplified Chinese. Keep mathematical notation unchanged.
Then provide: a summary, three practice questions, and one challenge problem.
```

**Türkçe**
```
I just completed Lesson 3.2 (Module 3) — The Intrinsic Matrix K.
Explain this lesson in Turkish. Keep robotics terminology in English where commonly used.
Then provide: a summary, three practice questions, and one challenge problem.
```

---

*Next lesson: 3.3 — Principal Point and Focal Length in Pixels.*
