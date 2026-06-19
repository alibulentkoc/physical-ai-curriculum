"""
world.py — the shared world-state model for Module 9 (System Integration).

This is the ONE genuinely new data structure Module 9 introduces at the foundation
level: a single greenhouse world that every layer reads from and writes to. It is a
*minimal kinematic* model only — no new physics, no dynamics, no digital twin. Those
belong to Module 10 (Digital Twin Capstone), which will MIRROR this state, not replace it.

Three objects:

  Fruit         — one tomato: position in the world, ripeness, and (for case studies)
                  whether perception can currently see it.
  GreenhouseWorld
                — the ground truth: the 2-link arm (real M6 FK) plus a row of fruit.
                  Layers never read ground truth directly except through perception.
  WorldState    — the BLACKBOARD. This is the integration contract: the shared dict-like
                  record that flows Perceive -> Understand -> Plan -> Execute -> Track ->
                  Recover. Each stage reads the fields it owns and writes the fields it
                  produces. Ownership is documented per field below.

Perception (model_perception) is the Module 3 boundary as Module 9 consumes it: it turns
ground-truth fruit into noisy *detections*. Module 9 does not re-teach perception; it only
consumes its output and writes it onto the blackboard.
"""
from dataclasses import dataclass, field
from typing import Optional
import numpy as np

from ._m6_velocity import P2, T2, fk_xy

# Reach of the 2-link arm (L1=0.4, L2=0.3): outer = L1+L2 = 0.7 (full extension),
# inner = |L1-L2| = 0.1. A small margin keeps targets off the exact singular boundary.
REACH_MAX = 0.68
REACH_MIN = 0.12


@dataclass
class Fruit:
    """One tomato in the greenhouse (ground truth)."""
    fid: str
    x: float
    y: float
    ripe: bool = True
    visible: bool = True       # set False to model occlusion in case studies
    picked: bool = False

    @property
    def xy(self):
        return np.array([self.x, self.y], dtype=float)


@dataclass
class GreenhouseWorld:
    """Ground-truth greenhouse: the arm and a row of fruit. Minimal kinematic sim."""
    fruit: list
    q: np.ndarray = field(default_factory=lambda: np.array([0.4, 0.8]))
    P: list = field(default_factory=lambda: list(P2))
    T: list = field(default_factory=lambda: list(T2))

    @classmethod
    def demo_row(cls, n=5, seed=0):
        """A reproducible row of fruit at varied reach, some unripe, one out of reach."""
        rng = np.random.default_rng(seed)
        fruit = []
        for i in range(n):
            r = 0.22 + 0.42 * (i / max(1, n - 1))         # spread across the 0.12-0.68 band
            ang = -0.5 + 1.0 * rng.random()
            x, y = r * np.cos(ang), r * np.sin(ang)
            ripe = bool(rng.random() > 0.25)
            fruit.append(Fruit("F%d" % i, float(x), float(y), ripe=ripe))
        return cls(fruit=fruit)

    def tool_xy(self):
        """Real forward kinematics (M6/M4) — where the gripper is right now."""
        return fk_xy(self.P, self.T, self.q)

    def reachable(self, xy):
        """Pure kinematic reach test against the 2-link workspace annulus."""
        r = float(np.linalg.norm(np.asarray(xy, float)))
        return REACH_MIN <= r <= REACH_MAX


@dataclass
class WorldState:
    """
    THE BLACKBOARD — the integration contract that flows through all six stages.

    Field ownership (who WRITES each field):
      detections      <- Perceive   (perception layer, Module 3 boundary)
      targets         <- Understand (target selection — a Module 9 decision)
      current_target  <- Understand / Recover
      q, tool_xy      <- Execute / the world  (real FK)
      reference       <- Plan       (Module 7 reference_layer)  [wired in Unit 3-4]
      command         <- Execute    (Module 8 tracking_controller) [wired in Unit 4]
      tracking_error  <- Track      (Module 8 telemetry)         [wired in Unit 5]
      health          <- every layer (cross-layer health signals) [Unit 6]
      stage           <- the orchestrator                         [Unit 7]
      harvested       <- the system  (outcome)
    """
    detections: list = field(default_factory=list)
    targets: list = field(default_factory=list)
    current_target: Optional[dict] = None
    q: Optional[np.ndarray] = None
    tool_xy: Optional[np.ndarray] = None
    reference: Optional[object] = None
    command: Optional[object] = None
    tracking_error: Optional[float] = None
    health: dict = field(default_factory=dict)
    stage: str = "idle"
    harvested: list = field(default_factory=list)

    def owner_of(self, field_name):
        """Return the subsystem that owns (writes) a blackboard field — the
        question Module 9 asks at every stage: 'who owns this decision?'."""
        return _FIELD_OWNERS.get(field_name, "unknown")


_FIELD_OWNERS = {
    "detections": "Perceive (Module 3 perception)",
    "targets": "Understand (Module 9 target selection)",
    "current_target": "Understand / Recover",
    "q": "Execute (world / real FK)",
    "tool_xy": "Execute (real forward kinematics)",
    "reference": "Plan (Module 7 reference_layer)",
    "command": "Execute (Module 8 tracking_controller)",
    "tracking_error": "Track (Module 8 telemetry)",
    "health": "all layers (cross-layer health signals)",
    "stage": "Orchestrator (Module 9)",
    "harvested": "System outcome",
}


def model_perception(world: GreenhouseWorld, rng=None, noise=0.0,
                     occlude=(), duplicate=()):
    """
    The Module 3 perception boundary, AS MODULE 9 CONSUMES IT.

    Turns ground-truth fruit into a list of detection dicts. Module 9 does NOT
    re-teach perception — this is a thin stand-in for the real perception layer's
    output so the integration story (Perceive -> Understand) is honest and runnable.

    Each detection: {"id", "xy": np.array, "ripe", "confidence"}.

    Args let the Unit 2 case study ("When Perception Lies") inject realistic faults:
      noise      — Gaussian position noise (metres) on each detection
      occlude    — iterable of fruit ids that are hidden this frame (dropped)
      duplicate  — iterable of fruit ids reported twice (duplicate detections)
    """
    rng = rng or np.random.default_rng(0)
    occlude = set(occlude)
    duplicate = set(duplicate)
    dets = []
    for f in world.fruit:
        if f.picked or not f.visible or f.fid in occlude:
            continue
        xy = f.xy + (rng.normal(0, noise, 2) if noise > 0 else 0.0)
        conf = float(np.clip(0.9 + rng.normal(0, 0.03), 0.0, 1.0))
        det = {"id": f.fid, "xy": np.asarray(xy, float),
               "ripe": bool(f.ripe), "confidence": conf}
        dets.append(det)
        if f.fid in duplicate:                      # second, slightly offset report
            d2 = dict(det)
            d2["xy"] = det["xy"] + rng.normal(0, max(noise, 0.01), 2)
            d2["confidence"] = float(np.clip(conf - 0.1, 0, 1))
            dets.append(d2)
    return dets
