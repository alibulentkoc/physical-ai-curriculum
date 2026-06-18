---
module: 07
unit: 08
lesson: 8.3
title: "Validate and Hand Off: The Reference Trajectory Layer"
core_idea: "The workflow's second half certifies and packages the trajectory. VALIDATE runs the complete suite on the timed trajectory; on pass, it is packaged as the reference trajectory layer — a validated, time-indexed reference(t) → (q_d, q̇_d, q̈_d) with metadata. This layer is Module 7's final artifact and the explicit input Module 8 consumes."
estimated_time: "45 min"
difficulty: "Advanced"
prerequisites:
  - "M7 L7.2 — Validating a trajectory"
  - "M7 L7.3 — Tracking prerequisites and the M7/M8 boundary"
learning_objectives:
  - "Execute the VALIDATE stage and gate the handoff on its verdict."
  - "Package a validated trajectory as the reference trajectory layer with its interface and metadata."
  - "Identify this layer as Module 7's final artifact, consumed by Module 8 (analogous to the M6 velocity layer)."
---

# Lesson 8.3 — Validate and Hand Off: The Reference Trajectory Layer

> Lesson 8.2 produced a timed trajectory. The workflow's second half **certifies** it and **packages** it for handoff. VALIDATE runs the complete suite; on pass, the trajectory becomes the **reference trajectory layer** — the validated, time-indexed reference Module 8 will consume. This is Module 7's final deliverable, the bookend to Module 6's velocity layer. We lead with the gate, then the package.

---

## 1. Why This Matters
A timed trajectory is *almost* a deliverable — but not until it's been **certified** and **packaged**. VALIDATE (Unit 7) is the gate: run the complete suite, and only a trajectory that passes every check may proceed. Then the validated trajectory must be wrapped in a clean, well-specified interface so that the next system — Module 8's tracker — can consume it without knowing how it was built. That package is the **reference trajectory layer**: a validated, time-indexed `reference(t)` that returns the desired position, velocity, and acceleration, plus metadata (duration, rate, the validated flag, quality metrics).

This layer is **Module 7's final artifact** — the single, complete object the whole module exists to produce. It is the deliberate bookend to **Module 6's velocity layer** (which Module 7 has imported and used throughout as the open-loop executor): just as Module 6 ended by handing Module 7 a clean `velocity_layer` interface, Module 7 ends by handing Module 8 a clean `reference` interface. Defining this handoff crisply — what's in it, what its contract is, and where Module 7's responsibility ends — is what makes the modules compose into a working system. For the harvester, the layer is the finished, certified reach-and-grasp motion, ready to run.

## 2. Physical Intuition
Think of shipping a finished product. The factory doesn't just make the part — it **inspects** it (does it pass QC?) and then **packages** it with a label: part number, spec sheet, a "passed inspection" stamp. The customer receives a sealed, certified package with a clear interface (how to use it), and doesn't need to know the manufacturing details. An uninspected or unlabeled part wouldn't ship.

The reference trajectory layer is the certified, packaged product of Module 7. VALIDATE is the inspection — the trajectory must pass every check to be stamped "valid." Packaging wraps it with a clean interface (call `reference(t)`, get the desired motion) and a spec sheet (duration, control rate, validated flag, quality metrics). Module 8 — the customer — receives this sealed package and consumes it through the interface, without needing to know it came from an RRT plan smoothed and timed a particular way. A trajectory that fails validation never ships; it goes back for rework (re-time or re-plan).

## 3. Mathematical Foundations
**VALIDATE (the gate).** Run the complete suite (7.2) on the timed trajectory $\mathbf q(t)$: endpoints match, rest-to-rest, continuity, within velocity and acceleration limits, collision-free along the whole arm, reachable. The verdict is $\text{valid} = \bigwedge(\text{checks})$. **Only if valid** does the handoff proceed; otherwise the trajectory is rejected with the failing check named, routing back to PARAMETERIZE (re-time) or PLAN (re-route), per the triage of Lesson 5.4.

**The reference trajectory layer (the package).** On pass, wrap the validated trajectory as an object exposing:

- **The reference interface:** $\texttt{reference}(t) \to (\mathbf q_d(t),\ \dot{\mathbf q}_d(t),\ \ddot{\mathbf q}_d(t),\ \text{info})$ — the feed-forward triple at any time, plus light info (e.g. phase $t/T$). This is precisely what the prerequisites (7.3) require a tracker to receive.
- **Metadata:** duration $T$, control **rate** $f$ (for discretization, 7.4), the **validated** flag, and the **quality metrics** (7.1).

This is the artifact analogous to Module 6's `velocity_layer`:

$$\underbrace{\text{Module 6}}_{\text{velocity\_layer}(q,\xi_d)\to\dot q}\ \longrightarrow\ \underbrace{\text{Module 7}}_{\text{reference}(t)\to(q_d,\dot q_d,\ddot q_d)}\ \longrightarrow\ \underbrace{\text{Module 8}}_{\text{tracker consumes the reference}}.$$

**The contract (and the boundary).** The layer's contract is: *a validated, feasible, continuous, time-indexed feed-forward reference.* What it explicitly does **not** contain — and what Module 8 owns — is any tracking error, control gain, torque, or motor command. The layer is the **input** to Module 8's controller, not a controller. "Hand off" means deliver this object (and, for open-loop playback within Module 7, step its $\dot{\mathbf q}_d$ through the imported Module 6 velocity layer); it never means closing a loop. The engine produces the layer with `reference_trajectory_layer(...)`, which runs PLAN+PARAMETERIZE (8.2), VALIDATE (7.2), and returns the dict with `reference`, `duration`, `rate`, `waypoints`, `metrics`, `validation`, and `validated`.

## 4. Visual Explanation
`[Visual: VALIDATE gate (checklist → valid/invalid) feeding the reference trajectory layer package — interface reference(t)→(q_d,q̇_d,q̈_d) + metadata — handed across the M7/M8 line, shown as the bookend to the M6 velocity layer]`

**Diagram Specification**

- **Objective:** show validation gating the packaging, and the layer as the M7→M8 handoff bookending M6.
- **Scene:** **Left:** a VALIDATE checklist with a "VALID ✓" stamp (and a dashed "INVALID → rework" branch back to PLAN/PARAMETERIZE). **Center:** a "reference trajectory layer" package box listing its interface `reference(t) → (q_d, q̇_d, q̈_d, info)` and metadata (duration, rate, validated, metrics). **Right:** a handoff arrow across the M7/M8 line into a greyed "Module 8 tracker". **Top band:** the chain "M6 velocity_layer → M7 reference layer → M8 tracker".
- **Labels:** "VALID gates handoff"; interface + metadata; "input to Module 8, not a controller"; the three-module chain.
- **Form:** SVG, gate → package → handoff. Valid emerald `#10b981`, package teal, M8 dashed/muted.

## 5. Engineering Example
This validate-then-package pattern is how motion systems deliver trajectories. A trajectory is validated against limits and collisions, then published as a standard reference object — a timestamped sequence of desired positions (and velocities/accelerations) — on the interface the controller subscribes to. The controller consumes that object through a fixed contract, decoupled from the planner/parameterizer that produced it. This is exactly why the same reference runs in simulation and on hardware, and why planning and control teams can work independently against the interface. For the harvester, Module 7 ships the validated reach-and-grasp reference as this layer; Module 8's controller subscribes to it and tracks it on the real arm. The layer is the contract between "deciding the motion" and "executing it."

## 6. Worked Example
Validate and package the greenhouse reach (canonical scenario; limits $\dot q_{\lim}=2$, $\ddot q_{\lim}=4$).

- **VALIDATE:** the timed trajectory from 8.2 passes the full suite — endpoints match, rest-to-rest, within velocity (peak ≤ 2) and acceleration (peak = 4, binding), continuous, collision-free, reachable → **VALID**.
- **PACKAGE:** wrap it as the reference layer. Query `reference(1.0)` → $(\mathbf q_d,\dot{\mathbf q}_d,\ddot{\mathbf q}_d,\text{info})$. Metadata: duration $\approx2.35$ s, rate (e.g. 100 Hz), `validated = True`, metrics (peak speed 1.52, peak accel 4.0, peak jerk, path length 0.70).
- **HANDOFF:** this layer is the deliverable. Within Module 7 it can be played open-loop (feed $\dot{\mathbf q}_d$ to the M6 velocity layer); for real tracking it is handed to Module 8.
- **Failure path:** break a segment's timing → VALIDATE fails → `validated = False`, no package shipped, routed back to re-time. The notebook builds the layer, asserts `validated`, queries the reference interface, prints the metadata, and shows the failure path rejecting the handoff.

## 7. Interactive Demonstration
*(Conceptual — runnable in the companion notebook; also the Validate/Execute stages of the Trajectory Studio.)*

**Certify, then package.** In the notebook you:

1. Run VALIDATE on the timed trajectory; on pass, build the reference layer.
2. Query the layer's `reference(t)` and read its metadata (duration, rate, validated, metrics) — the packaged handoff.
3. Break the trajectory so validation fails and confirm no valid layer is produced (the gate blocks the handoff).

## 8. Coding Exercise
*(Snippet / notebook task — uses `reference_trajectory_layer`, `validate_trajectory`.)*

