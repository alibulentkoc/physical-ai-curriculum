---
module: 02
unit: 04
lesson: 4.4
title: Translation Vectors in 3D
core_idea: "The translation part of an SE(3) pose is a 3D vector (tx, ty, tz) giving the position; in homogeneous form it sits in the last column."
estimated_time: 40
difficulty: Introductory
prerequisites: [4.3]
learning_objectives:
  - Interpret the SE(3) translation column as a 3D position vector.
  - Distinguish 3D points (w=1) from 3D directions (w=0).
  - Combine a 3D rotation and a 3D translation into one pose.
tags:
  - physical-ai
  - transformations
  - se3
---

# Lesson 4.4 — Translation Vectors in 3D

## 1. Why This Matters

Half of an SE(3) pose is *where* — the translation. In 3D that's a vector with three components $(t_x, t_y, t_z)$: how far along each axis the object sits. It's the direct generalization of the 2D translation column, and it's where a robot reads a fruit's or a gripper's **position in space**. Pairing this 3D position with the 3D rotation from Lesson 4.2 completes the full pose.

## 2. Physical Intuition

To tell a friend where something is in a room you give three numbers: how far right, how far forward, how far up. That triple is the translation vector. In the SE(3) matrix it lives in the **last column** — the same slot as the 2D case, just one entry taller. And the homogeneous bookkeeping from Unit 2 carries over unchanged: a **point** (a location) is $(x, y, z, 1)$ and *translates*; a **direction** (like a surface normal or an approach axis) is $(x, y, z, 0)$ and is rotated but *not* translated.

## 3. Mathematical Foundations

A 3D **point** in homogeneous form is $(x, y, z, 1)$; a 3D **direction** is $(x, y, z, 0)$. The SE(3) translation column $\mathbf{t} = (t_x, t_y, t_z)$ adds to a point's position because its $w=1$ multiplies the column; for a direction, $w=0$ zeroes the column, so directions only rotate. Applying SE(3):

$$T\begin{bmatrix}\mathbf{p}\\1\end{bmatrix} = \begin{bmatrix} R\mathbf{p} + \mathbf{t} \\ 1 \end{bmatrix}, \qquad T\begin{bmatrix}\mathbf{d}\\0\end{bmatrix} = \begin{bmatrix} R\mathbf{d} \\ 0 \end{bmatrix}.$$

A point is rotated and then offset by $\mathbf{t}$; a direction is only rotated. This is exactly the Unit 2 rule (points vs directions) in 3D.

## 4. Visual Explanation

`[Visual: faux-3D isometric — the translation vector (tx,ty,tz) drawn from origin to a gripper's position; a point (w=1) offset by t while a direction arrow (w=0) only rotates]`

**Diagram Specification**
- **Objective:** show the 3D translation vector as position, and the point-vs-direction rule in 3D.
- **Scene:** faux-3D isometric: origin with x,y,z axes; a translation vector to a gripper position with components (tx,ty,tz) shown as steps along each axis; a small inset: a point moves under translation while a direction arrow keeps its heading.
- **Labels:** "t = (tx, ty, tz)," "point (w=1): rotates + translates," "direction (w=0): rotates only."
- **Form:** SVG (faux-3D isometric).

## 5. Engineering Example

The camera's offset from the arm is a 3D translation vector (e.g. 5 cm back, 2 cm left, 25 cm down). A fruit's position in the camera frame is a 3D point ($w=1$) — it picks up offsets when re-framed. The fruit's surface normal (which way it faces) is a direction ($w=0$) — it must rotate with frames but never gain an offset. Tagging each correctly is what keeps positions and orientations consistent through the pipeline.

## 6. Worked Example

SE(3) with $R = I$ (no rotation) and $\mathbf{t} = (0.4, 0.3, 0.9)$. Apply to the point $(0,0,0,1)$: result $(0.4, 0.3, 0.9, 1)$ — moved to the translation. Apply the same to the direction $(0,0,1,0)$ (pointing up): result $(0,0,1,0)$ — unchanged, because $w=0$ zeroes the translation. Now add a rotation $R_z(90°)$: the point would rotate then offset; the direction would only rotate.

## 7. Interactive Demonstration

**Guided prediction.** A gripper sits at translation $(0.4, 0.3, 0.9)$. Predict the result of applying this SE(3) (with no rotation) to the point $(0,0,0,1)$ and to the direction $(0,0,1,0)$. Which one ends up at $(0.4, 0.3, 0.9)$ and which is unchanged? Predict how the answers change if a rotation is added to the block.

## 8. Coding Exercise

Build an SE(3) with a translation vector and identity rotation; apply it to a 3D point (w=1) and a 3D direction (w=0); confirm only the point moves. Then add a rotation and observe both rotate.

## 9. Knowledge Check

A check that the translation column is a 3D position vector, that w=1 points translate and w=0 directions don't, and that a point is rotated then offset.

## 10. Challenge Problem

A robot stores a fruit's position and its surface normal. After re-expressing both in a rotated, offset frame, which gains the offset and which doesn't? Explain using the w-coordinate and the SE(3) application rule.

## 11. Common Mistakes

- Tagging a 3D direction with $w=1$ (it then wrongly translates).
- Putting the translation vector in the bottom row instead of the last column.
- Forgetting a point is rotated *and* offset, while a direction is only rotated.

## 12. Key Takeaways

- The SE(3) **translation** is a 3D vector $(t_x, t_y, t_z)$ in the last column — the object's **position**.
- 3D **points** $(x,y,z,1)$ rotate **and** translate; 3D **directions** $(x,y,z,0)$ only rotate.
- $T(\mathbf{p}) = R\mathbf{p} + \mathbf{t}$ for points; $T(\mathbf{d}) = R\mathbf{d}$ for directions.
- This is the Unit 2 point/direction rule, in 3D.

---

## AI Learning Companion

Copy any prompt below into ChatGPT, Claude, or another AI assistant.

**Tutor prompt** — explain it another way
```
Explain Lesson 4.4 (Module 2) — Translation Vectors in 3D — using "how far right, forward, up" as the translation vector (tx,ty,tz) in the SE(3) last column. Cover why 3D points (w=1) translate but 3D directions (w=0) only rotate.
```

**Practice prompt** — generate more exercises
```
Give me 6 exercises applying an SE(3) translation to 3D points (w=1) and directions (w=0), with and without a rotation. Include answers.
```

**Explore prompt** — connect it to the real world
```
Show me how a camera's 3D mounting offset is a translation vector, and why a fruit's position (point) and its surface normal (direction) behave differently when re-framed.
```

## Global Learning Support

Need this lesson explained in another language? Copy one of the prompts below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

**Español**
```
I just completed Lesson 4.4 (Module 2) — Translation Vectors in 3D.
Explain this lesson in Spanish. Keep robotics and mathematical terminology in English when appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

**中文 (Simplified Chinese)**
```
I just completed Lesson 4.4 (Module 2) — Translation Vectors in 3D.
Explain this lesson in Simplified Chinese. Keep mathematical notation unchanged.
Then provide: a summary, three practice questions, and one challenge problem.
```

**Türkçe**
```
I just completed Lesson 4.4 (Module 2) — Translation Vectors in 3D.
Explain this lesson in Turkish. Keep robotics terminology in English where commonly used.
Then provide: a summary, three practice questions, and one challenge problem.
```

---

*Next lesson: 4.5 — Applying SE(3); Inverses in 3D.*
