"""
_m7_reference.py — Module 7 trajectory / reference layer, REUSED VERBATIM.

Vendored copy of the Module 7 capstone trajectory stack
(`modules/module07/notebooks/lesson32_capstone_harvest_cycle.ipynb`), reproduced
unchanged so the Module 9 adapter can WRAP the planner without REDEFINING it
(Architect ruling: "Wrap the real M7 planner verbatim; do not redefine it").

Public surface Module 9 wraps:
    reference_trajectory_layer(q_start, q_goal, center, radius, vlim, alim, rng, ...)
        -> dict with reference(t) -> (q_d, qd_d, qdd_d, info), duration, validation, ...

Do not edit the logic here. Constants P2/T2 are the canonical greenhouse arm
(L1=0.4, L2=0.3), matching _m6_velocity.P2. Only the notebook's own demo/test cell
was dropped; every planning function is verbatim.
"""
# --- Module 7 engine (embedded; builds on the M6 velocity layer) ---
"""
Module 7 engine - Trajectory Generation (Installment A: Units 1-2).
Builds ON the Module 6 velocity layer (imported verbatim, not reimplemented).
Greenhouse arm: planar 2R, L1=0.4, L2=0.3 (as in M5/M6); redundant 3R extension.
"""
import numpy as np

# ----- Module 6 base (reused verbatim from lesson32_capstone_velocity_layer) -----
def dh(th, d, a, al):
    ct, st, ca, sa = np.cos(th), np.sin(th), np.cos(al), np.sin(al)
    return np.array([[ct, -st*ca, st*sa, a*ct],
                     [st,  ct*ca, -ct*sa, a*st],
                     [0,      sa,     ca,   d ],
                     [0,       0,      0,   1 ]])

def forward_chain(P, T, q):
    M = np.eye(4); Ms = [M.copy()]
    for i, (th0, d0, a, al) in enumerate(P):
        th, d = (th0+q[i], d0) if T[i] == "R" else (th0, d0+q[i])
        M = M @ dh(th, d, a, al); Ms.append(M.copy())
    return Ms

def geometric_jacobian(P, T, q):
    Ms = forward_chain(P, T, q); on = Ms[-1][:3, 3]; J = np.zeros((6, len(q)))
    for i in range(len(q)):
        z = Ms[i][:3, 2]; o = Ms[i][:3, 3]
        if T[i] == "R": J[:3, i] = np.cross(z, on-o); J[3:, i] = z
        else: J[:3, i] = z
    return J

def Jv_planar(P, T, q): return geometric_jacobian(P, T, q)[:2, :]
def fk_xy(P, T, q): return forward_chain(P, T, q)[-1][:2, 3]

EPS = 0.08  # singularity threshold on sigma_min (M6 convention)

def analyze(P, T, q):
    J = Jv_planar(P, T, q); U, S, Vt = np.linalg.svd(J)
    w = float(np.prod(S)); kappa = float(S[0]/max(S[-1], 1e-12))
    return {"sigma": S, "w": w, "kappa": kappa,
            "axes": [(U[:, i], float(S[i])) for i in range(len(S))],
            "singular": bool(S[-1] < EPS), "sigma_min": float(S[-1]),
            "J": J, "U": U, "Vt": Vt}

def dls(J, lam): return J.T @ np.linalg.inv(J @ J.T + lam**2*np.eye(J.shape[0]))

def schedule_lambda(sigma_min, lam_max=0.1, eps=EPS):
    if sigma_min >= eps: return 0.0
    return float(np.sqrt((1-(sigma_min/eps)**2))*lam_max)

def velocity_layer(P, T, q, xi_d, z=None):
    """M6 deliverable: commanded tool twist -> joint rates (open-loop, singularity-robust)."""
    rep = analyze(P, T, q); lam = schedule_lambda(rep["sigma_min"])
    J = rep["J"]; Jd = dls(J, lam) if lam > 0 else np.linalg.pinv(J)
    qd = Jd @ xi_d
    if z is not None:
        qd = qd + (np.eye(len(q)) - Jd @ J) @ z
    info = {"w": rep["w"], "kappa": rep["kappa"], "sigma_min": rep["sigma_min"],
            "lambda": lam, "singular": rep["singular"]}
    return qd, info

# Canonical greenhouse arms
P2 = [(0, 0, 0.4, 0), (0, 0, 0.3, 0)]; T2 = ["R", "R"]                       # 2R, L1=0.4 L2=0.3
P3 = [(0, 0, 0.4, 0), (0, 0, 0.3, 0), (0, 0, 0.2, 0)]; T3 = ["R", "R", "R"]  # redundant 3R

