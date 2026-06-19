"""
layers.py — the Module 9 ADAPTER LAYER.

Per the Architect's ruling ("Adapters: Approved. Rule: Wrap. Do not redefine."), this
module re-exports the real layers built in Modules 3-8 through their published interfaces
and adds the small amount of glue that is legitimately Module 9's job: the six-stage layer
REGISTRY (the data-flow spine) and the Understand-stage target SELECTION decision.

What is wrapped (not rebuilt):
    velocity_layer   — Module 6, re-exported verbatim from _m6_velocity (real code).
    forward_chain/fk — Module 4/6 forward kinematics, re-exported verbatim.

What is documented as an interface for later wiring (Units 3-5 wire the real calls):
    reference_layer     — Module 7  reference_trajectory_layer(...)
    tracking_controller — Module 8  control_layer(...) -> tracking_controller(ref, meas, dt)

What is genuinely new here (integration glue only — no perception/IK/control theory):
    LAYER_REGISTRY      — the six-stage spine: who owns each stage, real signature, I/O.
    understand()        — target selection: detections -> ranked, reachable targets.
"""
import numpy as np

# Wrap, do not redefine: re-export the REAL Module 6 layer + FK.
from ._m6_velocity import (  # noqa: F401
    velocity_layer, forward_chain, fk_xy, geometric_jacobian, P2, T2,
)
# Wrap, do not redefine: re-export the REAL Module 5 inverse kinematics.
from ._m5_ik import ik_2link  # noqa: F401
# Wrap, do not redefine: re-export the REAL Module 7 planner / reference layer.
from ._m7_reference import reference_trajectory_layer  # noqa: F401
# Wrap, do not redefine: re-export the REAL Module 8 control layer + plant.
from ._m8_control import control_layer, Joint, step_plant  # noqa: F401
from .world import GreenhouseWorld, REACH_MIN, REACH_MAX, model_perception


# ---------------------------------------------------------------------------
# The six-stage spine. This is the dominant teaching object of Module 9.
# Each entry answers the questions every integration lesson repeats:
#   where does information come from?  who owns the decision?  what flows out?
# ---------------------------------------------------------------------------
LAYER_REGISTRY = [
    {"stage": "Perceive", "module": "Module 3",
     "signature": "model_perception(world) -> detections",
     "reads": ["camera / world"], "writes": ["state.detections"],
     "owns": "what the robot can see (raw detections + confidence)"},
    {"stage": "Understand", "module": "Module 9 (selection) + M4/M5",
     "signature": "understand(detections, world) -> targets, current_target",
     "reads": ["state.detections"], "writes": ["state.targets", "state.current_target"],
     "owns": "which fruit to pick and at what pose (the decision)"},
    {"stage": "Plan", "module": "Module 7",
     "signature": "reference_trajectory_layer(q_start, q_goal, ...).reference(t)",
     "reads": ["state.current_target", "state.q"], "writes": ["state.reference"],
     "owns": "WHEN to be WHERE — the timed reference trajectory"},
    {"stage": "Execute", "module": "Module 6 + Module 8",
     "signature": "tracking_controller(reference(t), measured_state, dt) -> command",
     "reads": ["state.reference", "state.q"], "writes": ["state.command", "state.q"],
     "owns": "turning the reference into real joint motion in real time"},
    {"stage": "Track", "module": "Module 8 telemetry",
     "signature": "controller.info -> tracking_error",
     "reads": ["state.reference", "state.q"], "writes": ["state.tracking_error", "state.health"],
     "owns": "measuring success: tracking error vs. tolerance"},
    {"stage": "Recover", "module": "Module 9 orchestrator",
     "signature": "orchestrator(state) routes on state.health",
     "reads": ["state.health", "state.tracking_error"], "writes": ["state.current_target", "state.stage"],
     "owns": "what to do when a stage fails (retry / replan / abort / degrade)"},
]

STAGES = [e["stage"] for e in LAYER_REGISTRY]


