---
module: 08
unit: 04
lesson: 4.2
title: "Feedback Reacts, Feedforward Anticipates"
core_idea: "Feedback waits for an error, then corrects it — always a step behind a moving target. Feedforward does the opposite: because Module 7 already told us where the joint is going (q̇_d) and how hard it must accelerate (q̈_d), the controller can compute most of the command in advance and apply it the instant it's needed — no error required. Feedback reacts to the past; feedforward anticipates the future. This is why Module 7 computed more than just q_d."
estimated_time: "45 min"
difficulty: "Intermediate"
prerequisites:
  - "M8 L4.1 — Tracking a trajectory with feedback"
  - "M7 — q_d, q̇_d, q̈_d from the reference layer"
learning_objectives:
  - "Explain feedforward as anticipation computed from the known reference, before any error forms."
  - "Explain why feedback alone lags and how feedforward removes the lag in principle."
  - "Identify exactly how q̇_d and q̈_d enter the feedforward command."
---

# Lesson 4.2 — Feedback Reacts, Feedforward Anticipates

> Last lesson exposed feedback's honest limit: it can only correct an error *after* it appears, so it always trails a moving reference. This lesson introduces the idea that fixes it — and it is the conceptual centre of Module 8. **Feedback reacts. Feedforward anticipates.** Because Module 7 already computed where each joint is going ($\dot q_d$) and how hard it must accelerate ($\ddot q_d$), the controller can work out most of the command *in advance* and apply it at the right instant — without waiting for an error. We meet feedforward as an idea — anticipation — before any equation.

---

## 1. Why This Matters
Everything in Module 8 has pointed here. Module 7 didn't just compute *where* the joint should be; it computed *where it's going* and *how hard it must push to get there on time* — the velocity $\dot q_d$ and acceleration $\ddot q_d$ of the planned motion. In Units 1–3 and Lesson 4.1 we threw those away and used only $q_d$, letting feedback discover the rest by trial and error, a step late. That's the source of the following-error lag.

Feedforward is the realisation that we don't have to discover what we already know. If the plan says "accelerate hard now," the controller can push hard *now* — not wait for the joint to fall behind and then react. This is the payoff of the whole Modules 7→8 pipeline, and the reason the handoff carried three signals instead of one. It also reframes the controller's job: feedforward handles the *known, planned* part of the motion; feedback is freed to handle only the *unknown* part — disturbances and model error. That division of labour is the most important idea in the module.

## 2. Physical Intuition
Two ways to carry a full cup of coffee to a table. The **reactive** way: walk, and whenever you see the coffee start to slosh, correct. You're always responding to a spill that's already begun — pure feedback, always a beat behind. The **anticipatory** way: you *know* you're about to stop at the table, so you ease off *before* you arrive, tilting the cup to counter the deceleration you know is coming. You prevent the slosh instead of chasing it. That's feedforward — acting on what you know is about to happen.

A driver does both at once. Approaching a known curve, you turn the wheel *as you enter* because you can see the curve coming (feedforward from the known road ahead) — you don't wait until the car has drifted toward the outside edge and then yank back (that would be feedback alone, and you'd swing wide every time). Feedback still matters — for the gust you didn't see, the patch of ice — but the bulk of the steering is anticipation. A robot joint following a Module-7 trajectory is exactly this: the plan is the road ahead. Feedforward steers for the known curve; feedback cleans up the surprises.

## 3. Mathematical Foundations
**Feedback** computes its command from the *measured error*:
$$u_{\text{fb}}(t) = \text{PID}\big(e(t)\big), \qquad e = q_d - q.$$
It needs an error to exist before it does anything — inherently reactive, inherently a step behind a moving reference.

**Feedforward** computes its command from the *known reference*, before any error forms. Our joint plant obeys $m\ddot q = u - b\dot q - \ell$. If we want the joint to follow the plan, we can ask: *what command would produce exactly the planned motion?* Rearranging with the planned $\dot q_d,\ \ddot q_d$ in place of the actual values gives the **inverse-model feedforward**:
$$u_{\text{ff}}(t) = m\,\ddot q_d(t) + b\,\dot q_d(t) + \ell.$$

Read it term by term — this is where Module 7's outputs are *consumed*:

- $m\,\ddot q_d$ — supply the force to produce the **planned acceleration** (uses $\ddot q_d$).
- $b\,\dot q_d$ — overcome the damping at the **planned velocity** (uses $\dot q_d$).
- $\ell$ — hold the known load.

