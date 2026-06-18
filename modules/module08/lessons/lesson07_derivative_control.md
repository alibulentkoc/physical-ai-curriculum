---
module: 08
unit: 02
lesson: 2.3
title: "Derivative Control: Anticipate and Damp"
core_idea: "Derivative control responds to how fast the error is changing: u_D = Kd·ė. It acts like a brake — opposing rapid approach to the target — so it damps overshoot and oscillation, letting you use higher P and I gains. Its weakness is noise: differentiating a noisy signal amplifies it, so derivative action must be filtered or taken on the measurement."
estimated_time: "40 min"
difficulty: "Intermediate"
prerequisites:
  - "M8 L2.1 — Proportional control"
  - "M8 L2.2 — Integral control"
learning_objectives:
  - "State the derivative control law u_D = Kd·ė and explain its damping (braking) effect."
  - "Explain how derivative action enables higher P/I gains by suppressing overshoot."
  - "Explain why derivative control amplifies noise and how filtering / derivative-on-measurement helps."
---

# Lesson 2.3 — Derivative Control: Anticipate and Damp

> Proportional tracked but offset; integral erased the offset but added overshoot and oscillation. Derivative control is the **brake** that calms it: it responds to how fast the error is changing, opposing a too-rapid approach so the joint eases into the target instead of overshooting. We lead with the **PID Playground** — drag all three gains and feel each term's job — then study derivative's damping and its one enemy, noise.

---

## 1. Why This Matters
Proportional and integral both *push* toward the target; neither anticipates arriving. So an aggressive P or I makes the joint rush at the target and sail past it — overshoot and ringing. Derivative control adds anticipation: it watches the *rate* at which the error is changing and pushes back against fast change, like a brake applied as you approach a wall. The faster you're closing the gap, the harder it eases off. This **damps** overshoot and oscillation.

That damping is what makes a controller usable at high performance. With derivative action calming the transient, you can raise the proportional and integral gains — getting faster, tighter tracking and quicker offset removal — *without* the overshoot those higher gains would otherwise cause. Derivative is the term that buys stability margin. Its price is sensitivity to **noise**: derivative means differentiating the error, and differentiating a noisy measurement amplifies the noise into a jittery, even destabilizing command. So derivative action is always filtered or applied carefully (often on the measurement rather than the error). This lesson completes the three control actions — and the **PID Playground** demo lets you feel proportional, integral, and derivative interact before the next lesson assembles them into the full PID law. This is the last piece of the **correction** toolkit before we study **stability** as its own unit.

## 2. Physical Intuition
Imagine catching a ball rolling toward a line you want it to stop on. Proportional says "push toward the line, proportional to distance." But if the ball is rolling *fast* toward the line, a pure proportional push won't stop it in time — it overshoots. What you actually do is *brake harder the faster it's approaching*: you watch its speed, and you resist proportionally to how fast it's closing in. That braking-by-approach-speed is derivative action. It doesn't care where the ball is, only how fast the gap is shrinking, and it opposes fast shrinkage so the ball eases to a stop on the line rather than blowing past it.

A robot joint's derivative term works the same way: it measures how fast the tracking error is changing and commands a counter-effort proportional to that rate. When the joint is rushing toward the target (error shrinking fast), derivative pushes back, slowing the approach and preventing overshoot — a velocity-dependent brake. The catch from the analogy: if your view of the ball is shaky (you can't tell its speed precisely), your braking becomes jerky and erratic. A robot's measured angle has sensor noise, and taking its rate of change magnifies that noise into a twitchy command — which is why derivative action must be smoothed.

## 3. Mathematical Foundations
**Derivative control** commands effort proportional to the *rate of change* of the error:

$$u_D(t) = K_d\,\dot e(t) = K_d\,\frac{d}{dt}\big(q_d - q\big),$$

with $K_d > 0$ the derivative gain. In discrete form: $\dot e \approx (e_k - e_{k-1})/\Delta t$, so $u_D = K_d (e_k - e_{k-1})/\Delta t$.

- **Damping (the brake).** When the joint approaches the target quickly, $e$ is shrinking fast, so $\dot e < 0$, and $u_D < 0$ opposes the motion — it brakes. This **damps overshoot and oscillation**: it removes energy from the transient as the target nears.
- **Enables higher P/I gains.** Because derivative suppresses the overshoot that high gains cause, you can raise $K_p$ and $K_i$ for faster, tighter response and quicker offset removal, then use $K_d$ to keep the transient clean. Derivative buys stability margin.
- **Anticipation, not memory.** Where integral acts on the *past* (accumulated error), derivative acts on the *trend* (where the error is heading) — it's the predictive term.

