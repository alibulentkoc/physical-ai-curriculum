# Module 10 — Installment C Milestone Report
### Units 5–6: Monitoring with the Twin → Prediction with the Twin (Lessons 5.1–6.4)

**Status:** Complete and verified. Paused at the Installment C milestone, awaiting Architect direction for Installment D.

---

## 1. What the student can now do

Installment C is where the twin stops being something the student *builds and inspects* and becomes something they *put to work*. By the end of these eight lessons, a learner can take the faithful-but-imperfect twin from the first half of the module and use it for two distinct jobs, each tied to a plain-English question.

**Monitoring (Unit 5) — "what is happening now?"** The student learns to watch a running system by holding the twin's mirrored state beside reality's live report and reading the difference. The central move is reframing monitoring away from "build a special detector" and toward "compare against the twin you already have." Divergence is the signal: agreement means the system is behaving as expected, and disagreement means something is happening worth attention. Crucially, the student learns there are *two* divergence signals — state divergence (the snapshot has gone stale, a re-syncable drift) and outcome divergence (reality is behaving differently than predicted, a genuine surprise) — and that telling them apart is what separates "refresh the display" from "investigate the cause." Finally, because the twin's divergence is localised (which fruit) and directional (optimistic vs pessimistic), the student can go past detection to *diagnosis*: composing which-fruit, which-direction, and which-health-signal-moved into a specific account such as "likely obstruction at F3."

**Prediction (Unit 6) — "what is likely to happen next?"** The student learns that the same twin, run *forward* from the current synced state, becomes a forecaster. Prediction is presented strictly as run-ahead simulation — executing the existing Module 9 system inside the twin — and explicitly *not* as machine learning, statistical forecasting, or adaptive control. From there the student builds two capabilities: lookahead (running far enough ahead to catch a problem in time to act) and what-if (running several candidate futures and comparing their outcomes to see what each would cost). The unit closes on the discipline that keeps forecasting honest: a prediction is a simulation, so it inherits the sim-to-real gap, and the student learns *calibrated confidence* — trust a forecast in proportion to the twin's measured fidelity, and treat optimistic forecasts with extra caution.

The installment's connective idea, reinforced in every lesson, is the now/next symmetry: **a monitor compares the twin to reality to answer "what is happening now?"; a predictor runs the twin forward to answer "what is likely to happen next?" — the same underlying model, used two ways.**

## 2. Conceptual progression

The eight lessons form a deliberate arc that mirrors the module's spine (Model · Mirror · Simulate · **Monitor · Predict** · Adapt):

- **5.1 → 5.2 → 5.3** moves from *the idea* of monitoring as comparison, to *reading* the signal in its two forms, to *interpreting* it as a diagnosis. Each step adds discrimination, not new machinery.
- **5.4** consolidates the twin as a live monitor and, importantly, plants the forward-looking question that Unit 6 answers — so the transition feels like a turn of the same handle, not a new tool.
- **6.1 → 6.2 → 6.3** mirrors the same shape for prediction: from *the idea* of run-ahead, to *multiplying* it into lookahead/what-if, to *bounding* it with calibrated confidence.
- **6.4** ties both units together on the now/next symmetry and sets up adaptation (acting on the answers) as the natural next step.

The progression is strongly cumulative: monitoring reuses the state-divergence tool from Installment A and the outcome-gap tool from Installment B; prediction reuses the simulation engine from Installment B; and the limits-of-prediction lesson reuses the entire sim-to-real-gap treatment from Installment B, now re-read as a confidence bound on forecasts. Nothing in Installment C introduces new theory — it is the disciplined *application* of capabilities the student already has, which is exactly the right shape for a capstone.

## 3. Educational risks and how they are handled

- **"Monitoring/prediction must be something fancier."** The strongest misconception risk is that students expect anomaly detectors or learned predictors. Every lesson explicitly names what these capabilities are *not* (no new estimation theory; no ML/RL/predictive models/adaptive control) and shows them falling out of existing tools. The Common Mistakes sections target this directly.
- **Conflating the two divergence signals.** A student who treats all divergence as one thing will "re-sync away" a real unmodeled effect. Lesson 5.2 and its worked example, plus the recap self-test, drill the state-vs-outcome distinction and pair each with its correct response (re-sync vs investigate/calibrate).
- **Over-trusting forecasts.** The most consequential risk in the whole installment: acting on a confident-but-wrong prediction. Lesson 6.3 is the explicit conscience here — a forecast is only as faithful as the twin — and the notebook demonstrates a forecast inheriting then shedding the gap via calibration, so the limit is felt, not just stated.
- **Losing the through-line.** With two capabilities introduced back to back, the now/next framing could blur. It is restated in the core idea of every lesson and made visual in both recap diagrams, so the symmetry stays in view.

## 4. Scope boundaries (held)

Installment C stays inside the locked Module 10 scope. Monitoring is taught purely as Reality ↔ Twin comparison with divergence as the signal, reusing the outcome gap and residual gap as the primary tools, with **no new estimation theory**. Prediction is taught purely as run-ahead / lookahead / what-if using the existing twin, with **no machine learning, reinforcement learning, predictive models, or adaptive control** — prediction is explicitly "executing the existing system inside the twin." The reality/twin separation, the single robot/twin/greenhouse setting, and the wrap-don't-redefine treatment of the Module 9 system are all preserved. Action selection is *previewed* (what-if comparison is named as its seed) but deliberately deferred to Unit 7, keeping the installment boundary clean.

## 5. Verification (brief)

All artifacts built and checked:

- **8 lessons** (5.1–6.4), full 12-section template, AI Learning Companion, four-language support, §4 visual placeholders.
- **8 SVGs** (`m10-l17`…`m10-l24`), one per lesson, all XML-validated.
- **8 notebooks**, self-verifying; **regression: 24/24 Module 10 notebooks pass** ("All checks passed.").
- **8 quizzes** (5 MC/TF + short answer each) and **8 answer keys**.
- **Flagship demo C** — *Lookahead & What-If Explorer* (Lesson 6.2) — self-contained, no browser storage; runs several candidate futures from a synced "now", shows forecast outcomes side by side, and ranks them by cost.
- **Substrate** extended additively: `monitor`, `predict`, `compare_futures` (thin wrappers over existing `divergence` / `simulate`; no new theory), exported and verified.
- **Site:** nav updated (Units 5–6; `· demo` marker on 6.2); regenerated to **317 pages**; `mkdocs build --strict` exit 0.
- Throwaway build scripts removed; reusable notebook/quiz builders retained.

All Module 10 work remains local to the working tree (not yet committed or pushed).

---

## 6. Recommended next step

Installment D — **Unit 7 (Adaptation: closing the twin-in-the-loop)** and **Unit 8 (Digital Twin Capstone & Curriculum Close)**, with the capstone at Lesson 8.2-area ("Self-Improving Greenhouse Harvest") and the final flagship demo. Per the locked scope, adaptation will be taught as pre-validation / action-selection via what-if — explicitly **not** machine learning. Awaiting Architect go-ahead before beginning.

**Paused at the Installment C milestone as directed.**
