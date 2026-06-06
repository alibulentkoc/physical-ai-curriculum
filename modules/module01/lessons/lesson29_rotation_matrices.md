---
module: 01
unit: 04
lesson: 4.5
title: Rotation Matrices
core_idea: "A rotation matrix turns all of space about the origin by an angle, preserving lengths and shapes — orientation changes, size does not."
estimated_time: 50
difficulty: Introductory
prerequisites: [4.4]
learning_objectives:
  - Describe a rotation matrix as the operator that turns space about the origin by angle theta.
  - Apply a rotation to points and confirm distances from the origin are preserved.
  - Connect rotation to reorienting a gripper or camera.
tags:
  - physical-ai
  - transformations
---

# Lesson 4.5 — Rotation Matrices

## 1. Why This Matters

Now a matrix that *does* something visible: a **rotation** turns space about the origin by an angle $\theta$. Reorienting the gripper to align with a tomato's stem, swinging the camera's view, spinning a part to a target pose — these are rotations. Crucially, a rotation changes **orientation but not size**: lengths and shapes are preserved, only the heading changes. This is the cleanest example of "a matrix is an action," and the one you'll use constantly.

## 2. Physical Intuition

Pin the origin and turn the whole plane like a record on a turntable by angle $\theta$. Every point swings along a circle around the origin; points farther out travel farther, but each keeps its **distance** from the center. A fruit cluster keeps its shape and size — it just faces a new direction. Set $\theta=0$ and nothing turns (that's the identity from 4.4). Increase $\theta$ toward 360° and the shape comes all the way back around.

## 3. Mathematical Foundations

The 2D rotation matrix for a counterclockwise angle $\theta$ about the origin:

$$R(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}, \qquad R(\theta)\,(x,y) = (x\cos\theta - y\sin\theta,\ x\sin\theta + y\cos\theta).$$

Its columns are where the unit arrows land: $(1,0)\to(\cos\theta,\sin\theta)$ and $(0,1)\to(-\sin\theta,\cos\theta)$ — both still unit-length and still perpendicular, which is why rotation preserves lengths and angles. $R(0)=I$ (the identity). Rotations compose by adding angles: $R(\alpha)R(\beta)=R(\alpha+\beta)$.

## 4. Visual Explanation

`[Visual: a greenhouse object rotated about the origin by theta, with a ghost of the original and the angle marked; points move along circles]`

**Diagram Specification**
- **Objective:** show rotation as turning space about the origin, preserving size, changing orientation.
- **Scene:** origin; faint original (ghost) shape and a solid rotated shape; an arc marking theta; a dashed circle through one point showing its distance from the origin is unchanged.
- **Labels:** "rotate by theta," "origin," "distance preserved," "R(theta)."
- **Form:** SVG.

## 5. Engineering Example

To grasp a tomato whose stem runs at 30°, the controller rotates the gripper's approach frame by 30° — a rotation matrix applied to the gripper's orientation. The camera gimbal that keeps a target centered as the robot turns applies the opposite rotation. In both, only orientation changes; the physical sizes of gripper and target are untouched — exactly the rotation property.

## 6. Worked Example

Rotate $\mathbf{p}=(1,0)$ by $\theta=90°$: $\cos90°=0,\ \sin90°=1$, so $R(90°)(1,0)=(1\cdot0 - 0\cdot1,\ 1\cdot1 + 0\cdot0) = (0,1)$. East became north. Distance from origin: $|(1,0)|=1=|(0,1)|$ — preserved. Rotating $(0,1)$ by another 90° gives $(-1,0)$, consistent with $R(90°)R(90°)=R(180°)$.

## 7. Interactive Demonstration

Drag a single slider from 0° to 360° and watch the greenhouse object turn about the origin — size constant, orientation changing — with the rotation matrix shown live.

## 8. Coding Exercise

Build $R(\theta)$ in NumPy, rotate a set of points, and confirm each point's distance from the origin is unchanged (rotation preserves length).

## 9. Knowledge Check

A check that rotation turns space about the origin, preserves distances, and that $R(0)=I$.

## 10. Challenge Problem

Show (by applying it) that rotating by 90° twice equals rotating by 180°, and explain why $R(\alpha)R(\beta)=R(\alpha+\beta)$ makes sense geometrically.

## 11. Common Mistakes

- Mixing up the sign of $\sin\theta$ (clockwise vs counterclockwise).
- Forgetting rotation is about the **origin** — a shape away from the origin also orbits it.
- Thinking rotation changes size; it never does.

## 12. Key Takeaways

- A **rotation matrix** $R(\theta)$ turns space about the origin by $\theta$.
- It **preserves lengths and shapes**; only orientation changes.
- $R(0)=I$; rotations compose by adding angles.
- Rotation is the workhorse for reorienting grippers and cameras.

---

## AI Learning Companion

Copy any prompt below into ChatGPT, Claude, or another AI assistant.

**Tutor prompt** — explain it another way
```
Explain Lesson 4.5 (Rotation Matrices) using a turntable spinning the plane about the origin. Make clear that rotation preserves size and distance and only changes orientation, and what R(theta)'s columns mean.
```

**Practice prompt** — generate more exercises
```
Give me 6 exercises rotating points by angles like 90, 180, 45 degrees about the origin, confirming distances are preserved. Include answers.
```

**Explore prompt** — connect it to the real world
```
Show me how a robot uses rotation matrices to reorient a gripper to a tilted object or to keep a camera pointed at a target.
```

## Global Learning Support

Need this lesson explained in another language? Copy one of the prompts below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

**Español**
```
I just completed Lesson 4.5 — Rotation Matrices.
Explain this lesson in Spanish. Keep robotics and mathematical terminology in English when appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

**中文 (Simplified Chinese)**
```
I just completed Lesson 4.5 — Rotation Matrices.
Explain this lesson in Simplified Chinese. Keep mathematical notation unchanged.
Then provide: a summary, three practice questions, and one challenge problem.
```

**Türkçe**
```
I just completed Lesson 4.5 — Rotation Matrices.
Explain this lesson in Turkish. Keep robotics terminology in English where commonly used.
Then provide: a summary, three practice questions, and one challenge problem.
```

---

*Next lesson: 4.6 — Scaling Transformations (stretching and shrinking space).*