**The noise problem.** Differentiation amplifies high-frequency content: if the measured $q$ has noise, $\dot e$ has *much* larger noise, producing a jittery, possibly destabilizing command. Fixes: (1) **filter** the derivative (low-pass the rate estimate); (2) take the **derivative on the measurement** ($-K_d \dot q$) rather than on the error, which avoids a spike when the setpoint changes ("derivative kick") and is standard practice; (3) keep $K_d$ modest. The engine computes derivative-on-error with a finite difference (`PIDController` with `Kd`); the notebook demonstrates both the damping benefit and the noise-amplification cost (and that filtering/modest $K_d$ tames it).

## 4. Visual Explanation
`[Visual: step responses comparing PI (overshoot and ringing) vs PID (the derivative term damping it to a clean settle); an inset shows the derivative command acting as a brake — large and opposing during fast approach — and a second inset shows noise amplification: a noisy measurement producing a smooth P command but a jagged D command]`

**Diagram Specification**

- **Objective:** show derivative damping overshoot (enabling clean high-gain response) and its noise-amplification cost.
- **Scene:** **Main:** step response — a **PI** curve overshooting and ringing, and a **PID** curve (same P, I, plus $K_d$) easing cleanly to the target with little/no overshoot. **Inset 1:** the derivative command $u_D$ plotted over the transient — large and *negative* (braking) during the fast approach, then fading. **Inset 2:** "noise" — a noisy measured $q$; the resulting P command (smooth-ish) vs the D command (jagged/amplified), with a note "filter or use derivative-on-measurement".
- **Labels:** "PI: overshoot/ring", "PID: damped, clean", "$u_D$ brakes the approach", "noise → D amplifies it".
- **Form:** SVG, main step-response + two insets. PI rose `#e11d48`, PID teal `#0d9488`, derivative-command violet `#8b5cf6`, noise muted/jagged.

## 5. Engineering Example
Derivative action is the damping term in countless real controllers. A drone's attitude controller uses the "D" (rate) term heavily — measured directly by the gyroscope as angular rate — to damp oscillation and hold steady; without it, the craft wobbles. Robot joint controllers use derivative (usually as velocity feedback, $-K_d\dot q$, read straight from the encoder's rate) to settle crisply at the target without ringing. Hard-disk head positioning, camera gimbals, and machine-tool axes all rely on derivative damping for clean, fast settling. And every one manages the noise: rate is either measured directly (gyro, tachometer) or filtered, because raw differentiation of a position sensor is too noisy to use directly. For the greenhouse arm, derivative damping is what lets a joint move quickly to a grasp pose and stop precisely without oscillating near the fruit — but the gain is kept modest and the rate is taken from the encoder velocity to avoid a twitchy command.

## 6. Worked Example
Damp the integral overshoot from Lesson 2.2.

- **Setup:** the PI controller ($K_p, K_i$) from Lesson 2.2 reached the target but overshot ~30%+ and rang before settling.
- **Add derivative:** introduce $K_d$. The derivative term brakes the fast approach, and the overshoot drops sharply — in the engine's check, from ~34% (PI) to ~0% (PID) — settling cleanly and faster, with the offset still zero (integral) and tracking still tight (proportional).
- **Raise the gains:** with derivative damping in place, push $K_p$ and $K_i$ higher for a snappier response; the derivative keeps the overshoot in check — performance you couldn't safely reach without it.
- **Noise test:** add measurement noise. The derivative-on-error command becomes jagged; switching to a filtered / derivative-on-measurement form (or a modest $K_d$) smooths it while keeping the damping. The notebook shows the overshoot collapse, the higher-gain headroom, and the noise effect with and without filtering.

