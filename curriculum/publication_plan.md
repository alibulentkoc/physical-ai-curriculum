# Publication Plan
*Phase 5 — Publication Plan · Release Manager · 2026-06 · plan only; nothing is pushed or deployed here*

EXECUTIVE SUMMARY

**Status:** Plan ready. The curriculum is complete and builds clean; this plan defines how to release it as **curriculum-v1.0**, deploy the site to GitHub Pages, and maintain versioned releases. No push or deploy is performed.

**Findings:** Remote is `github.com/alibulentkoc/physical-ai-curriculum` on `main`. The local clone is stale relative to `origin/main` (local tags show only `module08-complete`), so a sync is the first publication step. Toolchain pins `mkdocs-material` + `pymdown-extensions`; `site/` is gitignored; no `gh-pages` branch or CI workflow exists yet.

**Issues:** Two prerequisites before tagging: (1) run the recommended hygiene cleanup (orphan notebooks, stale flat `site_src` copies) and a final `--strict` rebuild; (2) reconcile the stale local clone with `origin/main` before pushing.

**Recommendations:** Sync → cleanup → strict rebuild → push Modules 9–10 with tags → establish Pages (CI) → cut `curriculum-v1.0`.

**Next:** Await approval. Per directive, stop here; execute only on go-ahead.

---

## 1. GitHub release strategy

**Branch model.** `main` is the single source of truth (current model). Releases are immutable **git tags** with attached GitHub Releases (notes + optional zipped artifacts).

**Pre-push reconciliation (required — the clone is perpetually stale).** Before any push:
1. `git fetch origin` and reset the tracked files that consistently diverge to the local/complete versions where appropriate.
2. `git pull origin main --allow-unrelated-histories` (the histories have diverged across sessions).
3. Resolve the recurring conflict files by keeping the local, complete copies: `git checkout --ours` for `curriculum/master_progress.md`, `curriculum/ARCHITECT_DECISIONS.md`, `curriculum/PROJECT_STATE.md`, and `mkdocs.yml`.
4. Commit the merge.

**Push order.** Push commits first, then tags, separately:
```
git push origin main
git push origin --tags
```

**Tags to create (in order):**
- `module09-complete` — if not already on origin (local shows only `module08-complete`; verify against origin during sync).
- `module10-complete` — Module 10 sign-off.
- `curriculum-v1.0` — the full-curriculum release (see §6).

**GitHub Release notes** for `curriculum-v1.0` should summarize: 10 modules / 325 lessons / 50 demos, the through-line, the completion reports, and known hygiene notes from the audit.

## 2. GitHub Pages deployment strategy

The site is generated (`site_src/` → `mkdocs build --strict` → `site/`), and `site/` is gitignored — so deployment must build in CI, not commit `site/`.

**Recommended: GitHub Actions → Pages.** Add `.github/workflows/docs.yml` that, on push to `main` (and on tags):
1. checks out, sets up Python, `pip install -r requirements-docs.txt`;
2. runs `python3 tools/generate_site_pages.py` (regenerate `site_src/` pages);
3. runs `mkdocs build --strict` (the release gate — fail the deploy on non-zero exit);
4. publishes `site/` to GitHub Pages (Pages "GitHub Actions" source, or `mkdocs gh-deploy --force` to a `gh-pages` branch).

**Prerequisites:** enable Pages in repo settings; ensure `requirements-docs.txt` pins the exact toolchain (and `mkdocs-static-i18n` later, if/when multilingual — see the translation strategy). Keep the generator step in CI so authoring edits never require a hand-built `site_src`.

## 3. Module-by-module publication strategy

All ten modules are already complete, so "publication" is a release ordering, not staged authoring:

- **Single-shot v1.0 (recommended).** Publish the whole site at once under `curriculum-v1.0`; the curriculum is designed to be consumed as one connected arc, and the strict build already validates all 325 pages together.
- **Phased visibility (optional).** If a staged rollout is desired, gate module visibility via nav rather than partial builds (the build is all-or-nothing under `--strict`). Modules can be announced in learning order (M1 → M10) while the full site is live.
- **Per-module artifacts.** Each module already carries its own installment + completion reports in `curriculum/`; these can anchor per-module release notes or announcements.

## 4. Review workflow

- **Pre-release review gate:** the audit report (Phase 1) + readiness report (Phase 2) must both read PASS, with the hygiene cleanup applied and a final `mkdocs build --strict` exit 0.
- **Change review (post-v1.0):** content changes land via pull request to `main`; CI runs generate + `--strict` build as a required check. No merge unless the strict build passes.
- **Architect sign-off:** retain the existing decision-log discipline — material changes recorded in `ARCHITECT_DECISIONS.md`; `PROJECT_STATE.md` and `master_progress.md` updated to match.
- **Reviewer checklist per change:** one figure per lesson; notebook self-verifies ("All checks passed."); recap lessons keep `## Coding Exercise` + `## Knowledge Check`; no emoji in SVGs; edits made in authoring sources, not generated trees.

## 5. Versioning strategy

- **Scheme:** semantic-style for the curriculum as a whole — `curriculum-vMAJOR.MINOR`.
  - **MAJOR** — structural changes (modules added/removed/reordered, spine or convention changes).
  - **MINOR** — additive or corrective content within the existing structure (new demos, lesson revisions, translations, fixes).
- **Module tags** (`moduleNN-complete`) remain as production milestones; **curriculum tags** (`curriculum-vX.Y`) mark released states of the whole.
- **Locked conventions are version-stable:** ξ = [v; ω], geometric Jacobian primary, w = ∏σᵢ, DLS from the SVD, arm L₁ = 0.4/L₂ = 0.3 — changing any is a MAJOR bump.
- **Changelog:** maintain a `CHANGELOG.md` (or use GitHub Releases) keyed to curriculum tags; `ARCHITECT_DECISIONS.md` remains the deep history.

## 6. curriculum-v1.0 release plan

**Definition of done for v1.0:** all 10 modules complete (✓), strict build green at 325 pages (✓), audit + readiness PASS (✓), hygiene cleanup applied, clone synced, pushed with tags, Pages live.

**Sequence (execute on approval):**
1. **Cleanup (optional but recommended):** remove the 42 orphan notebooks (M1/M2 `lessonNN_*.ipynb`), clear the 45 stale flat copies in `site_src/demos` + `site_src/quizzes`, remove the stray `lesson01_trace_the_loop_spec.md` from M1 demos and the two `engine/*_backup.py` files. *(All are unreferenced; this is hygiene, not correctness.)*
2. **Regenerate + gate:** `python3 tools/generate_site_pages.py` → `mkdocs build --strict` (must be exit 0, 325 pages).
3. **Sync the clone** with `origin/main` per §1 (fetch, pull `--allow-unrelated-histories`, resolve the four conflict files with `--ours`, commit).
4. **Push:** `git push origin main`; then create and push tags `module09-complete` (if missing on origin), `module10-complete`, and `curriculum-v1.0`; `git push origin --tags`.
5. **Establish Pages:** add the CI workflow (§2), enable Pages, confirm the deployed site renders all 325 pages, demos, and quizzes.
6. **Cut the GitHub Release** for `curriculum-v1.0` with notes summarizing the curriculum, totals, completion reports, and the audit's hygiene notes.
7. **Announce** (optional) in learning order, linking the published site.

**Rollback:** tags are immutable; if a defect is found post-release, fix on `main`, rebuild `--strict`, and cut `curriculum-v1.0.1` (MINOR) rather than moving the tag.

*Phase 5 complete. Nothing was pushed or deployed; awaiting approval to execute.*