If the model ($m, b, \ell$) were perfect and there were no disturbances, this command alone would make the joint follow $q_d(t)$ *exactly*, with **no error and no lag** — because it's computed from the plan, not from a gap. That's anticipation in one equation. The point is not the algebra; it's that $\dot q_d$ and $\ddot q_d$ — the very signals Module 7 took care to compute and that feedback ignored — are precisely what feedforward needs. This is why the reference layer carries the velocity and acceleration, not just the position. In the engine, `feedforward_full(qd_d, qdd_d, m, b, load_comp)` is exactly $m\ddot q_d + b\dot q_d + \ell$, and `track_reference(..., ff="full")` with **no feedback** tracks a fast trajectory to near-zero error when the model is good — anticipation demonstrated.

## 4. Visual Explanation
`[Visual: side-by-side on the same fast reference — LEFT 'feedback reacts': actual trails the reference, the correction command rising only after the error opens; RIGHT 'feedforward anticipates': the command computed from the plan rises in step with the reference's acceleration, the actual sitting right on the reference with no lag — with q̈_d and q̇_d shown feeding the feedforward command]`

**Diagram Specification**

- **Objective:** contrast reactive feedback (command follows the error) with anticipatory feedforward (command follows the plan), and show $\dot q_d,\ \ddot q_d$ feeding the feedforward.
- **Scene:** two panels sharing a fast reference $q_d(t)$. **LEFT (feedback reacts):** actual $q(t)$ trailing $q_d$ (shaded lag); below it, the command trace rising *after* the error grows, labelled "reacts to error". **RIGHT (feedforward anticipates):** actual $q(t)$ sitting on top of $q_d$ (no visible gap); below it, the command trace mirroring the reference's acceleration profile, labelled "computed from the plan". Small feed-in arrows on the right panel from "$\ddot q_d$" and "$\dot q_d$" into the command. A caption: "feedback uses the past error; feedforward uses the known future."
- **Labels:** "feedback reacts", "feedforward anticipates", "lag", "no lag", "$u_{ff}=m\ddot q_d+b\dot q_d+\ell$", "$\ddot q_d$", "$\dot q_d$".
- **Form:** SVG, two tracking panels + command traces + feed-in arrows. Feedback rose `#e11d48`, feedforward emerald `#10b981`, reference teal `#0d9488`.

## 5. Engineering Example
Feedforward is the standard tool of high-performance motion control, precisely because feedback alone can't keep up. CNC machines, laser cutters, pick-and-place machines, and printer carriages all use **velocity and acceleration feedforward** computed from the planned motion profile — without it, fast contours round off and corners are cut (the following error of Lesson 4.1). Camera gimbals feed forward the planned pan/tilt rate so the image stays locked during fast slews. Hard-disk head positioners and semiconductor steppers use feedforward to hit nanometre tracking at high speed. In every case the planner (our Module 7) supplies the velocity and acceleration, and the controller anticipates with them. The recurring industry lesson: *to track fast, anticipate; feedback alone is for the surprises.* This is also why a planner that only output positions would be crippling a high-speed controller — exactly why Module 7 was built to output the full triple.

## 6. Worked Example
Show anticipation removing the lag (good model, no disturbance).

