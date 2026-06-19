"""
Module 10 — Digital Twin (lightweight, in-repo).

The twin WRAPS the Module 9 integrated system; it does not redefine it. It keeps its
own virtual copy of the greenhouse world-state and MIRRORS what the real system
reports. Per the architect rulings:

  - §9.1  Lightweight Python twin (no Gazebo/Isaac; those are industrial tooling only).
  - §9.2  Reality (GroundTruth) and the twin are represented SEPARATELY, so a real
          sim-to-real gap can exist and be measured.
  - §9.3  Wrap, do not redefine — Modules 1-9 are imported, never re-implemented.

Installment A scope: build the twin and the mirror — snapshot, sync, divergence — and
the explicit reality/twin separation. Simulation, monitoring, prediction, and
adaptation are later installments and are added additively.
"""
import numpy as np
from modules.module09.integration import GreenhouseWorld, Fruit, fk_xy, P2, T2


def fruit_state(world):
    """The per-fruit observable state (position, ripeness, picked) as a copyable dict."""
    return {f.fid: {"xy": np.asarray(f.xy, float).copy(),
                    "ripe": bool(f.ripe), "picked": bool(f.picked)}
            for f in world.fruit}


def snapshot(world, health=None, stage="idle", harvested=None):
    """Capture the observable world-state the real system REPORTS — the twin's input.

    A plain, copyable 'telemetry frame': the joint configuration, the tool position,
    the fruit states, the health signals, the pipeline stage, and the harvested list.
    This is the only thing the twin ever sees of reality.
    """
    return {
        "q": np.asarray(world.q, float).copy(),
        "tool_xy": np.asarray(world.tool_xy(), float).copy(),
        "fruit": fruit_state(world),
        "health": dict(health or {}),
        "stage": str(stage),
        "harvested": list(harvested or []),
    }


def clone_layout(world, q=None):
    """A fresh GreenhouseWorld with the SAME layout (fruit + configuration). Used to give
    the twin its own world instance, separate from reality (§9.2)."""
    fruit = [Fruit(f.fid, f.x, f.y, ripe=f.ripe, visible=f.visible, picked=f.picked)
             for f in world.fruit]
    qq = world.q.copy() if q is None else np.asarray(q, float).copy()
    return GreenhouseWorld(fruit=fruit, q=qq)


class GroundTruth:
    """REALITY — the real greenhouse + robot.

    May carry UNMODELED effects the twin does not know about (here, a hidden joint
    offset `q_offset`) — the source of the sim-to-real gap. The twin only ever sees
    what GroundTruth *reports* (`report()`), never its true state (`true_report()`).
    With `q_offset = 0` reality is fully observable and a perfect mirror is possible;
    with a nonzero offset a residual gap remains even after a flawless sync.
    """

    def __init__(self, world, q_offset=None, unmodeled=None):
        self.world = world
        self.q_offset = (np.zeros_like(np.asarray(world.q, float)) if q_offset is None
                         else np.asarray(q_offset, float))
        # outcome-level unmodeled effects: an inject dict (per-fruit fault specs) that
        # reality experiences but the twin's model does not know about (the gap source).
        self.unmodeled = unmodeled or {}

    def run(self, **kw):
        """Run the REAL harvest — reality experiences its unmodeled effects. Returns the
        actual outcome (harvested/skipped/picks). Reuses Module 9's harvest_row verbatim."""
        from modules.module09.integration import harvest_row
        return harvest_row(clone_layout(self.world), inject=self.unmodeled, **kw)

    @property
    def true_q(self):
        """Reality's TRUE joint state (reported + the hidden offset)."""
        return np.asarray(self.world.q, float) + self.q_offset

    def true_tool_xy(self):
        return np.asarray(fk_xy(P2, T2, self.true_q), float)

    def report(self):
        """What reality REPORTS to the twin (its observable snapshot) — no hidden offset."""
        return snapshot(self.world)

    def true_report(self):
        """Reality's TRUE snapshot (incl. unmodeled effects). NOT visible to the twin;
        used only to MEASURE the real sim-to-real gap."""
        s = snapshot(self.world)
        s["q"] = self.true_q.copy()
        s["tool_xy"] = self.true_tool_xy().copy()
        return s


