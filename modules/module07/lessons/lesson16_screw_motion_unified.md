---
module: 07
unit: 04
lesson: 4.4
title: "Screw Motion: Unified Position + Orientation Interpolation"
core_idea: "A screw motion interpolates position and orientation together as a single coupled motion — a simultaneous rotation about and translation along one screw axis, at constant twist. It is the natural 'straight line' of full poses, unifying the position interpolation of 4.2 and the orientation SLERP of 4.3."
estimated_time: "45 min"
difficulty: "Intermediate"
prerequisites:
  - "M7 L4.2 — Cartesian position interpolation"
  - "M7 L4.3 — Orientation interpolation (SLERP)"
learning_objectives:
  - "Explain screw motion as a unified, constant-twist interpolation of a full pose."
  - "Contrast decoupled position+orientation interpolation with a single screw interpolation."
  - "Use the engine's SE(2) screw interpolation and verify it moves between two poses at constant twist."
---

# Lesson 4.4 — Screw Motion: Unified Position + Orientation Interpolation

> Lesson 4.2 interpolated **position**; Lesson 4.3 interpolated **orientation**. A full pose has both, and the most elegant way to move between two poses interpolates them *together* as one coupled motion: a **screw**. We lead with the motion — a single twisting glide — then give the constant-twist idea, and close Unit 4.

---

## 1. Why This Matters
A tool pose is position **and** orientation at once. So far we'd interpolate them separately: a straight line for position, a SLERP for orientation, run on a shared clock. That works and is common. But there's a more natural notion of "the straight line between two poses" — the **screw motion** — that treats the pose as one object and moves it along a single axis, rotating and translating in fixed proportion. It's how a bolt advances: turn and translate together along one axis.

Why care? Screw motion is the **geometrically intrinsic** interpolation of poses — coordinate-free, constant-twist, and the genuine analog of a straight line for full rigid-body motion (Chasles' theorem says *any* rigid displacement is a screw). It produces beautifully coordinated motions (the tool turns and advances as one), and it's the conceptual bridge to Module 8's rigid-body machinery. For the harvester, a screw approach lets the gripper rotate into the grasp orientation *while* advancing along the approach — one smooth coupled glide instead of two interpolations bolted together.

## 2. Physical Intuition
Watch a screw go into wood, or a corkscrew into a cork: it **rotates about** an axis and **translates along** that same axis simultaneously, in lockstep — one turn advances it a fixed distance. That single coupled motion, rotation-and-translation-along-one-axis, is a *screw motion*. It is the most economical way to get a rigid body from one pose to another: one axis, one constant "twist," and you're there.

Now the surprising fact: **every** way to move a rigid body from one pose to another can be achieved by *some* screw — pick the right axis, the right amount of rotation, and the right pitch (translation per rotation), and a single screw motion takes pose A exactly to pose B. So instead of "interpolate position, separately interpolate orientation," you can say "glide along the one screw that connects the poses." The tool turns and advances together, evenly, the whole way. That's the unified interpolation this lesson builds.

## 3. Mathematical Foundations
A full pose is a homogeneous transform $T=\begin{bmatrix}R & \mathbf p\\ \mathbf 0 & 1\end{bmatrix}$ (here in the plane, SE(2): $R$ a 2D rotation, $\mathbf p\in\mathbb R^2$). A **twist** is the velocity generator of a screw — combined linear and angular rate — living in the Lie algebra $\mathfrak{se}$, recovered by the **matrix logarithm**, and turned back into a transform by the **matrix exponential**.

**Constant-twist (screw) interpolation** between $T_0$ and $T_1$ at $s\in[0,1]$:

$$T(s) = T_0 \,\exp\!\big(s\,\log(T_0^{-1}T_1)\big).$$

Read it as: $T_0^{-1}T_1$ is the **relative** displacement from pose 0 to pose 1; $\log(\cdot)$ extracts the constant twist $\boldsymbol\xi$ that generates it; $\exp(s\,\boldsymbol\xi)$ replays a fraction $s$ of that twist; pre-multiplying by $T_0$ anchors it at the start. The result glides from $T_0$ ($s{=}0$) to $T_1$ ($s{=}1$) **at constant twist** — rotation and translation advance in fixed proportion, a single screw.

For **SE(2)** the exp/log are closed-form. A twist is $\boldsymbol\xi=(v_x,v_y,\omega)$; the exponential rotates by $\omega$ and translates by $V(\omega)\,\mathbf v$ with

$$V(\omega)=\frac{1}{\omega}\begin{bmatrix}\sin\omega & -(1-\cos\omega)\\ 1-\cos\omega & \sin\omega\end{bmatrix}\ (\omega\neq0),\qquad V\to I\ (\omega\to0),$$

and the log inverts this. The engine wraps it as `screw_interp_se2(T0, T1, s)` (with `se2(theta,x,y)` to build poses), so you can interpolate a full planar pose with one call.

**Decoupled vs screw.** Decoupled interpolation (straight-line position + SLERP orientation on a shared clock) and screw interpolation **agree at the endpoints** and are both smooth, but their *paths differ in the middle*: the screw's position path generally **curves** (it's coupled to the rotation), while decoupled keeps position dead straight. Use **decoupled** when the position path must be a literal straight line (e.g. sliding along a slot); use the **screw** when you want the most natural, coordinated full-pose motion and the exact position path is flexible. Compose either with a quintic $s(t)$ for $C^2$ timing.