# ----- Module 7 NEW: time parameterization (Units 1-2) -----
def poly_eval(c, t):
    """Evaluate ascending-coeff polynomial c=[c0..cn] and its 1st-3rd derivatives at t."""
    t = np.asarray(t, float); n = len(c)
    pos = sum(c[k]*t**k for k in range(n))
    vel = sum(k*c[k]*t**(k-1) for k in range(1, n)) if n > 1 else np.zeros_like(t)
    acc = sum(k*(k-1)*c[k]*t**(k-2) for k in range(2, n)) if n > 2 else np.zeros_like(t)
    jrk = sum(k*(k-1)*(k-2)*c[k]*t**(k-3) for k in range(3, n)) if n > 3 else np.zeros_like(t)
    return pos, vel, acc, jrk

def cubic_coeffs(q0, qf, v0, vf, T):
    """Cubic q(t) on [0,T] matching position+velocity endpoints. Ascending coeffs (C1)."""
    a0 = q0; a1 = v0
    a2 = (3*(qf-q0) - (2*v0+vf)*T) / T**2
    a3 = (2*(q0-qf) + (v0+vf)*T) / T**3
    return np.array([a0, a1, a2, a3])

def quintic_coeffs(q0, qf, v0, vf, a0, af, T):
    """Quintic q(t) on [0,T] matching position+velocity+acceleration endpoints. Ascending (C2)."""
    c0 = q0; c1 = v0; c2 = a0/2.0
    T2, T3, T4, T5 = T**2, T**3, T**4, T**5
    h = qf - q0
    c3 = (20*h - (8*vf + 12*v0)*T - (3*a0 - af)*T2) / (2*T3)
    c4 = (-30*h + (14*vf + 16*v0)*T + (3*a0 - 2*af)*T2) / (2*T4)
    c5 = (12*h - (6*vf + 6*v0)*T - (a0 - af)*T2) / (2*T5)
    return np.array([c0, c1, c2, c3, c4, c5])

def trapezoidal_profile(dist, v_max, a_max, n=400):
    """Trapezoidal velocity profile over scalar distance. Returns t, s, v, a, T_total.
    Acceleration is piecewise-constant -> discontinuous (jerk impulses at the corners)."""
    dist = float(dist); sgn = 1.0 if dist >= 0 else -1.0; D = abs(dist)
    if D == 0: t = np.linspace(0,1,n); z=np.zeros_like(t); return t,z,z,z,1.0
    t_acc = v_max / a_max
    d_acc = 0.5 * a_max * t_acc**2
    if 2*d_acc > D:                      # triangular (never reaches v_max)
        t_acc = np.sqrt(D / a_max); v_peak = a_max*t_acc; t_flat = 0.0
    else:
        v_peak = v_max; t_flat = (D - 2*d_acc) / v_max; d_acc = 0.5*a_max*t_acc**2
    Tf = 2*t_acc + t_flat
    t = np.linspace(0, Tf, n)
    s = np.zeros_like(t); v = np.zeros_like(t); a = np.zeros_like(t)
    for i, ti in enumerate(t):
        if ti < t_acc:
            a[i] = a_max; v[i] = a_max*ti; s[i] = 0.5*a_max*ti**2
        elif ti < t_acc + t_flat:
            a[i] = 0.0; v[i] = v_peak; s[i] = d_acc + v_peak*(ti - t_acc)
        else:
            td = ti - t_acc - t_flat
            a[i] = -a_max; v[i] = v_peak - a_max*td
            s[i] = d_acc + v_peak*t_flat + v_peak*td - 0.5*a_max*td**2
    return t, sgn*s, sgn*v, sgn*a, Tf