In the companion notebook:

1. Build a layer and assert `validated` is True only when `validation['valid']` is True (the gate). 
2. Assert the layer exposes `reference(t)` returning $(\mathbf q_d,\dot{\mathbf q}_d,\ddot{\mathbf q}_d,\text{info})$ and the metadata (duration, rate, metrics) — the full package/contract.
3. Force a validation failure (defective timing or a colliding route) and assert the layer reports `validated` False and ships **no** valid reference — the handoff is gated.

## 9. Knowledge Check
1. What gates the handoff, and what happens on a failed validation?
2. What does the reference trajectory layer expose (interface + metadata)?
3. Why is this layer analogous to the Module 6 velocity layer?
4. What does the layer explicitly **not** contain, and which module owns that?

## 10. Challenge Problem
Specify the full contract of the reference trajectory layer as if writing it for the Module 8 team: list exactly what `reference(t)` returns, what metadata travels with it, what guarantees the layer makes (validated, feasible, continuous), and — crucially — what Module 8 must supply that the layer does *not* (the tracking law, error correction, motor commands, any dynamics). Then explain why a crisp contract here makes Module 8 simpler to build and test. *(The handoff is a contract; its clarity is the point of the capstone.)*

## 11. Common Mistakes
- **Shipping an unvalidated trajectory.** The handoff is gated on VALIDATE; never package a trajectory that failed a check.
- **Putting control logic in the layer.** The layer is the reference (input to the controller), not a controller; no error/gain/torque.
- **Omitting metadata.** Duration, rate, and the validated flag are part of the package the consumer needs.
- **Blurring the bookend.** M6 hands M7 the velocity layer; M7 hands M8 the reference layer — keep the interfaces clean.

## 12. Key Takeaways
- The workflow's second half is **VALIDATE** (the complete suite, gating the handoff) then **package** the validated trajectory as the **reference trajectory layer**.
- The layer exposes `reference(t) → (q_d, q̇_d, q̈_d, info)` plus metadata (duration, rate, validated, metrics) — exactly the tracking prerequisites (7.3).
- It is **Module 7's final artifact**, the bookend to **Module 6's velocity layer**, and the explicit **input Module 8 consumes**.
- The layer contains **no** tracking error, gain, torque, or motor command — that is **Module 8**. The handoff is a clean contract, not a controller.

---

### AI Learning Companion

Copy any prompt below into your AI tutor.

- **Tutor (re-explain):** "Re-explain Validate and Hand Off using the 'inspect, then package and label the product' analogy. Stress that VALIDATE gates the handoff and the reference trajectory layer is the certified package (interface + metadata). Then ask me what the layer does NOT contain."
- **Practice (generate exercises):** "Give me three timed trajectories (one defective). Ask me which pass validation and may be packaged, and what the resulting layer's interface/metadata would be. Withhold answers until I respond."
- **Explore (connect to the real world):** "Explain how motion systems publish a validated trajectory as a standard reference object on a controller interface, and why that decouples planning from control."

### Global Learning Support

Per-language explanation prompts — use whichever you think best in.

- **English (authoritative):** "Explain Validate and Hand Off for a robot motion: the validation gate, and packaging the validated trajectory as the reference trajectory layer (reference(t) → q_d, q̇_d, q̈_d + metadata) that Module 8 consumes — the bookend to the Module 6 velocity layer — at a robotics-course level (the layer is not a controller)."
- **Español:** "Explica Validar y Entregar para un movimiento robótico: la compuerta de validación y el empaquetado de la trayectoria validada como la capa de trayectoria de referencia (reference(t) → q_d, q̇_d, q̈_d + metadatos) que consume el Módulo 8 — el cierre que hace juego con la capa de velocidad del Módulo 6 — a nivel de curso de robótica (la capa no es un controlador)."
- **中文（简体）：** "用机器人课程的水平，解释机器人运动的'验证与交接'：验证门控，以及把已验证轨迹打包为参考轨迹层（reference(t) → q_d, q̇_d, q̈_d 加元数据）供模块8使用——与模块6速度层相呼应（该层不是控制器）。"
- **Türkçe:** "Bir robot hareketi için Doğrula ve Devret'i açıkla: doğrulama kapısı ve doğrulanmış yörüngeyi Modül 8'in tükettiği referans yörünge katmanı olarak paketleme (reference(t) → q_d, q̇_d, q̈_d + meta veri) — Modül 6 hız katmanının karşılığı — robotik dersi düzeyinde (katman bir denetleyici değildir)."

---

*Next lesson: 8.4 — Capstone Integration: The Greenhouse Harvest Cycle (the whole workflow end to end on a full task), and the Module 7 recap.*
