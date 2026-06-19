---
module: 8
unit: 7
lesson: 7.3
type: answer_key
title: "Answer Key 7.3 — Jitter, Overruns, and Missed Deadlines"
audience: coaches
---

# Answer Key 7.3 — Jitter, Overruns, and Missed Deadlines

*Coaches' key. Multiple-choice answers with the correct option; model answers for the short-response items, with grading guidance; and common misconceptions to watch for.*

**Q1 — A.** The period varying cycle to cycle

*Why:* Jitter is variation in the actual interval between updates.

**Q2 — A.** Skip the update and hold the previous command

*Why:* The scheduled update is skipped, so a stale command is held another period.

**Q3 — B.** Adding loop delay

*Why:* All three increase the effective sense-to-act delay — the Unit-6 destabiliser.

**Q4 — C.** Unstable

*Why:* Same gains and plant — only the timing changed, and it crossed into instability.

**Q5 — B.** Predictable (deterministic, low-jitter)

*Why:* Predictability, not raw speed, is what restores the bounded delay the loop needs.

**Q6 — model answer.** Jitter: the period varies cycle to cycle (the next update lands late by a varying amount). Overrun: the cycle's work exceeds the period, violating the budget. Missed deadline: the consequence — the update is skipped and the previous command is held another period.

**Q7 — model answer.** Each increases the effective loop delay between sensing and acting (a late or skipped update holds a stale command). Unit 6 showed that at fixed gains, increasing delay marches the loop stable → marginal → unstable, so these hazards inherit exactly that boundary.

**Q8 — model answer.** A faster-on-average CPU can still jitter and overrun (e.g., under OS preemption or contention), so its worst-case timing may remain unbounded. The loop needs predictable, bounded timing; the fix is a real-time target that protects the loop's timing, not just more average speed.

*Grading: award full credit for a short answer that captures the key idea in the model answer, even if briefer or differently worded; partial credit if the core mechanism is named but not fully explained.*

### Common misconceptions to watch for

- Treating jitter as harmless noise; jitter is varying loop delay and enough of it destabilises.
- Ignoring missed deadlines — a skipped update holds a stale command, which is added delay.
- Trying to fix timing-induced instability with more gain or a faster average instead of predictable timing.
