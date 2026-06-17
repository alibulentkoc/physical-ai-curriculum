---
module: 05
unit: 01
lesson: 1.1
title: From Forward to Inverse
core_idea: "Forward kinematics evaluates a function θ → pose; inverse kinematics solves the reverse equation pose → θ. Solving is harder than evaluating, and it is the question a robot must answer to actually reach a target."
estimated_time: 40
difficulty: Core
prerequisites: [4.8]
learning_objectives:
  - State the inverse-kinematics problem as solving T_0^n(θ) = T_desired.
  - Contrast evaluating the forward map with solving the inverse equation.
  - Explain why inverse kinematics is the question a harvesting robot must answer.
tags:
  - physical-ai
  - kinematics
  - inverse-kinematics
---

# Lesson 1.1 — From Forward to Inverse

> Module 4 told us where the gripper is for any joint angles. Module 5 asks the reverse — which joint angles put the gripper on the fruit. This lesson frames that reversal.

---

## 1. Why This Matters

A harvesting robot never gets to choose its joint angles first and see where the gripper lands. It works the other way: perception hands it a fruit at some pose, and the arm must find the joint angles that *put the gripper there*. Forward kinematics — the whole of Module 4 — cannot do this directly. It answers "given the angles, where is the gripper?" The robot needs the opposite. Without solving that opposite question, every pose Module 4 computed is just a description; nothing actually reaches the tomato.

## 2. Physical Intuition

Reach your hand out and touch a specific spot on the table. You did not consciously pick your shoulder, elbow, and wrist angles and then check where your fingertip ended up — you fixed the *target* and your arm found a set of joint angles that worked. That is inverse kinematics. Notice two things you did without thinking: there was usually **more than one way** to bend your arm to touch the same spot (try it elbow-high, then elbow-low), and some spots were simply **out of reach** no matter how you bent. Both facts will matter for the rest of the module.

## 3. Mathematical Foundations

Module 4 built the **forward map** — a function of the joint vector $\boldsymbol\theta = (\theta_1,\dots,\theta_n)$:

$$T_0^n(\boldsymbol\theta) = \prod_{i=1}^{n} T_{i-1}^i(\theta_i) \in SE(3).$$

You *evaluate* it: plug in $\boldsymbol\theta$, get a pose. It is always defined and returns exactly one pose.

**Inverse kinematics** turns the arrow around. Given a desired pose $T_{\text{desired}}$, find the joint angles that produce it:

$$\text{find } \boldsymbol\theta \quad\text{such that}\quad T_0^n(\boldsymbol\theta) = T_{\text{desired}}.$$

This is no longer an evaluation — it is an **equation to solve** for $\boldsymbol\theta$. The forward map $T_0^n$ is built from sines and cosines of the joint angles, so this is a system of **nonlinear** equations. Unlike the forward map, it may have no solution, exactly one, or many (Lesson 1.2). Sometimes we only require the **position** to match, $\mathbf p(\boldsymbol\theta) = \mathbf p_{\text{desired}}$ (a 3-equation problem); sometimes the full pose, position **and** orientation.

## 4. Visual Explanation

`[Visual: forward map θ → pose drawn as a solid arrow labeled "evaluate (Module 4, easy)"; a dashed reverse arrow pose → θ labeled "solve (Module 5, hard)", with a note 0/1/many solutions]`

**Diagram Specification**
- **Objective:** make the evaluate-vs-solve reversal unmistakable.
- **Scene:** left box "joint angles θ"; right box "gripper pose T₀ⁿ"; a solid arrow left→right labeled "forward: evaluate — one answer (Module 4)"; a dashed arrow right→left labeled "inverse: solve — 0, 1, or many (Module 5)."
- **Labels:** "θ → pose," "pose → θ?", "evaluate vs solve," "this module."
- **Form:** SVG.

## 5. Engineering Example

In the greenhouse pipeline, Module 3 perceived a tomato and Module 4 placed it in the arm's base frame — a target position, and (with a chosen approach direction) a target *pose* for the gripper. The control system now needs joint commands. Inverse kinematics is the step that converts "the fruit's grasp pose is here" into "set joint 1 to this angle, joint 2 to that angle, …" — the first form of the problem that produces something the motors can act on.

## 6. Worked Example

