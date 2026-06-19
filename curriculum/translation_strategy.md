# Translation Strategy
*Phase 4/5 — Translation Readiness · Release Manager · 2026-06 · no content is translated here*
*Re-confirmed 2026-06 for the curriculum-v1.0 release-execution phase. Covers: English canonical source, language-switch architecture, GitHub Pages multilingual deployment, translation workflow, and maintenance workflow.*

EXECUTIVE SUMMARY

**Status:** Translation-ready in design; not yet a published multilingual site. The curriculum was authored with translation in mind (uniform templates, English-authoritative, per-lesson language-support blocks), so translation is a tractable, additive effort rather than a rebuild.

**Findings:** Every lesson uses the same 12-section Markdown template and already ships a **Global Learning Support** block offering on-demand AI translation into Español, 中文 (Simplified), and Türkçe with English as the authoritative source. The published site is MkDocs + Material (English-only today; no i18n plugin configured). Math, code, and notebooks are language-neutral; the main translatable surface is lesson prose (325 files), plus quiz/demo UI text and SVG label text for a *fully* localized site.

**Issues:** No blockers. The cost driver is scale: 325 lessons × N languages, and full localization additionally touches 325 quizzes, 50 demos, and 326 diagrams (text labels).

**Recommendations:** Keep the existing learner-driven AI translation as the zero-maintenance baseline; layer a static multilingual site (`mkdocs-static-i18n` + Material's language selector) on top for any language that warrants a first-class published edition, prose-first.

**Next:** Phase 5 (Publication Plan).

---

## 1. Translatability assessment

The curriculum is unusually well-positioned for translation:

- **Uniform structure.** Every lesson is the same 12-section template with an AI Learning Companion and a Global Learning Support block. A translator (human or AI) faces one predictable shape 325 times, not 325 bespoke documents.
- **English-authoritative by design.** The content explicitly designates English as the source of truth and instructs that robotics/math terminology stay in English where appropriate — so translations track one canonical version.
- **Language-neutral cores.** LaTeX math, Python notebooks, and the locked symbol conventions (ξ = [v; ω], w = ∏σᵢ, etc.) do not translate; they are shared across all languages.
- **Separation of authoring and presentation.** Authoring sources live in `modules/`; the published site is generated into `site_src/`. Translations can be managed as parallel authoring sources without disturbing the build.

What raises cost for a *fully* localized published site (beyond prose):
- **Quizzes (325)** contain question/answer/feedback UI text embedded in self-contained HTML.
- **Demos (50)** contain UI labels and captions in HTML/JS.
- **Diagrams (326 SVGs)** contain text labels baked into the SVG.

These can be deferred: a prose-only translation already delivers most of the learning value, with quizzes/demos/diagrams localized later or left in English with translated captions.

## 2. Recommended architecture

A **two-tier** approach that preserves what already works and adds a published multilingual site only where it pays off:

**Tier 1 — Learner-driven translation (already shipped, zero maintenance).** The per-lesson Global Learning Support block lets any learner obtain the lesson in Español/中文/Türkçe (or any language) via an AI assistant, anchored to the English source. This is the default for the long tail of languages and requires no build changes.

**Tier 2 — Static multilingual site (opt-in, per language).** For languages that warrant a first-class published edition, add the **`mkdocs-static-i18n`** plugin and Material's built-in language selector. Structure translated docs as a parallel tree under `site_src/` (e.g. `site_src/<page>.es.md` suffix mode, or a `/es/` folder mode), English as the default/fallback. Keep the generator English-first and feed it translated lesson sources per language.

This keeps English as the single authoritative pipeline, makes each additional language purely additive, and lets the project ship one language at a time without holding up the rest.

## 3. Language-switch approach

- Use **Material for MkDocs' native language selector** (`theme.language` + `extra.alternate`), which renders a top-bar switcher across editions.
- Drive page-level translations with **`mkdocs-static-i18n`** (suffix mode `page.es.md` / `page.zh.md` / `page.tr.md`, or folder mode `/es/...`). Missing translations **fall back to English** automatically, so a partially-translated language still ships a complete site.
- Set per-language `site_name`/`site_description`; keep URLs stable (`/` English, `/es/`, `/zh/`, `/tr/`).
- Leave math, code, and symbol conventions untranslated; translate prose, headings, nav titles, and (optionally, later) quiz/demo/diagram text.

## 4. GitHub Pages approach

- Publish with **`mkdocs gh-deploy`** (or a GitHub Actions workflow running `mkdocs build --strict` then deploying `site/` to the `gh-pages` branch). The multilingual build produces one site tree containing all enabled languages under their path prefixes — a single Pages deployment serves every language.
- Pin the toolchain in `requirements-docs.txt` (add `mkdocs-static-i18n`) so CI builds are reproducible.
- Gate every deploy on `mkdocs build --strict` exit 0, exactly as the monolingual site is gated today; the language fallback ensures strict mode passes even before a language is fully translated.

## 5. Translation workflow

1. **Freeze the English source** for a release (tagged, e.g. `curriculum-v1.0`) so translators work against a stable target.
2. **Prose-first pass.** For each lesson, translate the 12 sections + nav title into `page.<lang>.md`, preserving headings, LaTeX, code, and the locked terminology in English. The uniform template makes this batchable.
3. **AI-assisted drafting, human review.** Use the existing Global Learning Support prompt as the drafting instruction, then have a fluent reviewer correct terminology and tone. Translations remain anchored to the English source.
4. **Defer non-prose.** Leave quizzes, demos, and SVG labels in English initially (or add translated captions); schedule their localization as a later milestone per language.
5. **Build and verify** with `mkdocs build --strict`; confirm the language selector lists the new edition and that untranslated pages fall back cleanly.

## 6. Maintenance workflow

- **English is the single source of truth.** Every content change lands in English first; translations are downstream.
- **Track drift.** When an English lesson changes, flag its translations as stale (a simple front-matter `source_rev:` or a translation-status table per language). Re-translate only the changed sections — the template structure localizes drift to specific sections.
- **Per-language completeness is optional.** Fallback-to-English means a language can ship incrementally and stay valid under `--strict`.
- **Keep diagrams/quizzes/demos English by default** until a language reaches enough prose coverage to justify localizing them; this avoids maintaining N copies of every interactive artifact prematurely.
- **CI gate unchanged:** strict build per deploy; pin plugin versions.

## 7. Verdict

Translation is an **additive, prose-first effort**, not a re-architecture. The baseline (learner-driven AI translation) already covers any language at zero cost; a published multilingual site is a well-trodden MkDocs/Material path (`mkdocs-static-i18n` + language selector + English fallback) that can be adopted one language at a time after v1.0.

*Phase 4 complete. No content was translated.*