def stage_info(name):
    for e in LAYER_REGISTRY:
        if e["stage"].lower() == name.lower():
            return e
    raise KeyError(name)


# ---------------------------------------------------------------------------
# Understand stage: target selection. This is a Module 9 DECISION, not perception
# and not IK. It consumes perception's detections and produces a clean, ranked,
# reachable target list — exactly the "who owns this decision?" lesson.
# ---------------------------------------------------------------------------
def _reachable(xy):
    r = float(np.linalg.norm(np.asarray(xy, float)))
    return REACH_MIN <= r <= REACH_MAX


def dedupe(detections, tol=0.08):
    """Collapse duplicate detections of the same fruit (a perception artifact the
    Understand stage must own, not silently pass downstream)."""
    kept = []
    for d in sorted(detections, key=lambda x: -x.get("confidence", 0)):
        if all(np.linalg.norm(d["xy"] - k["xy"]) > tol for k in kept):
            kept.append(d)
    return kept


def understand(detections, world: GreenhouseWorld, tool_xy=None):
    """
    Turn raw detections into actionable targets.

    Returns (targets, current_target):
      targets        — ripe, reachable, de-duplicated detections, each annotated with
                       reachability and distance-from-tool, ranked nearest-first.
      current_target — the top-ranked target, or None if nothing is pickable.

    This stage OWNS the harvest decision. It deliberately does NOT solve IK or plan a
    trajectory (those are Modules 5 and 7); it only decides WHICH fruit and surfaces WHY.
    """
    tool = world.tool_xy() if tool_xy is None else np.asarray(tool_xy, float)
    targets = []
    for d in dedupe(detections):
        xy = np.asarray(d["xy"], float)
        t = {"id": d["id"], "xy": xy, "ripe": bool(d.get("ripe", True)),
             "confidence": float(d.get("confidence", 1.0)),
             "reachable": _reachable(xy),
             "dist": float(np.linalg.norm(xy - tool))}
        targets.append(t)
    pickable = [t for t in targets if t["ripe"] and t["reachable"]]
    pickable.sort(key=lambda t: t["dist"])
    targets.sort(key=lambda t: (not (t["ripe"] and t["reachable"]), t["dist"]))
    current = pickable[0] if pickable else None
    return targets, current


def to_configuration(target, L1=0.4, L2=0.3, elbow="up"):
    """
    Understand -> Plan seam (Unit 3): turn a committed target POSE into a goal
    CONFIGURATION via the real Module 5 IK. Returns the joint vector q_goal, or None
    if IK reports the pose unreachable.

    This is pure composition: it WRAPS ik_2link and adds no kinematics of its own. The
    decision of WHAT TO DO when IK returns None (replan, drop the target, re-select) is
    a Recover-stage concern, not this function's job.
    """
    if target is None:
        return None
    xy = target["xy"] if isinstance(target, dict) else target
    return ik_2link(float(xy[0]), float(xy[1]), L1=L1, L2=L2, elbow=elbow)


# numpy is needed for the default obstacle placeholder below
import numpy as _np  # noqa: E402


def plan_reference(q_start, q_goal, obstacle=None, vlim=2.0, alim=4.0,
                   rng=None, **plan_kw):
    """
    Plan stage (Unit 3-4): wrap the REAL Module 7 reference layer to turn a goal
    CONFIGURATION into a timed REFERENCE the controller can sample.

    Pure composition over reference_trajectory_layer (wrapped verbatim). Returns the
    layer dict (with reference(t) -> (q_d, qd_d, qdd_d, info), duration, validated, ...).
    `obstacle` is an optional (center_xy, radius) pair for the planner's collision
    avoidance; if None, a tiny far-away placeholder disk is used so the API is uniform.

    This adapter introduces NO planning theory: it only routes the goal into the
    existing planner and hands the reference forward. Deciding what to do when the
    planner fails to validate is a Recover-stage concern (Units 6-7).
    """
    if obstacle is None:
        center, radius = _np.array([10.0, 10.0]), 0.01     # effectively no obstacle
    else:
        center, radius = _np.asarray(obstacle[0], float), float(obstacle[1])
    rng = rng if rng is not None else _np.random.default_rng(0)
    return reference_trajectory_layer(q_start, q_goal, center, radius,
                                      vlim, alim, rng, **plan_kw)