## 4. Visual Explanation
`[Visual: a tool pose gliding from A to B by a screw motion — rotating about and translating along one screw axis — vs decoupled (straight position + SLERP) showing the paths agree at ends but differ between]`

**Diagram Specification**

- **Objective:** show the screw as one coupled rotate-and-advance motion, and how it differs from decoupled interpolation between the same poses.
- **Scene:** tool/gripper drawn at pose A and pose B, with intermediate poses from **screw** interpolation (emerald) turning and advancing together along a marked screw axis; faintly overlay the **decoupled** intermediate poses (straight position + SLERP, violet). Mark "agree at endpoints, differ between."
- **Labels:** "screw: rotate about + translate along one axis (constant twist)"; "decoupled: straight position + SLERP"; screw axis labeled.
- **Form:** SVG. Screw emerald `#10b981`; decoupled violet `#8b5cf6`; poses ink; screw axis muted dashed.

## 5. Engineering Example
Screw (and the closely related "twist") interpolation underlies modern robotics motion libraries and the product-of-exponentials formulation used across the field. Practically, it gives controllers a single, coordinate-free way to interpolate a full pose without splitting it into position and orientation and worrying about how to keep them consistent — the twist couples them automatically. For the harvester, a screw approach lets the gripper roll into the grasp orientation as it advances toward the fruit, a single natural glide; the planner picks decoupled straight-line position instead only when the approach must follow an exact line (e.g. between two leaves). Both are in the toolbox; the screw is the one that treats the pose as the single object it is.

## 6. Worked Example
Interpolate a planar pose from $T_0=\text{SE2}(0,\,0.4,\,0.0)$ (orientation $0$, at $(0.4,0)$) to $T_1=\text{SE2}(\tfrac{\pi}{2},\,0.2,\,0.3)$ (orientation $90^\circ$, at $(0.2,0.3)$).

- Relative displacement $T_0^{-1}T_1$ has a $90^\circ$ rotation and a translation; $\log$ gives a single twist $\boldsymbol\xi=(v_x,v_y,\omega)$ with $\omega=\pi/2$.
- $T(s)=T_0\exp(s\boldsymbol\xi)$ replays a fraction $s$ of that twist. At $s=0$ it equals $T_0$; at $s=1$ it equals $T_1$ (verified to machine precision); at $s=0.5$ the pose is rotated $45^\circ$ and positioned partway along the **curved** screw path — not the straight chord.
- Decoupled comparison: straight-line position + `slerp_angle` from $0$ to $90^\circ$ gives the same endpoints and orientation schedule but a **straight** position path. The notebook overlays both and confirms endpoints match while mid-paths differ, and that the screw advances at constant twist.

## 7. Interactive Demonstration
*(Conceptual — runnable in the companion notebook.)*

**One twist, end to end.** In the notebook you:

1. Build two planar poses and interpolate with `screw_interp_se2`; verify endpoints match $T_0$ and $T_1$ exactly.
2. Plot the screw position path and orientation schedule; confirm rotation and translation advance in fixed proportion (constant twist).
3. Overlay the decoupled (straight-position + SLERP) path to see the endpoints agree and the middles differ.

## 8. Coding Exercise
*(Snippet / notebook task — uses `se2`, `screw_interp_se2`, `slerp_angle`, `cartesian_line`.)*

In the companion notebook:

1. Interpolate a full planar pose with `screw_interp_se2` and assert the endpoints reproduce $T_0$ and $T_1$ (to machine precision).
2. Assert the motion is **constant-twist**: equal steps in $s$ produce equal incremental screw displacements (e.g. the relative transform between consecutive samples is constant).
3. Build the decoupled (straight position + `slerp_angle`) interpolation between the same poses; assert endpoints match but the mid-path positions differ — a runnable contrast of unified vs decoupled.

