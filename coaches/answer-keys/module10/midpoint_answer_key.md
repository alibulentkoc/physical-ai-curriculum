---
module: 10
type: midpoint_answer_key
title: "Module 10 Midpoint Assessment — Coaches' Answer Key (Units 1–4)"
---

# Module 10 — Midpoint Assessment: Coaches' Answer Key

Model answers and a grading rubric for the Units 1–4 midpoint. Award partial credit
generously where the reasoning is sound; the goal is to confirm conceptual understanding of
the *honest twin*, not exact wording. Total ≈ 100 pts (A–D: 18 each; E: 28).

---

## Section A — What Is a Digital Twin? (18 pts)

**A1 (6).** A **model** is a general description of how a system behaves; a **simulator** runs
a model forward for some scenario. A **digital twin** is a model + simulation *bound to a
specific real asset* and kept synchronized with it — it mirrors *this* robot's actual state,
not a generic one. "Twin" adds the binding to a particular real counterpart and the ongoing
correspondence with it.
*Rubric: model vs simulator distinction (2); twin = bound to a specific asset + synchronized (4).*

**A2 (6).** Twin (any three): the arm's joint configuration / tool pose; the fruit layout and
ripeness/picked status; the health/monitor signals; the harvest progress. Deliberately **not**
twinned (any one): fine contact mechanics, full sensor noise physics, actuator dynamics,
every environmental disturbance. Choosing what to twin is a design decision because a twin is
a *purposeful simplification* — copying everything is impossible and unnecessary; you twin
what the twin's job requires.
*Rubric: three twinned quantities (3); one excluded (1); "purposeful simplification, not total copy" (2).*

**A3 (6).** "Living" implies the twin is *kept in correspondence over time* with its real
asset — it is re-synced as reality changes, so it tracks the current robot, whereas a one-off
simulation is a single detached run with no ongoing tie to a specific real system.
*Rubric: ongoing synchronization/correspondence over time (4); contrast with a detached one-off run (2).*

---

## Section B — Building the Mirror (18 pts)

**B1 (6).** The twin's **state** is a copyable snapshot of the reported world-state: joint
config `q`, tool position, per-fruit state (xy, ripe, picked), plus health, stage, harvested
count (any three). It is a *snapshot* (a copy) rather than a live reference so the twin owns
an independent frame it can compare, simulate from, and hold fixed — it is not entangled with
reality's live state.
*Rubric: three quantities (3); copyable/independent snapshot rationale (3).*

**B2 (6).** `twin.sync(real_report)` overwrites the twin's mirrored state with the real
robot's reported state, so the twin reflects reality as of that report. Immediately after a
sync, the divergence between the twin and the real *report* is **zero** (they match).
*Rubric: sync mirrors the report into the twin (4); post-sync divergence-to-report = 0 (2).*

**B3 (6).** **Drift** is the divergence that accumulates *between* syncs as reality moves on
while the twin holds its last snapshot. The **residual gap to truth** is different: even right
after a flawless sync (divergence-to-report = 0), the twin can still differ from reality's
*true* state because reality carries effects it does **not report** (e.g., a hidden offset).
Syncing to the report cannot close a gap the report never contained.
*Rubric: drift = between-sync divergence (2); residual = gap to unreported truth even post-sync (3); "sync to report can't fix unreported effects" (1).*

---

## Section C — Simulating the System in the Twin (18 pts)

**C1 (6).** Simulation is **running the Module 9 harvester (`harvest_row`) forward on the
twin's own world to produce a predicted outcome.** Two rules make it a *twin* simulation:
(1) it runs on the **twin's own world** (a copy of reality's layout — it predicts *this*
robot's harvest); (2) it runs on a **fresh copy** each time (reality untouched, repeatable).
*Rubric: definition (2); runs on the twin's own world (2); runs on a copy / reality untouched (2).*

**C2 (6).** `harvest_row` **mutates** the world as it picks (fruit marked, arm moved).
Simulating on the twin's live state would *consume* that state, so the twin could not simulate
a second scenario from the same start nor keep mirroring. Running on a copy keeps the state
intact (repeatable, non-destructive).
*Rubric: harvest_row mutates the world (3); consequence = state consumed / no re-runs (3).*

**C3 (6).** Determinism: same world + same seed → **identical outcome**. This makes a
simulation a controlled experiment because you can **replay** a run exactly and change exactly
one thing while holding everything else fixed, so any difference is **attributable** to that
change. A difference between two runs with identical inputs means an **input actually changed**
(a stray injection, a mutated world, leaked state) — not inherent randomness.
*Rubric: same world+seed → identical (2); replay + one-change-attribution (2); difference ⇒ an input changed (2).*

