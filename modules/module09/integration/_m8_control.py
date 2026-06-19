"""
_m8_control.py — Module 8 control layer, REUSED VERBATIM.

Vendored copy of the Module 8 capstone control stack
(`modules/module08/notebooks/lesson32_capstone_closed_loop.ipynb`), reproduced
unchanged so the Module 9 adapter can WRAP the controller without REDEFINING it
("Wrap. Do not redefine."). Only the notebook's own demo/test cell was dropped.

Public surface Module 9 wraps:
    control_layer(gains, ff="full", ...) -> tracking_controller(reference_sample,
        measured_state, dt) -> (actuator_command, info), with .reset()
    Joint(...)        — the simulated single-joint plant (integrator + disturbance
                        + saturation; NO formal dynamics, per the M8 scope fence)
    step_plant(...)   — advance the plant one tick

Scope fence inherited from Module 8: no formal manipulator dynamics, no Laplace /
transfer functions; dynamics appears only as disturbance/load/friction/saturation.
"""
# --- Module 8 engine (embedded; Installment D adds real-time execution + the control stack/capstone) ---
"""
Module 8 engine — Feedback Control and Real-Time Execution.
Installment A scope (Units 1-2): the simulated plant, the Module 7 reference handoff,
open-loop vs closed-loop simulation, tracking error, and P / I / D / PID control.

Boundaries (architect rulings): NO formal manipulator dynamics, NO Laplace/transfer
functions. Dynamics enters only as disturbance/load/friction/saturation/model-mismatch
intuition. The plant is an integrator + disturbance + saturation model (per joint).
The controller consumes the Module 7 reference (q_d, qd_d, qdd_d).
"""
import numpy as np


# ---------------------------------------------------------------------------
# The Module 7 handoff: a reference(t) -> (q_d, qd_d, qdd_d).
# A rest-to-rest quintic, the SAME shape Module 7's reference_trajectory_layer emits.
# (Self-contained here so Module 8 notebooks can track a real M7-style reference.)
# ---------------------------------------------------------------------------
def quintic_reference(q0, qf, T):
    """Return ref(t) -> (q_d, qd_d, qdd_d) for a rest-to-rest quintic on one joint.
    This stands in for Module 7's reference layer: position + velocity + acceleration
    feed-forward, continuous, feasible."""
    q0, qf, T = float(q0), float(qf), float(T)
    def ref(t):
        t = min(max(t, 0.0), T)
        s = t / T
        S   = 10*s**3 - 15*s**4 + 6*s**5
        Sd  = (30*s**2 - 60*s**3 + 30*s**4) / T
        Sdd = (60*s - 180*s**2 + 120*s**3) / (T*T)
        return q0 + (qf-q0)*S, (qf-q0)*Sd, (qf-q0)*Sdd
    return ref, T


def setpoint_reference(q_target):
    """A constant setpoint reference (step target): q_d = q_target, qd_d = qdd_d = 0.
    Used for classic step-response intuition (P/I/D behaviour)."""
    q_target = float(q_target)
    def ref(t):
        return q_target, 0.0, 0.0
    return ref


# ---------------------------------------------------------------------------
# The simulated plant: a single joint as an integrator + disturbance + saturation.
#   m q'' = sat(u, u_max) - b q' - load            (load = gravity-like constant)
# No formal dynamics: m is an effective inertia, b a viscous-friction coefficient,
# load a constant gravity-like disturbance, u_max the actuator saturation limit.
# ---------------------------------------------------------------------------
class Joint:
    def __init__(self, m=0.5, b=0.8, load=2.0, u_max=20.0, q0=0.0, qd0=0.0):
        self.m, self.b, self.load, self.u_max = float(m), float(b), float(load), float(u_max)
        self.q, self.qd = float(q0), float(qd0)

    def saturate(self, u):
        return float(np.clip(u, -self.u_max, self.u_max))

    def step(self, u, dt, extra_disturbance=0.0):
        """Advance one timestep with semi-implicit Euler (stable). Returns applied (saturated) command."""
        u_app = self.saturate(u)
        qdd = (u_app - self.b*self.qd - self.load - extra_disturbance) / self.m
        self.qd += dt * qdd
        self.q  += dt * self.qd
        return u_app

    def reset(self, q0=0.0, qd0=0.0):
        self.q, self.qd = float(q0), float(qd0)


# ---------------------------------------------------------------------------
# Controllers: built up across Unit 2 (P -> PI -> PID). Stateful for I and D.
# ---------------------------------------------------------------------------
class PIDController:
    """A single-joint PID controller. Set Ki=0 for P/PD, Kd=0 for P/PI, etc.
    error e = q_d - q. Derivative is on the error (de/dt). Integral has optional
    anti-windup clamp. Feed-forward (u_ff) is accepted but only USED when use_ff=True
    (feed-forward + feedback is the Unit 4 theme; here it lets Unit 1 show open-loop)."""
    def __init__(self, Kp=0.0, Ki=0.0, Kd=0.0, i_clamp=None):
        self.Kp, self.Ki, self.Kd = float(Kp), float(Ki), float(Kd)
        self.i_clamp = i_clamp
        self.ei = 0.0
        self.e_prev = None

    def reset(self):
        self.ei = 0.0
        self.e_prev = None

    def command(self, q_d, q, dt, qd=None, qd_d=0.0):
        """Return the feedback control command for error e = q_d - q."""
        e = q_d - q
        # integral with anti-windup clamp
        self.ei += e * dt
        if self.i_clamp is not None:
            self.ei = float(np.clip(self.ei, -self.i_clamp, self.i_clamp))
        # derivative on error
        if self.e_prev is None:
            ed = 0.0
        else:
            ed = (e - self.e_prev) / dt
        self.e_prev = e
        return self.Kp*e + self.Ki*self.ei + self.Kd*ed