# Default greenhouse controller gains (tuned in Module 8 for the simulated joints).
DEFAULT_GAINS = (25.0, 12.0, 5.0)


def execute_reference(layer, gains=DEFAULT_GAINS, ff="full", dt=0.002,
                      load=2.0, load_comp=None, disturbance=None, n_joints=2,
                      telemetry=False):
    """
    Execute stage (Unit 4): drive a planned REFERENCE into real joint MOTION by
    tracking it closed-loop with the REAL Module 8 control layer against simulated
    joint plants. Returns a per-joint execution record:
        {t, q, q_d, error, rms, final_error, reached}.

    Pure coordination over the wrapped layers: it samples layer['reference'](t)
    (Module 7), feeds each sample to a tracking_controller (Module 8 control_layer),
    and steps the Joint plant (Module 8). It introduces NO new control law; the loop
    itself is the Execute stage's job (Module 9). `disturbance(t, joint) -> float`
    optionally perturbs a joint (used by the failure-injection lessons later).
    `load_comp` is the feed-forward load compensation; if None it matches the plant
    load (as in the Module 8 capstone), so a healthy run tracks tightly.

    With telemetry=True the record also carries health signals collected from the
    EXISTING layer outputs (no new theory): per-tick control effort `u`, a
    `saturated` flag (requested != delivered effort, from the M8 actuator), and the
    Jacobian-based manipulability `w` (= product of singular values, the M6
    convention) and `sigma_min`. These are the signals the Track and Failure-
    Detection stages read.
    """
    ref = layer["reference"]
    T = layer["duration"]
    n = int(round(T / dt)) + 1
    ts = _np.linspace(0, T, n)
    q0, _, _, _ = ref(0.0)
    n_joints = len(q0)
    lc = load if load_comp is None else load_comp
    controllers = [control_layer(gains, ff=ff, load_comp=lc) for _ in range(n_joints)]
    plants = [Joint(load=load) for _ in range(n_joints)]
    for j in range(n_joints):
        plants[j].reset(q0=float(q0[j]), qd0=0.0)
        controllers[j].reset()
    Q = _np.zeros((n, n_joints)); QD = _np.zeros((n, n_joints)); E = _np.zeros((n, n_joints))
    U = _np.zeros((n, n_joints)); SAT = _np.zeros(n, dtype=bool)
    W = _np.zeros(n); SIGMIN = _np.zeros(n)
    for i, ti in enumerate(ts):
        q_d, qd_d, qdd_d, _ = ref(ti)
        if telemetry:
            q_now = _np.array([plants[j].q for j in range(n_joints)])
            sv = _np.linalg.svd(geometric_jacobian(P2, T2, q_now)[:2, :], compute_uv=False)
            W[i] = float(_np.prod(sv)); SIGMIN[i] = float(sv.min())
        sat_tick = False
        for j in range(n_joints):
            Q[i, j] = plants[j].q
            QD[i, j] = q_d[j]
            E[i, j] = q_d[j] - plants[j].q
            u, info = controllers[j]((q_d[j], qd_d[j], qdd_d[j]),
                                     (plants[j].q, plants[j].qd), dt)
            U[i, j] = info["u_del"]
            if abs(info["u_req"] - info["u_del"]) > 1e-9:
                sat_tick = True
            if i < n - 1:
                extra = 0.0 if disturbance is None else float(disturbance(ti, j))
                step_plant(plants[j], u, dt, extra_disturbance=extra)
        SAT[i] = sat_tick
    final_err = _np.array([abs(E[-1, j]) for j in range(n_joints)])
    rms = float(_np.sqrt(_np.mean(E ** 2)))
    rec = {"t": ts, "q": Q, "q_d": QD, "error": E, "rms": rms,
           "final_error": final_err, "reached": bool(_np.all(final_err < 0.05))}
    if telemetry:
        rec.update({"u": U, "saturated": SAT, "w": W, "sigma_min": SIGMIN})
    return rec


