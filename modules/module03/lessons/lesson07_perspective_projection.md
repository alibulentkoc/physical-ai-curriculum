---
module: 03
unit: 02
lesson: 2.3
title: Perspective Projection of a 3D Point
core_idea: "Perspective projection maps a camera-frame 3D point to image coordinates by dividing by depth — the division by Z is what makes it perspective."
estimated_time: 45
difficulty: Introductory
prerequisites: [2.2]
learning_objectives:
  - Apply the perspective projection equations to a 3D point.
  - Explain the role of the divide-by-Z step.
  - Contrast perspective projection with a depth-independent (orthographic) map.
tags:
  - physical-ai
  - perception
  - projection
---

# Lesson 2.3 — Perspective Projection of a 3D Point

## 1. Why This Matters

This lesson makes the forward map concrete: given a 3D point in the camera frame, compute exactly where it lands on the image. The operation is short — two ratios — but the **divide-by-$Z$** in the middle is the heart of camera geometry. It's why distant things look small, why parallel rails appear to meet, and why projection isn't a rigid transform. Getting fluent with this calculation is the prerequisite for intrinsics and for everything in Unit 4.

## 2. Physical Intuition

Stand on straight railroad tracks and look down them: the rails are parallel, yet they appear to converge to a point on the horizon. Nothing about the rails changed — the *division by distance* did it. Points farther away (bigger $Z$) get pulled toward the image center by the $1/Z$ factor, so the two rails, equally far apart in the world, draw closer in the image as they recede. Perspective projection is exactly this "divide by how far away it is" rule, applied to every point. Without the divide (an *orthographic* map), faraway and near objects would image at the same size — no perspective at all.

## 3. Mathematical Foundations

A camera-frame point $\mathbf{P} = (X, Y, Z)$ with $Z > 0$ (in front of the camera) projects to image-plane coordinates

$$x = f\,\frac{X}{Z}, \qquad y = f\,\frac{Y}{Z}.$$

The shared denominator $Z$ is the perspective division. Compactly, projection is the map $(X, Y, Z) \mapsto (fX/Z,\ fY/Z)$ — **non-linear** in the coordinates (because of the division) and **many-to-one** (all points on a ray share $X/Z, Y/Z$). Contrast **orthographic** projection $(X,Y,Z)\mapsto(X,Y)$, which ignores $Z$: it has no size-with-distance effect and is only a good approximation when depth variation is tiny relative to distance. Real cameras are perspective; the divide-by-$Z$ stays. (Homogeneous coordinates from Module 2 will let us write even this division as a matrix-plus-divide in Unit 3.)

## 4. Visual Explanation

`[Visual: converging rails / a row of equally spaced tomatoes receding in depth, imaged with the divide-by-Z pulling distant ones toward the center]`

**Diagram Specification**
- **Objective:** show perspective division pulling distant points toward the image center.
- **Scene:** a row of equally spaced, equal-size tomatoes receding along +Z; their projected images on the plane getting smaller and closer to the center with depth; two guide rails converging to a vanishing point.
- **Labels:** "equal spacing in world," "converging in image," "x = fX/Z," "divide by Z = perspective."
- **Form:** SVG.

## 5. Engineering Example

When the robot projects a candidate 3D grasp point to check where it appears in the image (or to overlay a marker), it uses exactly $x=fX/Z,\ y=fY/Z$. Conversely, the non-linearity warns the engineer: you cannot average pixel coordinates and expect the average 3D point — perspective doesn't preserve midpoints in depth. Knowing projection is a divide-by-$Z$ map prevents a class of subtle localization bugs.

## 6. Worked Example

Camera focal length $f = 800$ (pixels, anticipating Unit 3). Tomato at $(X,Y,Z) = (0.06, -0.03, 0.3)$ m:
$$x = 800\cdot\frac{0.06}{0.3} = 160, \qquad y = 800\cdot\frac{-0.03}{0.3} = -80.$$
So it images 160 units right and 80 units up/down from the optical-axis intersection. Move it to $Z = 0.6$ m (same $X, Y$): $x = 80,\ y = -40$ — halved, the $1/Z$ effect. (Unit 3 adds the principal point to turn these into actual pixel coordinates.)

## 7. Interactive Demonstration

**Guided prediction.** Take a point $(0.06, 0, Z)$ and predict its image $x = fX/Z$ as $Z$ runs from near to far — does it move toward or away from center? Predict what a row of equally spaced points in depth looks like in the image. Confirm the divide-by-$Z$ produces convergence (perspective), unlike an orthographic map.

## 8. Coding Exercise

Implement `project(P, f)` returning $(fX/Z, fY/Z)$; project a row of equally spaced 3D points receding in depth and plot their image positions; compare against an orthographic map that drops $Z$.

## 9. Knowledge Check

A check on applying $x=fX/Z$, the role of the divide-by-$Z$, and perspective vs orthographic.

## 10. Challenge Problem

Show that two world points equally spaced in depth do **not** project to equally spaced image points, and explain how this convergence relates to the vanishing point of parallel lines.

## 11. Common Mistakes

- Forgetting the divide-by-$Z$ (that's the whole perspective effect).
- Projecting points with $Z \le 0$ (behind the camera) without flagging them.
- Assuming image coordinates combine linearly with 3D coordinates.

## 12. Key Takeaways

- Perspective projection: $x = f\,X/Z,\ y = f\,Y/Z$.
- The **divide-by-$Z$** makes it perspective: distant points pulled toward center; it is **non-linear** and **many-to-one**.
- **Orthographic** projection drops $Z$ — no size-with-distance effect; real cameras are perspective.
- This forward map is the basis for intrinsics (Unit 3).

---

## AI Learning Companion

Copy any prompt below into ChatGPT, Claude, or another AI assistant.

**Tutor prompt** — explain it another way
```
Explain Lesson 2.3 (Module 3) — Perspective Projection of a 3D Point — using converging railroad tracks. Make clear x = fX/Z, that the divide-by-Z is what makes it perspective, and how it differs from orthographic projection.
```

**Practice prompt** — generate more exercises
```
Give me 6 exercises projecting 3D camera-frame points with x = fX/Z, including how the image changes with depth. Include answers.
```

**Explore prompt** — connect it to the real world
```
Show me where a robot uses perspective projection (overlaying a 3D grasp point on the image) and why the divide-by-Z non-linearity matters for localization.
```

## Global Learning Support

Need this lesson explained in another language? Copy one of the prompts below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

**Español**
```
I just completed Lesson 2.3 (Module 3) — Perspective Projection of a 3D Point.
Explain this lesson in Spanish. Keep robotics and mathematical terminology in English when appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

**中文 (Simplified Chinese)**
```
I just completed Lesson 2.3 (Module 3) — Perspective Projection of a 3D Point.
Explain this lesson in Simplified Chinese. Keep mathematical notation unchanged.
Then provide: a summary, three practice questions, and one challenge problem.
```

**Türkçe**
```
I just completed Lesson 2.3 (Module 3) — Perspective Projection of a 3D Point.
Explain this lesson in Turkish. Keep robotics terminology in English where commonly used.
Then provide: a summary, three practice questions, and one challenge problem.
```

---

*Next lesson: 2.4 — The Pinhole Camera Model (Unit 2 recap).*