def p_command(q_d, q, Kp):
    """Stateless proportional command."""
    return Kp * (q_d - q)


# ---------------------------------------------------------------------------
# Feed-forward (inverse-model) command from the Module 7 reference.
# Open-loop = feed-forward ONLY (no measurement). It tracks only with a perfect model
# and no disturbance; the real plant has load/friction/model-mismatch, so it DRIFTS.
# This is the "experience why feedback is necessary" demonstration.
# ---------------------------------------------------------------------------
def feedforward_command(qdd_d, m_nominal, load_comp=0.0):
    """Nominal inverse-model command: u = m_nominal * qdd_d (+ optional load compensation)."""
    return m_nominal * qdd_d + load_comp


# ---------------------------------------------------------------------------
# Simulation drivers: open-loop vs closed-loop. The core Unit-1 contrast.
# ---------------------------------------------------------------------------
def simulate_open_loop(ref, plant, T, dt=0.002, m_nominal=None, load_comp=0.0,
                       extra_disturbance=lambda t: 0.0):
    """Open-loop: command the plant from the reference's feed-forward ONLY (no feedback).
    With model mismatch or disturbance, the actual trajectory drifts from q_d."""
    if m_nominal is None:
        m_nominal = plant.m
    plant.reset(q0=ref(0.0)[0], qd0=0.0)
    n = int(round(T/dt)) + 1
    t = np.linspace(0, T, n)
    Q = np.zeros(n); Qd_des = np.zeros(n); U = np.zeros(n); E = np.zeros(n)
    for i, ti in enumerate(t):
        q_d, qd_d, qdd_d = ref(ti)
        Q[i] = plant.q; Qd_des[i] = q_d; E[i] = q_d - plant.q
        u = feedforward_command(qdd_d, m_nominal, load_comp)
        if i < n-1:
            U[i] = plant.step(u, dt, extra_disturbance(ti))
    return {"t": t, "q": Q, "q_d": Qd_des, "error": E, "u": U}


def simulate_closed_loop(ref, plant, controller, T, dt=0.002,
                         use_ff=False, m_nominal=None, load_comp=0.0,
                         extra_disturbance=lambda t: 0.0):
    """Closed-loop: measure q, compute error, correct with the controller (optionally +
    feed-forward). Rejects disturbance/model-mismatch and tracks the reference."""
    if m_nominal is None:
        m_nominal = plant.m
    plant.reset(q0=ref(0.0)[0], qd0=0.0)
    controller.reset()
    n = int(round(T/dt)) + 1
    t = np.linspace(0, T, n)
    Q = np.zeros(n); Qd_des = np.zeros(n); U = np.zeros(n); E = np.zeros(n)
    for i, ti in enumerate(t):
        q_d, qd_d, qdd_d = ref(ti)
        Q[i] = plant.q; Qd_des[i] = q_d; E[i] = q_d - plant.q
        u_fb = controller.command(q_d, plant.q, dt, qd=plant.qd, qd_d=qd_d)
        u = u_fb + (feedforward_command(qdd_d, m_nominal, load_comp) if use_ff else 0.0)
        if i < n-1:
            U[i] = plant.step(u, dt, extra_disturbance(ti))
    return {"t": t, "q": Q, "q_d": Qd_des, "error": E, "u": U}


# ---------------------------------------------------------------------------
# Response & stability tooling (qualitative, per the ruling — no formal analysis).
# ---------------------------------------------------------------------------
def step_response_metrics(t, q, q_target, q0=0.0, settle_band=0.02):
    """Overshoot (%), settling time (to within settle_band of the target span),
    rise time (10->90%), and steady-state error. Qualitative response shape only."""
    q = np.asarray(q, float); t = np.asarray(t, float)
    span = q_target - q0
    ss = q[-1]
    ss_error = q_target - ss
    # overshoot
    if abs(span) > 1e-12:
        peak = np.max(q) if span > 0 else np.min(q)
        overshoot = max(0.0, (peak - q_target)/span) * 100.0
    else:
        overshoot = 0.0
    # settling time: last time it leaves the band around the target
    band = abs(settle_band * (span if abs(span) > 1e-9 else 1.0))
    outside = np.where(np.abs(q - q_target) > band)[0]
    settling_time = float(t[outside[-1]]) if len(outside) else 0.0
    # rise time 10->90%
    rise_time = float("nan")
    if abs(span) > 1e-9:
        lo, hi = q0 + 0.1*span, q0 + 0.9*span
        try:
            i_lo = np.where((q-q0)/span >= 0.1)[0][0]
            i_hi = np.where((q-q0)/span >= 0.9)[0][0]
            rise_time = float(t[i_hi] - t[i_lo])
        except IndexError:
            pass
    return {"overshoot_pct": float(overshoot), "settling_time": settling_time,
            "rise_time": rise_time, "steady_state_error": float(ss_error)}


