---
module: 04
unit: 02
lesson: 2.1
title: A One-Joint Arm
core_idea: "The simplest arm — one revolute joint and one link — has a gripper that traces a circle. Its pose is a pure rotation of the base frame plus the link offset."
estimated_time: 40
difficulty: Core
prerequisites: [1.4]
learning_objectives:
  - Describe the one-joint planar arm.
  - Compute the gripper position from the joint angle.
  - See the gripper's orientation rotate with the joint.
tags:
  - physical-ai
  - kinematics
  - one-joint
---

# Lesson 2.1 — A One-Joint Arm

## 1. Why This Matters

Everything in forward kinematics generalizes from one joint. If you can write the pose of a single revolute joint with one rigid link, you can chain the idea to any arm. So we start as small as possible — one joint, one link, motion in a plane — and compute the gripper's pose exactly. This is the atom of the whole module.

## 2. Physical Intuition

Picture a clock hand pinned at the center (the joint) with the tip as the gripper. Turn the hand by an angle $\theta$ and the tip sweeps a circle of radius equal to the hand's length. Two things change as you turn: the tip's **position** (it moves around the circle) and the hand's **orientation** (it points in a new direction). The joint angle $\theta$ controls both. That's the entire behavior of a one-joint arm — a rotation applied to a fixed link.

## 3. Mathematical Foundations

Place the joint at the base-frame origin, link length $L$ along the link's own $x$-axis, motion in the $xy$-plane. Rotating the joint by $\theta$ rotates the base frame by $\theta$ (a Module 2 planar rotation), and the gripper sits at distance $L$ along the rotated $x$-axis. The gripper **position** is

$$\mathbf{t}(\theta) = \big(L\cos\theta,\ L\sin\theta\big),$$

and the gripper **orientation** is the rotation by $\theta$:

$$R(\theta) = \begin{bmatrix}\cos\theta & -\sin\theta \\ \sin\theta & \cos\theta\end{bmatrix}.$$

Packed as a planar pose ($SE(2)$, a slice of the $SE(3)$ machinery from Module 2):

$$T_0^1(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta & L\cos\theta \\ \sin\theta & \cos\theta & L\sin\theta \\ 0 & 0 & 1 \end{bmatrix}.$$

One joint variable $\theta$ determines the whole pose. Notice the position is the *image of the link tip* $(L,0)$ under the rotation — exactly "rotate the frame, then read off where the fixed link end lands."

## 4. Visual Explanation

`[Visual: a one-joint arm (clock-hand style) at angle θ, gripper tracing a circle of radius L, with the gripper's position (Lcosθ, Lsinθ) and orientation arrow]`

**Diagram Specification**
- **Objective:** show the one-joint arm's pose vs angle.
- **Scene:** base joint at origin; a link of length L at angle θ; gripper at the tip with a small orientation arrow; a dashed circle of radius L showing the path; the position formula (Lcosθ, Lsinθ) labeled.
- **Labels:** "joint angle θ," "link length L," "gripper position (Lcosθ, Lsinθ)," "orientation rotates by θ."
- **Form:** SVG.

## 5. Engineering Example

The greenhouse arm's base swivel joint is essentially this: rotating it sweeps the whole arm (and gripper) around a circle. Even before adding the elbow and wrist, knowing the base joint's pose as a function of its angle is the first factor in the full chain. The one-joint formula is literally $T_0^1$ in the product we'll build.

## 6. Worked Example

Link $L=0.5$ m. At $\theta=0$: position $(0.5, 0)$, orientation $0°$. At $\theta=90°$: position $(0, 0.5)$, orientation $90°$. At $\theta=45°$: position $(0.5\cos45°, 0.5\sin45°)\approx(0.354, 0.354)$, orientation $45°$. Each angle yields one pose — position on the radius-$0.5$ circle, orientation equal to $\theta$. The pose matrix $T_0^1(45°)$ has the rotation block for $45°$ and translation $(0.354, 0.354)$.

## 7. Interactive Demonstration

**Guided prediction.** For $L=0.5$, predict the gripper position and orientation at $\theta=0°,45°,90°,180°$. Predict the path the gripper traces as $\theta$ sweeps $0\to360°$. Confirm: a circle of radius $L$; orientation equals $\theta$.

## 8. Coding Exercise

Implement `pose_one_joint(theta, L)` returning the $3\times3$ $SE(2)$ matrix; extract position and orientation; verify the worked-example values; plot the circle swept as $\theta$ varies.

## 9. Knowledge Check

A check on the one-joint position/orientation formulas and that one angle sets the whole pose.

## 10. Challenge Problem

The link is mounted with a fixed $90°$ bend at the tip (the gripper points perpendicular to the link). How does the orientation part of $T_0^1$ change, and why does the *position* stay $(L\cos\theta, L\sin\theta)$?

## 11. Common Mistakes

- Reporting only position and forgetting orientation rotates with $\theta$.
- Putting $L$ in the wrong place (it scales the rotated $x$-axis: $(L\cos\theta, L\sin\theta)$).
- Mixing degrees and radians in the trig.

## 12. Key Takeaways

- A one-joint arm's gripper position is $(L\cos\theta, L\sin\theta)$; orientation is rotation by $\theta$.
- The pose is the $SE(2)$ matrix $T_0^1(\theta)$ — rotation block + translation.
- One joint variable determines the entire pose.
- This is the building block chained in later units.

---

## AI Learning Companion

Copy any prompt below into ChatGPT, Claude, or another AI assistant.

**Tutor prompt** — explain it another way
```
Explain Lesson 2.1 (Module 4) — A One-Joint Arm — using a clock hand. Show the gripper position (Lcosθ, Lsinθ), orientation = θ, and the SE(2) pose matrix T_0^1(θ).
```

**Practice prompt** — generate more exercises
```
Give me 6 exercises computing the one-joint arm's gripper position, orientation, and SE(2) pose for various θ and L. Include answers.
```

**Explore prompt** — connect it to the real world
```
Show me how a robot's base swivel joint is a one-joint arm and how its pose becomes the first factor in the forward-kinematics product.
```

## Global Learning Support

Need this lesson explained in another language? Copy one of the prompts below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

**Español**
```
I just completed Lesson 2.1 (Module 4) — A One-Joint Arm.
Explain this lesson in Spanish. Keep robotics and mathematical terminology in English when appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

**中文 (Simplified Chinese)**
```
I just completed Lesson 2.1 (Module 4) — A One-Joint Arm.
Explain this lesson in Simplified Chinese. Keep mathematical notation unchanged.
Then provide: a summary, three practice questions, and one challenge problem.
```

**Türkçe**
```
I just completed Lesson 2.1 (Module 4) — A One-Joint Arm.
Explain this lesson in Turkish. Keep robotics terminology in English where commonly used.
Then provide: a summary, three practice questions, and one challenge problem.
```

---

*Next lesson: 2.2 — The Joint Transform.*
