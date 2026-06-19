# Release Execution Plan — curriculum-v1.0
*Phase 6 — Release Execution Plan · Release Engineer · 2026-06 · plan only; nothing is executed here*

EXECUTIVE SUMMARY

**Status:** Local QA executed and green; remote steps handed off. The recommended hygiene cleanup and a `--strict` re-gate were run in the sandbox (325 pages, exit 0, 701 refs / 0 broken, notebooks now 325). Push / tag-on-origin / GitHub Release / Pages **cannot be performed from the sandbox** (no git credentials: `git push` returns "could not read Username for github.com"), so those steps are packaged for execution in an authenticated environment.

**Findings (confirmed via `git ls-remote`):** `origin/main` = `f5db8eae` = tag **`module09-complete`** — Modules 1–9 are already committed and tagged on origin. The release delta to reach v1.0 is therefore **Module 10 + the v1.0 artifacts** (provided as `curriculum-v1.0-release-bundle.zip`). The local sandbox clone is behind (HEAD = `858e779` = `module08-complete`) and is disposable.

**Issues:** (1) No push credentials in the sandbox — remote steps run in your environment. (2) Recurring merge-conflict files keep local/complete with `--ours`: `curriculum/master_progress.md`, `curriculum/ARCHITECT_DECISIONS.md`, `curriculum/PROJECT_STATE.md`, `mkdocs.yml`. (3) Pages "Source = GitHub Actions" is a one-time UI setting.

**Recommendations:** Apply the bundle on top of `origin/main` (module09-complete), apply the listed deletions, re-gate `--strict`, commit, tag `module10-complete` + `curriculum-v1.0`, push commits then tags, cut the Release, enable Pages.

**Next:** Run the **Bundle-based handoff** section below in an authenticated clone.

---

## Bundle-based handoff (authenticated environment)

A release bundle `curriculum-v1.0-release-bundle.zip` is provided. It contains the full Module 10 delta (32 lessons, 32 notebooks, 32 quizzes, 4 demos, 32 SVGs, 34 answer keys, midpoint assessment, the `module10/twin/` substrate), all v1.0 reports, the updated tracking files, `mkdocs.yml` (M10 nav), `tools/generate_site_pages.py` (M10 registered), and `.github/workflows/deploy-pages.yml`.

```bash
# in a fresh, authenticated clone already at origin/main (module09-complete)
git fetch origin --tags && git checkout main && git pull --ff-only origin main

# 1) apply the v1.0 delta
unzip -o curriculum-v1.0-release-bundle.zip -d .

# 2) apply the cleanup DELETIONS (a zip cannot delete; do it explicitly)
git rm -q modules/module01/notebooks/lesson*.ipynb modules/module02/notebooks/lesson*.ipynb
git rm -q modules/module01/demos/lesson01_trace_the_loop_spec.md
git rm -q engine/m8_engine_B_backup.py engine/m8_engine_C_backup.py
rm -f site_src/demos/*.html site_src/quizzes/*.html   # stale flat copies (regenerated)

# 3) re-gate (must reproduce the sandbox result)
PYTHONUTF8=1 python3 tools/generate_site_pages.py   # -> 325 pages (UTF-8: see note)
mkdocs build --strict                                # -> exit 0

# 4) commit, tag, push (commits before tags)
git add -A
git commit -m "Module 10 — Digital Twin Capstone COMPLETE (D-075..D-078); curriculum v1.0"
git push origin main
git tag -a module10-complete -m "Module 10 — Digital Twin Capstone complete (D-078)"
git tag -a curriculum-v1.0   -m "Physical AI Curriculum v1.0 — 10 modules, 325 lessons"
git push origin --tags
```
Then complete Step 6 (GitHub Release with `RELEASE_NOTES_v1.0.md`) and Step 7 (enable Pages → "GitHub Actions"; the workflow deploys on the push/tag). If `git pull` reports divergence instead of fast-forward, fall back to Step 3's `--allow-unrelated-histories` + `--ours` reconciliation.

**Sandbox QA already verified (so your re-gate should match):** cleanup applied → notebooks 325; `generate_site_pages.py` → 325 pages; `mkdocs build --strict` → exit 0; 701 demo/quiz/figure refs, 0 broken.

> **Note — generator encoding.** `tools/generate_site_pages.py` assumes UTF-8 and can fail on Windows under a non-UTF-8 default; prefix it with `PYTHONUTF8=1` (or `set PYTHONUTF8=1`). `tools/build_publish.py` is UTF-8-safe and needs no prefix.
>
> **Note — Pages source conflict.** This bundle includes `.github/workflows/deploy-pages.yml`, which auto-deploys the **full** site from `main` via the *GitHub Actions* Pages source. If you publish via the **`gh-pages` branch** model (module-by-module), disable that workflow so the two sources don't compete — see `publish_branch_workflow.md` → One-time setup, step 2. Keep it only if you want CI to auto-publish the full site instead.

---

## Reference: full step sequence

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
