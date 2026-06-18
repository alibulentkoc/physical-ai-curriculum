---
module: 7
unit: 7
lesson: 4
type: answer_key
title: "Answer Key — Sampling and Representing the Reference: Discretization for Execution"
audience: coaches
---

# Answer Key 7.4 — Sampling and Representing the Reference: Discretization for Execution

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** A digital controller updates at a fixed rate, so the reference is discretized.

**Q2 — B.** Too coarse a rate misrepresents the motion (time-axis tunneling).

**Q3 — B.** The structure is the feed-forward series plus metadata (duration, rate, validated).

**Q4 — B.** Discretization only represents the reference; control is Module 8.

**Q5 — B.** The rate must be fine enough to capture the fastest variation.

---

**Q6 — model answer.** A film captures continuous motion as still frames; at enough frames per second it looks smooth, but too few frames give a jerky slideshow that misses what happened between them. A digital controller 'films' the reference, grabbing one frame (the desired position, velocity, acceleration) each control tick. A high enough rate makes the discrete sequence faithfully represent the smooth reference; too coarse a rate is a slideshow that can skip a velocity/acceleration peak — the time-axis version of collision tunneling. So the rule is to sample fine relative to how fast the motion changes.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** It contains the timestamped feed-forward series — for each tick, the time and the desired position, velocity, and acceleration — or equivalently a callable that returns those at any time. Alongside the signals it carries metadata: the total duration, the control rate it was sampled at, and the validated flag (and quality metrics). The metadata travels with it because the consumer (execution / Module 8) needs to know how long the motion is, what rate the samples correspond to, and that it passed validation before stepping through it.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** If the reference is stored as a fixed series sampled at one rate but the controller runs at a different rate, replaying the samples directly causes stair-stepping or requires interpolation. Keeping the reference as a callable q_d(t) lets the controller evaluate it at exactly its own tick times, at whatever rate it runs, producing a faithful sample wherever it asks. The continuous function is the source of truth; any discrete series is just one sampling of it, so the callable form removes any dependence on a particular build rate.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Sampling too coarsely (time-axis tunneling).
- Dropping the feed-forward (q̇_d, q̈_d) from the series; forgetting the metadata.
- Thinking discretization is control (it's representation only).
