---
module: 04
unit: 07
lesson: 7.3
title: Closing the Loop with Perception
core_idea: "Forward kinematics produces T_0^n = T(base←gripper); composed with the fixed base mounting it gives T(world←arm). This is exactly the transform Module 3's perception pipeline assumed — the two halves now meet."
estimated_time: 50
difficulty: Core
prerequisites: [7.2]
learning_objectives:
  - Identify T_0^n as the arm-to-world transform perception needs.
  - Compose the kinematic chain with perception to place a target in the arm's frame.
  - Articulate the full perceive-to-act loop.
tags:
  - physical-ai
  - kinematics
  - perception
  - integration
---

# Lesson 7.3 — Closing the Loop with Perception

## 1. Why This Matters

This is the lesson the whole curriculum has been building toward: kinematics and perception **meet**. Module 3 estimated a fruit's position in the world but had to *assume* it knew where the arm was. Module 4 computes exactly that — the arm's pose — from joint angles via forward kinematics. Put them together and the robot can see a fruit and know, in its own coordinates, where to send the gripper. The loop closes.

## 2. Physical Intuition

Perception and motion speak different "languages" until they share a frame. The camera says "the tomato is *there*, relative to me." The arm thinks in joint angles and its own base frame. Forward kinematics is the translator: from joint angles it builds the chain of transforms from the base out to the gripper, and (knowing how the base is bolted to the world, and where the camera is mounted) everything can be expressed in one common frame. Then "the tomato is there" and "my gripper is here" are statements in the *same* coordinates, and the difference is a motion command.

## 3. Mathematical Foundations

Forward kinematics gives the gripper relative to the arm's base: $T_{\text{base}}^{\text{gripper}} = T_0^n(\boldsymbol\theta)$. The base is mounted in the world by a fixed, known transform $T_{\text{world}}^{\text{base}}$. Composing,

$$T_{\text{world}}^{\text{gripper}} = T_{\text{world}}^{\text{base}}\,T_0^n(\boldsymbol\theta).$$

This is the **$T(\text{world}\leftarrow\text{arm})$** that Module 3 took as given. Now recall Module 3's perception output: a fruit position in the camera frame, $\mathbf{P}_{\text{cam}}$ (recovered from a pixel plus depth). With the camera mounted on the robot by a known $T_{\text{base}}^{\text{cam}}$ (or on the gripper, $T_{\text{gripper}}^{\text{cam}}$), the fruit in the **arm's base frame** is

$$\mathbf{P}_{\text{base}} = T_{\text{base}}^{\text{cam}}\,\mathbf{P}_{\text{cam}},$$

and in the gripper frame, $\mathbf{P}_{\text{gripper}} = (T_0^n)^{-1} T_{\text{base}}^{\text{cam}} \mathbf{P}_{\text{cam}}$. Every term is now something we can compute: perception supplies $\mathbf P_{\text{cam}}$, the mountings are calibrated constants, and forward kinematics supplies $T_0^n$. The perceive-to-act loop is one chain of $SE(3)$ products — the central idea of both modules, joined.

## 4. Visual Explanation

`[Visual: the full loop — camera sees fruit (P_cam) → T_base^cam → P_base; FK gives T_0^n; target expressed in the gripper frame → motion command]`

**Diagram Specification**
- **Objective:** show perception and kinematics meeting in one frame.
- **Scene:** a camera node outputting $\mathbf P_{\text{cam}}$; an arrow through $T_{\text{base}}^{\text{cam}}$ to $\mathbf P_{\text{base}}$; the arm with FK producing $T_0^n$; both feeding a box "target in gripper frame → move"; a faint label "this is the T(world←arm) Module 3 assumed."
- **Labels:** "perception: P_cam (Module 3)," "FK: T_0^n (Module 4)," "calibrated mounts," "same frame → motion command."
- **Form:** SVG.

## 5. Engineering Example

The greenhouse robot's full pipeline: the camera detects a ripe tomato and (with depth) gives $\mathbf P_{\text{cam}}$; the known camera mount $T_{\text{base}}^{\text{cam}}$ and current $T_0^n$ from the joint encoders place the tomato in the gripper frame; the controller computes the offset and approach and drives the arm. Forward kinematics is queried continuously so the robot always knows where its hand is relative to what it sees. This is the join the two modules were designed around.

## 6. Worked Example

