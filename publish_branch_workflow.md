# Two-Branch Publish Workflow
*Release Engineer · 2026-06 · main = full source · publish branch = what GitHub Pages serves*

EXECUTIVE SUMMARY

**Status:** Tooling built and verified; deploy steps handed off to your authenticated environment. A scoping tool (`tools/build_publish.py`) produces a content-pruned, nav-scoped, `--strict`-clean build for any module subset, so you can preview the whole site, take it down, and then release module by module — all without ever trimming `main`.

**Findings:** Verified in the sandbox — `--modules all` → 325 pages / 10 modules, `--modules 1` → 33 pages / 1 module, `--modules 1 2 3` → 101 pages / 3 modules; every scoped build is `mkdocs build --strict` exit 0 and contains only the chosen modules (no unpublished content leaks by URL).

**Issues:** Deploy/push requires credentials not present in the sandbox; run the `gh-deploy` / git steps in your authenticated clone. Pages "Source = Deploy from a branch → gh-pages" is a one-time setting.

**Recommendations:** Use `main` = full source, `gh-pages` = served slice, `moduleNN-complete` tags = approved milestones. Publish the full site to inspect, deploy the placeholder to unpublish, then deploy growing slices.

**Next:** Run Phase A (full preview) in your authenticated clone.

---

## Branch model

| Branch | Contains | Role |
|---|---|---|
| `main` | the complete curriculum source (all 10 modules) | source of truth — never trimmed |
| `gh-pages` | the **built** site for the currently-published slice | what GitHub Pages serves |
| tags `moduleNN-complete`, `curriculum-v1.0` | approved milestones on `main` | provenance / rollback points |

The full source always lives in `main`. What students see is whatever built HTML is on `gh-pages`. Changing the published slice never touches `main`.

## The scoping tool (runs anywhere — no credentials needed)

`tools/build_publish.py` writes a pruned docs tree (`publish_src/`) and a scoped config (`mkdocs.publish.yml`) with only the requested modules. Both are gitignored on `main` (build inputs for the publish step).

```bash
python tools/build_publish.py --modules all      # full preview (1..10) -> 325 pages
python tools/build_publish.py --modules 1        # Module 1 only        -> 33 pages
python tools/build_publish.py --modules 1 2 3    # Modules 1-3          -> 101 pages
```
Then build/inspect locally with the scoped config:
```bash
mkdocs build --strict -f mkdocs.publish.yml      # must be exit 0
mkdocs serve -f mkdocs.publish.yml               # preview at 127.0.0.1:8000
```

## One-time setup

1. Ensure `mkdocs.yml` (full) and `tools/build_publish.py` are on `main` (in the v1.0 release bundle).
2. **Resolve the Pages-source conflict (important).** GitHub Pages has a *single* source. The repo also contains `.github/workflows/deploy-pages.yml`, which auto-deploys the **full** site from `main` via the *GitHub Actions* source — that competes with this branch model. For module-by-module control, **disable that workflow** so only your `gh-deploy` slices publish:
   ```bash
   git mv .github/workflows/deploy-pages.yml .github/workflows/deploy-pages.yml.disabled
   git commit -m "Disable Actions Pages auto-deploy; use gh-pages branch flow"
   git push origin main
   ```
   *(Alternatives: delete the file, or comment out its `on:` triggers. Keep it only if you instead want CI to auto-publish the full site — but then you lose module-by-module gating.)*
3. Repo **Settings → Pages → Source = "Deploy from a branch" → Branch: `gh-pages` / `(root)`**.
4. Install the toolchain: `pip install -r requirements-docs.txt` (and `pip install pyyaml`).
5. **Encoding:** `tools/generate_site_pages.py` assumes UTF-8 and can fail on Windows under a non-UTF-8 default. Prefix generation with `PYTHONUTF8=1` (shown below), or set it for the session (`set PYTHONUTF8=1` / `$env:PYTHONUTF8=1`). `tools/build_publish.py` is UTF-8-safe and does not require it.

## Phase A — Publish the FULL site, then inspect

```bash
git checkout main && git pull
python tools/build_publish.py --modules all
mkdocs build --strict -f mkdocs.publish.yml          # gate
mkdocs gh-deploy -f mkdocs.publish.yml -b gh-pages -m "Publish: full curriculum (preview)"
```
`gh-deploy` builds and force-pushes the result to `gh-pages`; Pages serves it within a minute. Inspect the live site (all 325 pages, 50 demos, quizzes).

## Phase B — Unpublish (take it down for review)

Deploy the "under review" placeholder so the URL stays valid while you review:
```bash
git checkout gh-pages
git rm -rf . >/dev/null 2>&1
cp tools/publish_placeholder/index.html ./index.html      # from main; or keep a local copy
: > .nojekyll
git add -A && git commit -m "Unpublish: curriculum under review"
git push --force origin gh-pages
git checkout main
```
*(Alternative: disable Pages, or `git push origin --delete gh-pages` for a hard takedown.)*

## Phase C — Release module by module (cumulative)

After approving each module, deploy the next growing slice. `gh-deploy` force-replaces `gh-pages`, so each deploy simply sets the published scope:

```bash
git checkout main
# after Module 1 approved:
python tools/build_publish.py --modules 1     && mkdocs build --strict -f mkdocs.publish.yml \
  && mkdocs gh-deploy -f mkdocs.publish.yml -b gh-pages -m "Publish: Module 1"
# after Module 2 approved:
python tools/build_publish.py --modules 1 2   && mkdocs build --strict -f mkdocs.publish.yml \
  && mkdocs gh-deploy -f mkdocs.publish.yml -b gh-pages -m "Publish: Modules 1-2"
# ...continue 1-3, 1-4, ... or in batches (1 2 3), (1 2 3 4 5), etc.
python tools/build_publish.py --modules all   && mkdocs build --strict -f mkdocs.publish.yml \
  && mkdocs gh-deploy -f mkdocs.publish.yml -b gh-pages -m "Publish: full curriculum"
```
The published nav and content show only the listed modules; everything else stays private on `main`.

## Revert / rollback a published slice

Because `gh-deploy` always force-pushes a complete build, **reverting is just re-deploying the desired scope**:
```bash
python tools/build_publish.py --modules 1 2   # back to the last approved slice
mkdocs build --strict -f mkdocs.publish.yml
mkdocs gh-deploy -f mkdocs.publish.yml -b gh-pages -m "Revert: Modules 1-2"
```
Or reset the branch to a previous published commit and force-push:
```bash
git checkout gh-pages && git reset --hard <last-good-commit> && git push --force origin gh-pages
```
Either way, only the website changes — `main` is untouched.

## Optional: scoped deploy from CI

If you prefer a button over the terminal, the Pages workflow can be switched to a manual `workflow_dispatch` with a `modules` input that runs `build_publish.py <modules>` then deploys — same scoping, triggered from the Actions tab. The manual `gh-deploy` flow above is recommended for the controlled, module-by-module rollout you described.

## Verification already done (sandbox)

| Scope | Pages | Modules in build | `--strict` |
|---|---:|---:|:--:|
| `--modules all` | 325 | 10 | exit 0 |
| `--modules 1 2 3` | 101 | 3 | exit 0 |
| `--modules 1` | 33 | 1 | exit 0 |

*Deploy steps (`gh-deploy`, branch pushes, Pages setting) require your authenticated environment; the scoping/build steps are verified here.*