def classify_stability(q, tail_frac=0.3):
    """Qualitative: 'stable' (settles), 'marginal' (sustained oscillation), or
    'unstable' (diverges). Based on the envelope of the response, not poles."""
    q = np.asarray(q, float)
    if not np.all(np.isfinite(q)) or np.max(np.abs(q)) > 1e6:
        return "unstable"
    n = len(q); k = max(4, int(n*tail_frac))
    early = q[:k]; late = q[-k:]
    early_amp = np.max(early) - np.min(early)
    late_amp = np.max(late) - np.min(late)
    if late_amp > 1.2*early_amp + 1e-6:
        return "unstable"          # growing oscillation
    if late_amp < 0.1*early_amp + 1e-6:
        return "stable"            # decayed to ~constant
    return "marginal"              # sustained oscillation


def tracking_rms(error):
    """RMS tracking error of a run."""
    e = np.asarray(error, float)
    return float(np.sqrt(np.mean(e**2)))


# ===========================================================================
# Installment B extensions (additive):
#   Unit 3 — stability / response / tuning (latency, behavior classification)
#   Unit 4 — feed-forward + feedback whole-arm tracking
# All existing Installment-A functions are unchanged.
# ===========================================================================

def feedforward_full(qd_d, qdd_d, m_nominal, b_nominal, load_comp=0.0):
    """Full inverse-model feed-forward from the Module 7 reference: anticipates BOTH
    the acceleration (inertia term m*q̈_d) and the velocity (damping term b*q̇_d), plus
    known load. Consumes q̇_d AND q̈_d — the Unit 4 'anticipation' command."""
    return m_nominal*qdd_d + b_nominal*qd_d + load_comp


def track_reference(ref, plant, controller, T, dt=0.002, ff="none",
                    m_nominal=None, b_nominal=None, load_comp=0.0,
                    extra_disturbance=lambda t: 0.0, sensor_delay_steps=0):
    """Track a Module-7-style reference(t) -> (q_d, q̇_d, q̈_d) on one joint.
      ff: 'none' (feedback only) | 'accel' (m*q̈_d) | 'full' (m*q̈_d + b*q̇_d + load_comp).
      sensor_delay_steps: delay (in steps) of the measurement fed to the controller (latency).
    Plant starts matched to the reference start, ref(0)[0]."""
    if m_nominal is None: m_nominal = plant.m
    if b_nominal is None: b_nominal = plant.b
    plant.reset(q0=ref(0.0)[0], qd0=0.0); controller.reset()
    n = int(round(T/dt)) + 1; t = np.linspace(0, T, n)
    Q=np.zeros(n); QdD=np.zeros(n); QddD=np.zeros(n); Qdes=np.zeros(n); E=np.zeros(n); U=np.zeros(n)
    hist = [plant.q]*(sensor_delay_steps+1)
    for i, ti in enumerate(t):
        q_d, qd_d, qdd_d = ref(ti)
        q_meas = hist[len(hist)-1-sensor_delay_steps]
        Q[i]=plant.q; Qdes[i]=q_d; QdD[i]=qd_d; QddD[i]=qdd_d; E[i]=q_d-plant.q
        u_fb = controller.command(q_d, q_meas, dt)
        if   ff=="accel": u_ff = feedforward_command(qdd_d, m_nominal, load_comp)
        elif ff=="full":  u_ff = feedforward_full(qd_d, qdd_d, m_nominal, b_nominal, load_comp)
        else:             u_ff = 0.0
        if i < n-1:
            U[i] = plant.step(u_fb + u_ff, dt, extra_disturbance(ti))
            hist.append(plant.q)
    return {"t":t, "q":Q, "q_d":Qdes, "qd_d":QdD, "qdd_d":QddD, "error":E, "u":U}


class JointTracker:
    """Unit-4 multi-joint tracking controller: one PID per joint + an optional feed-forward
    mode. Joints are treated independently (no cross-coupling — within the dynamics boundary).
    Precursor to the Module 8 capstone tracking_controller."""
    def __init__(self, gains, ff="full"):
        self.controllers = [PIDController(*g) for g in gains]
        self.ff = ff
    def reset(self):
        for c in self.controllers: c.reset()
    def command(self, refs_t, q_meas, dt, m_nom, b_nom, load_comp=0.0):
        out = []
        for c, (q_d, qd_d, qdd_d), qm, mj, bj in zip(self.controllers, refs_t, q_meas, m_nom, b_nom):
            u_fb = c.command(q_d, qm, dt)
            if   self.ff=="accel": u_ff = feedforward_command(qdd_d, mj, load_comp)
            elif self.ff=="full":  u_ff = feedforward_full(qd_d, qdd_d, mj, bj, load_comp)
            else:                  u_ff = 0.0
            out.append(u_fb + u_ff)
        return out


def multi_quintic(specs, T):
    """specs: list of (q0, qf) per joint -> list of ref(t) -> (q_d, q̇_d, q̈_d)."""
    return [quintic_reference(q0, qf, T)[0] for (q0, qf) in specs]


