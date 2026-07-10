# reading-list

Zola-powered reading garden for `reading-list.oddship.net` and `oddship.github.io/reading-list`.

## What this repo is

This repo is both:

- the public reading-list site
- the operational source of truth for how Bosun curates, backfills, and publishes reading notes

## Repo structure

- `content/notes/` — individual reading notes
- `content/digests/` — weekly/newsletter-style roundups
- `templates/` — Zola templates
- `scripts/import_historical_reading.py` — repeatable historical importer/backfill script
- `docs/maintainer-guide.md` — repo and workflow operating notes
- `skills/` — repo-local agent skills for maintenance and Telegram ingest flow

## Content model

Each note carries frontmatter plus a short body. Useful fields in `[extra]` include:

- `source_url`
- `source_type`
- `status` (`reviewed` or `published` today)
- `why_it_matters`
- `newsletter_candidate`
- `saved_link`

## Operating model

1. Links arrive in Telegram.
2. Bosun reads the strongest available source and logs a compact grounded entry under `/root/work-wiki/reading-log/YYYY-MM-DD.md`.
3. Selected items are promoted into `content/notes/`.
4. Weekly writeups become `content/digests/`.
5. Pushes to `main` deploy to GitHub Pages.

## Historical backfill

Older material came from multiple sources:

- the canonical work reading log under `/root/work-wiki/reading-log/`
- older OpenClaw workspace memory files
- older weekly draft markdown files
- prior Google Drive draft history for verification

The importer script exists so future backfills stay repeatable rather than manual.

## Commit convention

Use Conventional Commits for repo changes.

Examples:

- `feat(content): add weekly digest`
- `fix(site): correct pagination links`
- `chore(repo): ignore generated artifacts`

## Local development

```bash
zola serve
```

## Build

```bash
zola build
```
