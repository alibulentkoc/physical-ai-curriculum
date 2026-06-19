# Module 10 — Installment B Milestone Report
### Units 3–4 · "Simulating the System in the Twin" → "The Sim-to-Real Gap" · the module midpoint

*Production Engineer report to the Curriculum Architect. Per the operating-mode directive,
this report foregrounds student understanding, conceptual progression, educational risks, and
scope boundaries; production metrics are confined to the closing verification section.*

---

## 1. What this installment teaches

Installment B is the pivot of the entire module. Installment A gave students a twin that
**reflects** — a faithful mirror of the real robot's reported state. Installment B gives that
twin the two capabilities that make it worth building: the power to **run** (Unit 3), and the
honesty to **know its own limits** (Unit 4). By the end — the module midpoint at L16 — students
hold a twin that is *faithful but intentionally imperfect*, and they understand precisely why
that imperfection is a managed feature rather than a defect.

The through-line is the module spine: **Model → Mirror → Simulate → Monitor → Predict →
Adapt.** Installment A lit *Mirror*; Installment B lights *Simulate* and confronts the
faithfulness question that gates everything after it.

---

## 2. Conceptual progression

The eight lessons move in a deliberate arc from a new power to a hard-won honesty about its
limits.

**Unit 3 — Simulating the System in the Twin (the twin learns to run).**
- **3.1 Running the System Inside the Twin** introduces simulation as *running the Module 9
  harvester forward on the twin's own world copy* to produce a predicted outcome — reframing
  the twin from a reflection into a predictor. The decisive idea is that this is not new
  machinery: it is `harvest_row`, reused verbatim, run on a copy so reality is never touched.
- **3.2 The Twin as a Sandbox** turns "run on a copy" into its practical payoff: you can inject
  faults and what-ifs the real robot could never safely face, and study the outcome with
  nothing real at stake. This is where students feel *why* a twin is valuable.
- **3.3 Replay and Reproduce: Determinism** supplies the scientific discipline: same world +
  same seed → identical outcome, so a simulation can be replayed and a single change isolated.
  Without this, no later comparison (gap, calibration) would be trustworthy.
- **3.4 Unit 3 Recap** consolidates "the twin now predicts, safely and reproducibly" and names
  the one assumption every prediction rests on — fidelity — which becomes Unit 4.

**Unit 4 — The Sim-to-Real Gap (the twin learns its limits).**
- **4.1 Why Twin and Reality Diverge** delivers the module's central honesty: identical logic
  on *different worlds* diverges because reality carries **unmodeled effects** the twin lacks.
  The gap is framed as inevitable *and* informative — not a bug to chase to zero.
- **4.2 Measuring the Gap** makes the gap actionable by quantifying it: which fruit diverged,
  in which direction (optimistic vs pessimistic), as a trackable number — built entirely from
  existing `harvest_row` outputs.
- **4.3 Calibrating the Twin** closes the loop: shrink the gap by *modeling a known
  previously-unmodeled effect*. Calibration is carefully framed as **modeling, not learning** —
  knowledge applied, not data fitted — and a residual is shown to always remain.
- **4.4 Unit 4 Recap and Midpoint** steps back: the twin mirrors, simulates, and is honestly
  imperfect; the back half will *use* it to monitor, predict, and adapt. The midpoint condition
  is stated in a phrase students will carry to the end: **faithful but intentionally imperfect.**

The flagship demo (the **Sim-to-Real Gap Explorer**, attached to 4.1) lets students toggle an
unmodeled effect, watch the predicted and actual harvests diverge fruit-by-fruit, read the
divergence scoreboard, and click *calibrate* to snap the prediction back into agreement — then
add a new effect and watch a fresh gap open. The whole Unit-4 arc is legible in one panel.

---

## 3. Where students are most likely to struggle

- **"The twin is broken."** The single most important misconception to pre-empt: when the twin
  predicts a fruit harvested and reality skips it, students instinctively read a bug. Every
  Unit-4 lesson reframes this explicitly — identical logic, different worlds, an unmodeled
  effect — and the worked examples and answer keys hammer "not broken, diagnostic." This is the
  conceptual heart of the installment and the place coaching attention pays off most.
- **Expecting a zero gap.** Closely related: students may treat calibration as a path to a
  perfect twin. 4.3 and 4.4 repeatedly assert the *residual always remains*; the calibration
  notebook proves it by reopening a gap with a new effect after one is closed.
- **Calibration mistaken for machine learning.** Because "calibration" and "shrinking error"
  evoke training, 4.3 states plainly that calibration models a *known* effect (the bathroom-scale
  analogy) and adds no fitting or inference — keeping the module inside its no-new-theory bound.
- **Simulating on live state.** A subtle but real trap: students may not see why simulation runs
  on a *copy*. 3.1/3.2 tie this directly to `harvest_row` mutating the world, and the notebooks
  assert non-destructiveness.
