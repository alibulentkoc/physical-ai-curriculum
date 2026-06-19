# Curriculum Release Audit Report
*Phase 1 — Repository Audit · Release Manager · 2026-06 · repository is the source of truth*
*Re-verified 2026-06 for the curriculum-v1.0 release-execution phase: repository state unchanged — parity ALL-MATCH (lessons = quizzes = keys = nav per module), totals 325 / 326 / 50 / 9, strict build exit 0. Findings below remain current.*

EXECUTIVE SUMMARY

**Status:** PASS (with minor hygiene issues). All ten modules are present, complete, and internally consistent; the site builds green at 325 lesson pages. No publication-blocking defects found.

**Findings:** 325 lessons across 10 modules, with full parity between lessons, quizzes, answer keys, and navigation entries in every module. 326 diagrams (M1 ships one extra by design), 50 interactive demos, and 9 midpoint assessments — all correctly injected. Page headers, diagram naming, and nav are consistent.

**Issues:** Seven non-blocking items, all hygiene rather than correctness: 42 orphan duplicate notebooks (M1/M2), 12 stale flat demo copies in generated `site_src/`, one stray spec file in a demos folder, two stale engine backups, sparse `· demo` nav annotations, two coexisting notebook-naming conventions, and M9 carrying no midpoint assessment (by design).

**Recommendations:** Defer all cleanup to an explicit post-audit cleanup pass (Phase 1 is read-only). Prioritise removing the 42 orphan notebooks and the 12 stale `site_src` demo copies before tagging v1.0; the remaining items are cosmetic and optional.

**Next:** Proceed to Phase 2 (Publication Readiness Review) — confirm a clean strict build and full render/injection coverage.

---

## 1. Artifact counts (repo-verified)

| Module | Lessons | Notebooks | SVGs | Quizzes | Answer keys | Demos | Midpoint |
|---|---:|---:|---:|---:|---:|---:|:--:|
| M01 — Mathematical Foundations | 33 | 66 | 34 | 33 | 33 | 12 | ✓ |
| M02 — Spatial Transformations & SE(3) | 36 | 45 | 36 | 36 | 36 | 6 | ✓ |
| M03 — Camera Geometry & Perception | 32 | 32 | 32 | 32 | 32 | 4 | ✓ |
| M04 — Forward Kinematics (DH) | 32 | 32 | 32 | 32 | 32 | 4 | ✓ |
| M05 — Inverse Kinematics | 32 | 32 | 32 | 32 | 32 | 4 | ✓ |
| M06 — Jacobians & Differential Motion | 32 | 32 | 32 | 32 | 32 | 4 | ✓ |
| M07 — Trajectory Generation & Planning | 32 | 32 | 32 | 32 | 32 | 4 | ✓ |
| M08 — Feedback Control & Real-Time (ROS 2) | 32 | 32 | 32 | 32 | 32 | 4 | ✓ |
| M09 — System Integration | 32 | 32 | 32 | 32 | 32 | 4 | — |
| M10 — Digital Twin Capstone | 32 | 32 | 32 | 32 | 32 | 4 | ✓ |
| **Total** | **325** | **367** | **326** | **325** | **325** | **50** | **9** |

**Canonical totals** (excluding duplicates): 325 lessons · **325 canonical notebooks** · 326 diagrams · 325 quizzes · 325 answer keys · 50 demos · 9 midpoint assessments. The 367 notebook figure includes 42 orphan duplicates (see Issue 1).

## 2. Consistency checks — PASS

- **Lesson / quiz / answer-key / nav parity.** In every module the lesson count equals the quiz count, the answer-key count, and the number of `mkdocs.yml` nav entries (33 / 36 / 32×8 = 325 each). No coverage gaps.
- **Diagram naming.** All diagrams follow `mMM-lN-slug.svg`; per-module counts match lesson counts, with M1 carrying one intentional extra (lesson 1.1 ships two figures, 34 total). No orphan SVGs outside the `mMM-lN` pattern.
- **Page-header consistency.** Every lesson H1 follows `# Lesson X.Y — Title` (em-dash) across all ten modules.
- **Demo injection.** All 50 demo files follow `lessonNN_*.html` and inject correctly via the module-namespaced path `demos/moduleMM/<file>` (M1 = 12, M2 = 6, M3–M10 = 4 each).
- **Generated site.** `site_src/` contains exactly 325 lesson pages; a figure is injected on all 325, a quiz on all 325, and a demo on the 50 demo lessons.
- **Generator.** `MODULES` lists all ten module codes; unit-title coverage resolves for every module (strict build succeeds — see Phase 2).
- **No duplicate lesson files** within any module; **no nested duplicate `physical-ai-curriculum/` folder** (a previously-noted artifact, now absent); **no leftover throwaway build scripts** (`tools/` holds only the reusable `_m9_nbbuild.py` and `_m9_quizbuild.py`).