---

## Section D — The Sim-to-Real Gap (18 pts)

**D1 (6).** The twin and reality run the **same orchestrator** but on **different worlds**:
reality's world carries **unmodeled effects** (disturbances, obstacles, calibration errors)
that the twin's world lacks. Identical logic on different inputs can produce different
outcomes — that difference is the sim-to-real gap, and its source is the unmodeled effect.
*Rubric: same logic / different worlds (3); unmodeled effects as the source (3).*

**D2 (6).** Only F3 diverged: the twin **predicted F3 harvested** but reality **skipped** it,
so the twin was **too optimistic** about F3 (it didn't model whatever stopped the real pick).
The metric is localised (F3) and directional (optimistic), telling calibration exactly what to
do: **add the missing effect on F3** to the twin's world.
*Rubric: only F3 differs (2); direction = too optimistic, predicted-harvested/actually-skipped (2); action = model the missing effect on F3 (2).*

**D3 (6).** **Calibration** shrinks the gap by **modeling a previously-unmodeled, *known*
effect** in the twin's world (e.g., adding the obstacle). It is *not* machine learning because
it does not infer or fit anything from data — you apply a known effect you have already
identified. Even after `match = true`, the twin is not a perfect replica because calibration
closes the gap **only for the modeled effect**; reality always carries *other* unmodeled
effects, so a residual remains and a new situation can reopen a gap.
*Rubric: calibration = model a known effect (2); not ML — applies known knowledge, no fitting (2); residual remains / per-effect, not global (2).*

---

## Section E — Integrative (28 pts)

**E1 (8).** Story: the twin first **mirrors** the real robot by holding a copyable snapshot of
its reported state and syncing to it; it then **simulates** by running `harvest_row` forward on
its own world copy — safely (reality untouched), as a sandbox (inject what-ifs), reproducibly
(determinism); running both twin and reality reveals the **sim-to-real gap** caused by
unmodeled effects, which is **measured** by `outcome_gap`; **calibration** shrinks that gap by
modeling the known missing effect, though a residual always remains. Midpoint condition (one
phrase): the twin is **faithful but intentionally imperfect** (an honest, useful twin).
*Rubric: mirror (1.5), simulate (1.5), gap (1.5), measure (1.5), calibrate (1); midpoint phrase (1).*

**E2 (10).** A reasonable principle: **trust a twin's prediction to act on it in regimes where
the measured gap is small and the relevant effects are calibrated; withhold action (or verify
on the real system / re-calibrate) where the gap is large or the situation exercises effects
the twin is known not to model.** Connect to 4.2: the **gap metric** quantifies *how far* and
*in which direction* (optimistic vs pessimistic) the twin diverges, so it supplies the
"how small is small" and flags optimistic predictions as the riskier kind to act on; connect
to 4.3: **calibration** is the lever that *moves* a situation from "untrusted" to "trusted" by
modeling the missing effect, and the persistent residual is why trust is always bounded.
*Rubric: a sound, gap-conditioned trust principle (4); ties to the gap metric incl. direction (3); ties to calibration as the trust lever + bounded by residual (3). Accept other defensible principles.*

**E3 (10).** An intentionally imperfect twin whose limits are *measured* lets you act where
it's reliable and abstain where it isn't — you can calibrate trust by the gap. (a) Trusting it
blindly as reality invites acting on optimistic predictions that reality won't honor (e.g.,
expecting F3 harvested when it will be skipped), causing real failures. (b) Discarding it for
imperfection throws away a genuinely useful forecasting/monitoring tool over a gap that is both
inevitable and manageable. The measured middle path — use it where the gap is small, keep
calibrating — captures the value while bounding the risk.
*Rubric: measured imperfection enables calibrated trust (4); concrete failure of blind trust (3); cost of discarding a useful-but-imperfect twin (3).*

---

### Scoring summary
- **90–100:** Strong grasp of the honest twin — mirror, simulate, measure, calibrate — and why imperfection is a managed feature, not a flaw.
- **75–89:** Solid; minor gaps, often in the drift-vs-residual distinction or the trust principle (E2).
- **60–74:** Partial; revisit Unit 3 (simulation on a copy / determinism) or Unit 4 (gap direction & calibration-is-not-learning).
- **< 60:** Re-study Units 1–4 before Installment C (Monitoring & Prediction), which builds directly on simulation and the gap.
