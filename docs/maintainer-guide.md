# Reading List Maintainer Guide

This repo is the source of truth for `reading-list.oddship.net` / `oddship.github.io/reading-list`.

## What lives here

- `content/notes/` — published reading notes
- `content/digests/` — digest pages and roundups
- `templates/` — Zola templates
- `.github/workflows/deploy.yml` — GitHub Pages deployment
- `skills/` — repo-local agent skills for maintaining the site and the Telegram ingest flow

## Current operating model

1. Links arrive in Telegram.
2. Bosun reads the source when feasible and logs a compact grounded entry in `/root/work-wiki/reading-log/YYYY-MM-DD.md`.
3. Selected items are backported or promoted into `content/notes/*.md` as published Zola notes.
4. Push to `main` triggers GitHub Pages deploy.

## Content conventions

Each note should include:

- `title`
- `date`
- `tags`
- `extra.source_url`
- `extra.source_type`
- `extra.status`
- `extra.newsletter_candidate`
- `extra.why_it_matters`

For X posts that primarily point somewhere else, prefer the linked article/blog/paper as `source_url` when it was actually read.
If only the X post text was accessible, keep the X URL and say so in a retrieval note.

## Publishing conventions

- Default public status for backported notes: `published`
- Keep note bodies concise and retrieval-friendly
- Preserve the strongest claim and why it matters
- Keep speculation separate from grounded source claims

## GitHub Pages notes

- During GitHub Pages hosting, `config.toml` should use:
  - `base_url = "https://oddship.github.io/reading-list"`
- After custom-domain cutover, switch it to:
  - `base_url = "https://reading-list.oddship.net"`

## Auth expectations for automation

- Repo update auth is expected via a dedicated env var for the scoped GitHub token
- Git credentials should remain scoped to `github.com/oddship/reading-list.git`
- Push permissions and Pages admin permissions are separate; do not assume one implies the other

## When updating this repo through automation

1. Modify or add note files
2. Check nav/base URL assumptions if deployment target changed
3. Commit with a descriptive message
4. Push to `main`
5. Verify the Pages workflow run succeeded
6. Check the live rendered page, not just the git push
