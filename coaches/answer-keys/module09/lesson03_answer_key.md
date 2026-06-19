---
module: 9
unit: 1
lesson: 3
type: answer_key
title: "Answer Key — System Walkthrough: Tracing One Tomato"
audience: coaches
---

# Answer Key 1.3 — System Walkthrough: Tracing One Tomato Through All Six Stages

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** A trace is the sequence of blackboard states with the changed field and its owner at each stage.

**Q2 — B.** Read the upstream stamp first: a `None` target can be empty detections (Perceive) or no ripe+reachable detection (a correct Understand result).

**Q3 — B.** Detections existed but none passed the ripe-and-reachable filter — a legitimate Understand outcome, not a bug.

**Q4 — B.** A trace localises a fault to a stage by checking the contract chain, before opening any layer.

**Q5 — True.** Carried state (`q`, the harvested set) persists between picks and is part of correctness.

---

**Q6 — model answer.** Checking the contract chain means confirming, at each step, that the stage's precondition held on the previous state and its postcondition holds on the new one — e.g. Understand's output target is one of Perceive's detections and is reachable. A correct trace is one where every link's contract holds; reading it verifies those links in order, pinpointing the first stage that violated its contract.
*Grading: credit the per-step precondition/postcondition idea and the "localise the first violated link" outcome.*
