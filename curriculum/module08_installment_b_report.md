---
title: "Module 8 — Installment B (Units 3–4 + midpoint) — Milestone Report"
module: 08
installment: B
units: [3, 4]
lessons: "L09–L16"
decision: D-068
status: delivered — paused for architect review
date: 2026-06
---

# Module 8 — Installment B Milestone Report

## EXECUTIVE SUMMARY

- **Module:** 8 — Feedback Control and Real-Time Execution (ROS 2)
- **Status:** Installment B (Units 3–4, lessons L09–L16) **plus the Module 8 midpoint assessment (Units 1–4)** delivered and verified; **paused at the milestone for architect review** (no auto-proceed to Installment C).
- **What was built:** 8 lessons (full 12-section template + AI Learning Companion + Global Learning Support in 4 languages), 8 SVG diagrams, 8 runnable notebooks (all "All checks passed." under Restart & Run All), 8 interactive quizzes (5 MC + 3 short), 8 coaches' answer keys, and 1 midpoint assessment + coaches' key. The shared engine was extended additively (latency, full feedforward, whole-arm tracking). Generator and nav extended for Units 3–4; `mkdocs build --strict` passes at **245 lesson pages** (237 → 245). **No new demo this installment** (per the plan; next demos are L17/L21 in Installment C).
- **Key educational achievement:** the **feedback-only vs feedforward+feedback comparison on an identical trajectory** — the required Unit 4 payoff. On the same fast 1.5 s move, feedback-only tracks at RMS ≈ 0.075 rad while feedforward+feedback tracks at RMS ≈ 0.017 rad — about **4.5× tighter, with *smaller* feedback effort** — and the disturbance test then proves feedback is non-negotiable (feedforward-only leaves a ≈1.4 rad error after a kick; feedforward+feedback recovers to ≈0.003 rad). Unit 4 visibly consumes Module 7's q̇_d and q̈_d in the feedforward command `m·q̈_d + b·q̇_d + ℓ`, making Modules 7 and 8 feel like one system.
- **Architect review focus:** (1) the **experience-first** delivery of Unit 3 — the correction spectrum (too weak → good → too strong → oscillation → runaway) is taught as recognised *behaviour* before any terminology, with stability names and the tuning workflow following; (2) Unit 4's **anticipation-first** framing of feedforward and the required, measurable feedback-only-vs-ff+fb comparison; (3) confirmation that the §9 fences held — no formal manipulator dynamics, no control-theory formalism (Laplace/Bode/Nyquist named only as out-of-scope), plant = integrator + disturbance + saturation + latency.
- **Next:** Installment C — Units 5 (Actuator Control) and 6 (Communication), with the flagship demos at L17 and L21, on approval.

---

## 1. Decision-id reconciliation

No collision. Module 8 installments run D-066 (launch), D-067 (Installment A), **D-068 (Installment B)**, following Module 7's last id (D-065). Recorded in `ARCHITECT_DECISIONS.md`. No action required.

## 2. What was delivered

**Unit 3 — Stability, Response, and Tuning** (experience-first: behaviour, then terminology)
- **L09 (3.1)** When Correction Goes Wrong — the correction spectrum (too weak → good → too strong → oscillation → runaway) recognised by eye *before* any vocabulary; latency causes runaway; good control is balance, not maximum.
- **L10 (3.2)** The Shape of a Response — naming what was seen: rise time, overshoot, settling time, steady-state error; the speed-vs-overshoot trade.
- **L11 (3.3)** Stable, Marginal, Unstable — classification by envelope; the three destabilisers (too much gain, too little damping, too much delay); why **latency is as dangerous as excess gain**.
- **L12 (3.4)** Tuning a Controller — a practical **P → D → I** workflow: raise Kp to the oscillation edge and back off, add D to damp (and buy Kp headroom), add I to erase the offset, verify the four metrics, leave margin.

**Unit 4 — Tracking the Whole Arm: Feedforward + Feedback** (the payoff)
- **L13 (4.1)** From One Joint to Many — per-joint independent PID tracking a Module-7 trajectory; the speed-dependent **following error** of feedback-only tracking (coupling treated as disturbance, no formal dynamics).
- **L14 (4.2)** Feedback Reacts, Feedforward Anticipates — the conceptual core; the inverse-model feedforward `m·q̈_d + b·q̇_d + ℓ` presented as anticipation, consuming M7's q̇_d, q̈_d; near-lag-free with a good model.
- **L15 (4.3)** Feedforward + Feedback Together — the **required comparison** on the identical trajectory (feedback-only ≈ 0.075 vs ff+fb ≈ 0.017 RMS, ~4.5× tighter, smaller feedback effort); the combination beats feedforward-only too.
- **L16 (4.4)** Disturbances, Load, and the Complete Tracker — feedforward can't reject disturbances (they enter the plant, not the reference), feedback can; the complete joint tracker and the `tracking_controller(reference, measured_state) → actuator_command` interface = the Module 9 handoff; ties back to Unit 1's open-loop drift.

**Midpoint assessment (Units 1–4)** — Sections A–E (A: tracking/feedback loop; B: PID; C: stability/response/tuning; D: feedforward+feedback; E: integrative), with a coaches' answer key. Behaviour-first grading guidance; no formal control theory expected.

## 3. Engine

