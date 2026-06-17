# Answer Key — Lesson 8.3: Verifying the Forward Kinematics

**Coaches only.** Capstone, formative.

1. **Why multiple independent checks** — each probes a different failure mode, so silent errors are caught.
2. **Match** — planar reduction → matches fk_planar; θ1 sweep → gives a revolution; RᵀR=I, det R=1 → rotation validity; SymPy → symbolic = numeric.
3. **"It runs" is the same as "it's correct"** — False.
4. **Two independent FK verification checks (short).** Any two of: known-config pose; planar reduction vs fk_planar; single-joint revolution; SymPy-vs-numeric; rotation validity (RᵀR=I, det R=1).

**Challenge rubric.** Full credit: setting α1=0 instead of 90° is caught by the checks that depend on the base twist standing the arm plane up — the zero-config pose check, the θ1-sweep revolution invariants (height/radius), and the SymPy-vs-numeric comparison; a check confined to the planar sub-arm (θ1=0) may *not* catch it since with θ1=0 the corrupted twist can leave the in-plane reach unchanged — showing why a *diverse* set of checks matters. Partial: identifies some catching checks without the diversity lesson.
