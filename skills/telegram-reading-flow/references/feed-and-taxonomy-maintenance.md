# Feed and taxonomy maintenance

## Feed model

The public site should expose tiered feeds:

- all site: `/rss.xml` and `/atom.xml`
- notes only: `/notes/rss.xml` and `/notes/atom.xml`
- digests only: `/digests/rss.xml` and `/digests/atom.xml`
- each public tag: `/tags/<tag>/rss.xml` and `/tags/<tag>/atom.xml`

Zola requirements:

- `config.toml` keeps `generate_feeds = true` and `feed_filenames = ["atom.xml", "rss.xml"]`.
- `content/notes/_index.md` and `content/digests/_index.md` keep `generate_feeds = true`.
- `config.toml` taxonomy entry keeps `{ name = "tags", feed = true }`.

## Public tags

Use these public tags by default:

- `agents`
- `ai-infra`
- `developer-tools`
- `llm-research`
- `org-design`
- `security`
- `systems`
- `other`

`other` is a temporary holding lane for worthwhile notes that do not fit the stable taxonomy. Do not create one-off tags just to avoid `other`.

When `other` grows past 20 notes, audit it. Either:

1. refile items into existing tags if they fit after a clearer read, or
2. create a genuinely reusable new public tag if the cluster is coherent and likely to recur.

## Never-public tags

Do not put these in `taxonomies.tags`:

- source mechanics: `x-post`, `article`, `video`, `paper`
- workflow provenance: `reading-log`, `historical-backfill`
- digest mechanics: `digest`, `weekly-reading`, `newsletter`
- host/domain slugs such as `github-com`, `bun-com`, or `example-com`

Put this information in `[extra]` metadata instead.

## Audit command

Run this before committing taxonomy/feed changes:

```bash
go run skills/telegram-reading-flow/scripts/audit_tags.go /root/reading-list-site
```

The audit fails if:

- a public tag is outside the approved vocabulary
- `other` exceeds 20 notes

## Verification

After deploy, check:

```bash
curl -fsSL https://reading-list.oddship.net/tags/ | grep -E 'Agents|AI Infra|Developer Tools|LLM Research|Org Design|Security|Systems'
curl -fsSL https://reading-list.oddship.net/notes/rss.xml | grep '<rss'
curl -fsSL https://reading-list.oddship.net/digests/rss.xml | grep '<rss'
curl -fsSL https://reading-list.oddship.net/tags/agents/rss.xml | grep '<rss'
```
