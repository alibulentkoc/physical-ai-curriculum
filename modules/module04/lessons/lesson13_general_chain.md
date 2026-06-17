---
module: 04
unit: 04
lesson: 4.1
title: The General Chain T₀ⁿ(θ)
core_idea: "Forward kinematics for any serial arm in 3D is the product of n SE(3) joint transforms, each a function of one joint variable. The product is a single function of the configuration vector."
estimated_time: 45
difficulty: Core
prerequisites: [3.4]
learning_objectives:
  - State the general forward-kinematics product in SE(3).
  - Treat T_0^n as a function of the configuration vector.
  - Move from planar to 3D transforms.
tags:
  - physical-ai
  - kinematics
  - forward-kinematics
  - SE3
---

# Lesson 4.1 — The General Chain T₀ⁿ(θ)

## 1. Why This Matters

Planar arms were a warm-up. Real arms move in 3D, with joints whose axes point in different directions. The beautiful part: nothing about the *structure* changes. Forward kinematics is still a product of per-joint transforms — now full $SE(3)$ matrices (Module 2) instead of planar $SE(2)$ ones. This lesson states the general map once and for all, so every later arm is just "fill in the factors."

## 2. Physical Intuition

Think of walking from the robot's base out to its gripper, stepping across one joint at a time. At each step you apply that joint's transform: rotate (or slide) by the joint variable, then ride the rigid link to the next joint. Whether the joint axis points up, sideways, or at an angle, the *step* is the same kind of operation — a rigid motion. The gripper's pose is everything you accumulated along the walk: the product of all the steps. The configuration vector just tells you how far each joint turned or slid.

## 3. Mathematical Foundations

For a serial arm with $n$ joints and configuration $\boldsymbol{\theta}=(\theta_1,\dots,\theta_n)$ (using $\theta$ for revolute, $d$ for prismatic), each joint contributes an $SE(3)$ transform $T_{i-1}^{i}(\theta_i)$ (Lesson 2.2, now in 3D). Forward kinematics is

$$\boxed{\,T_0^n(\boldsymbol{\theta}) = T_0^1(\theta_1)\,T_1^2(\theta_2)\cdots T_{n-1}^n(\theta_n) = \prod_{i=1}^{n} T_{i-1}^{i}(\theta_i)\,}$$

— a product evaluated left-to-right (base→tip), giving one $SE(3)$ element. Key points:

- It is a **function of the whole configuration**: change any $\theta_i$ and the product changes.
- Each factor is **rigid** ($SE(3)$), so the product is rigid — the gripper pose is a genuine rotation + translation.
- The 3D rotations don't generally commute, so **order matters** (as in Lesson 3.2).

The planar formulas were this product specialized to rotations about a single axis. In 3D the factors carry their own axes (encoded in the fixed link geometry), but the assembly rule is identical.

## 4. Visual Explanation

`[Visual: a 3D serial arm with frames at each joint and the product T_0^1 · T_1^2 · … · T_{n-1}^n = T_0^n mapping base to gripper]`

**Diagram Specification**
- **Objective:** show the general SE(3) chain product.
- **Scene:** a 3D-ish serial arm (base frame, a few joints with small coordinate frames, gripper frame); transforms T_0^1, …, T_{n-1}^n labeled across the links; the product equation T_0^n(θ) = ∏ T_{i-1}^i below.
- **Labels:** "each factor ∈ SE(3)," "product base→tip," "T_0^n is a function of θ," "order matters (3D rotations don't commute)."
- **Form:** SVG.

## 5. Engineering Example

A 6-DOF greenhouse arm has six $SE(3)$ factors. The controller stores each as a function of one motor angle and multiplies them whenever it needs the gripper pose — for collision checks, for comparing against a perceived fruit position, for logging where the hand is. The same product handles any arm; only the factors differ. This uniformity is why forward kinematics is a solved, library-level operation.

## 6. Worked Example

Take the planar 2-link arm but write its factors as $4\times4$ $SE(3)$ matrices (rotation about $z$, translation in the $xy$-plane). $T_0^2 = T_0^1(30°)T_1^2(60°)$ yields a rotation about $z$ by $90°$ and translation $(0.346, 0.5, 0)$ — the same answer as before, now embedded in 3D. Adding a third joint that rotates about a *different* axis (say a base swivel about $z$ underneath) would prepend one more factor; the product machinery is unchanged.

## 7. Interactive Demonstration

**Guided prediction.** For an $n$-joint arm, predict how many factors the product has and what happens to $T_0^n$ if you change only the last joint $\theta_n$. Predict whether reordering two factors changes the result. Confirm: $n$ factors; changing $\theta_n$ changes the product; reordering generally changes it.

## 8. Coding Exercise

Implement `se3_rotz(theta)`, `se3_trans(x,y,z)`, and `fk(factors)` that multiplies a list of $4\times4$ matrices; rebuild the planar arm in 3D and confirm $T_0^2$ matches the planar result (translation $(0.346,0.5,0)$, rotation about $z$ by $90°$).

## 9. Knowledge Check

A check on the general product $T_0^n=\prod T_{i-1}^i$, that it's a function of the configuration, and that order matters.

## 10. Challenge Problem

Explain why forward kinematics is always well-defined and easy to evaluate (just multiply), regardless of how complicated the arm is — and contrast this with why the *inverse* (Module 5) is hard. Frame it in terms of "evaluating a function" vs "solving an equation."

## 11. Common Mistakes

- Multiplying factors in the wrong order (must be base→tip).
- Assuming 3D rotations commute.
- Forgetting each factor is a full $SE(3)$ element (rotation + translation).

## 12. Key Takeaways

- General forward kinematics: $T_0^n(\boldsymbol{\theta}) = \prod_{i=1}^n T_{i-1}^i(\theta_i)$, an $SE(3)$ product base→tip.
- It is a **function of the configuration**; each factor depends on one joint variable.
- The planar formulas are this product specialized to one rotation axis.
- Forward = evaluate a product (easy); inverse = solve for $\boldsymbol{\theta}$ (Module 5, hard).

---

## AI Learning Companion

Copy any prompt below into ChatGPT, Claude, or another AI assistant.

**Tutor prompt** — explain it another way
```
Explain Lesson 4.1 (Module 4) — The General Chain T_0^n(θ) — as walking base→tip applying one SE(3) transform per joint, giving the product T_0^n = ∏ T_{i-1}^i, a function of the configuration. Note order matters in 3D.
```

**Practice prompt** — generate more exercises
```
Give me 6 exercises forming the SE(3) forward-kinematics product for small arms and reasoning about factor count and order. Include answers.
```

**Explore prompt** — connect it to the real world
```
Show me how a 6-DOF arm's forward kinematics is computed as a product of six 4x4 matrices in robot software.
```

## Global Learning Support

Need this lesson explained in another language? Copy one of the prompts below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

**Español**
```
I just completed Lesson 4.1 (Module 4) — The General Chain T_0^n(θ).
Explain this lesson in Spanish. Keep robotics and mathematical terminology in English when appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

**中文 (Simplified Chinese)**
```
I just completed Lesson 4.1 (Module 4) — The General Chain T_0^n(θ).
Explain this lesson in Simplified Chinese. Keep mathematical notation unchanged.
Then provide: a summary, three practice questions, and one challenge problem.
```

**Türkçe**
```
I just completed Lesson 4.1 (Module 4) — The General Chain T_0^n(θ).
Explain this lesson in Turkish. Keep robotics terminology in English where commonly used.
Then provide: a summary, three practice questions, and one challenge problem.
```

---

*Next lesson: 4.2 — Position and Orientation of the Gripper.*