The shared `m8_engine.py` was extended **additively** (a superset of Installment A; backup at `engine/m8_engine_A_backup.py`), so all Installment-A notebooks remain valid:
- **`feedforward_full(qd_d, qdd_d, m, b, load_comp)`** = m·q̈_d + b·q̇_d + ℓ — the inverse-model feedforward that consumes **both** q̇_d and q̈_d (the Unit 4 anticipation command).
- **`track_reference(ref, plant, controller, T, ff=…, sensor_delay_steps=…)`** — single-joint trajectory tracking with selectable feed-forward ('none'/'accel'/'full') and a **sensor-latency** option for the Unit-3 delay demonstrations.
- **`JointTracker(gains, ff='full')`** — per-joint PID + feed-forward; the complete tracker (precursor to the Unit-8 capstone), with `multi_quintic` and `track_arm` for whole-arm tracking + overall RMS.

Verified behaviours (locked into lessons/notebooks): the gain sweep reproduces the correction spectrum (weak offset → good → overshoot → oscillation); latency at fixed gains marches a loop stable → unstable (peak |q| ≈ 886 at 60-step delay); feedforward+feedback ≈ 4.5× tighter than feedback-only under realistic mismatch; feedforward-only cannot reject a disturbance while feedforward+feedback does. Running example: planar 2-link arm L₁=0.4, L₂=0.3 against the simulated plant.

## 4. Verification

- **Notebooks:** all 8 (L09–L16) execute clean end-to-end via nbclient Restart-and-Run-All (0 failures); each prints "All checks passed." Checks assert the actual numbers (the spectrum ordering, the latency-induced instability, the ~4.5× ff+fb improvement, the disturbance rejection contrast). One check (L14) was tightened during the build to assert anticipation directly — a large plan-driven feedforward command issued while max|error| stays < 0.06 — rather than a noisier correlation probe.
- **SVGs:** all 8 XML-valid (`role="img"` + `aria-label` + `viewBox`, design-system colours), with real engine curves. L9 was authored as a five-panel behaviour spectrum (clearer than an overlay) and L15's RMS-bar labels were de-collided; both rasterised and confirmed on-message.
- **Quizzes:** all 8 are self-contained interactive HTML (5 MC + 3 short), MathJax-enabled, no `localStorage`/`sessionStorage`.
- **Answer keys + midpoint:** 8 lesson keys in coaches' format; the midpoint assessment (Sections A–E) and its coaches' key both placed.
- **Site:** generator unit titles added for ("08","03") and ("08","04"); nav extended with Units 3–4; the run injected SVG/notebook/quiz into every page; validator clean (no `[Visual:]` leak; Diagram Specification stripped; SVGs inlined). `mkdocs build --strict` **passes (exit 0)** at 245 lesson pages.
- **DoD matrix:** all 8 lessons meet every gate (12 sections · SVG · passing notebook · 5 MC + 3 short quiz · answer key · companion blocks · published site page).

## 5. Boundaries held (§9)

- **Dynamics:** appears only as disturbance, load, friction, saturation, model mismatch, and **latency**. Inter-joint coupling is treated as a disturbance the per-joint feedback rejects — no mass matrix, Coriolis, computed-torque, or Euler-Lagrange anywhere.
- **Formalism:** stability and response are qualitative (settle/oscillate/diverge, the four metrics, the P→D→I workflow). Laplace, transfer functions, root locus, Bode, Nyquist, and poles appear **only** as named out-of-scope topics (boundary-scanned; every occurrence is exclusionary framing such as "no transfer functions," "a later course").
- **Plant:** integrator + disturbance + saturation + latency.
- **M7 continuity:** Unit 4 visibly consumes q̇_d and q̈_d in the feedforward command — the spine of the unit and the Modules 7→8 hinge.

## 6. Repository changes

- `modules/module08/lessons/lesson09..16_*.md` (8)
- `modules/module08/notebooks/lesson09..16_*.ipynb` (8)
- `modules/module08/quizzes/lesson09..16_quiz.html` (8)
- `assets/diagrams/m08-l9..l16-*.svg` (8)
- `coaches/answer-keys/module08/lesson09..16_answer_key.md` (8)
- `assessments/module08_midpoint_assessment.md` + `coaches/answer-keys/module08/midpoint_answer_key.md`
- `engine/m8_engine.py` extended (Installment-B utilities; backup retained)
- `tools/generate_site_pages.py` — unit titles for ("08","03") and ("08","04")
- `mkdocs.yml` — Units 3–4 nav added
- `curriculum/ARCHITECT_DECISIONS.md` — **D-068** appended
- `curriculum/master_progress.md`, `curriculum/PROJECT_STATE.md` — updated to Installments A–B; totals → 245 lessons / 246 SVGs / 39 demos / 245 pages / 8 midpoints
- `site_src/module08/lesson09..16.md` + `site/` — generated; strict build passing
- `curriculum/module08_installment_b_report.md` — this report

## 7. Milestone

**Installment B is complete and paused for architect review.** The first half of Module 8 is now whole: open-loop-vs-closed-loop → PID → stability/response/tuning → feedforward+feedback, with a midpoint assessment over Units 1–4. On approval, Installment C (Units 5–6: Actuator Control and Communication) follows, beginning with L17 (5.1) and carrying the flagship demos at L17 and L21.
