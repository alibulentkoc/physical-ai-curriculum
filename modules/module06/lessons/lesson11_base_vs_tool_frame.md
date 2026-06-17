---
module: 06
unit: 03
lesson: 3.3
title: "Base-Frame vs Tool-Frame Jacobian"
core_idea: "The same tool motion can be reported in the base frame or in the tool's own frame; since both reference the same point, the conversion is a pure rotation of each half of the Jacobian — J_tool = blkdiag(Rⁿ₀ᵀ, Rⁿ₀ᵀ) J_base — and it is just the twist transform of Lesson 1.4 applied to every column."
estimated_time: "35 min"
difficulty: "Intermediate"
prerequisites:
  - "M6 L1.4 — Transforming twists between frames"
  - "M6 L2.2–2.3 — The base-frame geometric Jacobian"
  - "M2 — The end-effector orientation Rⁿ₀"
learning_objectives:
  - "Explain why the same tool velocity has different numbers in the base vs tool frame."
  - "Convert the base-frame Jacobian to the tool frame by rotating both blocks."
  - "Connect this to the twist transform of Lesson 1.4 (same reference point ⇒ rotation only)."
  - "Decide which frame a given task naturally lives in."
tags:
  - tool-frame
  - base-frame
  - jacobian-transform
  - frames
---

# Lesson 3.3 — Base-Frame vs Tool-Frame Jacobian

## 1. Why This Matters
The geometric Jacobian we built (D-057) reports the tool twist in the **base/world
frame**. But tasks often speak in the tool's own language — "spin about my approach
axis," "slide along my $z$." Converting the base-frame Jacobian into a tool-frame one
is what lets a single model serve both views. And because both Jacobians reference the
*same* point (the tool origin), the conversion is the simplest possible case of the
Lesson 1.4 twist transform: a pure rotation, no lever-arm shift.

## 2. Physical Intuition
Watch the tool move. Standing at the robot's base, you call its velocity "0.1 m/s in
world $+X$." Riding on the tool, you call the identical motion "0.1 m/s along my own
forward axis." Same motion — the numbers differ only because your axes point
differently. Since you are both measuring the velocity *of the same point* (the tool
origin), there is no reference-point shift; you have merely turned your head. So the
conversion just re-expresses each arrow in the new orientation.

## 3. Visual Explanation
`[Visual: one moving tool with its twist drawn once; two coordinate readouts — base-frame components and tool-frame components — related by the end-effector rotation Rⁿ₀]`
**Diagram Specification (multi-panel)**

- **Panel 1 — base view:** the tool with its twist arrows resolved along world axes,
  labeled $\boldsymbol{\xi}_{\text{base}}$.
- **Panel 2 — tool view:** the same tool/motion with arrows resolved along the tool's
  own axes, labeled $\boldsymbol{\xi}_{\text{tool}}$, joined by
  $\boldsymbol{\xi}_{\text{tool}}=\mathrm{blkdiag}(R^\top,R^\top)\,\boldsymbol{\xi}_{\text{base}}$.
- Note: "same reference point ⇒ rotation only, no lever-arm term."
- Caption: "Base vs tool frame: turn your head, don't move your feet."

## 4. Mathematical Foundations
*In words first:* both Jacobians describe the velocity of the tool origin; only the
axes differ, so rotate both the linear and angular blocks by the end-effector
orientation.

Let $R^{n}_{0}$ be the end-effector orientation in the base frame. Each column of the
base-frame Jacobian is a twist about the tool origin in base coordinates; re-expressing
it in tool coordinates rotates both halves:

$$\boxed{\,J_{\text{tool}} = \begin{bmatrix} (R^{n}_{0})^\top & \mathbf{0} \\ \mathbf{0} & (R^{n}_{0})^\top \end{bmatrix} J_{\text{base}}.\,}$$

This is exactly the Lesson 1.4 transform with $\mathbf{d}=\mathbf{0}$ (same reference
point) — the block-diagonal, rotation-only case. The angular block rotates because the
axis is re-expressed; the linear block rotates for the same reason. *Back to motion:*
nothing about the robot's actual velocity changes — only the frame in which we report
it — which is why the physical motion is invariant under the transform (the notebook's
correctness check).

## 5. Engineering Example
A surface-finishing task commands the tool to press along its own approach axis while
sliding tangent to a curved part. Those commands are natural in the *tool* frame, so the
controller forms $J_{\text{tool}}$ from $J_{\text{base}}$ with the current $R^{n}_{0}$
and works there. When it instead needs world-frame reasoning (e.g., gravity
compensation direction), it uses $J_{\text{base}}$. One model, two frames, swapped by a
rotation.

