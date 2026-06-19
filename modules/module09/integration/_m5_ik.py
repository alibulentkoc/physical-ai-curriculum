"""
_m5_ik.py — Module 5 inverse kinematics, REUSED VERBATIM.

Vendored copy of the closed-form planar-2R inverse kinematics from the Module 5 / M7
capstone line, reproduced unchanged so the Module 9 adapter can WRAP it (not redefine
it). Returns joint angles for a Cartesian target, or None if the target is unreachable.

Used by the Understand -> Plan seam (Unit 3): a committed target POSE becomes a goal
CONFIGURATION via this layer. Link lengths default to the canonical greenhouse arm
(L1=0.4, L2=0.3), matching modules.module09.integration._m6_velocity.P2.
"""
import numpy as np


def ik_2link(x, y, L1=0.4, L2=0.3, elbow="up"):
    """Closed-form IK for the planar 2R arm. Returns (q1, q2) or None if unreachable.
    elbow='up' picks q2>=0; 'down' picks q2<=0."""
    r2 = x * x + y * y
    c2 = (r2 - L1 * L1 - L2 * L2) / (2 * L1 * L2)
    if c2 < -1.0 - 1e-9 or c2 > 1.0 + 1e-9:
        return None                      # outside the annulus -> unreachable
    c2 = min(1.0, max(-1.0, c2))
    s2 = np.sqrt(max(0.0, 1 - c2 * c2))
    if elbow == "down":
        s2 = -s2
    q2 = np.arctan2(s2, c2)
    q1 = np.arctan2(y, x) - np.arctan2(L2 * np.sin(q2), L1 + L2 * np.cos(q2))
    return np.array([q1, q2])
