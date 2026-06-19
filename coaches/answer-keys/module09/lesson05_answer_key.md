---
module: 9
unit: 2
lesson: 5
type: answer_key
title: "Answer Key — From Perception Output to World State"
audience: coaches
---

# Answer Key 2.1 — From Perception Output to World State

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** The world-state entry is the tidied belief: detections after dedupe, annotation, and frame normalization.

**Q2 — B.** De-duplicate, annotate (reachability/distance), normalize frame.

**Q3 — B.** It must not re-perceive — detecting new fruit or re-estimating positions is Module 3's job.

**Q4 — B.** Too-large τ merges genuinely distinct nearby fruit; too-small τ double-counts a jittery one.

**Q5 — True.** An unmerged duplicate becomes a wasted pick or a collision downstream — hence mandatory dedupe.

---

**Q6 — model answer.** Perception reports what it observes; the conversion organizes those reports into one trusted belief the whole system acts on (merge duplicates, annotate derived facts, normalize frame). That organization is a system-level decision shared by every downstream stage, with its own tuning, so it belongs at the integration seam — not buried inside a component where it would scatter system policy and re-mix "what we saw" with "what we believe and will act on."
*Grading: credit the shared-system-belief idea and the organize-vs-perceive boundary.*

**Q7 — model answer.** 0.03 m < τ = 0.08 m, so the two reports are merged into one world-state entry (keeping the higher-confidence copy). The world state contains a single annotated entry for that fruit; the duplicate never reaches selection.
*Grading: require the merge decision and "one entry, duplicate removed."*