def s_curve_profile(dist, v_max, a_max, j_max, n=600):
    """Jerk-limited (S-curve) profile by integrating a 7-segment jerk sequence.
    Returns t, s, v, a, j, T_total. Jerk is bounded by j_max -> acceleration is continuous."""
    dist = float(dist); sgn = 1.0 if dist >= 0 else -1.0; D = abs(dist)
    if D == 0: t = np.linspace(0,1,n); z=np.zeros_like(t); return t,z,z,z,z,1.0
    Tj = a_max / j_max
    t_const_a = max(v_max/a_max - Tj, 0.0)
    dt = 5e-4
    def simulate(coast):
        seg = [(+j_max, Tj), (0.0, t_const_a), (-j_max, Tj),
               (0.0, coast),
               (-j_max, Tj), (0.0, t_const_a), (+j_max, Tj)]
        ts=[0.0]; s=[0.0]; v=[0.0]; a=[0.0]; j=[0.0]
        for jv, dur in seg:
            steps = max(int(round(dur/dt)), 0)
            for _ in range(steps):
                a_n = a[-1]+jv*dt; v_n = v[-1]+a[-1]*dt; s_n = s[-1]+v[-1]*dt
                ts.append(ts[-1]+dt); j.append(jv); a.append(a_n); v.append(v_n); s.append(s_n)
        return (np.array(ts),np.array(s),np.array(v),np.array(a),np.array(j))
    lo, hi = 0.0, 20.0
    for _ in range(60):
        mid=(lo+hi)/2; _,s,_,_,_ = simulate(mid)
        if s[-1] < D: lo=mid
        else: hi=mid
    ts,s,v,a,j = simulate((lo+hi)/2)
    tt=np.linspace(0,ts[-1],n)
    s=np.interp(tt,ts,s); v=np.interp(tt,ts,v); a=np.interp(tt,ts,a); j=np.interp(tt,ts,j)
    return tt, sgn*s, sgn*v, sgn*a, sgn*j, float(ts[-1])

# ============================================================================
# Unit 3-4 additions (Installment B): joint-space & Cartesian-space trajectories
# Builds on the M6 base above (fk_xy, velocity_layer, P2/T2) and the Unit 1-2
# time utilities (cubic_coeffs, quintic_coeffs, poly_eval). No dynamics, no feedback.
# ============================================================================

# ---- planar 2R closed-form inverse kinematics (position only) --------------
def ik_2link(x, y, L1=0.4, L2=0.3, elbow="up"):
    """Closed-form IK for the planar 2R arm. Returns (q1, q2) or None if unreachable.
    elbow='up' picks q2>=0; 'down' picks q2<=0."""
    r2 = x*x + y*y
    c2 = (r2 - L1*L1 - L2*L2) / (2*L1*L2)
    if c2 < -1.0 - 1e-9 or c2 > 1.0 + 1e-9:
        return None                      # outside the annulus -> unreachable
    c2 = min(1.0, max(-1.0, c2))
    s2 = np.sqrt(max(0.0, 1 - c2*c2))
    if elbow == "down": s2 = -s2
    q2 = np.arctan2(s2, c2)
    q1 = np.arctan2(y, x) - np.arctan2(L2*np.sin(q2), L1 + L2*np.cos(q2))
    return np.array([q1, q2])

# ---- synchronized multi-joint polynomial trajectory ------------------------
def joint_traj(q0, qf, T, kind="quintic", v0=None, vf=None):
    """Per-joint polynomial coefficients for a synchronized rest-to-rest move
    over a COMMON duration T (all joints start and finish together).
    kind in {'cubic','quintic'}. Returns a list of coefficient arrays."""
    q0 = np.atleast_1d(np.asarray(q0, float)); qf = np.atleast_1d(np.asarray(qf, float))
    n = len(q0); v0 = np.zeros(n) if v0 is None else np.atleast_1d(v0)
    vf = np.zeros(n) if vf is None else np.atleast_1d(vf)
    coeffs = []
    for i in range(n):
        if kind == "cubic":
            coeffs.append(cubic_coeffs(q0[i], qf[i], v0[i], vf[i], T))
        else:
            coeffs.append(quintic_coeffs(q0[i], qf[i], v0[i], vf[i], 0.0, 0.0, T))
    return coeffs

def sample_joint_traj(coeffs, T, n=200):
    """Sample a multi-joint polynomial trajectory. Returns t, Q, Qd, Qdd (each n x dof)."""
    t = np.linspace(0, T, n)
    cols = [poly_eval(c, t) for c in coeffs]
    Q   = np.stack([c[0] for c in cols], axis=1)
    Qd  = np.stack([c[1] for c in cols], axis=1)
    Qdd = np.stack([c[2] for c in cols], axis=1)
    return t, Q, Qd, Qdd

def sync_duration(q0, qf, vmax):
    """Minimum common duration so no joint exceeds vmax under a quintic
    (peak speed = 15*|dq|/(8T)). The slowest joint sets the pace."""
    q0 = np.atleast_1d(np.asarray(q0, float)); qf = np.atleast_1d(np.asarray(qf, float))
    dq = np.abs(qf - q0)
    return float(np.max(15.0 * dq / (8.0 * vmax)))