- **Direction-blindness in the metric.** 4.2 stresses that "too optimistic" (predicted
  harvested, really skipped) and "too pessimistic" differ in consequence — a distinction that
  matters greatly once predictions drive action in the back half.

---

## 4. Educational risks and how they're handled

- **Risk: the gap reads as failure, demotivating students.** Handled by framing the gap as the
  module's *honesty* and its most useful signal — the thing that tells you what to model next —
  rather than a shortcoming. The midpoint lesson's "useful *because* its limits are measured"
  argument is the antidote.
- **Risk: scope creep into estimation/learning.** Calibration is the natural place a curriculum
  drifts toward parameter-fitting or ML. The installment holds the line: calibration models a
  *known* effect identified by the gap metric, full stop. No estimator, no optimizer, no fitting.
- **Risk: over-trust in the twin going into the back half.** Pre-empted at the midpoint by
  E2-style reasoning (the midpoint assessment asks students to propose *when* a prediction is
  trustworthy enough to act on), seeding the disciplined stance the back half requires.
- **Risk: the sandbox conflated with reality.** Repeatedly reinforced that injecting in the twin
  touches only the copy; the notebooks assert reality is unchanged after every what-if.

---

## 5. Scope boundaries honored

Per the Architect's standing guidance and the §9 rulings, this installment:
- **Reuses Module 9 verbatim; does not redefine it.** Simulation is `harvest_row` run forward
  in the twin; the sandbox uses M9's existing fault-injection; the outcome gap reads only
  existing `harvest_row` outputs. The substrate extension is purely additive.
- **Keeps the twin lightweight, faithful, and intentionally imperfect.** A small Python twin;
  no Gazebo/Isaac, no physics engine. The sim-to-real gap is explicit, measured, and preserved
  — never papered over.
- **Represents reality (`GroundTruth`) and the twin (`DigitalTwin`) separately.** Unmodeled
  effects live in reality; the twin only knows what it has been calibrated with. The separation
  is enforced in code and is the engine of the gap lessons.
- **Introduces no new theory.** No formal dynamics, no estimation/learning, no control theory.
  Calibration is modeling a known effect; determinism is inherited from M9's seeded execution.
- **Adds no new dependencies.** Same engine, same generator, same build pipeline.

---

## 6. Verification summary (production)

All Installment B artifacts are built, executed, and verified.

| Artifact | Count | Status |
|---|---|---|
| Lessons (L09–L16, full 12-section template) | 8 | ✅ written |
| Diagrams (`m10-l9 … m10-l16`, one per Visual Explanation) | 8 | ✅ XML-valid |
| Notebooks (self-verifying, `assert all(checks)`) | 8 | ✅ all "All checks passed." |
| Quizzes (6 items each) | 8 | ✅ generated & valid |
| Answer keys (MC + model short answers + grading notes) | 8 | ✅ written |
| Flagship demo — Sim-to-Real Gap Explorer (→ 4.1/L13) | 1 | ✅ self-contained, no storage |
| Midpoint assessment + coaches' answer key (§9.7) | 1+1 | ✅ written |

- **Substrate (additive simulate layer):** `GroundTruth.unmodeled` + `.run()`; `DigitalTwin.simulate()`,
  `.calibrate()`, `.calibration`; module-level `outcome_gap()`. Verified end to end: an
  unmodeled obstacle makes the twin predict F3 harvested while reality skips it
  (`outcome_gap` → n_diffs=2, match=false); simulation is reproducible under a fixed seed;
  calibrating the known effect closes the gap (match=true); a new effect reopens it.
- **Site generation:** `309 pages` (301 → 309), each L09–L16 page carrying its figure,
  notebook tip, and quiz; the demo iframe injected on L13 only.
- **Strict build:** `mkdocs build --strict` → **exit 0**.
- **Regression:** all **16/16** Module 10 notebooks (L01–L16) re-executed and pass.
- **Hygiene:** throwaway build scripts removed; reusable helpers (`_m9_nbbuild.py`,
  `_m9_quizbuild.py`) retained. All work is local working-tree only — **not yet pushed**.

---

## 7. State and next step

**Module 10 is at its midpoint:** Units 1–4 complete (16 lessons), the twin mirrors and
simulates, the sim-to-real gap is explicit, measured, and calibratable, and a residual is
honestly preserved. The spine reads **Model · Mirror · Simulate** done; **Monitor · Predict ·
Adapt** ahead.

**Pausing at the Installment B milestone, per directive.** Installment C (Units 5–6:
*Monitoring with the Twin* → *Prediction with the Twin*) is ready to begin on the Architect's
explicit go-ahead. Recommended pre-C confirmations: (1) monitoring is *comparing reality
against the twin* and treating divergence as a signal (it leans directly on the outcome gap and
the residual established here); (2) prediction is *run-ahead / what-if* with no learning, per
§9.4. No blockers.
