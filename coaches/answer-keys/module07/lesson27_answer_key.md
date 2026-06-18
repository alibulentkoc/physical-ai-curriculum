---
module: 7
unit: 7
lesson: 3
type: answer_key
title: "Answer Key — Tracking Prerequisites: What the Reference Must Provide"
audience: coaches
---

# Answer Key 7.3 — Tracking Prerequisites: What the Reference Must Provide

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** The reference must provide q_d, q̇_d, q̈_d (feed-forward) at every instant.

**Q2 — B.** Feed-forward lets the tracker keep up / anticipate, not just react to error.

**Q3 — B.** Module 7 produces the reference; Module 8 tracks it.

**Q4 — B.** Missing derivatives / infeasibility / discontinuity make it un-trackable.

**Q5 — C.** The reference contains no tracking error, torque, or motor command (Module 8).

---

**Q6 — model answer.** The composer (Module 7) writes a score that's playable: the notes (desired position), how they move (velocity), and phrasing cues to anticipate what's coming (acceleration) — complete and feasible. The musician (Module 8) performs it, reading the score and producing the sound, correcting as they go. The composer never performs; if the score is unplayable (impossibly fast, gaps), no musician can play it, and that's the composer's fault. So Module 7 provides the full feed-forward reference (q_d, q̇_d, q̈_d), continuous and feasible; Module 8 does the actual following.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** Feed-forward is the desired velocity and acceleration supplied alongside the desired position. With it, the tracker already knows how fast it should be moving and how that speed should change, so it can command roughly the right motion in advance and only correct the small residual error. Without it — given position alone — the tracker is always reacting to accumulated error and lags the reference, especially in fast motions. Providing the full triple makes the tracker's job well-posed and keeps the lag and error small; that work shouldn't be pushed onto Module 8.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** Module 7 ends at producing and validating the open-loop reference: q_d(t), q̇_d(t), q̈_d(t), continuous, feasible, sampled. Module 8 begins at consuming that reference and making the robot actually follow it — computing tracking error, applying control gains, accounting for dynamics, and commanding the actuators. The boundary is the reference signal itself: it's the input to Module 8's controller, not a controller. A clean boundary matters because it lets each layer be built and tested independently, and lets the same validated reference run in simulation and on hardware.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Providing position only (no feed-forward → the tracker lags).
- Handing off an infeasible or discontinuous reference.
- Doing tracking (error/gains/torque/motor commands) in Module 7 — that's Module 8.