# ---- C2 natural cubic spline through via-points (per scalar joint) ---------
def cubic_spline_natural(ts, ys):
    """Natural cubic spline (second derivative = 0 at the ends) through knots
    (ts, ys). Returns a dict usable by eval_spline. C2 at interior knots."""
    ts = np.asarray(ts, float); ys = np.asarray(ys, float); n = len(ts) - 1
    h = np.diff(ts)
    # solve for second derivatives m via tridiagonal system (natural BCs m0=mn=0)
    A = np.zeros((n+1, n+1)); rhs = np.zeros(n+1)
    A[0,0] = 1.0; A[n,n] = 1.0
    for i in range(1, n):
        A[i, i-1] = h[i-1]
        A[i, i]   = 2*(h[i-1] + h[i])
        A[i, i+1] = h[i]
        rhs[i] = 6*((ys[i+1]-ys[i])/h[i] - (ys[i]-ys[i-1])/h[i-1])
    m = np.linalg.solve(A, rhs)
    return {"ts": ts, "ys": ys, "m": m, "h": h}

def eval_spline(sp, t):
    """Evaluate a natural cubic spline and its first two derivatives at scalar t.
    Returns (y, yd, ydd)."""
    ts, ys, m, h = sp["ts"], sp["ys"], sp["m"], sp["h"]
    i = int(np.clip(np.searchsorted(ts, t) - 1, 0, len(ts)-2))
    dt = t - ts[i]; hi = h[i]
    A = (ts[i+1]-t)/hi; B = (t-ts[i])/hi
    y = (A*ys[i] + B*ys[i+1]
         + ((A**3 - A)*m[i] + (B**3 - B)*m[i+1]) * (hi*hi)/6.0)
    yd = ((ys[i+1]-ys[i])/hi
          - (3*A*A - 1)/6.0*hi*m[i] + (3*B*B - 1)/6.0*hi*m[i+1])
    ydd = A*m[i] + B*m[i+1]
    return y, yd, ydd

# ---- Cartesian straight-line tool motion + IK-per-sample -------------------
def cartesian_line(p0, p1, s):
    """Straight-line tool position at path parameter s in [0,1]."""
    p0 = np.asarray(p0, float); p1 = np.asarray(p1, float)
    return (1.0 - s)*p0 + s*p1

def cartesian_traj_ik(p0, p1, T, n=120, kind="quintic", elbow="up", L1=0.4, L2=0.3):
    """Straight-line tool path p0->p1, timed by a quintic time scaling s(t),
    with closed-form 2R IK solved at each sample. Returns t, Ptool (n x 2),
    Q (n x 2). Raises ValueError if any sample is unreachable."""
    t = np.linspace(0, T, n)
    cs = quintic_coeffs(0.0, 1.0, 0, 0, 0, 0, T)
    s, _, _, _ = poly_eval(cs, t)
    Ptool = np.stack([cartesian_line(p0, p1, si) for si in s])
    Q = np.zeros((n, 2))
    for k in range(n):
        sol = ik_2link(Ptool[k,0], Ptool[k,1], L1, L2, elbow)
        if sol is None:
            raise ValueError("unreachable tool point on the straight-line path at sample %d" % k)
        Q[k] = sol
    return t, Ptool, Q

# ---- orientation interpolation: SLERP --------------------------------------
def quat_axis_angle(axis, angle):
    axis = np.asarray(axis, float); axis = axis/np.linalg.norm(axis)
    return np.concatenate([[np.cos(angle/2)], np.sin(angle/2)*axis])  # [w, x, y, z]

def slerp(q0, q1, s):
    """Spherical linear interpolation between unit quaternions q0, q1 (w,x,y,z)."""
    q0 = np.asarray(q0, float); q1 = np.asarray(q1, float)
    q0 = q0/np.linalg.norm(q0); q1 = q1/np.linalg.norm(q1)
    d = np.dot(q0, q1)
    if d < 0:                       # take the shortest arc
        q1 = -q1; d = -d
    if d > 0.9995:                  # nearly parallel -> linear, then renormalize
        q = q0 + s*(q1 - q0); return q/np.linalg.norm(q)
    th0 = np.arccos(d); th = th0*s
    q2 = q1 - q0*d; q2 = q2/np.linalg.norm(q2)
    return q0*np.cos(th) + q2*np.sin(th)

def slerp_angle(a0, a1, s):
    """Shortest-arc interpolation of a planar orientation angle (radians)."""
    d = (a1 - a0 + np.pi) % (2*np.pi) - np.pi   # wrap to (-pi, pi]
    return a0 + s*d

# ---- screw interpolation in SE(2) (unified position + orientation) ---------
def se2(theta, x, y):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s, x], [s, c, y], [0, 0, 1.0]])

