# Release Execution Plan — curriculum-v1.0
*Phase 6 — Release Execution Plan · Release Engineer · 2026-06 · plan only; nothing is executed here*

EXECUTIVE SUMMARY

**Status:** Plan ready. Concrete push / tag / release / Pages / rollback sequences for `module10-complete` and `curriculum-v1.0`. No git, push, or deploy action is performed; execute only on approval.

**Findings:** Remote `github.com/alibulentkoc/physical-ai-curriculum`, branch `main`. The **local clone is behind**: its last commit is Module 8 (`858e779`, tag `module08-complete`), and **all of Module 9 + Module 10 + the release artifacts exist only as uncommitted working-tree changes** (~365 paths). Origin may already carry Module 9 (a `module09-complete` tag was created in a prior session from a different clone state). This must be reconciled before tagging v1.0.

**Issues:** (1) Local/origin divergence — fetch and inspect before committing. (2) Recurring conflict files on merge: `curriculum/master_progress.md`, `curriculum/ARCHITECT_DECISIONS.md`, `curriculum/PROJECT_STATE.md`, `mkdocs.yml` (keep local/complete with `--ours`). (3) Pages source must be set to "GitHub Actions" once before the first deploy.

**Recommendations:** Execute the steps in order; gate everything on `mkdocs build --strict` exit 0; push commits before tags; never move a published tag.

**Next:** Await approval. On approval, run Step 0 first (fetch + inspect) and adapt the commit step to whatever origin already contains.

---

## Preconditions (verify before starting)

- [ ] `mkdocs build --strict` exits 0 at 325 pages (re-confirmed this phase).
- [ ] Audit + readiness reports read PASS (re-confirmed this phase).
- [ ] (Optional, recommended) hygiene cleanup applied — see Step 1.
- [ ] Working tree reviewed; you know what is being committed.

## Step 0 — Reconnaissance (always first; the clone is stale)

```bash
git fetch origin --tags
git log --oneline origin/main -5         # what does origin actually contain?
git tag -l 'module*' 'curriculum-*'      # which tags exist locally
git ls-remote --tags origin              # which tags exist on origin
```
Decide from the output whether Module 9 is already committed/tagged on origin. This determines the commit scope in Step 2 (M9+M10, or M10 only).

## Step 1 — Optional hygiene cleanup (then re-gate)

All items are unreferenced (see `release_audit_report.md`); removing them is hygiene, not correctness.

```bash
# orphan duplicate notebooks (M1: 33, M2: 9)
git rm -q modules/module01/notebooks/lesson*.ipynb
git rm -q modules/module02/notebooks/lesson*.ipynb
# stray spec in demos; stale engine backups
git rm -q modules/module01/demos/lesson01_trace_the_loop_spec.md
git rm -q engine/m8_engine_B_backup.py engine/m8_engine_C_backup.py
# stale flat copies in the generated tree (regenerated anyway)
rm -f site_src/demos/*.html site_src/quizzes/*.html

# regenerate + re-gate
python3 tools/generate_site_pages.py
mkdocs build --strict        # MUST be exit 0
```

## Step 2 — Commit sequence

Commit the release content. If Step 0 shows Module 9 is **not** yet on origin, include it; otherwise commit Module 10 + the release artifacts only.

```bash
git add -A
git commit -m "Module 10 — Digital Twin Capstone COMPLETE (D-075..D-078); curriculum v1.0 release artifacts

- Module 10: 8 units, 32 lessons/notebooks/SVGs/quizzes/keys, 4 demos, midpoint
- Twin substrate modules/module10/twin/ (sync/simulate/monitor/predict/adapt)
- Completion + curriculum reports; release audit/readiness/overview/notes/plans
- Pages workflow .github/workflows/deploy-pages.yml (prepare only)
- Tracking files updated (PROJECT_STATE, master_progress, ARCHITECT_DECISIONS)"
```
*(If M9 is also uncommitted locally and absent on origin, either include it in this commit or make a preceding `module09-complete` commit so history is clean.)*

## Step 3 — Reconcile with origin

```bash
git pull origin main --allow-unrelated-histories     # histories diverged across sessions
# resolve the recurring conflicts by keeping the local, complete versions:
git checkout --ours curriculum/master_progress.md \
                    curriculum/ARCHITECT_DECISIONS.md \
                    curriculum/PROJECT_STATE.md \
                    mkdocs.yml
git add curriculum/master_progress.md curriculum/ARCHITECT_DECISIONS.md \
        curriculum/PROJECT_STATE.md mkdocs.yml
git commit --no-edit                                 # complete the merge
mkdocs build --strict                                # re-gate after merge
```

## Step 4 — Push sequence (commits before tags)

```bash
git push origin main
```

## Step 5 — Tag sequence

Create annotated tags, then push tags separately. (`module09-complete` only if Step 0 showed it missing on origin.)

```bash
# git tag -a module09-complete -m "Module 9 — System Integration complete (D-074)"   # if missing
git tag -a module10-complete -m "Module 10 — Digital Twin Capstone complete (D-078)"
git tag -a curriculum-v1.0   -m "Physical AI Curriculum v1.0 — all 10 modules, 325 lessons"
git push origin --tags
```

## Step 6 — GitHub Release sequence

1. GitHub → Releases → "Draft a new release".
2. Tag: `curriculum-v1.0`. Title: "Physical AI Curriculum v1.0".
3. Body: paste `curriculum/RELEASE_NOTES_v1.0.md`.
4. (Optional) attach a source zip of the curriculum.
5. Publish. (Optionally also publish a release on `module10-complete` as a milestone.)

## Step 7 — Pages deployment sequence

1. One-time: repo **Settings → Pages → Source = "GitHub Actions"**.
2. The `Deploy Pages` workflow (`.github/workflows/deploy-pages.yml`) triggers on the Step 4 push to `main` (and on the `curriculum-v*` tag). It regenerates pages, runs `mkdocs build --strict` (the gate), and deploys `./site`.
3. Verify the Actions run is green and the published site renders all 325 pages, 50 demos, and 325 quizzes.
4. Confirm the live Pages URL in the workflow run summary.

## Rollback sequence

Tags are immutable — never move a published tag. To recover from a post-release defect:

```bash
# fix on main
git checkout main
# ...apply fix in authoring sources...
python3 tools/generate_site_pages.py && mkdocs build --strict   # re-gate
git add -A && git commit -m "Fix: <description>"
git push origin main
# cut a patch release instead of moving v1.0
git tag -a curriculum-v1.0.1 -m "Patch: <description>"
git push origin --tags
```
- The push to `main` re-triggers the Pages workflow, redeploying the corrected site.
- If a deploy itself fails, the prior successful Pages deployment remains live; fix and re-run the workflow (no tag change needed).
- For a catastrophic bad release, mark the GitHub Release as a pre-release/draft and point users to the last good tag while preparing the patch.

## Target tags (this release)

- **`module10-complete`** — Module 10 sign-off.
- **`curriculum-v1.0`** — the full-curriculum public release.

*Phase 6 complete. No git, push, tag, release, or deploy action was performed; awaiting approval to execute.*
