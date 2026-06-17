# Answer Key — Lesson 5.3: Convergence, Step Size, and Failure Modes

**Coaches only.** Formative.

1. **Stop when** — |e| < tol, or the iteration cap is hit (then report failure).
2. **Too-large α causes** — overshoot / oscillation / divergence.
3. **Match** — unreachable → reachability check/reposition; divergence → smaller α or DLS; wrong solution → better seed / selection.
4. **Why return a status (short).** So the caller can re-seed, reposition, lower the gain, or abort, instead of committing a bad/nonexistent solution.

**Challenge rubric.** Full credit: backtracking — try α=1; if the error decreased keep it, else halve α and redo — gives Newton speed when the full step helps and automatically shrinks the step when it would overshoot; it composes with DLS (use DLS for the step direction, backtracking for its length) so the solver is both bounded and self-tuning. Partial: describes halving without explaining the speed/safety trade-off.

**Note on this lesson's solver.** For the bounded 2-link arm, a too-large α makes the error *oscillate* (it can't run to infinity — the gripper stays within the workspace), so the notebook flags it as `diverged` via a "reachable target whose error grows and stays above the start" test; an *unreachable* target instead *plateaus* and is reported as `max_iter`. Both are non-converged statuses the caller must handle.
