---
module: 01
unit: 03
lesson: 3.4
title: 3D Coordinate Systems
core_idea: "Real space needs three axes; (x, y, z) locates any point, and the right-hand rule fixes a consistent orientation."
estimated_time: 45
difficulty: Introductory
prerequisites: [3.3]
learning_objectives:
  - Extend the 2D system to three perpendicular axes and (x, y, z).
  - Apply the right-hand rule for a consistent axis orientation.
  - Locate a point in 3D greenhouse space and compute 3D distance.
tags:
  - physical-ai
  - coordinate-frames
---

# Lesson 3.4 — 3D Coordinate Systems

## 1. Why This Matters

Tomatoes don't live on a flat map — they hang at different **heights**. A gripper approaches in three dimensions. The moment the robot leaves the floor plane, it needs a third axis. A **3D coordinate system** $(x, y, z)$ is the real workspace of a harvesting arm, and it's the setting for cameras, depth, and everything in Module 2's kinematics.

Still Unit 3's question: those three axes belong to a frame. The robot's $z$ (up from its base) and the camera's $z$ (out from its lens) are different — same idea, different owner.

## 2. Physical Intuition

Stand in the corner of the greenhouse. Two walls and the floor meet there — three mutually perpendicular directions: along one wall ($x$), along the other ($y$), straight up ($z$). Any point in the room is "so far along, so far across, so far up." A tomato at eye level above a spot on the floor just adds a $z$ to its floor address.

To keep everyone's axes consistent, robotics uses the **right-hand rule**: point your right hand's fingers along $+x$, curl them toward $+y$, and your thumb points along $+z$. It removes the ambiguity of "which way is positive up."

## 3. Mathematical Foundations

A 3D Cartesian frame has three perpendicular axes and locates a point as $(x, y, z)$. Distance extends the Pythagorean pattern:

$$d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2 + (z_2-z_1)^2}$$

A **right-handed** frame satisfies the $x \to y \to z$ curl above (it's the convention used across robotics, so frames compose consistently). The cross product from Unit 2 lives natively here: $x \times y = z$ in a right-handed frame.

## 4. Visual Explanation

`[Visual: faux-3D isometric axes (x, y, z) from an origin with a tomato located at (x, y, z) and dashed drop-lines to the floor plane; a small right-hand-rule inset]`

**Diagram Specification**
- **Objective:** convey three perpendicular axes and a located 3D point without a 3D engine (isometric SVG).
- **Scene:** isometric origin with x, y, z axes; a tomato at some (x, y, z); dashed lines dropping to the xy-floor and up to the point to show the three components; a small inset showing the right-hand rule (x→y→z).
- **Labels:** "x," "y," "z (up)," "P = (x, y, z)," "right-hand rule."
- **Form:** SVG (faux-3D isometric; no WebGL).

## 5. Engineering Example

The harvesting arm plans in 3D base coordinates: a tomato at $(0.35, 0.15, 0.20)$ m means forward 0.35, left 0.15, up 0.20 from the base. Height ($z$) decides whether the arm tilts up to reach a high truss tomato or down to a low one — information a 2D map simply can't hold.

## 6. Worked Example

Gripper at $(0.10, 0.10, 0.05)$, tomato at $(0.40, 0.30, 0.25)$ (meters, robot base frame). Displacement: $(0.30, 0.20, 0.20)$. Distance: $\sqrt{0.30^2+0.20^2+0.20^2} = \sqrt{0.17} \approx 0.412$ m. If the arm's reach is 0.5 m, it's reachable.

## 7. Interactive Demonstration

*(The 3.6 transform demo handles the interactive frame work; this lesson uses the isometric figure above.)*

## 8. Coding Exercise

Place a few tomatoes in 3D, compute 3D distances from the gripper, and pick the nearest reachable one.

## 9. Knowledge Check

A check on (x, y, z) location, 3D distance, and the right-hand rule.

## 10. Challenge Problem

A tomato sits directly above another (same $x$, same $y$, higher $z$). Explain why they share a 2D map position but are different 3D points, and what fails if the robot ignores $z$.

## 11. Common Mistakes

- Ignoring $z$ and treating a 3D problem as 2D (the arm crashes high or short).
- Using a left-handed axis set by accident, flipping a sign on $z$.
- Forgetting the third axis still belongs to a specific frame (robot up ≠ camera forward).

## 12. Key Takeaways

- Real space needs **three** perpendicular axes: $(x, y, z)$.
- 3D distance extends the Pythagorean formula with a $z$ term.
- The **right-hand rule** gives a consistent orientation across frames.
- Height ($z$) is essential information a 2D map can't carry.

---

## AI Learning Companion

Copy any prompt below into ChatGPT, Claude, or another AI assistant.

**Tutor prompt** — explain it another way
```
Explain Lesson 3.4 (3D Coordinate Systems) using the corner of a room where two walls and the floor meet. Make the three axes and the right-hand rule intuitive.
```

**Practice prompt** — generate more exercises
```
Give me 8 exercises locating points in 3D (x, y, z), computing 3D distance, and applying the right-hand rule, in a harvesting-robot context. Include answers.
```

**Explore prompt** — connect it to the real world
```
Show me how a robot arm uses 3D base coordinates and why height (z) matters for reaching fruit at different truss levels.
```

## Global Learning Support

Need this lesson explained in another language? Copy one of the prompts below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

**Español**
```
I just completed Lesson 3.4 — 3D Coordinate Systems.
Explain this lesson in Spanish. Keep robotics and mathematical terminology in English when appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

**中文 (Simplified Chinese)**
```
I just completed Lesson 3.4 — 3D Coordinate Systems.
Explain this lesson in Simplified Chinese. Keep mathematical notation unchanged.
Then provide: a summary, three practice questions, and one challenge problem.
```

**Türkçe**
```
I just completed Lesson 3.4 — 3D Coordinate Systems.
Explain this lesson in Turkish. Keep robotics terminology in English where commonly used.
Then provide: a summary, three practice questions, and one challenge problem.
```

---

*Next lesson: 3.6 — Conceptual Frame Transformations (moving a point between frames, no matrices).*