def track_arm(refs, plants, tracker, T, dt=0.002, load_comp=0.0,
              extra_disturbance=lambda t, j: 0.0):
    """Track an N-joint reference with a JointTracker. Returns per-joint q/q_d/error and
    the overall RMS tracking error across all joints."""
    N = len(plants)
    for j in range(N): plants[j].reset(q0=refs[j](0.0)[0], qd0=0.0)
    tracker.reset()
    m_nom = [p.m for p in plants]; b_nom = [p.b for p in plants]
    n = int(round(T/dt)) + 1; t = np.linspace(0, T, n)
    Q=[np.zeros(n) for _ in range(N)]; Qd=[np.zeros(n) for _ in range(N)]; E=[np.zeros(n) for _ in range(N)]
    for i, ti in enumerate(t):
        refs_t = [refs[j](ti) for j in range(N)]
        q_meas = [plants[j].q for j in range(N)]
        for j in range(N):
            Q[j][i]=plants[j].q; Qd[j][i]=refs_t[j][0]; E[j][i]=refs_t[j][0]-plants[j].q
        u = tracker.command(refs_t, q_meas, dt, m_nom, b_nom, load_comp)
        if i < n-1:
            for j in range(N): plants[j].step(u[j], dt, extra_disturbance(ti, j))
    allE = np.concatenate(E)
    return {"t":t, "q":Q, "q_d":Qd, "error":E, "rms":float(np.sqrt(np.mean(allE**2)))}



# ===========================================================================
# Installment C extensions (additive — every Installment-A/B function above is
# unchanged):
#   Unit 5 — Actuator Control: the request->delivery converter and its plant-level
#            nonlinearities (deadband, saturation, rate limit) + stiction; the full
#            command pipeline and the feasibility envelope (ties back to Module 7).
#   Unit 6 — Communication: a tiny in-process publish/subscribe Bus (the PATTERN,
#            not a framework), per-hop loop latency, and a finite-control-rate loop
#            that — with latency — reproduces the Unit-3 instability.
#
# Boundaries (architect rulings): NO motor electrodynamics / current loops /
# formal actuator dynamics (Unit 5 is plant-level intuition only); communication
# is the pub/sub PATTERN, not middleware (ROS 2 is the Unit-8 implementation);
# stability stays QUALITATIVE (no Laplace/transfer functions; control rate is
# "the controller acts N times per second on slightly stale information", not
# discrete-time/sampling theory).
# ===========================================================================


# ---------------------------------------------------------------------------
# Unit 5 — the actuator as a request -> delivery converter.
# ---------------------------------------------------------------------------
class Actuator:
    """A plant-level request->delivery converter. Given a REQUESTED command it
    returns the DELIVERED effort, distorted by three plant-level nonlinearities:
      - deadband : |request| <= deadband delivers 0 (tiny commands do nothing);
      - saturation: delivered effort is capped at +/- u_max (the effort ceiling);
      - rate limit: delivered effort cannot slew faster than rate_max per second.
    Models WHAT the actuator delivers, never motor internals (no current loops,
    no electrodynamics, no actuator dynamics)."""
    def __init__(self, u_max=20.0, deadband=0.0, rate_max=None):
        self.u_max = float(u_max)
        self.deadband = float(deadband)
        self.rate_max = None if rate_max is None else float(rate_max)
        self.u_prev = 0.0
        self.clipped = False        # saturation hit on the last deliver()
        self.rate_limited = False   # rate limit hit on the last deliver()

    def reset(self):
        self.u_prev = 0.0
        self.clipped = False
        self.rate_limited = False

    def _static(self, u_req):
        """Deadband + saturation only — the static transfer characteristic."""
        if abs(u_req) <= self.deadband:
            u = 0.0
        else:
            u = u_req - np.sign(u_req) * self.deadband
        return float(np.clip(u, -self.u_max, self.u_max))

    def deliver(self, u_req, dt):
        """Requested command in -> delivered effort out (deadband, saturation, slew)."""
        u = self._static(u_req)
        self.clipped = (abs(u_req) - self.deadband) > (self.u_max + 1e-9)
        self.rate_limited = False
        if self.rate_max is not None:
            du_max = self.rate_max * dt
            lo, hi = self.u_prev - du_max, self.u_prev + du_max
            if u < lo - 1e-12 or u > hi + 1e-12:
                self.rate_limited = True
            u = float(np.clip(u, lo, hi))
        self.u_prev = u
        return u

    def characteristic(self, u_grid):
        """Vectorised static requested->delivered curve (for the transfer plot)."""
        return np.array([self._static(float(u)) for u in u_grid])


def apply_stiction(net_effort, qd, stiction):
    """Plant-level static/Coulomb friction (breakaway). Returns the net forcing
    that actually accelerates the joint:
      - at (near) rest, motion begins only once |net_effort| exceeds the breakaway
        threshold `stiction`; below it the joint stays put;
      - while moving, a Coulomb friction of magnitude `stiction` opposes motion.
    Intuition-level only (no Stribeck/LuGre model)."""
    if stiction <= 0.0:
        return net_effort
    if abs(qd) < 1e-4:                                  # at rest: must break away
        if abs(net_effort) <= stiction:
            return 0.0
        return net_effort - np.sign(net_effort) * stiction
    return net_effort - np.sign(qd) * stiction          # moving: kinetic friction opposes


def step_plant(plant, u_delivered, dt, stiction=0.0, extra_disturbance=0.0):
    """Advance `plant` one step from an ALREADY-DELIVERED actuator effort, with
    optional stiction. Mirrors Joint.step's semi-implicit Euler but takes the
    delivered effort directly (the Actuator already saturated/dead-banded it) and
    adds plant-level static friction. Leaves Joint.step untouched."""
    net = u_delivered - plant.b * plant.qd - plant.load - extra_disturbance
    net = apply_stiction(net, plant.qd, stiction)
    qdd = net / plant.m
    plant.qd += dt * qdd
    plant.q  += dt * plant.qd
    return u_delivered


