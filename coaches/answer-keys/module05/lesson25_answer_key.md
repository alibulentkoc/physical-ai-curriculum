# Answer Key — Lesson 7.1: Verifying a Solution with Forward Kinematics

**Coaches only.** Formative.

1. **Discipline** — solve → verify with FK → accept or reject.
2. **Accept when** — ‖p_target − f(θ_c)‖ < tol.
3. **FK catches analytical, numerical, and selection errors** — True (it's independent of how the candidate was made).
4. **Why an independent FK model (short).** A bug in the solver's own FK or target would pass its internal check; an independent, trusted FK exposes the mismatch.

**Challenge rubric.** Full credit: names two bugs — (i) the solver minimized error against the *wrong* target (e.g. un-transformed or stale), so its internal residual is small but the true residual is large; (ii) the solver's internal FK/Jacobian doesn't match the real arm (wrong link length/model), so it "converges" to a pose that misses — and explains that an independent FK with the *true* model recomputes the real gripper position and catches both. Partial: one bug, or no explanation of why independence matters.
