---
module: 02
unit: 03
lesson: 3.3
title: Applying SE(2) to Points and Shapes
core_idea: "Multiplying an SE(2) matrix by a homogeneous point moves that point rigidly; applied to every point, it moves a whole shape as one."
estimated_time: 45
difficulty: Introductory
prerequisites: [3.2]
learning_objectives:
  - Apply an SE(2) matrix to a homogeneous point.
  - Transform a whole shape by transforming all its points.
  - Confirm the result is rigid (distances preserved).
tags:
  - physical-ai
  - transformations
  - se2
---

# Lesson 3.3 — Applying SE(2) to Points and Shapes

## 1. Why This Matters

An SE(2) matrix is only useful once you *apply* it. Multiplying it by a point gives that point's new location after the rigid move; applying it to every point of a shape carries the whole shape — a fruit cluster, the gripper outline, a detected bounding box — as one rigid unit. This is the everyday operation of a planar robot: "where does this land after the move?" is one matrix-times-vector.

## 2. Physical Intuition

Stamp the move onto each point. Take the gripper's outline, written as a handful of points; multiply each by the SE(2) matrix; the outline reappears turned and shifted, exactly the same size and shape. Because the matrix is rigid, you can transform just a few key points and trust the rest of the shape follows faithfully — nothing warps. It's the difference between *describing* a move and *carrying it out* on real coordinates.

## 3. Mathematical Foundations

Apply SE(2) matrix $T$ to a homogeneous point $\mathbf{p} = (x, y, 1)$:

$$T\mathbf{p} = \begin{bmatrix} \cos\theta & -\sin\theta & t_x \\ \sin\theta & \cos\theta & t_y \\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} x \\ y \\ 1 \end{bmatrix} = \begin{bmatrix} x\cos\theta - y\sin\theta + t_x \\ x\sin\theta + y\cos\theta + t_y \\ 1 \end{bmatrix}.$$

The point is rotated by $\theta$ and shifted by $(t_x, t_y)$, in one multiply. For a shape, stack its points as columns of a $3\times n$ matrix $P$ and compute $T P$ — every column transforms identically. Directions (Lesson 2.2) carry $w=0$, so they rotate but don't translate. Because $T$ is rigid, the output preserves all pairwise distances: $\lVert T\mathbf{p} - T\mathbf{q}\rVert = \lVert \mathbf{p}-\mathbf{q}\rVert$.

## 4. Visual Explanation

`[Visual: a gripper-outline shape (ghost) and its SE(2)-transformed copy, same size, turned and shifted; one edge length labeled identical in both]`

**Diagram Specification**
- **Objective:** show a whole shape moved rigidly by applying SE(2) to all its points.
- **Scene:** a small polygon (gripper outline) shown as ghost at the origin and solid after T (rotated θ, moved (tx,ty)); dashed arrows from a couple of original vertices to their images; one edge labeled with the same length in both copies.
- **Labels:** "apply T to every point," "θ," "(tx, ty)," "same edge length (rigid)."
- **Form:** SVG.

## 5. Engineering Example

A detected fruit cluster arrives as a set of points in one frame; applying the frame's SE(2) transform relocates the whole cluster into the robot's planning frame in a single matrix multiply over all points. The gripper's footprint is swept through a candidate pose the same way to check for collisions — transform the outline, test the result. One matrix, many points, rigidly.

## 6. Worked Example

Apply $T$ with $\theta = 90°$, $(t_x, t_y) = (2, 1)$ to the point $(1, 0)$:
$$T(1,0,1)^\top = (1\cdot 0 - 0\cdot 1 + 2,\ 1\cdot 1 + 0\cdot 0 + 1,\ 1) = (2, 2, 1) \Rightarrow (2, 2).$$
Apply the same $T$ to $(0, 0)$: $(2, 1)$. Check rigidity: original points $(1,0)$ and $(0,0)$ are $1$ apart; images $(2,2)$ and $(2,1)$ are also $1$ apart. The shape moved without deforming.

## 7. Interactive Demonstration

Set the rotation θ and translation (tx, ty) of an SE(2) transform and watch a greenhouse-object outline move rigidly — same size, new pose. An **inverse** control sends the shape back to where it started, previewing the next lesson. The matrix and a tracked edge-length readout are shown so you can confirm the motion is rigid.

## 8. Coding Exercise

Build an SE(2) matrix, apply it to a shape stored as a 3×n array of homogeneous points, plot or print before/after, and assert pairwise distances are unchanged.

## 9. Knowledge Check

A check that applying SE(2) rotates+translates a point in one multiply, transforms a shape point-by-point, and preserves distances.

## 10. Challenge Problem

You transform a 4-point square with an SE(2) matrix and find one pair of transformed points is farther apart than before. What must have gone wrong (since SE(2) is rigid), and where would you look in the matrix?

## 11. Common Mistakes

- Forgetting the homogeneous "1" on points (translation then misbehaves).
- Translating directions (w=0) that should only rotate.
- Concluding the shape deformed when a coordinate change is just the rigid move re-described.

## 12. Key Takeaways

- Applying SE(2) to a point: one matrix multiply rotates and shifts it.
- Transform a **shape** by transforming all its points ($T P$).
- The motion is **rigid** — all distances/angles preserved.
- Directions (w=0) rotate but don't translate.

---

## AI Learning Companion

Copy any prompt below into ChatGPT, Claude, or another AI assistant.

**Tutor prompt** — explain it another way
```
Explain Lesson 3.3 (Module 2) — Applying SE(2) to Points and Shapes — by stamping a rigid move onto each point of a gripper outline. Show the matrix-times-point computation and why the shape keeps its size.
```

**Practice prompt** — generate more exercises
```
Give me 6 exercises applying SE(2) matrices to points and small shapes, computing the new coordinates and checking that distances are preserved. Include answers.
```

**Explore prompt** — connect it to the real world
```
Show me how a robot transforms a whole detected fruit cluster or a gripper footprint by applying one SE(2) matrix to all its points.
```

## Global Learning Support

Need this lesson explained in another language? Copy one of the prompts below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

**Español**
```
I just completed Lesson 3.3 (Module 2) — Applying SE(2) to Points and Shapes.
Explain this lesson in Spanish. Keep robotics and mathematical terminology in English when appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

**中文 (Simplified Chinese)**
```
I just completed Lesson 3.3 (Module 2) — Applying SE(2) to Points and Shapes.
Explain this lesson in Simplified Chinese. Keep mathematical notation unchanged.
Then provide: a summary, three practice questions, and one challenge problem.
```

**Türkçe**
```
I just completed Lesson 3.3 (Module 2) — Applying SE(2) to Points and Shapes.
Explain this lesson in Turkish. Keep robotics terminology in English where commonly used.
Then provide: a summary, three practice questions, and one challenge problem.
```

---

*Next lesson: 3.4 — Inverse Transformations (how do I go back?).*
