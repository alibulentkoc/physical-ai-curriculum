---
module: 8
unit: 7
lesson: 7.1
type: answer_key
title: "Answer Key 7.1 — What Real-Time Means: Deadlines, Determinism, and Worst-Case Timing"
audience: coaches
---

# Answer Key 7.1 — What Real-Time Means: Deadlines, Determinism, and Worst-Case Timing

*Coaches' key. Multiple-choice answers with the correct option; model answers for the short-response items, with grading guidance; and common misconceptions to watch for.*

**Q1 — B.** Correct AND on time — every result within its deadline

*Why:* Real-time is about timing correctness: a result is only useful if it also arrives on time.

**Q2 — C.** The worst-case cycle time

*Why:* A single late cycle can destabilise the loop, so the worst case is the figure of merit.

**Q3 — B.** Unstable, because the worst case was large

*Why:* Despite a small average interval, the large worst-case interval destabilised it.

**Q4 — B.** The inner joint control loop

*Why:* A missed deadline in the inner loop can destabilise the robot — a hard requirement.

**Q5 — B.** A late correction is applied at the wrong moment, injecting loop delay

*Why:* Timing is part of correctness; a late correction acts like added delay (Unit 6).

**Q6 — model answer.** Fast describes average speed; real-time describes meeting deadlines every cycle. A loop can be fast on average yet miss its worst-case deadline, which is what actually decides correctness and stability. Real-time requires a bounded worst case, not just a good average.

**Q7 — model answer.** Because a single very late cycle holds a stale command, injecting the loop delay that Unit 6 showed destabilises a fixed-gain loop. The average being small does not prevent that one bad cycle, so stability depends on bounding the worst case.

**Q8 — model answer.** Hard real-time: a missed deadline is a failure (the inner control loop, a flight controller). Soft real-time: an occasional miss only degrades quality (video playback, outer planning layers). The inner loop is hard; the slow outer layers are soft.

*Grading: award full credit for a short answer that captures the key idea in the model answer, even if briefer or differently worded; partial credit if the core mechanism is named but not fully explained.*

### Common misconceptions to watch for

- Equating real-time with raw speed — it is on-time-every-time, with a bounded worst case, not a fast average.
- Benchmarking the average cycle time; the loop's correctness depends on the worst case.
- Treating one late cycle as harmless — a single stale-command cycle can start the divergence (Unit 6).