def _se2_log(Tm):
    """Matrix log of an SE(2) element -> twist (vx, vy, omega)."""
    th = np.arctan2(Tm[1,0], Tm[0,0]); p = Tm[:2, 2]
    if abs(th) < 1e-9:
        return np.array([p[0], p[1], 0.0])
    A = np.sin(th)/th; B = (1 - np.cos(th))/th
    Vinv = np.array([[A, B], [-B, A]]) / (A*A + B*B)
    v = Vinv @ p
    return np.array([v[0], v[1], th])

def _se2_exp(xi):
    """Exp of an se(2) twist (vx, vy, omega) -> SE(2) element."""
    vx, vy, th = xi
    if abs(th) < 1e-9:
        return se2(0.0, vx, vy)
    V = np.array([[np.sin(th), -(1-np.cos(th))], [(1-np.cos(th)), np.sin(th)]]) / th
    p = V @ np.array([vx, vy])
    return se2(th, p[0], p[1])

def screw_interp_se2(T0, T1, s):
    """Constant-twist (screw) interpolation between SE(2) poses T0, T1 at s in [0,1].
    T(s) = T0 * exp(s * log(T0^{-1} T1)) -> a single screw motion."""
    T0inv = np.linalg.inv(T0)
    xi = _se2_log(T0inv @ T1)
    return T0 @ _se2_exp(s * xi)

# ============================================================================
# Unit 5-6 additions (Installment C): feasibility (limits, time scaling) and
# motion planning (configuration space, collision checking, RRT, path smoothing).
# Static obstacle only. No optimization/kinodynamic planning, no feedback, no dynamics.
# ============================================================================

# ---- quintic peak velocity / acceleration (for a rest-to-rest move) ---------
# s(t)=10tau^3-15tau^4+6tau^5: peak |s'| = 15/(8T); peak |s''| = (10/sqrt(3))/T^2.
def quintic_peaks(dq, T):
    """Peak |velocity| and |acceleration| of a rest-to-rest quintic of displacement dq over T."""
    dq = abs(float(dq))
    vmax = 15.0*dq/(8.0*T)
    amax = (10.0/np.sqrt(3.0))*dq/(T*T)
    return vmax, amax

# ---- feasibility: is a timed move within limits? ---------------------------
def is_feasible(q0, qf, T, vlim, alim, kind="quintic"):
    """True if a synchronized rest-to-rest move (common T) keeps every joint within
    velocity and acceleration limits."""
    q0 = np.atleast_1d(np.asarray(q0, float)); qf = np.atleast_1d(np.asarray(qf, float))
    for dq in (qf - q0):
        v, a = quintic_peaks(dq, T)
        if v > vlim + 1e-9 or a > alim + 1e-9:
            return False
    return True

# ---- slowing down to restore feasibility -----------------------------------
def feasible_duration(q0, qf, vlim, alim, kind="quintic"):
    """Minimum common duration T so every joint's quintic stays within vlim and alim.
    Velocity binds as T_v = 15|dq|/(8 vlim); acceleration as T_a = sqrt((10/sqrt3)|dq|/alim).
    The feasible duration is the max over joints of max(T_v, T_a)."""
    q0 = np.atleast_1d(np.asarray(q0, float)); qf = np.atleast_1d(np.asarray(qf, float))
    Ts = []
    for dq in np.abs(qf - q0):
        Tv = 15.0*dq/(8.0*vlim)
        Ta = np.sqrt((10.0/np.sqrt(3.0))*dq/alim)
        Ts.append(max(Tv, Ta))
    return float(max(Ts)) if Ts else 0.0

def uniform_time_scale_factors(T0, T1):
    """How peaks scale when a trajectory is stretched from T0 to T1:
    velocity scales by T0/T1, acceleration by (T0/T1)^2."""
    r = T0 / T1
    return r, r*r

# ---- arm geometry for collision checking -----------------------------------
def arm_points2(q, L1=0.4, L2=0.3):
    """Base, elbow, tool points of the planar 2R arm at configuration q."""
    q = np.asarray(q, float)
    b = np.array([0.0, 0.0])
    e = b + L1*np.array([np.cos(q[0]), np.sin(q[0])])
    t = e + L2*np.array([np.cos(q[0]+q[1]), np.sin(q[0]+q[1])])
    return b, e, t

def _seg_point_dist(a, b, p):
    """Distance from point p to segment ab."""
    a=np.asarray(a,float); b=np.asarray(b,float); p=np.asarray(p,float)
    ab=b-a; L2=ab@ab
    if L2 < 1e-15: return np.linalg.norm(p-a)
    u=np.clip((p-a)@ab/L2, 0.0, 1.0)
    return np.linalg.norm(p-(a+u*ab))