# Default Track-stage success criteria (integration thresholds, not new theory).
TRACK_TOL_RMS = 0.02
TRACK_TOL_FINAL = 0.05


def track(record, target=None, tool_xy=None, tol_rms=TRACK_TOL_RMS,
          tol_final=TRACK_TOL_FINAL, tol_pose=0.01):
    """
    Track stage (Unit 5): JUDGE the executed motion against success criteria by
    reading Execute's output — it adds no control, it decides whether the run
    succeeded. Returns a verdict:
        {success, reached, rms, final_error_max, criteria, reason}.

    Criteria (all reusing existing signals): the per-joint final error is within
    tol_final, the tracking RMS is within tol_rms, and (if a target pose is given)
    the executed tool position is within tol_pose of the target. `success` is the
    conjunction; `reason` localises the first criterion that failed. The Track stage
    OWNS this judgement; the controller (M8) only produced the motion.
    """
    fe = float(_np.max(record["final_error"]))
    rms = float(record["rms"])
    crit = {"final_error": fe <= tol_final, "rms": rms <= tol_rms}
    pose_err = None
    if target is not None:
        xy = target["xy"] if isinstance(target, dict) else _np.asarray(target, float)
        if tool_xy is None:
            tool_xy = fk_xy(P2, T2, record["q"][-1])
        pose_err = float(_np.linalg.norm(_np.asarray(tool_xy, float) - xy))
        crit["pose"] = pose_err <= tol_pose
    success = all(crit.values())
    reason = "ok" if success else next(k for k, v in crit.items() if not v)
    return {"success": success, "reached": bool(record["reached"]),
            "rms": rms, "final_error_max": fe, "pose_error": pose_err,
            "criteria": crit, "reason": reason}


def system_monitor(record):
    """
    System monitoring (Unit 5): summarise a telemetry-enabled execution record into
    system-level HEALTH SIGNALS, reading only what the layers already emit. Returns:
        {peak_error, rms, final_error_max, min_manipulability, min_sigma_min,
         peak_effort, saturation_fraction, samples}.

    This is observation, not control — the dashboard the Track and Failure-Detection
    stages read. Requires execute_reference(..., telemetry=True).
    """
    if "u" not in record:
        raise ValueError("system_monitor needs telemetry=True execution record")
    E = record["error"]
    return {
        "samples": int(E.shape[0]),
        "peak_error": float(_np.max(_np.abs(E))),
        "rms": float(record["rms"]),
        "final_error_max": float(_np.max(record["final_error"])),
        "min_manipulability": float(_np.min(record["w"])),
        "min_sigma_min": float(_np.min(record["sigma_min"])),
        "peak_effort": float(_np.max(_np.abs(record["u"]))),
        "saturation_fraction": float(_np.mean(record["saturated"])),
    }


# ---------------------------------------------------------------------------
# Unit 6 — Failure Detection (integration events; reads existing outputs only).
# The taxonomy is integration-focused: each event is a known telemetry/verdict
# condition crossing a line, tagged with the three questions the Architect's
# sequence asks BEFORE recovery: what failed, where, who owns the fix. No
# estimation, fault-diagnosis, or control theory is introduced.
# ---------------------------------------------------------------------------
FAILURE_TAXONOMY = {
    "NO_TARGET": dict(
        what="No committable target",
        where="Understand",
        who="Perceive / Understand (re-perceive or widen search)",
        signal="understand() committed nothing (no ripe, reachable detection)"),
    "UNREACHABLE": dict(
        what="Target pose unreachable",
        where="Understand \u2192 Plan (IK seam)",
        who="Understand (re-select a reachable target)",
        signal="to_configuration() returned None"),
    "PLAN_INVALID": dict(
        what="No valid plan to the goal",
        where="Plan",
        who="Plan (replan / relax limits) or Recover",
        signal="reference layer validated == False"),
    "TRACKING_FAILURE": dict(
        what="Execution missed the success criteria",
        where="Execute \u2192 Track",
        who="Execute / Recover",
        signal="Track verdict success == False"),
    "NEAR_SINGULAR": dict(
        what="Planned path passed near a singularity (fragile)",
        where="Execute (geometry of the planned path)",
        who="Plan (re-path) / Track (flag)",
        signal="min manipulability below threshold"),
    "EXCESS_EFFORT": dict(
        what="Controller effort abnormally high",
        where="Execute",
        who="Execute / Plan",
        signal="peak control effort above threshold (disturbance or saturation)"),
}

