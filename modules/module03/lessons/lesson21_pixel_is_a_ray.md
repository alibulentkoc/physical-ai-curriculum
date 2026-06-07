---
module: 03
unit: 06
lesson: 6.1
title: A Pixel Is a Ray
core_idea: "Back-projection turns a pixel into a ray through the camera center: the pixel fixes a direction but not a distance, so one image cannot place the point in depth."
estimated_time: 40
difficulty: Core
prerequisites: [5.4]
learning_objectives:
  - Explain why a pixel corresponds to a ray, not a point.
  - Construct the back-projected ray from an undistorted pixel.
  - Connect this to the depth ambiguity from Unit 1.
tags:
  - physical-ai
  - perception
  - back-projection
---

# Lesson 6.1 — A Pixel Is a Ray

## 1. Why This Matters

In Unit 1 we learned the painful truth of perception: a single image discards depth. Now we make that precise and *useful*. **Back-projection** is the inverse of projection — but because projection is many-to-one, the inverse of a single pixel is not a point, it's a whole **ray**: the set of all 3D points that would project to that pixel. This is the foundation for recovering 3D: the pixel gives us the *direction*, and the next lessons add depth to pin down the *point*.

## 2. Physical Intuition

Stand at the camera's pinhole and look out through one pixel. Everything along that line of sight — a nearby leaf, a fruit behind it, a wall far away — lands on the *same* pixel. So when you see a bright spot at a pixel, you know the object lies *somewhere along that ray* shooting out from the camera center through that pixel, but you don't know how far. The pixel fixes a direction in space and nothing more. Recovering the point means answering "how far along the ray?" — which needs extra information (depth).

## 3. Mathematical Foundations

Given an **undistorted** pixel $(u, v)$ (Unit 5 made it obey the ideal pinhole), apply $K^{-1}$ to get the normalized direction:

$$x_n = \frac{u - c_x}{f_x}, \qquad y_n = \frac{v - c_y}{f_y}.$$

The back-projected ray, in the camera frame, is all points

$$\mathbf{P}_c(\lambda) = \lambda \begin{bmatrix} x_n \\ y_n \\ 1 \end{bmatrix}, \quad \lambda > 0,$$

a line from the camera center (origin) through the direction $(x_n, y_n, 1)$. Every point on this ray projects back to $(u,v)$: projecting $\lambda(x_n,y_n,1)$ gives $u = f_x (\lambda x_n)/(\lambda) + c_x = f_x x_n + c_x$, independent of $\lambda$. The parameter $\lambda$ is exactly the depth $Z_c$ (since the third component is $\lambda$). So **the pixel fixes the ray's direction; $\lambda = Z_c$ (depth) selects the point.** One image gives the direction; it cannot give $\lambda$.

## 4. Visual Explanation

`[Visual: a single pixel back-projected into a ray from the camera center; several candidate 3D points along the ray all project to the same pixel]`

**Diagram Specification**
- **Objective:** show a pixel as a ray, with depth ambiguity.
- **Scene:** a camera center; a ray shooting through one image pixel into the scene; three candidate points (near, mid, far) on the ray, each with a dashed line back to the same pixel; a "?" on the depth.
- **Labels:** "pixel (u,v)," "K⁻¹ → direction (x_n,y_n,1)," "ray P_c(λ)=λ(x_n,y_n,1)," "λ = depth = unknown from one image."
- **Form:** SVG (faux-3D).

## 5. Engineering Example

When the robot's detector reports "fruit at pixel (480,160)," the perception code back-projects that pixel into a ray in the camera frame. That ray is the robot's knowledge from one image: the fruit is *somewhere along it*. To grasp, the robot must resolve depth — from a depth camera, stereo, or known geometry — which the next lessons add. The ray itself is already useful: it constrains the search and points the arm in the right direction.

## 6. Worked Example