## 6. Worked Example
Take the spatial 3R arm at a configuration with end-effector orientation $R^{n}_{0}$.
Form $J_{\text{tool}}=\mathrm{blkdiag}((R^{n}_{0})^\top,(R^{n}_{0})^\top)J_{\text{base}}$.
For any joint-rate $\dot{\mathbf{q}}$, the base-frame twist $J_{\text{base}}\dot{\mathbf{q}}$
and the tool-frame twist $J_{\text{tool}}\dot{\mathbf{q}}$ describe the identical motion:
rotating the tool-frame twist back by $R^{n}_{0}$ recovers the base-frame twist exactly.
That invariance is the proof the conversion is right.

## 7. Interactive Demonstration
*(Guided prediction; flagship demos at L17/L21.)*

**Predict, then check.**

1. **Predict** whether converting base→tool introduces any lever-arm ($\boldsymbol{\omega}\times\mathbf{d}$) term.
2. **Predict** what rotating the tool-frame twist by $R^{n}_{0}$ should recover.
3. **Check** both in the notebook.

## 8. Coding Exercise
In the companion notebook:

1. Compute $J_{\text{base}}$ and $R^{n}_{0}$ for a spatial arm.
2. Form $J_{\text{tool}}=\mathrm{blkdiag}((R^{n}_{0})^\top,(R^{n}_{0})^\top)J_{\text{base}}$.
3. Verify invariance: $R^{n}_{0}$-rotating the tool-frame twist returns the base-frame
   twist, for random $\dot{\mathbf{q}}$.

Prints `All checks passed.`

## 9. Knowledge Check
1. Why is the base→tool conversion a rotation only (no shift)?
2. Write $J_{\text{tool}}$ in terms of $J_{\text{base}}$ and $R^{n}_{0}$.
3. Which Lesson 1.4 special case is this?
4. Give one task that is more natural in the tool frame and one in the base frame.

## 10. Challenge Problem
Suppose you wanted the Jacobian about the *fingertip*, offset by $\mathbf{r}$ from the
tool origin, expressed in the tool frame. Combine the reference-point shift (Lesson 1.4)
with the rotation here to write the full transform, and identify exactly when the
lever-arm term reappears.

## 11. Common Mistakes
- **Adding a lever-arm term for base↔tool.** Same reference point ⇒ rotation only.
- **Rotating only one block.** Both the linear and angular halves rotate.
- **Using a stale $R^{n}_{0}$.** It changes with configuration; recompute each pose.

## 12. Key Takeaways
- Base and tool Jacobians describe the same tool-origin motion in different axes.
- $J_{\text{tool}}=\mathrm{blkdiag}((R^{n}_{0})^\top,(R^{n}_{0})^\top)\,J_{\text{base}}$.
- It is the rotation-only ($\mathbf{d}=0$) case of the Lesson 1.4 twist transform.
- Correctness = invariance of the physical twist; pick the frame the task lives in.

---

### AI Learning Companion

- **Tutor (re-explain):** "Explain base vs tool Jacobian as 'turn your head, don't move
  your feet,' and why it's rotation-only. Then quiz me."
- **Practice (generate exercises):** "Give me three problems converting base↔tool
  Jacobians and verifying invariance. Hold solutions."
- **Explore (connect to the real world):** "Which manipulation tasks are natural in the
  tool frame vs the base frame, and why?"

### Global Learning Support

- **English (authoritative):** "Explain the base-frame vs tool-frame Jacobian and the
  rotation-only transform $J_{\text{tool}}=\mathrm{blkdiag}(R^\top,R^\top)J_{\text{base}}$."
- **Español:** "Explica el jacobiano en marco base vs marco herramienta y la
  transformación de solo rotación $J_{\text{tool}}=\mathrm{blkdiag}(R^\top,R^\top)J_{\text{base}}$."
- **中文（简体）：** "用机器人学课程的水平，解释基坐标系与工具坐标系雅可比，以及纯旋转变换
  $J_{\text{tool}}=\mathrm{blkdiag}(R^\top,R^\top)J_{\text{base}}$。"
- **Türkçe:** "Taban ve takım çerçevesi Jacobian'ını ve yalnızca-dönme dönüşümü
  $J_{\text{tool}}=\mathrm{blkdiag}(R^\top,R^\top)J_{\text{base}}$'yi robotik düzeyde açıkla."

---

*Next lesson: 3.4 — Representation Singularities vs Kinematic Singularities.*
