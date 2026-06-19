---
module: 8
unit: 7
lesson: 7.4
type: answer_key
title: "Answer Key 7.4 — Running the Inner Loop on a Real-Time Target"
audience: coaches
---

# Answer Key 7.4 — Running the Inner Loop on a Real-Time Target

*Coaches' key. Multiple-choice answers with the correct option; model answers for the short-response items, with grading guidance; and common misconceptions to watch for.*

**Q1 — B.** Protected, deterministic, low-jitter

*Why:* A microcontroller / RT thread / dedicated hardware gives the loop protected, predictable timing.

**Q2 — B.** Latency-critical → real-time; latency-tolerant → best-effort

*Why:* The inner loop is latency-critical; planning/perception are latency-tolerant.

**Q3 — B.** Jittery and unstable

*Why:* It suffers jitter and missed deadlines (7.3) and can oscillate.

**Q4 — B.** Move it to a real-time target

*Why:* The problem is the target's timing, not the gains.

**Q5 — B.** Best-effort compute (loose timing is OK)

*Why:* They are latency-tolerant and update references at lower rates.

**Q6 — model answer.** A real-time target (microcontroller, high-priority RT thread, or dedicated motion-control hardware) protects the loop's timing so it is deterministic and low-jitter. The inner loop runs there because it is latency-critical — delay inside it destabilises (Unit 6) — so the designed rate must be the achieved rate with a bounded worst case.

**Q7 — model answer.** Latency-critical → real-time target; latency-tolerant → best-effort. The inner feedback loop is latency-critical (delay destabilises), so it goes on the real-time target. Planning, perception, and supervision are latency-tolerant — they set references at lower rates the inner loop tracks between updates — so they run best-effort.

**Q8 — model answer.** Because the instability comes from the target's jitter and missed deadlines (added, unpredictable loop delay), not from the gains. No gain choice removes the timing variability; the correct fix is to move the loop to a protected real-time target.

*Grading: award full credit for a short answer that captures the key idea in the model answer, even if briefer or differently worded; partial credit if the core mechanism is named but not fully explained.*

### Common misconceptions to watch for

- Running the inner loop best-effort (a shared general-purpose computer) and expecting stable timing.
- Re-tuning the gains to fix what is really a placement problem (the target, not the gains).
- Confusing a 'fast computer' with a 'real-time target' — predictability, not average speed, is what matters.