# Health-guard thresholds (integration choices on existing signals, not new theory).
DETECT_THRESHOLDS = dict(min_manipulability=0.03, peak_effort=30.0)


def failure_event(code, severity="failure", detail=None):
    """Build a failure event from the taxonomy, tagged with severity and optional detail.
    severity: 'failure' (the run failed) or 'warning' (health flag; run may have succeeded)."""
    ev = dict(FAILURE_TAXONOMY[code]); ev.update(code=code, severity=severity)
    if detail is not None:
        ev["detail"] = detail
    return ev


def localize(event):
    """Format an event as the three-question fault-localisation triad (Unit 6's
    discipline, BEFORE recovery): what failed, where, who owns the fix."""
    return ("What failed?  %s\nWhere did it fail?  %s\nWho owns the fix?  %s"
            % (event["what"], event["where"], event["who"]))


def run_pipeline(world, q_start, disturbance=None, perception=None, obstacle=None,
                 rng_seed=7, thresholds=None, target=None):
    """
    Run the forward path (Perceive \u2192 Understand \u2192 Plan \u2192 Execute \u2192 Track) with a
    DETECTION GUARD at each stage, returning the outcome plus a list of failure
    events. Every guard reads an EXISTING output (understand's commit, the IK
    seam's None, the planner's validated flag, the Track verdict, the telemetry
    dashboard) — no new theory. The pipeline STOPS at the first hard failure (a
    stage whose output the next stage cannot consume) and localises it; a completed
    run is judged and health-screened. Recovery is NOT performed here (that is
    Unit 7) — this only detects and localises.

    `perception` is a kwargs dict for model_perception (e.g. occlude / noise /
    duplicate) so failures can be injected. If `target` is supplied, the
    Perceive+Understand front end is skipped and the run drives that committed
    target (this is the seam the Unit 7 orchestrator uses to pick a chosen fruit).
    Returns:
        {reached, events, success, target, q_goal, layer, record, verdict, monitor}
    """
    th = dict(DETECT_THRESHOLDS)
    if thresholds:
        th.update(thresholds)
    events = []
    out = {"reached": None, "events": events, "success": False, "target": None,
           "q_goal": None, "layer": None, "record": None, "verdict": None,
           "monitor": None}

    # Perceive + Understand --------------------------------------------------
    if target is None:
        pk = perception or {}
        dets = model_perception(world, rng=_np.random.default_rng(rng_seed), **pk)
        _, target = understand(dets, world)
        out["reached"] = "Understand"
        if target is None:
            out["target"] = None
            events.append(failure_event("NO_TARGET"))
            return out
    out["target"] = target
    if out["reached"] is None:
        out["reached"] = "Understand"

    # Understand -> Plan (IK seam) -------------------------------------------
    q_goal = to_configuration(target)
    out["q_goal"] = q_goal
    out["reached"] = "Plan(IK)"
    if q_goal is None:
        events.append(failure_event("UNREACHABLE", detail=target.get("id")))
        return out

    # Plan -------------------------------------------------------------------
    layer = plan_reference(q_start, q_goal, obstacle=obstacle,
                           rng=_np.random.default_rng(0))
    out["layer"] = layer
    out["reached"] = "Plan"
    if not layer["validated"]:
        events.append(failure_event("PLAN_INVALID"))
        return out

    # Execute + Track + health screen ----------------------------------------
    rec = execute_reference(layer, disturbance=disturbance, telemetry=True)
    verdict = track(rec, target=target)
    mon = system_monitor(rec)
    out.update(record=rec, verdict=verdict, monitor=mon, reached="Track")
    if not verdict["success"]:
        events.append(failure_event("TRACKING_FAILURE", detail=verdict["reason"]))
    if mon["min_manipulability"] < th["min_manipulability"]:
        events.append(failure_event("NEAR_SINGULAR", severity="warning",
                                     detail=round(mon["min_manipulability"], 4)))
    if mon["peak_effort"] > th["peak_effort"]:
        events.append(failure_event("EXCESS_EFFORT", severity="warning",
                                     detail=round(mon["peak_effort"], 2)))
    out["success"] = verdict["success"] and not any(
        e["severity"] == "failure" for e in events)
    return out