## 3. Issues found (non-blocking)

**Issue 1 — Orphan duplicate notebooks (42).** M1 contains 33 `lessonNN_*.ipynb` notebooks in addition to the 33 canonical `M01_U..L.._*.ipynb` notebooks the generator actually injects; M2 contains 9 such `lessonNN_*.ipynb` duplicates alongside its 36 canonical `M02_U..L..` notebooks. The generator and nav reference only the `M..U..L..` scheme for M1/M2 (verified: 0 nav references to `module01/notebooks/lesson*`), so the 42 `lessonNN` notebooks are unreferenced orphans. *Impact:* repository clutter only; no effect on the built site. *Recommendation:* remove in the cleanup pass.

**Issue 2 — Stale flat copies in `site_src/` (45).** The current generator copies demos and quizzes to module-namespaced paths (`site_src/demos/moduleMM/` — 50 files; `site_src/quizzes/moduleMM/` — 325 files), all referenced. An earlier generator emitted flat copies; **12 flat demo copies** (`site_src/demos/*.html`) and **33 flat quiz copies** (`site_src/quizzes/*.html`) remain and are referenced by no page (verified: 0 pages reference a flat path). *Impact:* stale build artifacts in the generated tree only. *Recommendation:* clear the flat copies (and ideally have the generator wipe `site_src/demos` and `site_src/quizzes` before regenerating).

**Issue 3 — Stray spec file in a demos folder.** `modules/module01/demos/lesson01_trace_the_loop_spec.md` is a design-spec markdown living among demo HTML. *Impact:* cosmetic; it is not a `.html` demo and is not injected. *Recommendation:* relocate to a specs/notes folder or remove.

**Issue 4 — Stale engine backups (2).** `engine/m8_engine_B_backup.py` and `engine/m8_engine_C_backup.py` are development snapshots retained during Module 8 production. *Impact:* none on the build. *Recommendation:* remove or move to an archive branch.

**Issue 5 — Sparse `· demo` nav annotations.** The nav carries 23 `· demo` markers against 50 injected demos. Demo injection is driven by file presence, not the marker, so no demo is missing — but the nav annotation is incomplete. *Impact:* cosmetic discoverability only. *Recommendation:* optionally annotate all demo lessons, or drop the convention for consistency.

**Issue 6 — Two coexisting notebook-naming conventions.** M1/M2 use descriptive `MNN_UNN_LX_Y_Title.ipynb`; M3–M10 use `lessonNN_slug.ipynb`. The generator supports both, so nothing is broken, but the inconsistency is worth recording. *Impact:* none functionally. *Recommendation:* leave as-is for v1.0 (renaming risks churn); document the dual convention.

**Issue 7 — M9 has no midpoint assessment.** Nine of ten modules ship a midpoint assessment; Module 9 (Integration) intentionally does not. *Impact:* none — this matches the Module 9 design and tracker. *Recommendation:* record as intentional, not a gap.

## 4. Cross-reference integrity

- Every lesson page resolves a figure, a quiz, and (where applicable) a demo to a file that exists; no broken figure/quiz/demo references were found in the generated pages.
- Diagram, quiz, and answer-key inventories are one-to-one with lessons (canonical scheme).
- The notebook orphans (Issue 1) and stale `site_src` demo copies (Issue 2) are *unreferenced* — they do not produce broken links; they are surplus, not missing.

## 5. Audit verdict

The curriculum is **structurally sound and consistent**. All correctness-level checks pass; the only findings are hygiene items that do not affect the built site or the learner experience. The repository is fit to proceed to publication-readiness review, with an optional cleanup pass recommended before the v1.0 tag.

*Phase 1 complete. No content was modified.*