Camera (mounted on the base) reports a tomato at $\mathbf P_{\text{cam}} = (0.05, 0.0, 0.40)$ m. The camera mount is $T_{\text{base}}^{\text{cam}}$ = a translation $(0.10, 0, 0.50)$ with no rotation. Then $\mathbf P_{\text{base}} = (0.15, 0.0, 0.90)$. Forward kinematics says the gripper is currently at $\mathbf p_{\text{gripper,base}} = (0.15, 0, 0.60)$. The tomato is $0.30$ m directly above the gripper in the base frame — a clean vertical move (subject to reachability from Lesson 7.2). Same coordinates, so the command is just the difference.

## 7. Interactive Demonstration

**Guided prediction.** Given $\mathbf P_{\text{cam}}$ and a pure-translation camera mount, predict $\mathbf P_{\text{base}}$. Predict how to get the target relative to the gripper given $T_0^n$. Confirm: $\mathbf P_{\text{base}} = T_{\text{base}}^{\text{cam}}\mathbf P_{\text{cam}}$; $\mathbf P_{\text{gripper}} = (T_0^n)^{-1}\mathbf P_{\text{base}}$.

## 8. Coding Exercise

Given $\mathbf P_{\text{cam}}$, a camera-mount transform, and a `dh_fk` pose $T_0^n$, compute the fruit position in the base frame and in the gripper frame; print the base-frame offset from gripper to fruit (the move vector). Reuse the SE(3) helpers from Module 2.

## 9. Knowledge Check

A check that $T_0^n = T(\text{base}\leftarrow\text{gripper})$, that composing with the base mount gives $T(\text{world}\leftarrow\text{arm})$, and that this is what Module 3 assumed.

## 10. Challenge Problem

The camera is mounted on the **gripper** (eye-in-hand), not the base. Write the transform that places a camera-frame fruit into the base frame using $T_0^n$ and $T_{\text{gripper}}^{\text{cam}}$, and explain why eye-in-hand makes the placement depend on the current configuration.

## 11. Common Mistakes

- Forgetting that perception's $T(\text{world}\leftarrow\text{arm})$ is exactly $T_0^n$ (composed with the base mount).
- Mixing up the camera mount frame (base- vs gripper-mounted).
- Comparing the fruit and gripper in different frames before transforming to a common one.

## 12. Key Takeaways

- $T_0^n = T(\text{base}\leftarrow\text{gripper})$; with the base mount it is $T(\text{world}\leftarrow\text{arm})$ — the transform **Module 3 assumed**.
- Perception's $\mathbf P_{\text{cam}}$ plus calibrated mounts plus FK puts the fruit in the **arm's frame**.
- The perceive-to-act loop is one chain of $SE(3)$ products.
- This is where camera geometry (Module 3) and forward kinematics (Module 4) join.

---

## AI Learning Companion

Copy any prompt below into ChatGPT, Claude, or another AI assistant.

**Tutor prompt** — explain it another way
```
Explain Lesson 7.3 (Module 4) — Closing the Loop with Perception — showing T_0^n is the T(world←arm) Module 3 assumed, and how P_cam + calibrated camera mount + FK place a fruit in the arm/gripper frame. Use the "translator between two languages" analogy.
```

**Practice prompt** — generate more exercises
```
Give me 6 exercises composing perception output (P_cam), camera mounts, and FK poses to place a target in the base/gripper frame. Include answers.
```

**Explore prompt** — connect it to the real world
```
Show me the full perceive-to-act loop for a fruit-picking robot: detect, recover P_cam, transform via camera mount and FK, compute the move.
```

## Global Learning Support

Need this lesson explained in another language? Copy one of the prompts below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

**Español**
```
I just completed Lesson 7.3 (Module 4) — Closing the Loop with Perception.
Explain this lesson in Spanish. Keep robotics and mathematical terminology in English when appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

**中文 (Simplified Chinese)**
```
I just completed Lesson 7.3 (Module 4) — Closing the Loop with Perception.
Explain this lesson in Simplified Chinese. Keep mathematical notation unchanged.
Then provide: a summary, three practice questions, and one challenge problem.
```

**Türkçe**
```
I just completed Lesson 7.3 (Module 4) — Closing the Loop with Perception.
Explain this lesson in Turkish. Keep robotics terminology in English where commonly used.
Then provide: a summary, three practice questions, and one challenge problem.
```

---

*Next lesson: 7.4 — Pose, Workspace, and Perception (Unit 7 Recap).*