# ---------------------------------------------------------------------------
# Unit 7 — Recover (the orchestrator). PURE COORDINATION on top of the existing
# layers and the Unit-6 detection signals. The recovery for a fault is an
# EXISTING layer call re-invoked (re-perceive, retry-execute) or the target
# advanced/skipped — never a new estimator, planner, or controller. The policy
# distinguishes retryable (transient) faults from deterministic ones, and a
# retry budget with state across attempts stops looping faults from spinning.
# ---------------------------------------------------------------------------
RECOVERY_POLICY = {
    # event           response            retryable  owner
    "NO_TARGET":        dict(response="re-perceive",       retryable=True,
                             owner="Perceive / Understand"),
    "TRACKING_FAILURE": dict(response="retry-execute",     retryable=True,
                             owner="Execute"),
    "UNREACHABLE":      dict(response="re-select-target",  retryable=False,
                             owner="Understand"),
    "PLAN_INVALID":     dict(response="skip-target",       retryable=False,
                             owner="Plan"),
}


def _resolve(spec, attempt):
    """A fault injector may be static OR a callable of the attempt index, so a
    fault can be transient (clears on a later attempt) or persistent. This is how
    the orchestrator's re-tries are honest: retrying only helps a transient fault."""
    return spec(attempt) if callable(spec) else spec


def recover(world, q_start, perception=None, disturbance=None, obstacle=None,
            max_attempts=3, rng_seed=7, thresholds=None, target=None):
    """
    Recover stage (Unit 7): coordinate the forward path under failure. Runs the
    guarded pipeline (run_pipeline); on a hard failure it localises the fault,
    looks up a TARGETED response in RECOVERY_POLICY keyed by the fired event, and:

      * retryable fault (NO_TARGET -> re-perceive, TRACKING_FAILURE -> retry-execute):
        re-attempt, up to max_attempts. A transient fault clears and the cycle
        recovers; a persistent one exhausts the budget and ESCALATES.
      * deterministic fault (UNREACHABLE, PLAN_INVALID): retrying the same goal is
        pointless, so escalate immediately (skip / re-select).

    State is carried across attempts (the attempt log and counter), which is what
    prevents a looping fault from spinning forever. Returns:
        {success, recovered, escalated, n_attempts, attempts[], final_event,
         target, record}.
    `perception` / `obstacle` may be a static value or a callable of the attempt
    index; `disturbance` (being itself a callable) is always an attempt-provider:
    `attempt -> ((t, joint) -> float)` or None, so a persistent disturbance is
    `lambda a: kick` and a transient one `lambda a: kick if a == 0 else None`.
    NO new estimation / planning / control theory is introduced — every response
    is an existing layer call re-invoked.
    """
    attempts = []
    last = None
    for attempt in range(max_attempts):
        pk = _resolve(perception, attempt)
        dist = _resolve(disturbance, attempt)
        obs = _resolve(obstacle, attempt)
        # re-perceive across attempts by advancing the perception frame seed
        r = run_pipeline(world, q_start, disturbance=dist, perception=pk,
                         obstacle=obs, rng_seed=rng_seed + attempt,
                         thresholds=thresholds, target=target)
        last = r
        if r["success"]:
            return {"success": True, "recovered": attempt > 0, "escalated": False,
                    "n_attempts": attempt + 1, "attempts": attempts,
                    "final_event": None, "target": r["target"], "record": r}
        ev = next((e for e in r["events"] if e["severity"] == "failure"), None)
        pol = RECOVERY_POLICY.get(ev["code"]) if ev else None
        attempts.append({"attempt": attempt, "event": ev["code"] if ev else None,
                         "where": r["reached"],
                         "owner": pol["owner"] if pol else None,
                         "response": pol["response"] if pol else None,
                         "retryable": bool(pol and pol["retryable"])})
        if not pol or not pol["retryable"]:
            # deterministic fault: do not loop — escalate (skip / re-select)
            return {"success": False, "recovered": False, "escalated": True,
                    "n_attempts": attempt + 1, "attempts": attempts,
                    "final_event": ev["code"] if ev else None,
                    "target": r["target"], "record": r,
                    "escalation": "skip-target"}
        # retryable: loop to the next attempt
    # budget exhausted on a retryable (persistent) fault
    last_ev = attempts[-1]["event"] if attempts else None
    return {"success": False, "recovered": False, "escalated": True,
            "n_attempts": max_attempts, "attempts": attempts,
            "final_event": last_ev, "target": last["target"] if last else None,
            "record": last, "escalation": "retry-budget-exhausted"}


