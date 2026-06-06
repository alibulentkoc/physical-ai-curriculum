---
module: 02
unit: 06
lesson: 6.3
title: Reading and Writing Poses
core_idea: "A pose can be read from or written to its matrix; as the robot moves, its pose updates by composing the motion onto the old pose."
estimated_time: 45
difficulty: Introductory
prerequisites: [6.2]
learning_objectives:
  - Read position and orientation out of a pose matrix.
  - Write a pose matrix from a position and orientation.
  - Update a stored pose as the robot moves by composing the motion.
tags:
  - physical-ai
  - transformations
  - pose
---

# Lesson 6.3 — Reading and Writing Poses

## 1. Why This Matters

Poses aren't static — the robot moves, and its pose must stay current. This lesson covers the practical mechanics: **reading** position and orientation out of a pose matrix, **writing** a pose matrix from given values, and **updating** a pose as the robot drives or the arm swings. Updating is where Unit 5 pays off again: a motion is a transform, and applying it to the old pose by composition gives the new pose.

## 2. Physical Intuition

A pose is like a labeled pin on a map with a little arrow for facing. **Reading** it: look at where the pin is (position) and where the arrow points (orientation). **Writing** it: place the pin and aim the arrow. **Updating**: when the robot rolls forward half a meter and turns, you don't recompute from scratch — you take the old pin-and-arrow and apply the move to it. The new pose is the motion *composed onto* the old pose. Move again, compose again; the pose tracks the robot continuously.

## 3. Mathematical Foundations

From a pose matrix $T = \begin{bmatrix} R & \mathbf{t} \\ \mathbf{0}^\top & 1\end{bmatrix}$: the **position** is the translation column $\mathbf{t}$; the **orientation** is the rotation block $R$ (which you can summarize as an angle in 2D, or axis–angle in 3D). To **write** a pose, place $R$ and $\mathbf{t}$ into the blocks. To **update** when the robot undergoes a motion $\Delta$ (itself an SE(2)/SE(3) transform):

$$T_{\text{new}} = T_{\text{old}}\,\Delta \quad\text{(motion expressed in the robot's own frame)}$$
$$\text{or}\quad T_{\text{new}} = \Delta\,T_{\text{old}} \quad\text{(motion expressed in the world frame).}$$

Which side you multiply on depends on whether the motion is described in the robot's frame (right-multiply) or the world frame (left-multiply) — a direct consequence of composition order (Unit 5). Either way, updating a pose is one matrix multiply.

## 4. Visual Explanation

`[Visual: a robot pose (frame) before and after a move; the motion transform applied to the old pose yields the new pose; position and orientation labeled on each]`

**Diagram Specification**
- **Objective:** show read (position/orientation off the matrix) and update (compose motion onto old pose).
- **Scene:** top-down: a robot frame at an old pose with position/heading labeled; an arrow "motion Δ"; the new pose frame after composing; small matrix snippets showing t (position) and R (orientation).
- **Labels:** "read: t = position, R = orientation," "update: T_new = T_old · Δ," "old pose," "new pose."
- **Form:** SVG.

## 5. Engineering Example

A mobile base keeps its world pose as an SE(3) matrix. Each control step it has a small motion (from wheel odometry) expressed in its own frame; it right-multiplies that onto its pose to get the new one. The arm does the same as joints move. Reading the pose gives the planner the current position and heading; writing/initializing a pose sets a known start. All three operations are matrix reads, writes, and one multiply.

## 6. Worked Example

Old pose: at $(2, 1)$ heading $0°$ (2D), $T_{\text{old}} = \begin{bmatrix}1&0&2\\0&1&1\\0&0&1\end{bmatrix}$. Motion in the robot's own frame: drive forward (its +x) by 1, then turn $90°$ — $\Delta = $ translate $(1,0)$ then rotate $90°$. Update: $T_{\text{new}} = T_{\text{old}}\,\Delta$ places the robot at $(3, 1)$ now heading $90°$. Reading $T_{\text{new}}$: position $(3,1)$, orientation $90°$.

## 7. Interactive Demonstration

**Guided prediction.** A robot at $(2,1)$ heading $0°$ drives forward 1 (its own frame) and turns $90°$. Predict its new position and heading, and whether you'd right-multiply (motion in robot frame) or left-multiply (motion in world frame) the motion onto the old pose. Confirm by reading position and orientation off the updated matrix.

## 8. Coding Exercise

Write a pose from (x, y, θ); read (x, y, θ) back; apply a robot-frame motion by right-multiplication and a world-frame motion by left-multiplication; confirm the resulting positions/orientations.

## 9. Knowledge Check

A check on reading position/orientation from a pose, writing a pose, and updating by composing a motion (right vs left multiply).

## 10. Challenge Problem

The same physical motion is described once in the robot's frame and once in the world frame. Explain why one is a right-multiply and the other a left-multiply, and when they give the same result.

## 11. Common Mistakes

- Reading position from the bottom row instead of the translation column.
- Multiplying the motion on the wrong side (robot-frame vs world-frame).
- Recomputing the pose from scratch instead of composing the incremental motion.

## 12. Key Takeaways

- **Read** a pose: position = translation column, orientation = rotation block.
- **Write** a pose: place $R$ and $\mathbf{t}$ into the blocks.
- **Update**: compose the motion onto the old pose — right-multiply (robot frame) or left-multiply (world frame).
- Updating a pose is one matrix multiply, every control step.

---

## AI Learning Companion

Copy any prompt below into ChatGPT, Claude, or another AI assistant.

**Tutor prompt** — explain it another way
```
Explain Lesson 6.3 (Module 2) — Reading and Writing Poses — using a pin-and-arrow on a map: reading position/orientation, writing a new pose, and updating by composing a motion onto the old pose. Cover right vs left multiplication.
```

**Practice prompt** — generate more exercises
```
Give me 6 exercises reading/writing pose matrices and updating a pose with a robot-frame or world-frame motion. Include answers.
```

**Explore prompt** — connect it to the real world
```
Show me how a mobile base updates its world pose each control step by composing an odometry motion, and how the planner reads the current position and heading.
```

## Global Learning Support

Need this lesson explained in another language? Copy one of the prompts below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

**Español**
```
I just completed Lesson 6.3 (Module 2) — Reading and Writing Poses.
Explain this lesson in Spanish. Keep robotics and mathematical terminology in English when appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

**中文 (Simplified Chinese)**
```
I just completed Lesson 6.3 (Module 2) — Reading and Writing Poses.
Explain this lesson in Simplified Chinese. Keep mathematical notation unchanged.
Then provide: a summary, three practice questions, and one challenge problem.
```

**Türkçe**
```
I just completed Lesson 6.3 (Module 2) — Reading and Writing Poses.
Explain this lesson in Turkish. Keep robotics terminology in English where commonly used.
Then provide: a summary, three practice questions, and one challenge problem.
```

---

*Next lesson: 6.4 — Pose in Physical AI (Unit 6 recap).*