def track_reference_actuated(ref, plant, controller, actuator, T, dt=0.002,
                             ff="none", m_nominal=None, b_nominal=None, load_comp=0.0,
                             stiction=0.0, extra_disturbance=lambda t: 0.0,
                             sensor_delay_steps=0, control_period_steps=1):
    """Track a Module-7-style reference through the FULL command pipeline:
        reference -> controller (+ optional feed-forward) -> REQUESTED command
                  -> Actuator (deadband / saturation / rate limit) -> DELIVERED effort
                  -> plant (integrator + load + friction/stiction + disturbance).
    Communication / timing levers (Unit 6):
        sensor_delay_steps   : measurement latency (steps) fed to the controller;
        control_period_steps : the controller updates only every k steps (a finite
                               control rate); the request is held between updates
                               (zero-order hold) — "acts N times per second".
    Records requested vs delivered effort and whether the effort/rate envelope was
    hit, so a lesson can assert 'the pipeline respects the effort/rate bounds'."""
    if m_nominal is None: m_nominal = plant.m
    if b_nominal is None: b_nominal = plant.b
    plant.reset(q0=ref(0.0)[0], qd0=0.0); controller.reset(); actuator.reset()
    n = int(round(T / dt)) + 1
    t = np.linspace(0, T, n)
    Q = np.zeros(n); Qdes = np.zeros(n); E = np.zeros(n)
    Ureq = np.zeros(n); Udel = np.zeros(n)
    hist = [plant.q] * (sensor_delay_steps + 1)
    k = max(1, int(control_period_steps))
    u_req = 0.0
    clip_hits = 0; rate_hits = 0
    for i, ti in enumerate(t):
        q_d, qd_d, qdd_d = ref(ti)
        q_meas = hist[len(hist) - 1 - sensor_delay_steps]
        Q[i] = plant.q; Qdes[i] = q_d; E[i] = q_d - plant.q
        if i % k == 0:                              # finite control rate
            u_fb = controller.command(q_d, q_meas, dt * k)
            if   ff == "accel": u_ff = feedforward_command(qdd_d, m_nominal, load_comp)
            elif ff == "full":  u_ff = feedforward_full(qd_d, qdd_d, m_nominal, b_nominal, load_comp)
            else:               u_ff = 0.0
            u_req = u_fb + u_ff
        Ureq[i] = u_req
        u_del = actuator.deliver(u_req, dt)
        Udel[i] = u_del
        if actuator.clipped: clip_hits += 1
        if actuator.rate_limited: rate_hits += 1
        if i < n - 1:
            step_plant(plant, u_del, dt, stiction=stiction,
                       extra_disturbance=extra_disturbance(ti))
            hist.append(plant.q)
    return {"t": t, "q": Q, "q_d": Qdes, "error": E, "u_req": Ureq, "u_del": Udel,
            "effort_clipped": clip_hits > 0, "rate_limited": rate_hits > 0,
            "clip_frac": clip_hits / n, "rate_frac": rate_hits / n,
            "rms": float(np.sqrt(np.mean(E ** 2)))}


def feasibility_envelope(actuator):
    """The actuator's feasibility envelope: the (effort, rate) bounds the joint can
    actually deliver. A trajectory whose required effort/rate exceeds this cannot be
    TRACKED — the plant-level complement to Module 7's geometric/velocity feasibility."""
    return {"u_max": actuator.u_max,
            "rate_max": (float("inf") if actuator.rate_max is None else actuator.rate_max),
            "deadband": actuator.deadband}


# ---------------------------------------------------------------------------
# Unit 6 — communication: the loop as messages over a publish/subscribe bus.
# ---------------------------------------------------------------------------
class Bus:
    """A tiny in-process publish/subscribe broker. Independent NODES publish
    MESSAGES to named TOPICS and subscribe to the topics they need, without
    referencing one another. This is the pub/sub PATTERN — the conceptual shape
    Unit 8's ROS 2 implements — not a middleware. No networking, no rclpy."""
    def __init__(self):
        self._latest = {}
        self._subs = {}

    def subscribe(self, topic, callback):
        self._subs.setdefault(topic, []).append(callback)

    def publish(self, topic, msg):
        self._latest[topic] = msg
        for cb in self._subs.get(topic, []):
            cb(msg)

    def latest(self, topic, default=None):
        return self._latest.get(topic, default)

    def topics(self):
        return sorted(self._latest.keys())


def loop_latency(hops):
    """End-to-end loop latency = the sum of the per-hop transit/processing times
    (seconds). Each arrow of sense->compare->correct->actuate is a message that
    takes time; the loop delay is their sum. This is the PHYSICAL SOURCE of the
    delay Unit 3 treated abstractly."""
    return float(np.sum(np.asarray(list(hops), float)))


def latency_to_steps(latency_s, dt):
    """Convert a communication latency (seconds) into simulation steps of size dt."""
    return int(round(float(latency_s) / float(dt)))


