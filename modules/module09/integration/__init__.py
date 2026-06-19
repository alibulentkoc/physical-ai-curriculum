"""
module09.integration — the System Integration foundation.

Public surface used by the Module 9 lessons and notebooks:

    World / blackboard:
        GreenhouseWorld, Fruit, WorldState, model_perception
    Layers (wrapped real code + integration glue):
        velocity_layer, forward_chain, fk_xy, geometric_jacobian, P2, T2
        LAYER_REGISTRY, STAGES, stage_info
        understand, dedupe

Design rule (Architect): adapters WRAP, they do not REDEFINE. The orchestrator
(Units 7-8) and the full motion-stack wiring (Units 3-5) build on top of this.
"""
from .world import (
    GreenhouseWorld, Fruit, WorldState, model_perception,
    REACH_MIN, REACH_MAX,
)
from .layers import (
    velocity_layer, forward_chain, fk_xy, geometric_jacobian, P2, T2,
    LAYER_REGISTRY, STAGES, stage_info, understand, dedupe,
    ik_2link, to_configuration, reference_trajectory_layer, plan_reference,
    control_layer, Joint, step_plant, execute_reference, DEFAULT_GAINS,
    track, system_monitor, TRACK_TOL_RMS, TRACK_TOL_FINAL,
    FAILURE_TAXONOMY, DETECT_THRESHOLDS, failure_event, localize, run_pipeline,
    RECOVERY_POLICY, recover, harvest_row,
)

__all__ = [
    "GreenhouseWorld", "Fruit", "WorldState", "model_perception",
    "REACH_MIN", "REACH_MAX",
    "velocity_layer", "forward_chain", "fk_xy", "geometric_jacobian", "P2", "T2",
    "LAYER_REGISTRY", "STAGES", "stage_info", "understand", "dedupe",
    "ik_2link", "to_configuration", "reference_trajectory_layer", "plan_reference",
    "control_layer", "Joint", "step_plant", "execute_reference", "DEFAULT_GAINS",
    "track", "system_monitor", "TRACK_TOL_RMS", "TRACK_TOL_FINAL",
    "FAILURE_TAXONOMY", "DETECT_THRESHOLDS", "failure_event", "localize", "run_pipeline",
    "RECOVERY_POLICY", "recover", "harvest_row",
]
