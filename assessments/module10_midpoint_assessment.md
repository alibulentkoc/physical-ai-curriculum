---
module: 10
type: midpoint_assessment
title: "Module 10 Midpoint Assessment — Units 1–4"
covers: "What a digital twin is · building the mirror (state & sync) · simulating the system in the twin · the sim-to-real gap (divergence, measurement, calibration)"
estimated_time: "60–75 min"
---

# Module 10 — Midpoint Assessment (Units 1–4)

You are halfway through Module 10, the Digital Twin capstone. The first half built an
*honest* twin from the ground up: from *what a digital twin is* (and how it differs from a
model or a generic simulator), to *building the mirror* (representing the twin's state and
synchronizing it to the real robot), to *simulating the system in the twin* (running the
Module 9 harvester forward, safely and reproducibly, as a sandbox), to *the sim-to-real gap*
(why twin and reality diverge, how to measure the divergence, and how calibration shrinks it
without ever reaching a permanent zero). This assessment checks that arc. Sections A–D mirror
the four units; Section E is integrative. Computational items can be answered with the lesson
notebooks.

Throughout, the twin wraps Module 9 verbatim: the same `harvest_row` orchestrator runs in
both the twin (on its own world copy) and reality (on its world, carrying unmodeled effects).
Reality is represented by `GroundTruth`, the twin by `DigitalTwin`; they are kept separate by
design. No new robotics theory is needed or expected — answer in terms of mirroring,
simulation, divergence, and calibration. The running robot remains the planar 2-link arm
($L_1=0.4,\ L_2=0.3$).

---

## Section A — What Is a Digital Twin? (Unit 1)

**A1.** In one or two sentences, distinguish a **digital twin** from (a) a *model* and
(b) a generic *simulator*. What does the word "twin" add that those two do not?

**A2.** Name three things we choose to twin about the greenhouse robot, and one thing we
deliberately do **not** twin. Why is choosing what to twin a design decision rather than an
attempt to copy everything?

**A3.** A digital twin is described as a *living* counterpart of a specific real asset.
Explain what "living" implies that a one-off simulation does not.

## Section B — Building the Mirror: State & Synchronization (Unit 2)

**B1.** Define the twin's **state** (the mirrored world-state frame). Name three quantities it
holds, and say why it is stored as a *copyable snapshot* rather than a live reference to
reality.

**B2.** Explain **synchronization**: what `twin.sync(real_report)` does, and what the
divergence between twin and the real *report* becomes immediately after a sync.

**B3.** Distinguish **drift** (between syncs) from the **residual gap** to *truth*. After a
flawless sync, why can a gap to reality's true state still remain? (Hint: reality may carry an
effect it does not report.)

## Section C — Simulating the System in the Twin (Unit 3)

**C1.** Define **simulation** in the twin in one sentence, and state the two design rules that
make it a *twin* simulation rather than a generic one (where it runs, and on what).

**C2.** Why must simulation run on a **copy** of the twin's world rather than the twin's live
state? Give the consequence of not doing so.

**C3.** State the **determinism** property (same world + same seed → ?). Explain how it turns
a one-off simulation into a *controlled experiment*, and what a difference between two runs
with identical inputs would tell you.

## Section D — The Sim-to-Real Gap (Unit 4)

**D1.** The twin runs the **same** `harvest_row` as reality, yet its predicted harvest can
differ from the actual one. Explain why, naming the source of the divergence.

**D2.** With an unmodeled obstacle on F3, `outcome_gap` reports
`harvested_only_in_sim = [F3]`, `skipped_only_in_real = [F3]`, `match = false`. Interpret this:
which fruit diverged, in which **direction** (optimistic or pessimistic), and what the metric
tells calibration to do.

**D3.** Define **calibration**, and state clearly why it is *not* machine learning. After
calibrating a known effect so that `match = true`, why is the twin still *not* a perfect
replica of reality?

## Section E — Integrative

**E1.** Tell the first-half story in one paragraph: take the twin from *mirror* → *simulate* →
*sim-to-real gap* → *calibrate*, and end by stating the midpoint condition in one phrase
(what the twin now is).

**E2.** The back half will *use* the twin to **monitor**, **predict**, and **adapt** the real
system — all leaning on its predictions. Propose a principle for *when* a twin's prediction
should be trusted enough to act on and when it should not, and connect your principle to the
**gap metric** (4.2) and **calibration** (4.3).

**E3.** Argue, in three or four sentences, why an *intentionally imperfect* twin whose limits
are measured is more useful than either (a) a twin trusted blindly as if it were reality, or
(b) a twin discarded for not being a perfect replica.

---

*Coaches: model answers and a grading rubric are in
`coaches/answer-keys/module10/midpoint_answer_key.md`.*