def zoh_reference(ref, hold_T):
    """Wrap a reference so it only UPDATES every hold_T seconds — a slow OUTER
    planner publishing setpoints while the inner loop still runs fast. Used to show
    the outer layer tolerates a latency the inner loop cannot (Unit 6.4)."""
    hold_T = float(hold_T)
    def wrapped(t):
        tq = (int(t / hold_T)) * hold_T if hold_T > 0 else t
        return ref(tq)
    return wrapped


def run_pubsub_loop(ref, plant, controller, actuator, T, dt=0.002, bus=None,
                    ff="none", m_nominal=None, b_nominal=None, load_comp=0.0,
                    stiction=0.0, sensor_hops=(0.0,), command_hops=(0.0,),
                    extra_disturbance=lambda t: 0.0):
    """Run the control loop as MESSAGES over a Bus: a sensor node publishes
    'joint/state', the controller node subscribes and publishes 'joint/command', an
    actuator node subscribes and drives the plant. The loop runs purely through
    topics (Unit 6.1/6.2). The per-hop times (sensor_hops + command_hops) sum into a
    loop latency, realised as a measurement delay (the Unit 6.3 link to instability)."""
    if bus is None: bus = Bus()
    if m_nominal is None: m_nominal = plant.m
    if b_nominal is None: b_nominal = plant.b
    lat = loop_latency(list(sensor_hops) + list(command_hops))
    delay_steps = latency_to_steps(lat, dt)
    plant.reset(q0=ref(0.0)[0], qd0=0.0); controller.reset(); actuator.reset()
    n = int(round(T / dt)) + 1
    t = np.linspace(0, T, n)
    Q = np.zeros(n); Qdes = np.zeros(n); E = np.zeros(n); U = np.zeros(n)
    hist = [plant.q] * (delay_steps + 1)
    mailbox = {"u_req": 0.0}

    def on_state(msg):                               # controller NODE
        q_d, qd_d, qdd_d = msg["ref"]
        u_fb = controller.command(q_d, msg["q"], dt)
        if   ff == "accel": u_ff = feedforward_command(qdd_d, m_nominal, load_comp)
        elif ff == "full":  u_ff = feedforward_full(qd_d, qdd_d, m_nominal, b_nominal, load_comp)
        else:               u_ff = 0.0
        bus.publish("joint/command", {"u": u_fb + u_ff})

    def on_command(msg):                             # actuator NODE (latches request)
        mailbox["u_req"] = msg["u"]

    bus.subscribe("joint/state", on_state)
    bus.subscribe("joint/command", on_command)

    for i, ti in enumerate(t):
        q_d, qd_d, qdd_d = ref(ti)
        Q[i] = plant.q; Qdes[i] = q_d; E[i] = q_d - plant.q
        q_meas = hist[len(hist) - 1 - delay_steps]   # delayed by the loop latency
        bus.publish("joint/state", {"q": q_meas, "ref": (q_d, qd_d, qdd_d)})  # sensor NODE
        u_del = actuator.deliver(mailbox["u_req"], dt)
        U[i] = u_del
        if i < n - 1:
            step_plant(plant, u_del, dt, stiction=stiction,
                       extra_disturbance=extra_disturbance(ti))
            hist.append(plant.q)
    return {"t": t, "q": Q, "q_d": Qdes, "error": E, "u": U,
            "loop_latency": lat, "delay_steps": delay_steps, "bus": bus,
            "rms": float(np.sqrt(np.mean(E ** 2)))}


# ===========================================================================
# Installment D extensions (additive — every A/B/C function above is unchanged):
#   Unit 7 — Embedded Execution and Real-Time Control: the inner loop as a
#            PERIODIC task with bounded timing; timing jitter, overruns, and
#            missed deadlines; real-time vs best-effort execution.
#   Unit 8 — ROS 2 Integration and the Control Stack (capstone): the closed-loop
#            stack as nodes/topics; the lightweight tracker node; and the
#            CONTROL LAYER  tracking_controller(reference, measured_state) ->
#            actuator_command  — the Module 9 handoff.
#
# Boundaries (architect rulings): NO formal real-time scheduling theory
# (rate-monotonic / WCET analysis named only as out-of-scope; timing is "run
# every period, on time" — qualitative). ROS 2 is conceptual + lightweight (the
# pub/sub Bus stands in for the middleware; no rclpy). NO system integration
# beyond the control layer (that is Module 9). No formal dynamics, no advanced
# control theory.
# ===========================================================================

import random as _random