def harvest_row(world, max_attempts=3, inject=None, rng_seed=7, thresholds=None,
                max_picks=64):
    """
    Full System Integration (Unit 8): run the COMPLETE self-healing pick cycle
    across a whole ROW of fruit. This is the top-level orchestrator and the whole
    of Module 9 in one call: it perceives the scene, chooses the next ripe,
    reachable target (Understand), drives that target through the recovering pick
    cycle (recover, Unit 7 -> Plan, Execute, Track, Detect, Recover), and keeps a
    ledger so each fruit is attempted once and the harvest terminates.

    A fruit that is picked is recorded as HARVESTED and removed from re-selection;
    a fruit whose recovery escalates is recorded as SKIPPED (with its fault) and
    also excluded, so one stubborn fruit never stalls the row. Pure coordination
    over the existing stages + recovery -- NO new estimation, planning, or control
    theory. `inject` maps a fruit id -> a per-target fault spec with any of
    {disturbance, obstacle, perception} (each static or attempt-aware, as in
    recover), so a single failure can be injected mid-row and watched to recover or
    be skipped while the rest of the row harvests cleanly. Returns:
        {harvested:[ids], skipped:[ids], n_picks, picks:[...], row_size, complete}.
    """
    inject = inject or {}
    harvested = []
    skipped = []
    picks = []
    complete = False
    for step in range(max_picks):
        excluded = set(harvested) | set(skipped)
        dets = model_perception(world, rng=_np.random.default_rng(rng_seed + step))
        avail = [d for d in dets if d["id"] not in excluded]
        _, target = understand(avail, world)
        if target is None:
            complete = True
            break  # row complete: nothing ripe + reachable remains
        tid = target["id"]
        spec = inject.get(tid, {})
        res = recover(world, world.q.copy(), target=target,
                      max_attempts=max_attempts,
                      disturbance=spec.get("disturbance"),
                      obstacle=spec.get("obstacle"),
                      perception=spec.get("perception"),
                      rng_seed=rng_seed + step, thresholds=thresholds)
        if res["success"]:
            harvested.append(tid)
            picks.append({"target": tid, "outcome": "harvested",
                          "n_attempts": res["n_attempts"],
                          "recovered": res["recovered"]})
        else:
            skipped.append(tid)
            picks.append({"target": tid, "outcome": "skipped",
                          "n_attempts": res["n_attempts"],
                          "fault": res.get("final_event"),
                          "escalation": res.get("escalation")})
    return {"harvested": harvested, "skipped": skipped,
            "n_picks": len(picks), "picks": picks,
            "row_size": len(world.fruit), "complete": complete}