Undistorted pixel $(u,v) = (480, 160)$, $K$ with $f_x=f_y=800$, principal point $(320,240)$. Direction: $x_n = (480-320)/800 = 0.2$, $y_n = (160-240)/800 = -0.1$. Ray: $\mathbf{P}_c(\lambda) = \lambda(0.2, -0.1, 1)$. At $\lambda = 0.3$ m: $(0.06, -0.03, 0.3)$ — the very point from Unit 3 that projected to $(480,160)$. At $\lambda = 0.6$: $(0.12, -0.06, 0.6)$, which *also* projects to $(480,160)$. Same pixel, two depths — the ambiguity made concrete.

## 7. Interactive Demonstration

**Guided prediction.** For pixel $(480,160)$ with the $K$ above, compute the ray direction $(x_n,y_n,1)$. Predict the 3D point at $\lambda=0.3$ and at $\lambda=0.5$, and confirm both project back to $(480,160)$. Predict what a pixel at the principal point back-projects to (direction?).

## 8. Coding Exercise

Implement `backproject_ray(u,v,K)` returning the direction $(x_n,y_n,1)$; sample points $\lambda d$ for several $\lambda$ and verify each projects back to $(u,v)$; show the principal point yields direction $(0,0,1)$ (straight ahead).

## 9. Knowledge Check

A check that a pixel maps to a ray (not a point), how the direction is built with $K^{-1}$, and that depth $\lambda$ is unknown from one image.

## 10. Challenge Problem

Two different fruits project to the *same* pixel in one image. Explain, using the ray, why the camera cannot distinguish them from that image alone, and what single extra measurement would separate them.

## 11. Common Mistakes

- Treating a back-projected pixel as a 3D point (it's a ray).
- Forgetting to undistort before back-projecting.
- Thinking direction includes depth (the "1" in $(x_n,y_n,1)$ is a direction convention, not a known $Z$).

## 12. Key Takeaways

- **Back-projection** of a pixel is a **ray** from the camera center, not a point.
- Direction from $K^{-1}$: $(x_n, y_n, 1)$ with $x_n=(u-c_x)/f_x$, $y_n=(v-c_y)/f_y$.
- The ray is $\mathbf{P}_c(\lambda)=\lambda(x_n,y_n,1)$; $\lambda = Z_c$ (depth) is unknown from one image.
- Undistort first; the ray gives direction, depth must come from elsewhere.

---

## AI Learning Companion

Copy any prompt below into ChatGPT, Claude, or another AI assistant.

**Tutor prompt** — explain it another way
```
Explain Lesson 6.1 (Module 3) — A Pixel Is a Ray — by looking out through one pixel from the camera center. Show the ray P_c(λ)=λ(x_n,y_n,1) from K⁻¹, and why depth λ is unknown from one image.
```

**Practice prompt** — generate more exercises
```
Give me 6 exercises back-projecting pixels into rays with given K and checking that multiple depths project to the same pixel. Include answers.
```

**Explore prompt** — connect it to the real world
```
Show me how a robot uses a back-projected ray from a fruit detection and why it still needs depth to grasp.
```

## Global Learning Support

Need this lesson explained in another language? Copy one of the prompts below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

**Español**
```
I just completed Lesson 6.1 (Module 3) — A Pixel Is a Ray.
Explain this lesson in Spanish. Keep robotics and mathematical terminology in English when appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

**中文 (Simplified Chinese)**
```
I just completed Lesson 6.1 (Module 3) — A Pixel Is a Ray.
Explain this lesson in Simplified Chinese. Keep mathematical notation unchanged.
Then provide: a summary, three practice questions, and one challenge problem.
```

**Türkçe**
```
I just completed Lesson 6.1 (Module 3) — A Pixel Is a Ray.
Explain this lesson in Turkish. Keep robotics terminology in English where commonly used.
Then provide: a summary, three practice questions, and one challenge problem.
```

---

*Next lesson: 6.2 — Adding Depth Recovers a Point.*