def arm_hits_disk(q, center, radius, L1=0.4, L2=0.3):
    """True if either link of the arm at q intersects the disk obstacle (center, radius)."""
    b, e, t = arm_points2(q, L1, L2)
    return (_seg_point_dist(b, e, center) <= radius) or (_seg_point_dist(e, t, center) <= radius)

# ---- configuration-space occupancy grid (a way to *see* the constraints) ----
def cspace_grid(center, radius, n=120, lo=-np.pi, hi=np.pi, L1=0.4, L2=0.3):
    """Boolean n x n grid over (q1,q2) in [lo,hi]^2: True where the arm is in collision
    (C-obstacle). The free space is the complement (C_free)."""
    q1 = np.linspace(lo, hi, n); q2 = np.linspace(lo, hi, n)
    G = np.zeros((n, n), dtype=bool)
    for i, a in enumerate(q1):
        for j, bb in enumerate(q2):
            G[j, i] = arm_hits_disk((a, bb), center, radius, L1, L2)
    return q1, q2, G

# ---- collision checking along a C-space edge / path ------------------------
def edge_collision_free(qa, qb, center, radius, step=0.05, L1=0.4, L2=0.3):
    """Check a straight C-space segment qa->qb for collision by dense sampling."""
    qa=np.asarray(qa,float); qb=np.asarray(qb,float)
    n=max(2, int(np.ceil(np.linalg.norm(qb-qa)/step)))
    for u in np.linspace(0,1,n):
        if arm_hits_disk(qa+u*(qb-qa), center, radius, L1, L2): return False
    return True

def path_collision_free(path, center, radius, step=0.05, L1=0.4, L2=0.3):
    """Check a whole C-space path (list of configs) edge by edge."""
    for k in range(len(path)-1):
        if not edge_collision_free(path[k], path[k+1], center, radius, step, L1, L2):
            return False
    return True

# ---- sampling-based planning: RRT in configuration space -------------------
def rrt(q_start, q_goal, center, radius, rng, step=0.15, goal_bias=0.1,
        max_iter=4000, goal_tol=0.2, lo=-np.pi, hi=np.pi, L1=0.4, L2=0.3):
    """Basic RRT in C-space. Grows a tree from q_start, biased toward q_goal, rejecting
    edges that collide with the static disk obstacle. Returns a collision-free path
    (list of configs) from start to goal, or None if not found within max_iter.
    Practical and intuitive — no optimality, no rewiring, no kinodynamics."""
    q_start=np.asarray(q_start,float); q_goal=np.asarray(q_goal,float)
    nodes=[q_start]; parent=[-1]
    for _ in range(max_iter):
        q_rand = q_goal if rng.random() < goal_bias else rng.uniform(lo, hi, size=2)
        d=[np.linalg.norm(q_rand-nd) for nd in nodes]; i=int(np.argmin(d))
        q_near=nodes[i]; v=q_rand-q_near; nv=np.linalg.norm(v)
        if nv < 1e-9: continue
        q_new=q_near + min(step, nv)*v/nv
        if not edge_collision_free(q_near, q_new, center, radius, 0.05, L1, L2): continue
        nodes.append(q_new); parent.append(i)
        if np.linalg.norm(q_new-q_goal) <= goal_tol and \
           edge_collision_free(q_new, q_goal, center, radius, 0.05, L1, L2):
            nodes.append(q_goal); parent.append(len(nodes)-2)
            # backtrace
            path=[]; k=len(nodes)-1
            while k != -1: path.append(nodes[k]); k=parent[k]
            return list(reversed(path))
    return None

# ---- path smoothing: random shortcutting -----------------------------------
def shortcut_smooth(path, center, radius, rng, iters=200, L1=0.4, L2=0.3):
    """Shorten a collision-free C-space path by repeatedly trying to replace a
    sub-path between two random points with a straight (collision-free) shortcut."""
    path=[np.asarray(p,float) for p in path]
    for _ in range(iters):
        if len(path) <= 2: break
        i=rng.integers(0, len(path)-1); j=rng.integers(i+1, len(path))
        if j-i < 2: continue
        if edge_collision_free(path[i], path[j], center, radius, 0.05, L1, L2):
            path = path[:i+1] + path[j:]
    return path

def path_length(path):
    """Total C-space length of a path (sum of segment lengths)."""
    return float(sum(np.linalg.norm(np.asarray(path[k+1])-np.asarray(path[k])) for k in range(len(path)-1)))

# ============================================================================
# Unit 7-8 additions (Installment D, capstone): trajectory quality metrics,
# a validation suite, reference sampling/representation, the integrated
# Plan->Parameterize->Validate->Execute pipeline, and the REFERENCE TRAJECTORY
# LAYER consumed by Module 8. STRICT BOUNDARY: no feedback, no dynamics, no
# actuator control. The layer emits an open-loop reference (q_d, qd_d, qdd_d)
# only; tracking it is Module 8.
# ============================================================================