class DigitalTwin:
    """A lightweight virtual replica that MIRRORS the M9 system's reported state.

    Holds its OWN world instance (separate from reality, §9.2) and a mirrored state
    frame. `sync` copies a reported snapshot into the twin; `divergence` measures the
    gap between the twin and any snapshot (→ ~0 against the report it synced to;
    nonzero against reality's TRUE report when an unmodeled effect is present). The
    twin never re-implements Modules 1-9 (§9.3).
    """

    def __init__(self, layout_world):
        self.world = clone_layout(layout_world)   # the twin's own world
        self.state = snapshot(self.world)
        self.calibration = {}                      # effects the twin has been told about

    def simulate(self, inject=None, **kw):
        """Run the Module 9 harvester FORWARD inside the twin's own world (on a fresh
        copy, so the twin can simulate repeatedly without consuming its world). The twin
        applies any effects it has been told about (`calibration`) plus an optional
        scenario `inject` for what-if. Reuses harvest_row verbatim — no new theory."""
        from modules.module09.integration import harvest_row
        eff = dict(self.calibration)
        if inject:
            eff.update(inject)
        return harvest_row(clone_layout(self.world), inject=(eff or None), **kw)

    def calibrate(self, unmodeled):
        """Shrink the sim-to-real gap by TELLING the twin about an effect it was missing
        (a previously-unmodeled inject). Calibration is just modeling a known effect — a
        simple, explained adjustment, not a learning algorithm."""
        self.calibration = dict(unmodeled or {})
        return self.calibration

    def sync(self, real_report):
        """Mirror the real system's reported state into the twin (q, tool, fruit, health)."""
        self.state = {k: (v.copy() if hasattr(v, "copy") else
                          ({kk: dict(vv) for kk, vv in v.items()} if isinstance(v, dict)
                           else v))
                      for k, v in real_report.items()}
        self.world.q = np.asarray(real_report["q"], float).copy()
        for f in self.world.fruit:
            fr = real_report["fruit"].get(f.fid)
            if fr is not None:
                f.ripe = bool(fr["ripe"]); f.picked = bool(fr["picked"])
        return self.state

    def divergence(self, real_report):
        """The sim-to-real gap between the twin's state and a reported state: the joint
        gap, the tool-position gap, and the count of fruit-status mismatches. Reads
        existing state only — no new theory. `synced` is True when the gap is ~0."""
        rq = np.asarray(real_report["q"], float)
        rxy = np.asarray(real_report["tool_xy"], float)
        dq = float(np.linalg.norm(rq - np.asarray(self.state["q"], float)))
        dxy = float(np.linalg.norm(rxy - np.asarray(self.state["tool_xy"], float)))
        mismatch = sum(
            1 for fid, fr in real_report["fruit"].items()
            if self.state["fruit"].get(fid, {}).get("picked") != fr["picked"]
        )
        return {"q_gap": dq, "tool_gap": dxy, "fruit_mismatch": mismatch,
                "synced": (dq < 1e-9 and dxy < 1e-9 and mismatch == 0)}


def outcome_gap(sim, real):
    """The sim-to-real gap at the OUTCOME level: how a simulated harvest (the twin's
    prediction) differs from the real harvest (reality's actual result). Compares the
    harvested and skipped sets and the per-fruit attempt counts. Reads existing
    harvest_row outputs only — no new theory. `match` is True when they agree."""
    sh, rh = set(sim["harvested"]), set(real["harvested"])
    ss, rs = set(sim["skipped"]), set(real["skipped"])
    sim_att = {p["target"]: p["n_attempts"] for p in sim["picks"]}
    real_att = {p["target"]: p["n_attempts"] for p in real["picks"]}
    attempt_diffs = {fid: (sim_att.get(fid), real_att.get(fid))
                     for fid in (set(sim_att) | set(real_att))
                     if sim_att.get(fid) != real_att.get(fid)}
    harvested_only_sim = sorted(sh - rh)
    harvested_only_real = sorted(rh - sh)
    skipped_only_sim = sorted(ss - rs)
    skipped_only_real = sorted(rs - ss)
    match = (sh == rh and ss == rs and not attempt_diffs)
    return {
        "harvested_only_in_sim": harvested_only_sim,
        "harvested_only_in_real": harvested_only_real,
        "skipped_only_in_sim": skipped_only_sim,
        "skipped_only_in_real": skipped_only_real,
        "attempt_diffs": attempt_diffs,
        "n_outcome_diffs": (len(harvested_only_sim) + len(harvested_only_real)
                            + len(skipped_only_sim) + len(skipped_only_real)),
        "match": match,
    }