## 9. Knowledge Check
1. What is a screw motion, and what does "constant twist" mean?
2. Write the screw-interpolation formula and explain each factor ($T_0$, $\log$, $\exp$).
3. How do decoupled (straight-position + SLERP) and screw interpolation compare at the endpoints and in between?
4. When would you prefer decoupled interpolation over a screw?

## 10. Challenge Problem
Chasles' theorem says any rigid displacement is a single screw. Take a pure translation (no rotation) and a pure rotation about the tool point (no translation), and describe the screw for each — in particular, what is the screw axis and pitch (translation per rotation) in each limiting case? Then explain what the screw interpolation $T(s)=T_0\exp(s\log(T_0^{-1}T_1))$ reduces to in each case, and why the formula handles both without special-casing. *(This connects to the SE(2)/SE(3) exp–log machinery that Module 8 builds on.)*

## 11. Common Mistakes
- **Assuming the screw keeps position straight.** The screw's position path generally curves (coupled to rotation); use decoupled interpolation when you need a literal straight line.
- **Interpolating $T_1^{-1}T_0$ or mis-ordering the product.** The relative transform is $T_0^{-1}T_1$, applied as $T_0\exp(s\log(\cdot))$.
- **Forgetting the $\omega\to0$ limit.** When there's little/no rotation, $V(\omega)\to I$; the closed form must handle it (the engine does).
- **Treating screw as dynamics.** Twist here is a *kinematic* interpolation generator — no forces or torques (that's Module 8).

## 12. Key Takeaways
- A **screw motion** rotates about and translates along **one axis** at **constant twist** — the natural "straight line" between two full poses (Chasles' theorem).
- **Screw interpolation:** $T(s)=T_0\exp(s\log(T_0^{-1}T_1))$ — extract the relative twist, replay a fraction $s$ of it; constant-twist, endpoints exact.
- **Decoupled** (straight position + SLERP) and **screw** agree at the endpoints but differ between; choose decoupled for a literal straight position path, screw for the most natural coupled full-pose motion.
- **Unit 4 recap:** why Cartesian (4.1) → straight-line position via interpolate-then-IK with branch consistency (4.2) → orientation by SLERP (4.3) → unified position+orientation by screw (4.4). The trajectory is always a **reference** the M6 velocity layer executes open-loop — no feedback (Module 8). Units 5–6 next add **feasibility** (limits, time-optimal timing) and **planning** (collision-free paths) on top of these trajectory primitives.

---

### AI Learning Companion

Copy any prompt below into your AI tutor.

- **Tutor (re-explain):** "Re-explain screw motion using the bolt/corkscrew analogy and Chasles' theorem (every rigid displacement is one screw). Keep the exp/log light. Then contrast screw vs decoupled interpolation for me."
- **Practice (generate exercises):** "Give me three full-pose interpolation problems (start and end pose). Ask me whether a screw or decoupled interpolation fits the stated requirement (e.g. 'position must stay on a straight line') and why. Withhold answers until I respond."
- **Explore (connect to the real world):** "Explain where screw/twist interpolation and the product-of-exponentials formulation are used in modern robotics, and why treating a pose as one object (not split into position and orientation) is convenient."

### Global Learning Support

Per-language explanation prompts — use whichever you think best in.

- **English (authoritative):** "Explain screw-motion interpolation of a robot tool's full pose: a constant-twist rotation-about-and-translation-along one axis, the formula T(s)=T0·exp(s·log(T0⁻¹T1)), and how it differs from decoupled position+SLERP, at a robotics-course level (keep exp/log light)."
- **Español:** "Explica la interpolación por movimiento helicoidal (screw) de la pose completa de la herramienta de un robot: una rotación-y-traslación de torsión constante alrededor de un eje, la fórmula T(s)=T0·exp(s·log(T0⁻¹T1)), y en qué difiere de la interpolación desacoplada posición+SLERP, a nivel de curso de robótica (sin profundizar en exp/log)."
- **中文（简体）：** "用机器人课程的水平，解释机器人工具完整位姿的螺旋运动（screw）插值：绕一个轴的等旋量旋转兼平移，公式 T(s)=T0·exp(s·log(T0⁻¹T1))，以及它与位置+SLERP 解耦插值的区别（exp/log 从简）。"
- **Türkçe:** "Bir robot aracının tam pozunun vida-hareketi (screw) interpolasyonunu açıkla: tek bir eksen etrafında sabit-twist dönme-ve-öteleme, T(s)=T0·exp(s·log(T0⁻¹T1)) formülü ve bunun ayrık konum+SLERP interpolasyonundan farkı — robotik dersi düzeyinde (exp/log hafif tutulsun)."

---

*Next: the Module 7 midpoint assessment (Units 1–4), then Installment C — Unit 5 (Trajectory Feasibility and Time-Optimal Timing).*