# ---- piecewise rest-to-rest quintic over smoothed waypoints ----------------
def piecewise_quintic(waypoints, seg_T):
    """Build a C2 reference q(t) from waypoints joined by rest-to-rest quintic
    segments (qd=qdd=0 at every waypoint, so velocity/acceleration are continuous).
    Returns (ref_fn, T_total) where ref_fn(t) -> (q, qd, qdd) as arrays."""
    W = [np.asarray(w, float) for w in waypoints]
    seg_T = list(map(float, seg_T))
    nseg = len(W) - 1
    # per-joint quintic coefficients per segment
    coeffs = []
    for k in range(nseg):
        cs = [quintic_coeffs(W[k][j], W[k+1][j], 0,0,0,0, seg_T[k]) for j in range(len(W[0]))]
        coeffs.append(cs)
    starts = np.concatenate([[0.0], np.cumsum(seg_T)])
    T_total = float(starts[-1])
    def ref_fn(t):
        t = min(max(t, 0.0), T_total)
        k = int(np.searchsorted(starts, t, side='right') - 1)
        k = min(max(k, 0), nseg-1)
        tau = t - starts[k]
        q=[];qd=[];qdd=[]
        for j in range(len(W[0])):
            qj,qdj,qddj,_ = poly_eval(coeffs[k][j], np.array([tau]))
            q.append(qj[0]); qd.append(qdj[0]); qdd.append(qddj[0])
        return np.array(q), np.array(qd), np.array(qdd)
    return ref_fn, T_total

# ---- reference sampling / representation (discretize for execution) --------
def sample_reference(ref_fn, T_total, rate=100.0):
    """Sample a continuous reference into a time-indexed reference at a control
    rate (Hz): returns (t, Q, Qd, Qdd) arrays. This is the discrete reference a
    downstream controller would step through (M8). No control is performed here."""
    n = max(2, int(round(T_total*rate))+1)
    t = np.linspace(0.0, T_total, n)
    Q=[];Qd=[];Qdd=[]
    for ti in t:
        q,qd,qdd = ref_fn(ti); Q.append(q); Qd.append(qd); Qdd.append(qdd)
    return t, np.array(Q), np.array(Qd), np.array(Qdd)

# ---- trajectory quality metrics --------------------------------------------
def trajectory_metrics(ref_fn, T_total, L1=0.4, L2=0.3, rate=200.0):
    """Quality summary of a reference: duration, peak |speed|, peak |accel|,
    peak |jerk| (finite-difference of qdd), and the Cartesian tool path length.
    Geometric/temporal quality only -- not energy or dynamics."""
    t, Q, Qd, Qdd = sample_reference(ref_fn, T_total, rate)
    dt = t[1]-t[0] if len(t)>1 else T_total
    jerk = np.diff(Qdd, axis=0)/dt if len(t)>1 else np.zeros_like(Qdd)
    # cartesian tool path length via FK
    tool = np.array([arm_points2(q, L1, L2)[2] for q in Q])
    clen = float(np.sum(np.linalg.norm(np.diff(tool, axis=0), axis=1)))
    return {
        "duration": float(T_total),
        "peak_speed": float(np.max(np.abs(Qd))) if len(Qd) else 0.0,
        "peak_accel": float(np.max(np.abs(Qdd))) if len(Qdd) else 0.0,
        "peak_jerk": float(np.max(np.abs(jerk))) if len(jerk) else 0.0,
        "cartesian_path_length": clen,
    }

