---
module: 02
unit: 07
lesson: 7.3
title: Building the Transformation Chain
core_idea: "Camera to world is a composed chain of poses: detection in camera, camera on arm, arm in world — multiplied in order."
estimated_time: 45
difficulty: Introductory
prerequisites: [7.2]
learning_objectives:
  - Assemble the camera→arm→world chain as a product of SE(3) poses.
  - Apply the chain to convert a detection into the world frame.
  - Use the inverse chain to go from world back to camera.
tags:
  - physical-ai
  - transformations
  - camera
  - composition
---

# Lesson 7.3 — Building the Transformation Chain

## 1. Why This Matters

Now we assemble the pipeline. A detection sits in the camera frame; the camera sits on the arm (extrinsics); the arm sits in the world (its pose). Stack these and you get the **camera→world chain** — a composition of SE(3) poses, exactly the Unit 5 machinery. This chain is the mathematical core of "how a detected object becomes a robot target," and it's what the Unit 8 capstone is built on.

## 2. Physical Intuition

Three nested statements: "the tomato is *here* from the camera," "the camera is *there* on the arm," "the arm is *there* in the world." Read them outward — camera to arm to world — and you've placed the tomato in the world. Each "is there" is a pose; reading them in sequence is composition. It's the head-camera friend again, but now the friend is on a moving arm in a known place: follow the chain of "who is where relative to whom" and the cup's world location falls out.

## 3. Mathematical Foundations

Compose the poses along the path (Unit 5), inner frames cancelling:

$$T_{\text{world}\leftarrow\text{cam}} = T_{\text{world}\leftarrow\text{arm}}\; T_{\text{arm}\leftarrow\text{cam}}.$$

Then a detection in the camera frame becomes a world point in one multiply:

$$\mathbf{p}_{\text{world}} = T_{\text{world}\leftarrow\text{arm}}\; T_{\text{arm}\leftarrow\text{cam}}\;\mathbf{p}_{\text{cam}}.$$

Here $T_{\text{arm}\leftarrow\text{cam}}$ is the fixed extrinsics and $T_{\text{world}\leftarrow\text{arm}}$ is the arm's current pose (it changes as the arm moves — just recompute the product). To go the other way (a world goal expressed in the camera frame), use the **inverse chain**: $T_{\text{cam}\leftarrow\text{world}} = (T_{\text{world}\leftarrow\text{cam}})^{-1} = T_{\text{arm}\leftarrow\text{cam}}^{-1}\,T_{\text{world}\leftarrow\text{arm}}^{-1}$ — undo the last-applied transform first. If the detection carries an orientation (a full pose), the same chain transforms the whole pose, not just the point.

## 4. Visual Explanation

`[Visual: the chain camera -> arm -> world as three composed SE(3) poses, with a tomato detection carried from the camera frame to the world frame]`

**Diagram Specification**
- **Objective:** show the camera→arm→world chain as composed poses applied to a detection.
- **Scene:** faux-3D isometric: camera frame (with tomato detection vector), arm frame, world frame; arrows labeled T(arm←cam) [extrinsics] and T(world←arm) [arm pose]; the composed product T(world←cam) shown carrying the tomato to a world position.
- **Labels:** "detection p_cam," "extrinsics T(arm←cam)," "arm pose T(world←arm)," "p_world = T(world←arm)·T(arm←cam)·p_cam."
- **Form:** SVG (faux-3D isometric).

## 5. Engineering Example

Every detection cycle, the robot reads the arm's current pose, multiplies it by the fixed camera extrinsics to get camera→world, and converts the detected tomato into the world (or base) frame for the planner. When the arm moves to look from a new angle, only $T_{\text{world}\leftarrow\text{arm}}$ changes; recompute the product and the conversion stays correct. This is the literal implementation of perception-to-pose.

## 6. Worked Example

Extrinsics $T_{\text{arm}\leftarrow\text{cam}}$ = translate $(0, 0, 0.1)$, no rotation. Arm pose $T_{\text{world}\leftarrow\text{arm}}$ = translate $(1.0, 0.5, 0.0)$, no rotation. A detection $\mathbf{p}_{\text{cam}} = (0, 0, 0.3)$:
- camera→world product: translate $(1.0, 0.5, 0.1)$.
- $\mathbf{p}_{\text{world}} = (1.0, 0.5, 0.4)$.
The 0.3 m depth plus the 0.1 m mount offset gives $z = 0.4$; the arm's world offset places $x,y$. One composed chain, one detection, one world point.

## 7. Interactive Demonstration

**Guided prediction.** With extrinsics = translate $(0,0,0.1)$ and arm pose = translate $(1.0, 0.5, 0)$, predict the camera→world product and then the world coordinates of a detection at $(0,0,0.3)$. Predict which factor changes when the arm moves but the camera stays bolted on. Confirm the inner "arm" frame cancels in the product.

## 8. Coding Exercise

Build the extrinsics and arm-pose SE(3) matrices; compose camera→world; convert a detection to the world; then invert the chain to bring a world goal back into the camera frame and confirm a round trip.

## 9. Knowledge Check

A check that camera→world = arm-pose · extrinsics, that it converts a detection in one multiply, and that the inverse chain reverses it.

## 10. Challenge Problem

The arm moves to a new pose between two detection cycles, but the code reuses the old camera→world product. Explain the resulting error and which factor was stale. How would the inverse chain be used to verify a computed world pose back in the camera frame?

## 11. Common Mistakes

- Composing extrinsics and arm pose in the wrong order.
- Forgetting to update the arm-pose factor when the arm moves.
- Inverting only one factor instead of the whole chain (in reverse order).

## 12. Key Takeaways

- **Camera→world** = $T_{\text{world}\leftarrow\text{arm}}\,T_{\text{arm}\leftarrow\text{cam}}$ — arm pose composed with extrinsics.
- A detection becomes a world point in **one multiply** by the chain.
- The arm-pose factor changes as the arm moves; the extrinsics factor is fixed.
- The **inverse chain** goes world→camera (undo last first).

---

## AI Learning Companion

Copy any prompt below into ChatGPT, Claude, or another AI assistant.

**Tutor prompt** — explain it another way
```
Explain Lesson 7.3 (Module 2) — Building the Transformation Chain — as three nested "who is where" statements (tomato in camera, camera on arm, arm in world) composed into camera→world. Show the product and how a detection becomes a world point.
```

**Practice prompt** — generate more exercises
```
Give me 6 exercises composing extrinsics and an arm pose into camera→world and converting detections to the world frame; include one using the inverse chain. Include answers.
```

**Explore prompt** — connect it to the real world
```
Show me how a robot recomputes camera→world each cycle (updating only the arm-pose factor) to convert detections, and how it would verify a world pose by mapping it back to the camera frame.
```

## Global Learning Support

Need this lesson explained in another language? Copy one of the prompts below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

**Español**
```
I just completed Lesson 7.3 (Module 2) — Building the Transformation Chain.
Explain this lesson in Spanish. Keep robotics and mathematical terminology in English when appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

**中文 (Simplified Chinese)**
```
I just completed Lesson 7.3 (Module 2) — Building the Transformation Chain.
Explain this lesson in Simplified Chinese. Keep mathematical notation unchanged.
Then provide: a summary, three practice questions, and one challenge problem.
```

**Türkçe**
```
I just completed Lesson 7.3 (Module 2) — Building the Transformation Chain.
Explain this lesson in Turkish. Keep robotics terminology in English where commonly used.
Then provide: a summary, three practice questions, and one challenge problem.
```

---

*Next lesson: 7.4 — Camera-to-Robot Reasoning (Unit 7 recap).*
