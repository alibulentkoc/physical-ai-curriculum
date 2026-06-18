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