# ---- the complete validation suite -----------------------------------------
def validate_trajectory(ref_fn, T_total, waypoints, seg_T, vlim, alim,
                        center=None, radius=None, L1=0.4, L2=0.3, rate=200.0,
                        q_start=None, q_goal=None):
    """Validate a reference against every gate (Unit 5 feasibility + Unit 6
    collision + continuity + endpoints). Returns a dict of per-check booleans and
    an overall 'valid'. No control, no dynamics -- pure validation of the reference."""
    t, Q, Qd, Qdd = sample_reference(ref_fn, T_total, rate)
    checks = {}
    # endpoints match start/goal (if given) and are at rest
    W = [np.asarray(w,float) for w in waypoints]
    checks["endpoints_match"] = (
        (q_start is None or np.allclose(Q[0], q_start, atol=1e-6)) and
        (q_goal  is None or np.allclose(Q[-1], q_goal,  atol=1e-6)))
    checks["rest_to_rest"] = bool(np.allclose(Qd[0],0,atol=1e-6) and np.allclose(Qd[-1],0,atol=1e-6)
                                  and np.allclose(Qdd[0],0,atol=1e-6) and np.allclose(Qdd[-1],0,atol=1e-6))
    # within velocity / acceleration limits everywhere
    checks["within_velocity"] = bool(np.max(np.abs(Qd)) <= vlim + 1e-6)
    checks["within_acceleration"] = bool(np.max(np.abs(Qdd)) <= alim + 1e-6)
    # continuity: position/velocity/acceleration continuous (no jumps) across the sampled path
    jump = np.max(np.abs(np.diff(Q,axis=0))) if len(Q)>1 else 0.0
    vjump = np.max(np.abs(np.diff(Qd,axis=0))) if len(Qd)>1 else 0.0
    checks["continuous"] = bool(jump < 0.5 and vjump < 0.5)   # no discontinuous leaps at this rate
    # collision-free along the path (if an obstacle is given) -- whole arm
    if center is not None and radius is not None:
        checks["collision_free"] = bool(all(not arm_hits_disk(q, center, radius, L1, L2) for q in Q))
    else:
        checks["collision_free"] = True
    # reachability: every configuration is finite/valid (and tool within annulus)
    reach_ok = True
    for q in Q:
        tool = arm_points2(q, L1, L2)[2]; r = np.linalg.norm(tool)
        if not (np.all(np.isfinite(q)) and (L1-L2)-1e-6 <= r <= (L1+L2)+1e-6):
            reach_ok = False; break
    checks["reachable"] = reach_ok
    checks["valid"] = all(checks.values())
    return checks

# ---- the integrated pipeline: Plan -> Parameterize -> Validate -------------
def plan_parameterize(q_start, q_goal, center, radius, vlim, alim, rng,
                      step=0.2, goal_bias=0.15, max_iter=5000, goal_tol=0.25,
                      smooth_iters=300, L1=0.4, L2=0.3):
    """PLAN a collision-free path (RRT) and PARAMETERIZE it into a timed reference:
    smooth the path, then time each rest-to-rest segment to the minimum feasible
    duration (respecting velocity/acceleration limits). Returns
    (waypoints, seg_T, ref_fn, T_total) or None if no path is found."""
    path = rrt(q_start, q_goal, center, radius, rng, step, goal_bias, max_iter, goal_tol, L1=L1, L2=L2)
    if path is None:
        return None
    way = shortcut_smooth(path, center, radius, rng, smooth_iters, L1, L2)
    seg_T = [feasible_duration(way[k], way[k+1], vlim, alim) for k in range(len(way)-1)]
    seg_T = [max(t, 1e-3) for t in seg_T]
    ref_fn, T_total = piecewise_quintic(way, seg_T)
    return way, seg_T, ref_fn, T_total

# ---- the REFERENCE TRAJECTORY LAYER (the Module 8 handoff) ------------------
def reference_trajectory_layer(q_start, q_goal, center, radius, vlim, alim, rng,
                               rate=100.0, L1=0.4, L2=0.3, **plan_kw):
    """Capstone artifact: PLAN -> PARAMETERIZE -> VALIDATE, then package a validated
    open-loop REFERENCE consumed by Module 8. Returns a dict with:
        reference(t) -> (q_d, qd_d, qdd_d, info)   # the feed-forward reference signal
        duration, rate, waypoints, seg_T, metrics, validation, validated
    EXECUTE means stepping this reference open-loop (e.g. via the M6 velocity layer)
    and handing it to Module 8. NO feedback, NO dynamics, NO actuator control here."""
    out = plan_parameterize(q_start, q_goal, center, radius, vlim, alim, rng, L1=L1, L2=L2, **plan_kw)
    if out is None:
        return {"validated": False, "reference": None, "reason": "no path found"}
    way, seg_T, ref_fn, T_total = out
    val = validate_trajectory(ref_fn, T_total, way, seg_T, vlim, alim,
                              center, radius, L1, L2, q_start=q_start, q_goal=q_goal)
    met = trajectory_metrics(ref_fn, T_total, L1, L2)
    def reference(t):
        q,qd,qdd = ref_fn(t)
        info = {"t": float(t), "duration": T_total, "phase": min(t/T_total,1.0) if T_total>0 else 1.0}
        return q, qd, qdd, info
    return {
        "reference": reference,        # q_d, qd_d, qdd_d (feed-forward) for M8
        "duration": T_total, "rate": rate,
        "waypoints": way, "seg_T": seg_T,
        "metrics": met, "validation": val, "validated": bool(val["valid"]),
    }
