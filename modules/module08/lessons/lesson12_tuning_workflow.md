---
module: 08
unit: 03
lesson: 3.4
title: "Tuning a Controller: A Practical Workflow"
core_idea: "Tuning isn't guesswork or theory — it's a repeatable recipe driven by behaviour. Raise the proportional gain until the response is brisk and just begins to oscillate, back it off; add derivative to damp the overshoot, which buys room for more proportional; add just enough integral to erase the steady-state offset. Watch the four metrics, respect the stability edge, and stop at 'good' rather than 'maximum.'"
estimated_time: "45 min"
difficulty: "Beginner"
prerequisites:
  - "M8 L3.2 — The shape of a response"
  - "M8 L3.3 — Stable, marginal, unstable"
learning_objectives:
  - "Apply a step-by-step P→D→I tuning workflow to reach a good response."
  - "Use the four response metrics to judge each tuning step."
  - "Tune while respecting the stability edge — stop at balanced, not maximal."
---

# Lesson 3.4 — Tuning a Controller: A Practical Workflow

> You can read a response's shape and name its stability. Now you can *tune*. Tuning has a reputation for black magic, but in practice it's a short, repeatable recipe grounded entirely in the behaviour you've learned to see: bring up the proportional gain until it's brisk and just starts to oscillate, back off; add derivative to damp the overshoot (which lets you push proportional further); add just enough integral to erase the leftover offset. The four metrics are your scoreboard and the stability edge is your guardrail. This lesson closes Unit 3 by turning understanding into a method.

---

## 1. Why This Matters
Everything in Unit 3 has been building to a single practical skill: given a joint and a controller, *set the gains well.* A controller with bad gains is worse than useless — it can be sluggish, imprecise, or dangerous. Yet tuning is often taught either as superstition ("nudge it until it feels right") or as heavy theory (pole placement, frequency response) that's overkill for most robot joints. There's a middle path: a **behaviour-driven workflow** that gets you a good response reliably, using exactly the concepts you already have.

This matters because you'll do it constantly — every new joint, every payload change, every mechanism rebuild can need a retune. A method that's fast, safe, and explainable beats both guessing and grinding through math. And it sets up Unit 4: once a single joint tracks a step well, we point the tuned loop at a *moving* Module 7 reference and discover the next idea — feedforward.

## 2. Physical Intuition
Tuning is like dialling in the sensitivity on a game controller or a car's steering. You start with the response too soft — sluggish, vague. You turn up the responsiveness until steering feels crisp and quick. Push a touch too far and it gets twitchy, darting and overshooting; you back off slightly to the edge of crisp-but-calm. If it still feels floaty or bouncy, you add damping (stiffer return-to-centre) so quick inputs don't ring. If it consistently sits a hair off-centre, you add a slow trim that nudges it exactly to centre over a second or two. At every step you're *feeling the behaviour* and adjusting one thing — never blindly maximising. A robot joint tunes the same way: proportional for crispness, derivative for calm, integral for precision, each added in turn and judged by what the response does.

## 3. Mathematical Foundations
A reliable, behaviour-first workflow (a practical cousin of classic hand-tuning, kept entirely qualitative):

1. **Start with P only** ($K_i=K_d=0$). Raise $K_p$ from small. The response gets faster and the steady-state offset ($\ell/K_p$) shrinks. Keep raising until the response is brisk and **just begins to oscillate** (the marginal edge from 3.3). Note that gain, then **back off** to roughly half to two-thirds of it — brisk but clearly damped.
2. **Add derivative $K_d$** to kill the overshoot/ringing. Derivative removes energy from fast motion, so overshoot drops and the response calms. Because $K_d$ adds damping, it also **buys headroom**: you can now raise $K_p$ a bit more for speed without ringing. Increase $K_d$ until overshoot is acceptable; don't overdo it (too much $K_d$ amplifies sensor noise — Lesson 2.3).
3. **Add integral $K_i$** to erase the **steady-state offset** that P+D still leaves under load. Use the *smallest* $K_i$ that drives $e_{ss}\to 0$ in acceptable time. Too much $K_i$ adds lag and overshoot (and risks windup — use the anti-windup clamp from 2.2).
4. **Check the four metrics and the stability margin.** Confirm rise time, overshoot, settling time, and steady-state error all meet the spec, and that you're comfortably *inside* stable (not riding the marginal edge). Leave margin for payload changes, delay, and wear.

