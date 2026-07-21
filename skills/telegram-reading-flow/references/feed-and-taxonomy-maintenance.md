# Feed and taxonomy maintenance

Use this when maintaining the public reading-list site, especially after the user reports bad tags, missing RSS feeds, or archive navigation problems.

## Public feed model

The site should expose multiple feeds, not only the all-site feed:

- All site: `/rss.xml` and `/atom.xml`
- Notes: `/notes/rss.xml` and `/notes/atom.xml`
- Digests: `/digests/rss.xml` and `/digests/atom.xml`
- Per tag: `/tags/<tag>/rss.xml` and `/tags/<tag>/atom.xml`

For Zola:

- Keep `generate_feeds = true` in `config.toml` for the global feed.
- Keep `feed = true` on the `tags` taxonomy.
- Add `generate_feeds = true` to section `_index.md` files that need section-specific feeds, especially `content/notes/_index.md` and `content/digests/_index.md`.
- Link section feeds in archive templates so users can discover them.
- Link per-tag feeds from the tag index and individual tag pages.

## Public tag model

Public tags are reader-facing topic lanes only. They are not ingestion metadata.

Default approved public tags:

- `agents`
- `ai-infra`
- `developer-tools`
- `llm-research`
- `org-design`
- `security`
- `systems`
- `other`

`other` is a holding lane for worthwhile notes that do not fit the stable taxonomy. It is better than inventing a one-off novelty tag. When `other` exceeds 20 notes, audit it and either:

1. refile items into existing tags, or
2. create a genuinely reusable new public tag if a coherent cluster has emerged.

Do not put these in `taxonomies.tags`:

- source mechanics: `x-post`, `article`, `video`, `paper`, `reading-log`
- import state: `historical-backfill`
- digest mechanics: `digest`, `weekly-reading`, `newsletter`
- one-off host/domain slugs like `github-com`, `bun-com`, `medium-com`
- one-off narrow labels unless they are likely to become a real browsing lane

Store source mechanics in `[extra]` fields such as `source_url`, `source_type`, `saved_link`, `newsletter_candidate`, and `why_it_matters`.

## Ingest rule

When ingesting a new note:

1. Start with the approved public tags.
2. Reuse existing tags whenever the fit is good enough.
3. Prefer 1 to 3 strong tags over 4 weak ones.
4. Use `other` only when none of the stable lanes fits.
5. Create a new public tag only if it will group multiple notes and a reader would actually browse it.
6. Before committing, run or replicate the tag audit and confirm there are no non-approved tags and `other` is not over threshold. If the repo has `skills/telegram-reading-flow/scripts/audit_tags.go`, that script should fail when `other` has more than 20 notes so the threshold cannot be ignored.

## Verification checklist

After taxonomy/feed changes, verify live URLs, not just the build or deploy:

- `/tags/` shows only the approved topic lanes.
- `/notes/rss.xml` returns note entries and no digest entries.
- `/digests/rss.xml` returns digest entries and no note entries.
- A representative tag feed, such as `/tags/agents/rss.xml`, returns only matching notes.
- Old mechanics/domain tags do not appear as tag pages or visible tag labels.
