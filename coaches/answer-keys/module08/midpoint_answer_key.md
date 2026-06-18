---
module: 8
type: midpoint_assessment_answer_key
title: "Module 8 Midpoint Assessment — Coaches' Answer Key"
audience: coaches
---

# Midpoint Assessment — Coaches' Key (Units 1–4)

Grading philosophy: reward the **behaviour / cause-and-effect** explanation first; formulas
support it. Give partial credit for correct intuition with minor algebra slips. The recurring
theme to listen for: *open-loop drifts because it never measures; feedback corrects the error
it senses; PID = present/past/future of the error; stability is a balance threatened by gain,
lost damping, and delay; feedforward anticipates the known plan while feedback rejects the
unknown — and only the two together track a real arm.* No formal control theory should appear;
if a student reaches for Laplace/Bode, note it is out of scope and redirect to behaviour.

## Section A
**A1.** Open-loop runs the planned command without ever measuring the result, so any load,
friction, or model error accumulates uncorrected and the joint drifts off the reference.
Closed-loop **measures** the actual position, forms the error $e=q_d-q$, and **corrects** it,
so it holds the reference despite those effects. *(Unit 1.1.)*
**A2.** Tracking error $e = q_d - q$ (reference minus measured). The four parts: **reference**
(the target, from M7), **plant** (the joint being controlled), **controller** (computes the
command), **feedback** (the measured output fed back). The connecting signal is the
**measurement of the plant's output** ($q$, the feedback signal). *(Unit 1.2, 1.4.)*
**A3.** **Sense → compare → correct → actuate** (measure $q$; compare to $q_d$ to form $e$;
compute a correction; apply it to the plant). Open-loop omits the **sense/compare** step —
it never measures, so it cannot correct. *(Unit 1.3.)*

## Section B
**B1.** $u = K_p e + K_i \!\int\! e\,dt + K_d \dot e$. **Proportional** responds to the
*present* error (how wrong now); **integral** to the *past* (accumulated error, erases
offset); **derivative** to the *future* (rate of change, anticipates/damps). *(Unit 2.4.)*
**B2.** Offset $e_{ss} = \ell/K_p$. It is structural because at rest the command must exactly
hold the load ($u_{ss}=\ell$), and since $u=K_p e$, a nonzero error is *required* to generate
that command — at zero error the push would be zero and the load would win. The **integral**
term erases it (it keeps accumulating until the error is gone). *(Unit 2.1, 2.2.)*
**B3.** $e_{ss} = 2.0/40 = 0.05$ rad. Risk of raising $K_p$: overshoot/oscillation
(approaching the stability edge), plus noise amplification and saturation — and it never
reaches zero. Derivative's two jobs: **helpful** — damps overshoot/ringing (and buys headroom
for more $K_p$); **watch out** — it amplifies sensor noise if set too high. *(Unit 2.1, 2.3.)*

## Section C
**C1.** **Rise time** — how fast it climbs (speed). **Overshoot** — how far it sails past the
target (aggressiveness). **Settling time** — when it stops ringing (enters/stays in a small
band). **Steady-state error** — the residual offset once settled (precision). Central trade:
**speed vs overshoot** — faster rise tends to mean more overshoot (and longer settling).
*(Unit 3.2.)*
**C2.** **Stable**: envelope decays, response settles. **Marginal**: envelope constant,
sustained ringing. **Unstable**: envelope grows, response diverges. Three destabilisers:
**too much gain, too little damping, too much delay**. Latency is as dangerous as excess gain
because stale measurements make the correction mistimed — applied for a past state — so it can
push in the wrong direction and add energy, like pushing a swing a beat late. *(Unit 3.3.)*
**C3.** **P**: raise $K_p$ to the brisk/just-oscillating edge, then back off (sets speed,
shrinks offset). **D**: add derivative to damp overshoot (and gain $K_p$ headroom). **I**: add
the smallest integral that erases the steady-state offset. Stop at good-with-margin because
payload changes, wear, and added delay eat stability margin — a loop tuned to the edge on the
bench oscillates on the floor. *(Unit 3.4.)*

## Section D
**D1.** Feedback only acts on an error *after* it forms, so while the reference keeps moving it
is always a step behind — a following error that grows with reference speed. Raising gains
reduces it only slightly and spends stability margin / amplifies noise (and never reaches
zero). The ignored signals are the planned velocity $\dot q_d$ and acceleration $\ddot q_d$.
*(Unit 4.1.)*
**D2.** $u_{\text{ff}} = m\,\ddot q_d + b\,\dot q_d + \ell$. The $m\ddot q_d$ term uses
$\ddot q_d$ (supplies the force for the planned acceleration — inertia); the $b\dot q_d$ term
uses $\dot q_d$ (overcomes damping at the planned speed); $\ell$ holds the known load.
Feedforward tracks with almost no lag because it computes the command from the *plan* in
advance — it never waits for an error to form, unlike feedback. *(Unit 4.2.)*
**D3.** A disturbance enters the **plant** (it perturbs the joint's motion), not the
**reference**. Feedforward is computed from the reference and model only, so it never sees the
disturbance and cannot respond — it issues the same planned command and the error persists.
Feedback is computed from the measured error, which the disturbance changes, so it corrects it
without needing to know the disturbance exists. Complete tracker:
$u = \underbrace{m\ddot q_d + b\dot q_d + \ell}_{\text{feedforward: known plan}} +
\underbrace{\text{PID}(q_d - q)}_{\text{feedback: unknown residual + disturbance}}$, one per
joint. *(Unit 4.4.)*

## Section E
**E1.** **Feedforward** is responsible for the known, planned motion — it supplies most of the
command in advance for lag-free performance. **Feedback** is responsible for the unknown — the
model mismatch and disturbances — giving robustness. Neither alone suffices: feedforward-only
is fragile to disturbance/model error; feedback-only lags moving references. *(Unit 4.3, 4.4.)*
**E2.** Per joint: $u = m\ddot q_d + b\dot q_d + \ell + \text{PID}(q_d - q)$. The
**feedforward** part (using M7's $\dot q_d,\ \ddot q_d$) gives the speed/accuracy on the fast
trajectory; the **feedback** PID gives robustness — it rejects the bumps and the
approximate-load mismatch. During tuning, keep the feedback gains modest and leave stability
margin (don't tune to the oscillation edge); check overshoot/settling and that the loop stays
"stable" with comfortable margin given the uncertain load. *(Unit 3.4, 4.3, 4.4.)*
Reward students who note the feedback effort should be *small* if feedforward is doing its job.
**E3.** They're different layers. **Module 7** produces the **reference trajectory** —
$(q_d,\ \dot q_d,\ \ddot q_d)$ over time, an *open-loop plan* of where/how to move, with no
measurement. **Module 8** produces the **controller** that *makes the arm actually follow*
that reference on a real, imperfect plant — it measures, anticipates with feedforward, and
corrects with feedback. The deliverable handed to Module 9 is
`tracking_controller(reference, measured_state) → actuator_command`. M7 defines the motion;
M8 executes it closed-loop. *(Unit 1.4, 4.4; M7/M8 boundary.)*

---

*Listen for the through-line: measure → correct (feedback), present/past/future (PID),
balance threatened by gain/damping/delay (stability), anticipate the known + correct the
unknown (feedforward + feedback). Algebra slips are minor if the behaviour is right.*