The whole loop is: **P for speed → D for calm → I for precision → verify and leave margin.** The engine lets you measure each step with `step_response_metrics` and guard the edge with `classify_stability`. There is no Laplace, no pole placement — just the behaviours of Unit 3, applied in order.

## 4. Visual Explanation
`[Visual: a four-panel tuning progression on the same step — (1) P-only: brisk but offset and some overshoot; (2) +D: overshoot damped; (3) +I: offset erased, lands on target; (4) final: clean response with the four metrics annotated and a "stability margin" note — each panel captioned with the step taken]`

**Diagram Specification**

- **Objective:** show tuning as a sequence of single-knob improvements, each fixing one defect, ending at a balanced response.
- **Scene:** four small step-response panels sharing a target line. **Panel 1 (P only):** fast-ish rise, visible overshoot, settles short (offset) — caption "P: speed, but overshoot + offset". **Panel 2 (+D):** same rise, overshoot damped, still slightly short — caption "+D: damp the overshoot". **Panel 3 (+I):** reaches the target, offset gone, small overshoot — caption "+I: erase the offset". **Panel 4 (final):** clean response annotated with rise/overshoot/settling/$e_{ss}$ and a small "margin to instability" note — caption "verify + leave margin".
- **Labels:** the four captions, "target", and on panel 4 the four metric labels.
- **Form:** SVG, four real engine responses showing the progression. P rose `#e11d48`, +D amber `#d97706`, +I sky `#0ea5e9`, final emerald `#10b981`.

## 5. Engineering Example
This workflow is what practitioners actually do, and what auto-tuners approximate. A field technician commissioning a new robot joint brings up $K_p$ until the joint "buzzes" slightly when nudged, backs off, adds $K_d$ until the buzz is gone and the joint feels crisp, then adds a little $K_i$ so it parks exactly on the commanded angle under its own weight. Commercial servo drives ship "auto-tune" buttons that run a fast version of this — excite the joint, watch the response, set gains to a target overshoot/bandwidth. Process plants use the same P→D→I logic by hand. Crucially, good technicians *leave margin*: they don't tune to the ragged edge of oscillation, because the payload will change, the gearbox will wear, and a comms hiccup will add delay — all of which eat stability. A loop tuned to the edge in the lab oscillates on the floor.

## 6. Worked Example
Tune a joint ($0\to1$ rad, load $\ell=2$) from scratch:

- **Step 1 — P:** raise $K_p$; at $K_p\approx 60$ on this joint it gets twitchy/oscillatory. Back off to $K_p=30$ — brisk, ~10% overshoot, but settles ~0.07 rad short (the $\ell/K_p$ offset).
- **Step 2 — +D:** add $K_d=10$ → overshoot drops, response calms; the added damping lets $K_p=30$ stay without ringing.
- **Step 3 — +I:** add $K_i=20$ → the joint now reaches 1.0 exactly; offset gone, overshoot still ~10%, settles in a few seconds.
- **Verify:** rise ~0.5 s, overshoot ~10%, settling ~3.5 s, $e_{ss}\approx 0$, classification "stable" with comfortable margin. Good enough for general use; tighten $K_d$ or trim $K_i$ if the spec is stricter.

Compare the lazy alternatives: cranking $K_p$ alone to kill the offset → oscillation; adding huge $K_i$ for speed → overshoot and windup. The ordered recipe avoids both. The notebook runs this exact progression and asserts each step improves the intended metric.

## 7. Interactive Demonstration
*(Conceptual — runnable in the companion notebook; the L07 PID Playground lets you tune by hand.)*

**Tune it yourself.** In the notebook you:

1. Start P-only, raise $K_p$ to the oscillation edge, then back off — watch offset shrink and overshoot appear.
2. Add $K_d$ and watch overshoot fall (and confirm you can nudge $K_p$ back up).
3. Add $K_i$ and watch the steady-state offset go to zero; verify the four metrics and the stability classification.

## 8. Coding Exercise
*(Snippet / notebook task — uses `track_reference`, `step_response_metrics`, `classify_stability`.)*

In the companion notebook:

1. P-only: find a $K_p$ that is brisk, then assert a smaller $K_p$ is sluggish and a much larger one is non-stable (`classify_stability`).
2. Add $K_d$ to a chosen $K_p$ and assert overshoot **decreases** versus P-only.
3. Add $K_i$ and assert steady-state error goes to ≈ 0 while the response stays "stable" — then assert the final response meets a small spec (overshoot < 15%, $e_{ss}\approx0$).

