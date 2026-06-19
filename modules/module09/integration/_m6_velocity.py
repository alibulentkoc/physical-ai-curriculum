"""
_m6_velocity.py — Module 6 velocity layer, REUSED VERBATIM.

This file is a vendored copy of the resolved-rate velocity layer produced by the
Module 6 capstone (`modules/module06/notebooks/lesson32_capstone_velocity_layer.ipynb`).
It is reproduced unchanged so the Module 9 adapter can WRAP it without REDEFINING it
(per the Architect's adapter ruling: "Wrap. Do not redefine.").

Do not edit the logic here. If Module 6 changes, re-vendor from its capstone.
The public surface Module 9 depends on:
    forward_chain(P, T, q)            -> list of 4x4 frames (real FK, shared with M4)
    fk_xy(P, T, q)                    -> tool (x, y)
    geometric_jacobian(P, T, q)       -> 6xn geometric Jacobian
    velocity_layer(P, T, q, xi_d, z)  -> (q_dot, info)  [the M6 handoff]
    P2, T2                            -> the greenhouse 2-link planar arm
"""
import numpy as np


def dh(th, d, a, al):
    ct, st, ca, sa = np.cos(th), np.sin(th), np.cos(al), np.sin(al)
    return np.array([[ct, -st * ca, st * sa, a * ct],
                     [st, ct * ca, -ct * sa, a * st],
                     [0, sa, ca, d],
                     [0, 0, 0, 1]])


def forward_chain(P, T, q):
    M = np.eye(4)
    Ms = [M.copy()]
    for i, (th0, d0, a, al) in enumerate(P):
        th, d = (th0 + q[i], d0) if T[i] == "R" else (th0, d0 + q[i])
        M = M @ dh(th, d, a, al)
        Ms.append(M.copy())
    return Ms


def geometric_jacobian(P, T, q):
    Ms = forward_chain(P, T, q)
    on = Ms[-1][:3, 3]
    J = np.zeros((6, len(q)))
    for i in range(len(q)):
        z = Ms[i][:3, 2]
        o = Ms[i][:3, 3]
        if T[i] == "R":
            J[:3, i] = np.cross(z, on - o)
            J[3:, i] = z
        else:
            J[:3, i] = z
    return J


def Jv_planar(P, T, q):
    return geometric_jacobian(P, T, q)[:2, :]


def fk_xy(P, T, q):
    return forward_chain(P, T, q)[-1][:2, 3]


# The greenhouse harvesting arm: a 2-link planar manipulator.
# Canonical link lengths L1=0.4, L2=0.3 (consistent with M5 IK and M7's reference
# layer), so the velocity layer, IK, and planner all share one workspace.
P2 = [(0, 0, 0.4, 0), (0, 0, 0.3, 0)]
T2 = ["R", "R"]

EPS = 0.08  # singularity threshold on sigma_min


def analyze(P, T, q):
    """One SVD -> full capability report (Units 4-6 in one function)."""
    J = Jv_planar(P, T, q)
    U, S, Vt = np.linalg.svd(J)
    w = float(np.prod(S))
    kappa = float(S[0] / max(S[-1], 1e-12))
    return {"sigma": S, "w": w, "kappa": kappa,
            "axes": [(U[:, i], float(S[i])) for i in range(len(S))],
            "singular": bool(S[-1] < EPS), "sigma_min": float(S[-1]),
            "J": J, "U": U, "Vt": Vt}


def dls(J, lam):
    return J.T @ np.linalg.inv(J @ J.T + lam ** 2 * np.eye(J.shape[0]))


def schedule_lambda(sigma_min, lam_max=0.1, eps=EPS):
    """lambda^2 = (1-(smin/eps)^2) lam_max^2 inside the band, else 0."""
    if sigma_min >= eps:
        return 0.0
    return float(np.sqrt((1 - (sigma_min / eps) ** 2)) * lam_max)


def velocity_layer(P, T, q, xi_d, z=None):
    rep = analyze(P, T, q)
    lam = schedule_lambda(rep["sigma_min"])
    J = rep["J"]
    Jd = dls(J, lam) if lam > 0 else np.linalg.pinv(J)
    qd = Jd @ xi_d
    if z is not None:  # null-space secondary objective (redundant arms)
        qd = qd + (np.eye(len(q)) - Jd @ J) @ z
    info = {"w": rep["w"], "kappa": rep["kappa"], "sigma_min": rep["sigma_min"],
            "lambda": lam, "singular": rep["singular"]}
    return qd, info