def monitor(twin, real_report, q_tol=1e-6, tool_tol=1e-6):
    """MONITOR — "what is happening now?" Compare reality against the twin's current
    mirrored state. Divergence is the signal: when reality has moved away from what the
    twin holds (beyond a tolerance), the monitor raises an alert. Reuses twin.divergence
    and the residual gap idea from Installment B; introduces no new estimation theory."""
    d = twin.divergence(real_report)
    alert = (d["q_gap"] > q_tol) or (d["tool_gap"] > tool_tol) or (d["fruit_mismatch"] > 0)
    return {**d, "alert": bool(alert),
            "summary": ("reality matches the twin (in sync)" if not alert
                        else "reality has diverged from the twin — a signal to investigate")}


def predict(twin, inject=None, sync_report=None, **kw):
    """PREDICT — "what is likely to happen next?" Run the EXISTING system ahead inside the
    twin (run-ahead simulation) from its current state, optionally re-synced to the latest
    real report first. Prediction comes from executing the existing system in the twin —
    no machine learning, no predictive model, no adaptive control. Reuses twin.simulate."""
    if sync_report is not None:
        twin.sync(sync_report)
    return twin.simulate(inject=inject, **kw)


def compare_futures(twin, scenarios, **kw):
    """LOOKAHEAD / WHAT-IF — forecast several candidate futures by simulating each named
    scenario in the twin and returning their outcomes side by side for comparison. Pure
    run-ahead over the existing system; no new theory."""
    return {name: twin.simulate(inject=inj, **kw) for name, inj in (scenarios or {}).items()}


# ---------------------------------------------------------------------------
# Installment D — ADAPTATION layer (Unit 7): closing the twin-in-the-loop.
# Adaptation is PRE-VALIDATION + ACTION-SELECTION using the existing twin.
# No machine learning, no reinforcement learning, no adaptive control, no
# optimization framework — just running candidate actions ahead in the twin
# and choosing with a simple, explained rule. Reuses simulate/compare_futures.
# ---------------------------------------------------------------------------

def prevalidate(twin, action=None, ok=None, **kw):
    """PRE-VALIDATE — before committing an action in reality, run it FORWARD in the twin
    and inspect the predicted outcome. `action` is a what-if inject describing the
    candidate (e.g. an obstacle the robot would face, or no change for the nominal plan).
    A simple, explained acceptance test `ok(forecast)` returns the verdict; the default
    accepts a plan that completes with nothing skipped. This is pre-validation using the
    existing twin — not learning, not optimization. Returns the forecast and the verdict."""
    forecast = twin.simulate(inject=action, **kw)
    if ok is None:
        ok = lambda f: bool(f.get("complete", False)) and not f.get("skipped")
    return {"action": action, "forecast": forecast, "accept": bool(ok(forecast))}


def select_action(twin, candidates, score=None, **kw):
    """ACTION SELECTION — choose the better action by PRE-VALIDATING each candidate in the
    twin and ranking the results with a simple, explained score. `candidates` maps a name
    to a what-if inject. The default score prefers more fruit harvested, then fewer skipped
    (a plain tuple comparison, not an optimizer). Returns each candidate's forecast, the
    ranking, the per-candidate scores, and the chosen name. Pure compare-and-pick over twin
    run-aheads — no RL, no optimization framework."""
    if score is None:
        score = lambda f: (len(f.get("harvested", [])), -len(f.get("skipped", [])))
    futures = compare_futures(twin, candidates, **kw)
    ranked = sorted(futures.items(), key=lambda kv: score(kv[1]), reverse=True)
    chosen = ranked[0][0] if ranked else None
    return {"futures": futures,
            "ranking": [name for name, _ in ranked],
            "scores": {name: score(f) for name, f in futures.items()},
            "chosen": chosen}


def twin_in_the_loop(twin, real_report, candidates, q_tol=1e-6, tool_tol=1e-6, **kw):
    """THE TWIN-IN-THE-LOOP CYCLE — one full turn of the closed loop, assembled entirely
    from pieces built earlier in the module:
        MONITOR  reality against the twin  ("what is happening now?")
        re-SYNC  the twin if reality has drifted (so decisions use the latest state)
        PREDICT  by running the existing system ahead in the twin ("what happens next?")
        ADAPT    by pre-validating candidate actions and selecting the better one
    Returns each stage's result and the chosen action. This is the spine
    Mirror -> Simulate -> Monitor -> Predict -> Adapt, with no new theory."""
    m = monitor(twin, real_report, q_tol=q_tol, tool_tol=tool_tol)
    if m["alert"]:
        twin.sync(real_report)                 # re-mirror before deciding
    forecast = twin.simulate(**kw)             # predict from the (re)synced state
    decision = select_action(twin, candidates, **kw)
    return {"monitor": m, "resynced": bool(m["alert"]),
            "forecast": forecast, "decision": decision, "chosen": decision["chosen"]}
