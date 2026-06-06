---
module: 02
unit: 02
lesson: 2.2
title: Points vs Directions
core_idea: "The homogeneous w-coordinate distinguishes a point (w=1, a location that translates) from a direction (w=0, an arrow that does not translate)."
estimated_time: 40
difficulty: Introductory
prerequisites: [2.1]
learning_objectives:
  - Distinguish a point (w=1) from a direction (w=0) in homogeneous coordinates.
  - Explain why directions must be immune to translation.
  - Apply the right w-value when transforming positions vs displacements.
tags:
  - physical-ai
  - transformations
  - homogeneous
---

# Lesson 2.2 — Points vs Directions

## 1. Why This Matters

Homogeneous coordinates quietly encode a deep distinction: some things are **locations** (where the tomato *is*) and some things are **directions** (which way the gripper *faces*, or the *displacement* from here to there). When you move to a new frame, a location should shift — but a pure direction should **not**. The extra coordinate, $w$, is exactly the switch: $w=1$ marks a point that translates, $w=0$ marks a direction that doesn't. Getting this right prevents a classic bug: translating something that should never be translated.

## 2. Physical Intuition

Stand in the greenhouse and consider two things: the *spot* where a tomato hangs, and the *heading* "north-east." Now walk 3 meters east (change your frame). The tomato's *spot*, described relative to you, changes — you're closer or farther, so its position numbers shift. But "north-east" is still north-east; a heading doesn't care where you're standing. A **point** moves with translation; a **direction** is immune to it.

Homogeneous coordinates bake this in. Tag a location with $w=1$ and it picks up the translation. Tag a direction with $w=0$ and the translation multiplies by zero — it has no effect. Same matrix, correct behavior for both, automatically.

## 3. Mathematical Foundations

A 2D **point**: $\begin{bmatrix}x\\y\\1\end{bmatrix}$ ($w=1$). A 2D **direction** (or displacement): $\begin{bmatrix}d_x\\d_y\\0\end{bmatrix}$ ($w=0$).

Under a homogeneous transform whose translation column is $(t_x, t_y)$, the translation entries are multiplied by $w$. For a point ($w=1$) the offset $(t_x, t_y)$ is added; for a direction ($w=0$) it contributes $0$ — the direction is rotated/scaled but **never translated**. This matches the geometry exactly: positions translate, displacements don't. (A displacement is the difference of two points, and indeed $w=1$ minus $w=1$ gives $w=0$.)

## 4. Visual Explanation

`[Visual: under a translation, a point (w=1) shifts to a new spot while a direction arrow (w=0) keeps pointing the same way]`

**Diagram Specification**
- **Objective:** show a point moving under translation while a direction is unchanged.
- **Scene:** a translation applied to the scene; a labeled point (w=1) moves to a new location; a labeled direction arrow (w=0) is drawn before and after, pointing identically (only its base may shift, its heading does not change).
- **Labels:** "point (w=1): translates," "direction (w=0): unchanged by translation."
- **Form:** SVG.

## 5. Engineering Example

A detected tomato's *position* is a point ($w=1$): converting it to the robot frame must include the camera-to-arm offset. But the tomato's *surface normal* or the gripper's *approach direction* is a direction ($w=0$): converting it between frames should rotate it but **not** add any offset. Use $w=1$ for both and the normal ends up wrongly shifted; the $w$-flag is what keeps positions and directions behaving correctly through the same transform pipeline.

## 6. Worked Example

Translate by $(t_x, t_y) = (5, 0)$.
- Point $\begin{bmatrix}2\\3\\1\end{bmatrix}$ → $\begin{bmatrix}2+5\\3+0\\1\end{bmatrix} = \begin{bmatrix}7\\3\\1\end{bmatrix}$ — moved.
- Direction $\begin{bmatrix}2\\3\\0\end{bmatrix}$ → $\begin{bmatrix}2+5\cdot0\\3+0\cdot0\\0\end{bmatrix} = \begin{bmatrix}2\\3\\0\end{bmatrix}$ — unchanged.
The only difference was the last coordinate; the translation respected it automatically.

## 7. Interactive Demonstration

*(The 2.3 translation demo lets you watch a point move while a direction stays fixed under the same translation.)*

## 8. Coding Exercise

Represent a point as (x, y, 1) and a displacement as (dx, dy, 0); apply a translation matrix to both and confirm only the point moves.

## 9. Knowledge Check

A check that w=1 is a point (translates), w=0 is a direction (doesn't), and that a displacement is a difference of points (w=0).

## 10. Challenge Problem

A robot stores a fruit's position and the direction of its stem. After the robot drives forward, which of the two should change when re-expressed in the robot frame, and why does the w-coordinate produce the right answer for each?

## 11. Common Mistakes

- Tagging a direction with $w=1$ and accidentally translating it.
- Tagging a position with $w=0$ and losing its location offset.
- Forgetting that subtracting two points yields a direction ($w=0$).

## 12. Key Takeaways

- $w=1$ marks a **point** (a location) — it **translates**.
- $w=0$ marks a **direction/displacement** — it is **immune to translation** (still rotates/scales).
- The same transform handles both correctly because translation entries are multiplied by $w$.
- Use the right $w$: positions are points; headings and displacements are directions.

---

## AI Learning Companion

Copy any prompt below into ChatGPT, Claude, or another AI assistant.

**Tutor prompt** — explain it another way
```
Explain Lesson 2.2 (Module 2) — Points vs Directions — using "a spot in the room" (w=1) versus "the heading north-east" (w=0) and what happens to each when you change frames. Make clear why w=0 directions don't translate.
```

**Practice prompt** — generate more exercises
```
Give me 6 exercises applying a translation to points (w=1) and directions (w=0), showing which change. Include answers.
```

**Explore prompt** — connect it to the real world
```
Show me a robotics case where confusing a point (w=1) with a direction (w=0) — like a surface normal — causes a bug, and how the w-coordinate prevents it.
```

## Global Learning Support

Need this lesson explained in another language? Copy one of the prompts below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

**Español**
```
I just completed Lesson 2.2 (Module 2) — Points vs Directions.
Explain this lesson in Spanish. Keep robotics and mathematical terminology in English when appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

**中文 (Simplified Chinese)**
```
I just completed Lesson 2.2 (Module 2) — Points vs Directions.
Explain this lesson in Simplified Chinese. Keep mathematical notation unchanged.
Then provide: a summary, three practice questions, and one challenge problem.
```

**Türkçe**
```
I just completed Lesson 2.2 (Module 2) — Points vs Directions.
Explain this lesson in Turkish. Keep robotics terminology in English where commonly used.
Then provide: a summary, three practice questions, and one challenge problem.
```

---

*Next lesson: 2.3 — Translation as a Matrix (at last).*