# ---------------------------------------------------------------------------
# Unit 7 — the inner loop as a periodic real-time task.
# ---------------------------------------------------------------------------
def track_reference_variable_delay(ref, plant, controller, actuator, T, dt=0.002,
                                   delay_fn=lambda i: 0, ff="none", m_nominal=None,
                                   b_nominal=None, load_comp=0.0, stiction=0.0,
                                   extra_disturbance=lambda t: 0.0):
    """Track a reference where the MEASUREMENT delay may vary per step via
    delay_fn(i) -> steps. Lets a lesson hold the AVERAGE delay fixed while changing
    the WORST-CASE (occasional spikes), to show that real-time correctness depends
    on the worst-case timing, not the average."""
    if m_nominal is None: m_nominal = plant.m
    if b_nominal is None: b_nominal = plant.b
    plant.reset(q0=ref(0.0)[0], qd0=0.0); controller.reset(); actuator.reset()
    n = int(round(T / dt)) + 1; t = np.linspace(0, T, n)
    Q = np.zeros(n); Qdes = np.zeros(n); E = np.zeros(n); U = np.zeros(n)
    hist = [plant.q]
    dmax = 0
    for i, ti in enumerate(t):
        q_d, qd_d, qdd_d = ref(ti)
        Q[i] = plant.q; Qdes[i] = q_d; E[i] = q_d - plant.q
        d = max(0, int(delay_fn(i))); dmax = max(dmax, d)
        q_meas = hist[max(0, len(hist) - 1 - d)]
        u_fb = controller.command(q_d, q_meas, dt)
        if   ff == "accel": u_ff = feedforward_command(qdd_d, m_nominal, load_comp)
        elif ff == "full":  u_ff = feedforward_full(qd_d, qdd_d, m_nominal, b_nominal, load_comp)
        else:               u_ff = 0.0
        U[i] = actuator.deliver(u_fb + u_ff, dt)
        if i < n - 1:
            step_plant(plant, U[i], dt, stiction=stiction, extra_disturbance=extra_disturbance(ti))
            hist.append(plant.q)
    return {"t": t, "q": Q, "q_d": Qdes, "error": E, "u": U,
            "rms": float(np.sqrt(np.mean(E ** 2))), "max_delay_steps": dmax}


def track_reference_rt(ref, plant, controller, actuator, T, dt=0.002,
                       period_steps=1, jitter_steps=0, overrun_prob=0.0,
                       spike_prob=0.0, spike_steps=0,
                       ff="none", m_nominal=None, b_nominal=None, load_comp=0.0,
                       stiction=0.0, extra_disturbance=lambda t: 0.0, seed=0):
    """Track a reference with a PERIODIC inner control loop subject to real-time
    imperfections:
      period_steps : the nominal control period (the loop updates every k steps);
      jitter_steps : random extra steps added to each period (timing JITTER — the
                     next update lands late by 0..jitter_steps steps);
      overrun_prob : probability a scheduled update OVERRUNS and is skipped this
                     cycle (a MISSED DEADLINE; the previous command is held);
      spike_prob/spike_steps : with prob spike_prob the NEXT interval is extended by
                     spike_steps (a RARE LONG STALL) — gives a low MEAN interval but
                     a high WORST-CASE interval, to show real-time cares about the
                     worst case, not the average.
    Deterministic (jitter=overrun=spike=0) is the 'real-time' case; the rest are the
    'best-effort' case. Returns t,q,error,rms and timing stats. Timing is qualitative
    — no scheduling formalism."""
    if m_nominal is None: m_nominal = plant.m
    if b_nominal is None: b_nominal = plant.b
    rng = _random.Random(seed)
    plant.reset(q0=ref(0.0)[0], qd0=0.0); controller.reset(); actuator.reset()
    n = int(round(T / dt)) + 1; t = np.linspace(0, T, n)
    Q = np.zeros(n); Qdes = np.zeros(n); E = np.zeros(n); U = np.zeros(n)
    u_req = 0.0; next_tick = 0
    intervals = []; misses = 0; updates = 0
    for i, ti in enumerate(t):
        q_d, qd_d, qdd_d = ref(ti)
        Q[i] = plant.q; Qdes[i] = q_d; E[i] = q_d - plant.q
        if i >= next_tick:
            jit = rng.randint(0, jitter_steps) if jitter_steps > 0 else 0
            spike = spike_steps if (spike_prob > 0.0 and rng.random() < spike_prob) else 0
            interval = max(1, period_steps + jit + spike)
            next_tick = i + interval
            if overrun_prob > 0.0 and rng.random() < overrun_prob:
                misses += 1                          # overrun → skip update, hold command
            else:
                u_fb = controller.command(q_d, plant.q, dt * period_steps)
                if   ff == "accel": u_ff = feedforward_command(qdd_d, m_nominal, load_comp)
                elif ff == "full":  u_ff = feedforward_full(qd_d, qdd_d, m_nominal, b_nominal, load_comp)
                else:               u_ff = 0.0
                u_req = u_fb + u_ff
                intervals.append(interval); updates += 1
        U[i] = actuator.deliver(u_req, dt)
        if i < n - 1:
            step_plant(plant, U[i], dt, stiction=stiction, extra_disturbance=extra_disturbance(ti))
    return {"t": t, "q": Q, "q_d": Qdes, "error": E, "u": U,
            "rms": float(np.sqrt(np.mean(E ** 2))),
            "updates": updates, "missed_deadlines": misses,
            "mean_interval_steps": float(np.mean(intervals)) if intervals else float(period_steps),
            "max_interval_steps": int(np.max(intervals)) if intervals else period_steps}