- **Setup:** the same fast 1.5 s move from Lesson 4.1; compare feedback-only vs feedforward-only.
- **Feedback-only** (tuned PID, $q_d$ only): tracking RMS ≈ **0.075 rad** — the familiar following-error lag during the fast middle.
- **Feedforward-only** ($u_{\text{ff}}=m\ddot q_d+b\dot q_d+\ell$ from Module 7's signals, **no** feedback, near-accurate model): tracking RMS ≈ **0.016 rad** — the joint rides on the reference because the command was computed from the plan, not from an error. With a *perfect* model and no disturbance it would be essentially zero.
- **Reading it:** feedforward alone, with a good model, beats a tuned feedback loop on a known trajectory — because it never waits for an error. But notice the caveat hiding in "good model" and "no disturbance": that's the gap feedback fills, and the subject of the next two lessons.
- The notebook computes both RMS values and confirms feedforward's near-zero following error on the known move.

## 7. Interactive Demonstration
*(Conceptual — runnable in the companion notebook.)*

**See anticipation.** In the notebook you:

1. Track the fast reference with feedback only and plot the following-error gap.
2. Switch to feedforward only (computed from $\dot q_d,\ \ddot q_d$, no feedback) and watch the actual ride on the reference — the gap nearly vanishes.
3. Plot the feedforward command and see it mirror the planned acceleration profile — the controller pushing *before* any error exists.

## 8. Coding Exercise
*(Snippet / notebook task — uses `track_reference(ff="none"/"full")`, `feedforward_full`, `tracking_rms`.)*

In the companion notebook:

1. Track the fast reference with `ff="none"` (feedback only) and record the tracking RMS.
2. Track the same reference with `ff="full"` and **zero feedback gains** (feedforward only) using a near-accurate model; assert the tracking RMS is **much smaller** than feedback-only.
3. Assert the feedforward command magnitude scales with $\ddot q_d$ (largest where the planned acceleration is largest) — confirming it's computed from the plan, not the error.

## 9. Knowledge Check
1. In one sentence each, contrast what feedback and feedforward act on.
2. Write the inverse-model feedforward command and say which Module 7 signal each term uses.
3. Why can feedforward (with a good model) track a fast trajectory with almost no lag, when feedback can't?
4. Why did Module 7 compute $\dot q_d$ and $\ddot q_d$, not just $q_d$?

## 10. Challenge Problem
Starting from the plant balance $m\ddot q = u - b\dot q - \ell$, derive the feedforward command that would make the joint follow a planned $q_d(t)$ exactly under a perfect model, and identify which Module 7 signal supplies each term. Then explain precisely *why* this command produces zero following error in the ideal case while feedback cannot — referring to *when* each controller gets its information. Finally, name the two assumptions ("perfect model," "no disturbance") that make pure feedforward fragile, and predict what real effect each broken assumption would cause — motivating the combination in the next lesson. *(You are proving anticipation works, and finding exactly where it needs help.)*

## 11. Common Mistakes
- **Thinking feedforward is just a bigger gain.** It's a different signal source — the known plan — not a stronger reaction to error.
- **Believing feedforward replaces feedback.** It handles the *known* motion; it can't reject the *unknown* (disturbances, model error) — that still needs feedback.
- **Using only $q_d$ for feedforward.** Position alone isn't enough; anticipation needs $\dot q_d$ (damping) and $\ddot q_d$ (inertia).
- **Forgetting the model.** Feedforward's accuracy depends on knowing $m, b, \ell$; a wrong model leaves a residual — which feedback then cleans up.

## 12. Key Takeaways
- **Feedback reacts** to errors that have already formed; **feedforward anticipates** using the known plan — it acts before any error exists.
- The inverse-model feedforward $u_{\text{ff}} = m\ddot q_d + b\dot q_d + \ell$ **consumes Module 7's $\ddot q_d$ and $\dot q_d$** — exactly why they were computed.
- With a good model and no disturbance, feedforward alone tracks a fast trajectory with almost **no lag** — something feedback cannot do.
- Feedforward handles the **known**; feedback must still handle the **unknown**. Next: combine them — the payoff.

---

### AI Learning Companion

Copy any prompt below into your AI tutor.

- **Tutor (re-explain):** "Re-explain feedforward as anticipation using the 'carrying coffee / steering into a known curve' analogy: feedback reacts to a spill or drift that already started; feedforward acts on what you know is coming. Then show how the command u_ff = m·q̈_d + b·q̇_d + ℓ uses Module 7's q̈_d and q̇_d, keeping it intuition-first."
- **Practice (generate exercises):** "Quiz me: for a given trajectory segment (accelerating, cruising, decelerating), ask what the feedforward command should do and which signal drives it. Withhold answers until I respond."
- **Explore (connect to the real world):** "Explain how CNC machines and camera gimbals use velocity/acceleration feedforward from the planned motion, and why feedback alone rounds off fast corners."

### Global Learning Support

Per-language explanation prompts — use whichever you think best in.

- **English (authoritative):** "Explain feedforward as anticipation for a robot joint: feedback reacts to existing error while feedforward computes the command from the known reference (u_ff = m·q̈_d + b·q̇_d + ℓ), consuming Module 7's q̈_d and q̇_d, and why this removes following-error lag with a good model — at a robotics-course level (no formal control theory)."
- **Español:** "Explica el control anticipativo (feedforward) como anticipación para una articulación de robot: la realimentación reacciona al error existente mientras el feedforward calcula el comando a partir de la referencia conocida (u_ff = m·q̈_d + b·q̇_d + ℓ), usando q̈_d y q̇_d del Módulo 7, y por qué esto elimina el retardo de seguimiento con un buen modelo — a nivel de curso de robótica."
- **中文（简体）：** "把前馈解释为机器人关节的'预判'：反馈对已存在的误差作出反应，而前馈根据已知参考计算指令（u_ff = m·q̈_d + b·q̇_d + ℓ），消耗模块7的 q̈_d 和 q̇_d，并说明在模型良好时这为何能消除跟踪滞后——机器人课程水平（不涉及形式控制理论）。"
- **Türkçe:** "İleri beslemeyi bir robot eklemi için öngörü olarak açıkla: geri besleme var olan hataya tepki verirken ileri besleme komutu bilinen referanstan hesaplar (u_ff = m·q̈_d + b·q̇_d + ℓ), Modül 7'nin q̈_d ve q̇_d değerlerini kullanır; iyi bir modelle bunun izleme gecikmesini neden ortadan kaldırdığını anlat — robotik dersi düzeyinde."

---

*Next lesson: 4.3 — Feedforward + Feedback Together.*
