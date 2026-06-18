---
module: 8
unit: 4
lesson: 1
type: answer_key
title: "Answer Key — From One Joint to Many: Tracking a Trajectory with Feedback"
audience: coaches
---

# Answer Key 4.1 — From One Joint to Many: Tracking a Trajectory with Feedback

*Coaches' key. Multiple choice followed by model short answers and grading notes.*

---

**Q1 — B.** One independent PID per joint, each tracking its q_d(t).

**Q2 — B.** Tracking follows a moving reference; regulation holds a setpoint.

**Q3 — B.** Feedback-only tracking has a speed-dependent following error.

**Q4 — B.** Coupling is treated as a disturbance the feedback rejects.

**Q5 — B.** Gains reduce but never erase following error and cost stability.

---

**Q6 — model answer.** Regulation holds a single fixed target — the controller drives the error to zero and a good PID eventually nails it. Tracking follows a target q_d(t) that changes every instant, straight from Module 7. Feedback-only tracking lags because feedback can only act on an error after it has formed: at each instant it corrects the gap that already opened while the reference has moved on. The result is a following error that persists throughout fast motion and grows with the reference's speed. No finite PID gains remove it, because feedback has no information about where the reference is heading — only where the joint is relative to where it was asked to be.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q7 — model answer.** We run one PID per joint, each treating its joint as its own plant (integrator + disturbance + saturation) with its own gains. This is simple, robust, and standard, and it keeps us within the module's dynamics boundary. What we deliberately ignore is the inter-joint coupling — the way one joint's motion exerts forces on another (the mass-matrix and Coriolis effects of full manipulator dynamics). Instead of modelling that coupling, we let each joint's feedback reject it as just another disturbance. This is the intuition-first stance: feedback handles the coupling as an unmodelled effect, so we get whole-arm control without deriving formal dynamics.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

**Q8 — model answer.** Module 7 provides the planned velocity q̇_d(t) and acceleration q̈_d(t) of the trajectory, alongside the position q_d(t). Feedback-only control uses only q_d (the position target) and discards the velocity and acceleration. They matter because they describe where the reference is heading and how hard the joint must push to follow it on time — exactly the information needed to stop lagging. The following error exists precisely because feedback ignores them. The next lessons use q̇_d and q̈_d in a feedforward term that anticipates the motion, removing the lag that feedback alone cannot. This is why Module 7 bothered to compute the derivatives, not just positions.
*Grading: award credit for the core idea above; accept equivalent phrasings and valid examples.*

---

### Common misconceptions to watch for
- Expecting feedback to track a fast reference with zero error.
- Trying to model inter-joint dynamics here (treat coupling as disturbance).
- Confusing following error (moving-target lag) with steady-state error.