## 9. Knowledge Check
1. State the P→D→I tuning workflow in order, and say what each step fixes.
2. Why add derivative before integral?
3. How does adding $K_d$ let you use more $K_p$?
4. Why should you not tune to the very edge of oscillation?

## 10. Challenge Problem
You tune a joint perfectly on the bench, then the robot picks up a heavy payload and the same gains now overshoot badly and oscillate. Explain which metric/behaviour changed and why (hint: the effective load and inertia changed). Propose how the workflow would re-tune for the loaded case, and explain why "leaving margin" during the original tuning would have reduced the problem. Then argue when a single fixed gain set is acceptable versus when you'd want gains that adapt to the payload — without invoking any formal control theory. *(Robustness is the reason we stop at "good," not "maximal.")*

## 11. Common Mistakes
- **Tuning all three gains at once.** Change one knob at a time, in the P→D→I order, judging one metric per step.
- **Tuning to the oscillation edge.** Leave margin for payload, wear, and delay; the floor is harsher than the bench.
- **Using integral to go faster.** Integral is for offset, not speed; too much adds lag, overshoot, and windup.
- **Over-using derivative.** It damps, but too much amplifies sensor noise into a jittery command.

## 12. Key Takeaways
- Tuning is a **repeatable, behaviour-driven recipe**, not magic or heavy theory.
- **P for speed → D for calm → I for precision → verify and leave margin.** One knob at a time, judged by the four metrics.
- Derivative damps overshoot *and* buys headroom for more proportional; integral erases the offset but adds lag if overused.
- Stop at **good with margin**, not maximal — the real world adds load, wear, and delay. Next: point the tuned loop at a moving reference and meet feedforward.

---

### AI Learning Companion

Copy any prompt below into your AI tutor.

- **Tutor (re-explain):** "Re-explain the P→D→I tuning workflow using the 'dialling in game-controller sensitivity' analogy: P for crispness up to the twitchy edge then back off, D for damping (which buys more P), I for trimming the offset. Keep it behavioural — no pole placement — then walk me through tuning a described joint step by step."
- **Practice (generate exercises):** "Give me a joint's current gains and its response metrics and ask me what single tuning change to make next and why. Withhold the answer until I respond, then critique my choice."
- **Explore (connect to the real world):** "Explain how commercial servo auto-tune buttons approximate this workflow, and why technicians deliberately leave stability margin instead of tuning to the edge of oscillation."

### Global Learning Support

Per-language explanation prompts — use whichever you think best in.

- **English (authoritative):** "Explain a practical P→D→I controller tuning workflow for a robot joint — raise Kp to the oscillation edge and back off, add Kd to damp overshoot (buying more Kp headroom), add Ki to erase the steady-state offset, then verify the four metrics and leave stability margin — at a robotics-course level (no pole placement or frequency-domain methods)."
- **Español:** "Explica un flujo práctico de ajuste P→D→I para una articulación de robot — subir Kp hasta el borde de oscilación y retroceder, añadir Kd para amortiguar el sobrepaso (ganando margen para más Kp), añadir Ki para eliminar el error en régimen permanente, y verificar las cuatro métricas dejando margen de estabilidad — a nivel de curso de robótica (sin ubicación de polos ni métodos en frecuencia)."
- **中文（简体）：** "为机器人关节解释一个实用的 P→D→I 调参流程——把 Kp 提高到振荡边缘再回退，加入 Kd 来抑制超调（从而为更大的 Kp 留出余量），加入 Ki 消除稳态偏差，然后核对四个指标并留出稳定裕度——机器人课程水平（不涉及极点配置或频域方法）。"
- **Türkçe:** "Bir robot eklemi için pratik bir P→D→I ayar akışını açıkla — Kp'yi salınım eşiğine kadar yükselt ve geri çek, aşımı sönümlemek için Kd ekle (daha fazla Kp için pay kazandırır), kalıcı-durum hatasını silmek için Ki ekle, sonra dört ölçütü doğrula ve kararlılık payı bırak — robotik dersi düzeyinde (kutup yerleştirme veya frekans yöntemleri yok)."

---

*Next lesson: 4.1 — From One Joint to Many: Tracking a Trajectory with Feedback.*
