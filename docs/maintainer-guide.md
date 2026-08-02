# Reading List Maintainer Guide

This repo is the source of truth for `reading-list.oddship.net` / `oddship.github.io/reading-list`.

## What lives here

- `content/notes/`, published reading notes
- `content/digests/`, digest pages and roundups
- `templates/`, Zola templates
- `.github/workflows/deploy.yml`, GitHub Pages deployment
- `skills/`, repo-local agent skills for maintaining the site and the Telegram ingest flow

## Current operating model

1. Links arrive in Telegram.
2. Bosun reads the source when feasible and logs a compact grounded entry in `/root/work-wiki/reading-log/YYYY-MM-DD.md`, resolving the date in Asia/Kolkata.
3. Every useful item is backported or promoted into `content/notes/*.md` right away.
4. Push to `main` triggers deploy.
5. The workflow is not complete until the deploy succeeds and the live page, or at least `/notes/`, reflects the update.

Routine work-thread link drops are publish-by-default. Do not wait for a separate publish instruction unless the user clearly asks for backlog-only/private capture or the source grounding is too weak for a public note.

## Historical import sources

When backfilling old reading history, prefer this order:

1. `work-wiki/reading-log/` as the canonical current source
2. old OpenClaw work memory files for missing dates
3. old weekly draft markdown files for digest pages
4. prior Google Drive drafts only as verification/reference, not as the first write source

Current repo helper:

- `scripts/import_historical_reading.py`

The importer is incremental. It should add missing notes/digests from local history, not delete and rebuild the whole `content/notes/` or `content/digests/` tree. Preserve editorially cleaned titles and stable slugs. If an entry is title-only because the source was blocked and no gist was extracted, keep it in the local log rather than publishing a public note from title-only evidence.

Operational playbooks:

- `docs/link-drop-playbook.md`, publish-by-default checklist for normal work-thread link drops
- `scripts/link_digest_notes.py`, idempotent helper that links digest source URLs back to matching public note pages

It imports historical `content/notes/` and `content/digests/` from the local sources above without overwriting already curated pages.

## Content conventions

Each note should include:

- `title`
- `date`
- `tags`
- `extra.source_url`
- `extra.source_type`
- `extra.newsletter_candidate`
- `extra.why_it_matters`
- `logged at IST` in the body when the log captured the original arrival time

For X posts that primarily point somewhere else, treat the post as the saved/shared link and the destination as the source.

- Prefer the linked article/blog/paper/repo/product page as `source_url` when it was actually read.
- Keep the original X URL as `extra.saved_link` and add the canonical X status as `extra.related_url` when it differs.
- Add `extra.source_archive_url` or `extra.saved_archive_url` when an archive was created or found.
- If only the X post text was accessible, keep the X URL as `source_url`, preserve the post text or close description in the note/log, and say so in `retrieval_note`.
- Do not publish a note from tweet-card/title metadata alone when the real linked website was not read.

## Tagging guidance

- Reuse the current public topic tags before creating new ones: `agents`, `ai-infra`, `developer-tools`, `llm-research`, `org-design`, `security`, `systems`, `other`.
- Use `other` only as a temporary holding lane for worthwhile notes that do not fit the stable taxonomy.
- When `other` grows past 20 notes, audit it and either refile items into existing tags or introduce a genuinely reusable new category.
- Keep mechanics/provenance tags out of the public taxonomy and store that information in metadata instead.
- Do not put `reading-log`, `x-post`, `article`, `historical-backfill`, `digest`, `weekly-reading`, or host/domain labels in `taxonomies.tags`.
- Create a new tag only when it is likely to organize multiple notes meaningfully.
- When in doubt, fewer but more reliable tags are better.

## Feed conventions

- The site has an all-site feed at `/rss.xml` and `/atom.xml`.
- The notes section should keep its own feeds at `/notes/rss.xml` and `/notes/atom.xml`.
- The digests section should keep its own feeds at `/digests/rss.xml` and `/digests/atom.xml`.
- Each public tag should expose tag feeds at `/tags/<tag>/rss.xml` and `/tags/<tag>/atom.xml`.
- If feeds disappear after a template/config change, check `generate_feeds = true` on section `_index.md` files and `feed = true` on the tag taxonomy in `config.toml`.

## Publishing conventions

- Every useful note should be promoted into the repo without waiting for a separate "publish" step.
- Keep note bodies concise and retrieval-friendly.
- Preserve the strongest claim and why it matters.
- Keep speculation separate from grounded source claims.
- Prefer stable explicit slugs in note frontmatter when importer-generated titles may collide.
- Digest entries should not be dead-end source roundups. After editing or backfilling digests, run `python3 scripts/link_digest_notes.py` so cited URLs that match note metadata get compact `Reading note(s)` backlinks.

## Link-drop completion contract

For a normal useful link dropped in the work thread, complete this whole path before replying:

1. Read the strongest accessible source, following linked articles/blogs/papers/repos/product pages when feasible. For X links, expand the card/URLs and ground the note in the destination website unless the tweet itself is the only source.
2. Append the compact grounded entry to `/root/work-wiki/reading-log/YYYY-MM-DD.md` using an IST timestamp.
3. Dedupe against existing notes by source URL and likely title.
4. Create or update `content/notes/*.md` with full IST datetime frontmatter, approved public tags, source metadata, and concise public-facing prose.
5. If a digest mentions the item, run `python3 scripts/link_digest_notes.py` so the digest links to the note entry.
6. Run `python3 scripts/humanize_repo_content.py`.
7. Build with Zola. If `zola` is missing globally, use an available release binary or the same build path CI uses.
8. Commit with a Conventional Commit and push to `main`.
9. Check the deploy run for the pushed `HEAD` SHA.
10. Verify the live note or `/notes/` page on `https://reading-list.oddship.net/`.

If blocked, report the precise partial state: `logged but not published`, `note written but build failed`, `pushed but deploy failed`, or `deploy passed but live verification blocked`.

## GitHub Pages notes

- During GitHub Pages hosting, `config.toml` should use:
 - `base_url = "https://oddship.github.io/reading-list"`
- After custom-domain cutover, switch it to:
 - `base_url = "https://reading-list.oddship.net"`

## Auth expectations for automation

- Repo update auth is expected via a dedicated env var for the scoped GitHub token
- Git credentials should remain scoped to `github.com/oddship/reading-list.git`
- Push permissions and Pages admin permissions are separate; do not assume one implies the other
- Before commits, run a humanizer pass on user-facing prose and strip em dashes unless explicitly requested

## When updating this repo through automation

1. Modify or add note files
2. Check nav/base URL assumptions if deployment target changed
3. Run a humanizer pass over user-facing prose before the commit lands
4. Build with Zola
5. Commit with a Conventional Commit message
6. Push to `main`
7. Verify the deploy workflow run succeeded
8. Check the live rendered page, not just the git push
9. For site-shape changes, verify homepage, `/notes/`, pagination, and `/digests/`
10. When the workflow itself changes, update `skills/` and this guide in the same commit, then sync the matching local Hermes skill if needed