Take the one-joint arm from Module 4: gripper position $(L\cos\theta, L\sin\theta)$ with $L = 0.5$. **Forward:** given $\theta = 30°$, the gripper is at $(0.5\cos30°, 0.5\sin30°) = (0.433, 0.250)$ — plug in, done. **Inverse:** given the target $(0.433, 0.250)$, what is $\theta$? We must *solve* $0.5\cos\theta = 0.433$ and $0.5\sin\theta = 0.250$. Dividing, $\tan\theta = 0.250/0.433$, so $\theta = \operatorname{atan2}(0.250, 0.433) = 30°$. Notice the inverse already needed a tool (`atan2`) and a small derivation, where the forward direction needed only substitution — even for the simplest possible arm.

## 7. Interactive Demonstration

**Guided prediction.** Stand the one-joint arm at several angles and read off the gripper position (forward). Now cover the angle and try to recover it from the position alone (inverse). For the target $(0, 0.5)$, what $\theta$ works? For $(0.5, 0)$? For $(0.4, 0.4)$ — is it even on the radius-$0.5$ circle? Predict which targets are reachable before checking.

## 8. Coding Exercise

Write two functions for the one-joint arm: `fk(theta, L)` returning the gripper position (forward), and `ik(target, L)` returning the angle via `atan2` (inverse). Confirm that `fk(ik(target, L), L)` reproduces any reachable `target`. Note what `ik` should do if the target is not on the radius-$L$ circle — we handle that in Lesson 1.3.

## 9. Knowledge Check

Short checks that the student can state the IK equation, distinguish evaluate from solve, and recover an angle from a position with `atan2`.

## 10. Challenge Problem

For the one-joint arm, forward kinematics always returns exactly one position, yet inverse kinematics for a *reachable* target on the circle also returns exactly one angle in $[0, 360°)$. Will that one-to-one tidiness survive when we add a second joint? Argue informally why adding a joint should let the arm reach the same point in more than one way.

## 11. Common Mistakes

- Treating IK as "just rearrange the formula" — for multi-joint arms there is usually no clean closed-form rearrangement.
- Using $\arctan(y/x)$ instead of $\operatorname{atan2}(y, x)$ and losing the quadrant.
- Assuming a solution always exists; many targets are unreachable.
- Assuming a solution is unique; multi-joint arms typically have several.

## 12. Key Takeaways

- Forward kinematics **evaluates** $T_0^n(\boldsymbol\theta)$; inverse kinematics **solves** $T_0^n(\boldsymbol\theta) = T_{\text{desired}}$ for $\boldsymbol\theta$.
- The inverse problem is nonlinear and is the question a robot must answer to actually reach a target.
- A target may have no solution, one, or many — unlike the always-one-answer forward map.
- Even the one-joint arm shows the asymmetry: solving needs `atan2` and care, evaluating needs only substitution.

---

## AI Learning Companion

Copy any prompt below into ChatGPT, Claude, or another AI assistant.

**Tutor prompt** — explain it another way
```
Re-explain Lesson 1.1 (Module 5) — From Forward to Inverse — using the example of touching a spot on a table. Emphasize evaluate (forward) vs solve (inverse) and that a target can have 0, 1, or many solutions.
```

**Practice prompt** — generate more exercises
```
Give me 6 exercises that ask me to identify whether a robotics problem is forward or inverse kinematics, and to set up (not solve) the equation T_0^n(θ) = T_desired. Include answers.
```

**Explore prompt** — connect it to the real world
```
Show me real robots where inverse kinematics is the step that turns a target pose into joint commands, and what fails if it is skipped.
```

## Global Learning Support

Need this lesson explained in another language? Copy one of the prompts below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

**Español**
```
I just completed Lesson 1.1 (Module 5) — From Forward to Inverse.
Explain this lesson in Spanish. Keep robotics and mathematical terminology in English when appropriate.
Then provide: a summary, three practice questions, and one challenge problem.
```

**中文 (Simplified Chinese)**
```
I just completed Lesson 1.1 (Module 5) — From Forward to Inverse.
Explain this lesson in Simplified Chinese. Keep mathematical notation unchanged.
Then provide: a summary, three practice questions, and one challenge problem.
```

**Türkçe**
```
I just completed Lesson 1.1 (Module 5) — From Forward to Inverse.
Explain this lesson in Turkish. Keep robotics terminology in English where commonly used.
Then provide: a summary, three practice questions, and one challenge problem.
```

---

*Next lesson: 1.2 — Why It's Hard: Nonlinear, and 0/1/Many Solutions.*
