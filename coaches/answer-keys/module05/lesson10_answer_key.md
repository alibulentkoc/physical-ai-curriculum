# Answer Key — Lesson 3.2: The atan2 Tool and Choosing the Right Quadrant

**Coaches only.** Formative.

1. **Why atan2 not arctan** — atan2 uses the two signs to return the correct quadrant; arctan(y/x) loses it and breaks at x=0.
2. **atan2(0.5, −0.5)** — 135° (second quadrant).
3. **arctan undefined at x=0; atan2 fine** — True.
4. **Behind-the-base with arctan (short).** It aims the shoulder ~180° wrong, into the opposite half-plane, because arctan only spans (−90°, 90°).

**Challenge rubric.** Full credit: atan2(|a×b|, a·b) stays accurate for tiny and near-180° angles because it never divides by a vanishing quantity, whereas acos((a·b)/(|a||b|)) loses precision where its argument nears ±1 (same conditioning issue as Lesson 3.1). Partial: states atan2 is "more stable" without the near-±1 argument.