# ---------------------------------------------------------------------------
# Unit 8 — the ROS 2 control stack and the CONTROL LAYER (capstone).
# ---------------------------------------------------------------------------
def control_layer(gains, ff="full", m_nominal=0.5, b_nominal=0.8, load_comp=0.0,
                  i_clamp=None, actuator=None):
    """Build the Module 8 CONTROL LAYER: a stateful tracking_controller that maps
        (reference_sample, measured_state, dt) -> (actuator_command, info)
    where reference_sample = (q_d, qd_d, qdd_d) is one sample of Module 7's reference
    and measured_state = (q, qd) is the measured joint state. It combines feedforward
    (anticipation, consuming M7's q̇_d/q̈_d) with PID feedback (correction), passes
    the request through the actuator (delivered effort), and returns the actuator
    command. THIS IS THE MODULE 9 HANDOFF — the control layer in the chain
    velocity_layer (M6) -> reference layer (M7) -> control layer (M8) -> integration (M9).
    No system integration beyond this layer (that is Module 9)."""
    Kp, Ki, Kd = gains
    pid = PIDController(Kp, Ki, Kd, i_clamp=i_clamp)
    act = actuator if actuator is not None else Actuator(u_max=1e12)
    def tracking_controller(reference_sample, measured_state, dt):
        q_d, qd_d, qdd_d = reference_sample
        q, qd = measured_state
        u_fb = pid.command(q_d, q, dt)
        if   ff == "accel": u_ff = feedforward_command(qdd_d, m_nominal, load_comp)
        elif ff == "full":  u_ff = feedforward_full(qd_d, qdd_d, m_nominal, b_nominal, load_comp)
        else:               u_ff = 0.0
        u_req = u_fb + u_ff
        u_del = act.deliver(u_req, dt)
        return u_del, {"u_req": u_req, "u_ff": u_ff, "u_fb": u_fb, "u_del": u_del}
    def _reset():
        pid.reset(); act.reset()
    tracking_controller.reset = _reset
    return tracking_controller


def run_control_stack(ref, plant, control_fn, T, dt=0.002, bus=None,
                      sensor_hops=(0.0,), command_hops=(0.0,), stiction=0.0,
                      extra_disturbance=lambda t: 0.0):
    """Run the CLOSED-LOOP CONTROL STACK as a ROS-2-style pub/sub graph: a sensor
    node publishes 'joint/state' (carrying the measured state and the M7 reference
    sample), the CONTROL LAYER node (control_fn = a tracking_controller from
    control_layer) subscribes, computes the actuator command, and publishes
    'joint/command'; an actuator node subscribes and drives the plant. Conceptual
    ROS 2 — the Bus stands in for the middleware (no rclpy)."""
    if bus is None: bus = Bus()
    lat = loop_latency(list(sensor_hops) + list(command_hops)); delay_steps = latency_to_steps(lat, dt)
    plant.reset(q0=ref(0.0)[0], qd0=0.0)
    if hasattr(control_fn, "reset"): control_fn.reset()
    n = int(round(T / dt)) + 1; t = np.linspace(0, T, n)
    Q = np.zeros(n); Qdes = np.zeros(n); E = np.zeros(n); U = np.zeros(n)
    hist = [plant.q] * (delay_steps + 1); mailbox = {"u": 0.0}
    def on_state(msg):                                  # CONTROL LAYER node
        u, info = control_fn(msg["ref"], msg["state"], dt)
        bus.publish("joint/command", {"u": u})
    def on_cmd(msg):                                    # actuator node
        mailbox["u"] = msg["u"]
    bus.subscribe("joint/state", on_state); bus.subscribe("joint/command", on_cmd)
    for i, ti in enumerate(t):
        q_d, qd_d, qdd_d = ref(ti)
        Q[i] = plant.q; Qdes[i] = q_d; E[i] = q_d - plant.q
        q_meas = hist[len(hist) - 1 - delay_steps]
        bus.publish("joint/state", {"ref": (q_d, qd_d, qdd_d), "state": (q_meas, plant.qd)})  # sensor node
        U[i] = mailbox["u"]                             # already a delivered actuator command
        if i < n - 1:
            step_plant(plant, U[i], dt, stiction=stiction, extra_disturbance=extra_disturbance(ti))
            hist.append(plant.q)
    return {"t": t, "q": Q, "q_d": Qdes, "error": E, "u": U,
            "rms": float(np.sqrt(np.mean(E ** 2))), "loop_latency": lat, "bus": bus}


def run_arm_control_stack(refs, plants, control_fns, T, dt=0.002, stiction=0.0,
                          extra_disturbance=lambda t, j: 0.0):
    """Close the loop on an N-joint arm with one CONTROL LAYER per joint. Returns
    per-joint q/error and the overall RMS — the Module 8 closed-loop capstone on the
    planar 2-link greenhouse arm. Joints are treated independently (coupling, if
    any, is a disturbance — within the no-dynamics boundary)."""
    N = len(plants)
    for j in range(N): plants[j].reset(q0=refs[j](0.0)[0], qd0=0.0)
    for cf in control_fns:
        if hasattr(cf, "reset"): cf.reset()
    n = int(round(T / dt)) + 1; t = np.linspace(0, T, n)
    Q = [np.zeros(n) for _ in range(N)]; Qdes = [np.zeros(n) for _ in range(N)]; E = [np.zeros(n) for _ in range(N)]
    for i, ti in enumerate(t):
        for j in range(N):
            q_d, qd_d, qdd_d = refs[j](ti)
            Q[j][i] = plants[j].q; Qdes[j][i] = q_d; E[j][i] = q_d - plants[j].q
            u, info = control_fns[j]((q_d, qd_d, qdd_d), (plants[j].q, plants[j].qd), dt)
            if i < n - 1:
                step_plant(plants[j], u, dt, stiction=stiction, extra_disturbance=extra_disturbance(ti, j))
    allE = np.concatenate(E)
    return {"t": t, "q": Q, "q_d": Qdes, "error": E, "rms": float(np.sqrt(np.mean(allE ** 2)))}


import numpy as np