## 7. Interactive Demonstration
**Use the PID Playground (this lesson's demo).** Steps:

1. Start with **P only** — see the steady-state offset under load (drag $K_p$: tighter but overshoot/oscillation appears).
2. Add **I** — watch the offset go to zero, but overshoot/ringing grow.
3. Add **D** — watch the overshoot get damped out; the response eases cleanly to the target. Read the live metrics (overshoot, settling time, steady-state error) update as you drag each gain.
4. Toggle **measurement noise** and watch the derivative command get jittery — then reduce $K_d$ or enable filtering to tame it.

The Playground makes each term's job tangible: P pushes, I erases offset, D damps — the whole story of the next lesson, felt by hand.

## 8. Coding Exercise
*(Snippet / notebook task — uses `PIDController(Kp, Ki, Kd, i_clamp)`, `simulate_closed_loop`, `step_response_metrics`.)*

In the companion notebook:

1. Run PI vs PID on the same loaded step and assert PID's overshoot is substantially smaller than PI's (derivative damps).
2. With derivative present, raise $K_p$/$K_i$ and assert the response is faster while overshoot stays bounded (derivative buys gain headroom).
3. Add noise to the measurement and assert the derivative command's variance is much larger than the proportional command's (noise amplification), then show a modest $K_d$ / filtered rate reduces it.

## 9. Knowledge Check
1. State the derivative control law and describe its braking/damping effect.
2. How does derivative action let you use higher P and I gains?
3. Why does derivative control amplify noise?
4. Name two ways to manage derivative noise.

## 10. Challenge Problem
Explain why derivative is the only one of the three terms that is *predictive* (it acts on where the error is heading, not where it is or where it's been), and why that makes it the natural damping term. Then explain "derivative kick": why taking the derivative of the *error* causes a command spike when the setpoint suddenly changes, and why taking the derivative of the *measurement* ($-K_d\dot q$) avoids it while preserving the damping. *(Derivative anticipates — but must be applied carefully.)*

## 11. Common Mistakes
- **Too much $K_d$.** Excessive derivative makes the command jittery (noise) and sluggish; it's a damping term, used in moderation.
- **Differentiating raw noisy position.** Always filter the rate or measure it directly (encoder velocity, gyro) — raw differentiation amplifies noise badly.
- **Derivative on error causing kick.** A setpoint jump makes $\dot e$ spike; use derivative-on-measurement to avoid the command spike.
- **Expecting derivative to remove offset or track alone.** Derivative only damps; it needs P (and I for zero offset) — it's never used by itself.

## 12. Key Takeaways
- **Derivative control** $u_D = K_d \dot e$ responds to the *rate of change* of error — a velocity-dependent **brake** that **damps overshoot and oscillation**.
- It is the **predictive/anticipatory** term, and it **enables higher P and I gains** by keeping the transient clean — it buys stability margin.
- Its weakness is **noise amplification**; manage it with **filtering**, **derivative-on-measurement** ($-K_d\dot q$), and **modest gains**.
- P pushes, I erases offset, D damps. Next we assemble all three into the complete **PID controller**.

---

### AI Learning Companion

Copy any prompt below into your AI tutor.

- **Tutor (re-explain):** "Re-explain derivative control using the 'brake harder the faster the ball approaches the line' analogy. Stress u_D = Kd·ė as a velocity-dependent brake that damps overshoot, enables higher P/I gains, and amplifies noise (so filter it or use derivative-on-measurement). Then ask me why it's the predictive term."
- **Practice (generate exercises):** "Give me PI responses with overshoot and ask me what adding derivative does, whether higher P/I become usable, and what noise does to the derivative command. Withhold answers until I respond."
- **Explore (connect to the real world):** "Explain how a drone uses the gyroscope's rate measurement as the derivative term to damp attitude oscillation, and why rate is measured directly rather than differentiated from position."

### Global Learning Support

Per-language explanation prompts — use whichever you think best in.

- **English (authoritative):** "Explain derivative control u_D = Kd·ė for a robot joint: its damping (braking) effect on overshoot, how it enables higher P/I gains, and why it amplifies measurement noise (managed by filtering or derivative-on-measurement), at a robotics-course level (no formal control theory)."
- **Español:** "Explica el control derivativo u_D = Kd·ė para una articulación de robot: su efecto de amortiguamiento (freno) sobre el sobreimpulso, cómo permite ganancias P/I más altas, y por qué amplifica el ruido de medición (gestionado con filtrado o derivada sobre la medición), a nivel de curso de robótica (sin teoría de control formal)."
- **中文（简体）：** "用机器人课程的水平（不涉及形式控制理论），解释机器人关节的微分控制 u_D = Kd·ė：它对超调的阻尼（制动）作用、如何允许更高的 P/I 增益，以及为什么它会放大测量噪声（通过滤波或对测量量求导来处理）。"
- **Türkçe:** "Bir robot eklemi için türev kontrolü u_D = Kd·ė açıkla: aşım üzerindeki sönümleme (frenleme) etkisi, daha yüksek P/I kazançlarını nasıl mümkün kıldığı ve ölçüm gürültüsünü neden yükselttiği (filtreleme veya ölçüm-üzerinden-türev ile yönetilir) — robotik dersi düzeyinde (biçimsel kontrol teorisi yok)."

---

*Next lesson: 2.4 — The PID Controller: The Complete Single-Joint Tracker (assembling P + I + D, and the Unit 2 recap).*
