---
module: 8
unit: 6
lesson: 3
type: answer_key
title: "Answer Key — Latency and Control Rate: How Communication Destabilises the Loop"
audience: coaches
---

# Answer Key 6.3 — Latency and Control Rate: How Communication Destabilises the Loop

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** message latency and a finite control rate

**Q2 — B.** the correction lags the true state, so it can reinforce the swing instead of damping it

**Q3 — B.** the controller acts on stale information and holds its command between updates

**Q4 — B.** marches the loop from stable through oscillation to unstable

**Q5 — B.** bound the loop delay — faster/dedicated communication, a higher and more predictable control rate (real-time, Unit 7)

---

**Q6 — model answer.** In Unit 3 we inserted a delay by hand and showed that, at fixed gains, enough of it turns corrective action into the thing that drives the oscillation, marching the loop stable → marginal → unstable. Here the delay isn't artificial — it's the unavoidable cost of real communication (message latency) plus a finite control rate (acting on stale information, holding commands between updates). The mechanism is identical: the correction is based on old information and arrives late, so it lags the true state and can reinforce rather than damp the swing. Unit 6 simply supplies the physical source of the delay Unit 3 treated abstractly.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** Two distinct effects raise the loop delay. The added message jitter/latency means each measurement reaches the controller later and more variably, so corrections lag the true state. The lowered control rate means the controller updates less often, acting on staler information and holding its last command longer between updates, which adds roughly half an update period of delay and spaces corrections further apart. Both push the effective loop delay up; at the unchanged gains, their combined delay crosses the stability boundary. The fixes target each: a faster/dedicated bus for latency, and a higher, more predictable update rate (an isolated real-time control task) for the control rate.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** Because once you accept that communication delay and a finite control rate can topple an otherwise well-tuned loop, the requirement isn't merely 'be fast on average' — it's 'keep the loop delay small and bounded'. A loop that is usually fast but occasionally late (jitter) can still go unstable on the late cycles. Real-time execution provides exactly that guarantee: a high, predictable control rate with bounded worst-case timing for the inner loop. So real-time stops being an optimisation and becomes a correctness requirement for the inner control loop, which is what Unit 7 delivers.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Blaming the gains for hardware-only oscillation — the culprit is often loop delay.
- Ignoring the control rate — a fast bus can't save a loop whose controller updates too slowly.
- Reaching for formal stability math — stability stays qualitative (settle/oscillate/diverge).
