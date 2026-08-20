---
name: telegram-reading-flow
description: Use when processing reading links dropped in Telegram and turning them into grounded reading-log entries or publishable Zola notes.
version: 1.1.0
author: Bosun
license: MIT
metadata:
  hermes:
    tags: [telegram, reading-list, curation, zola]
    related_skills: [reading-list-repo-maintenance]
---

# Telegram Reading Flow

## Overview

This skill captures the operating model for the Telegram-to-reading-list pipeline.
Links arrive in Telegram first, get grounded against the actual source when feasible, are logged compactly in the work reading log, and every useful item is then promoted into the public site.

This is a publish-by-default workflow. A useful link drop is not complete when it is only saved to `/root/work-wiki/reading-log/`; it is complete only after the repo note exists, the site builds, the change is pushed, the deploy succeeds, and the live site is checked when feasible. Leave an item log-only only when the user clearly asks for private/backlog-only capture, or when source access is too weak to publish a grounded public note.

## When to Use

Use when:
- links are dropped into the work Telegram thread
- a note needs to be logged for later review
- prior reading-log items need to be backported into the Zola site
- the assistant is deciding whether a link is ready for publication

Do not use when:
- the task is unrelated to reading links or curation
- the user wants direct long-form drafting without the logging step

## Workflow

1. Identify the source type.
   - X post, blog post, essay, paper, video, repo, or roundup.
   - Completion criterion: each shared link is classified.

2. Read the strongest available source.
   - Treat X/Twitter as discovery and provenance, not automatically as the source.
   - If an X post mainly points to an external article, blog, paper, repo, product page, or video, expand the URL/card and read that destination when feasible.
   - If only the X post text is accessible, preserve the post text or a close description and say so explicitly in the retrieval note.
   - Do not publish from tweet-card/title metadata alone when a real linked website exists but was not read.
   - Completion criterion: the gist is grounded in retrieved source material or the blocker is clearly recorded.

3. Log to the work reading dropbox first.
   - Resolve the dated log file in Asia/Kolkata before writing, not the machine timezone.
   - Append compact entries to `/root/work-wiki/reading-log/YYYY-MM-DD.md`.
   - Completion criterion: the canonical work log contains the new entry.

4. Promote every useful item to the public site.
   - Convert useful items into `content/notes/*.md` with tags, source URL, a short why-it-matters field, and preserve `logged at IST` when available.
   - For X-linked destinations, set `source_url` to the actual website that was read, keep the incoming tweet as `saved_link`, add the canonical tweet as `related_url` when distinct, and add archive fields when available (`source_archive_url`, `saved_archive_url`).
   - Tag thoughtfully: use only the compact public topic vocabulary (`agents`, `ai-infra`, `developer-tools`, `llm-research`, `org-design`, `security`, `systems`, `other`) unless a genuinely reusable new category is needed. Keep source mechanics, import state, digest grouping, and host/domain labels in metadata, never in `taxonomies.tags`. Use `other` only when none of the stable lanes fits, and audit it once it passes 20 notes.
   - Avoid host/domain tags unless the source itself is the story or the host is a meaningful recurring lens.
   - Do not wait for a separate "publish" instruction for routine work-thread link drops. Rohan has delegated this repo upkeep.
   - Completion criterion: the Zola note is concise, grounded, tagged deliberately, committed, pushed, deployed, and visible on the live site without waiting for a separate publish decision.

5. Preserve the distinction between capture and heavier synthesis.
   - The reading log is still the intake layer, but useful notes should move into the repo by default.
   - Completion criterion: the local log stays canonical and the public site stays current.

6. Treat historical imports differently from live curation.
   - For older OpenClaw or Drive-era backfills, prefer local work-reading logs first, then missing OpenClaw memory files, then weekly draft markdowns for digest pages.
   - Preserve provenance when the historical wording is imported as-is.
   - Keep importer runs incremental: add missing pages, but do not delete/rebuild already curated public notes or digests because that churns stable URLs.
   - When adding or backfilling digest pages, run `python3 scripts/link_digest_notes.py` so digest source URLs link back to the relevant public note entries.
   - If a historical entry is title-only because access was blocked and no gist was extracted, leave it log-only rather than publishing a public note from title-only evidence.
   - Completion criterion: old material is recoverable in the site without pretending every item was freshly curated by hand.

7. Run a humanizer pass before committing public-facing prose.
   - Clean up AI-ish phrasing and strip em dashes unless the user explicitly asked for them.
   - Completion criterion: content promoted into the repo reads naturally and respects the user's punctuation preferences.

8. Keep the local and repo-local workflow skills aligned.
   - When this workflow changes, patch the local `~/.hermes/skills/openclaw-imports/work-reading-dropbox/SKILL.md` too unless the difference is intentionally repo-specific.
   - Also sync durable playbook changes into `docs/maintainer-guide.md` and this repo's local skills in the same commit.
   - Completion criterion: Bosun does not carry conflicting versions of the same reading workflow across local and repo contexts.

## Link-drop completion contract

The short repo playbook lives at `docs/link-drop-playbook.md`; keep it synced with this section.

For a normal useful work-thread link drop, finish all of these before replying:

1. Read the strongest accessible source, including linked articles/blogs/papers/repos/product pages when feasible. For X links, expand and read the actual destination unless the tweet itself is the source.
2. Append the grounded compact entry to `/root/work-wiki/reading-log/YYYY-MM-DD.md` using the IST timestamp.
3. Dedupe against existing `content/notes/` by source URL and likely title.
4. Create or update the Zola note with full IST datetime frontmatter, approved public tags, `source_url`, `source_type`, `saved_link`, `why_it_matters`, and concise body copy.
   - The public page renders distinct source links, so preserve `saved_link`, `related_url`, and optional archive URLs rather than collapsing everything into a single X link.
   - If tweet or YouTube links appear in the body, include the repo's Zola shortcodes `{{< tweet id="..." url="..." >}}` or `{{< youtube id="..." url="..." >}}` near the source link. X embeds must stay opt-in via the site's local placeholder and browser `localStorage` consent. For broad backfills, run `python3 scripts/backfill_social_embeds.py`.
5. If the item is folded into a digest, run `python3 scripts/link_digest_notes.py` so the digest points back to the note entry.
6. Run `python3 scripts/humanize_repo_content.py`.
7. Build with Zola. If `zola` is not installed globally, use a downloaded release binary or the repo's available build path instead of skipping verification.
8. Commit with a Conventional Commit and push to `main`.
9. Check the deploy run for the pushed `HEAD` SHA.
10. Verify the live note or `/notes/` page on `https://reading-list.oddship.net/`.

If any step is blocked, report the exact unfinished state, for example: `logged but not published`, `committed but deploy failed`, or `deployed but live verification is stale/blocked`.

## Tagging guidance

- Use only the current public topic vocabulary by default: `agents`, `ai-infra`, `developer-tools`, `llm-research`, `org-design`, `security`, `systems`, `other`.
- Reuse one of those tags whenever it fits cleanly. Prefer a stable small vocabulary over one-off novelty tags.
- Use `other` only when none of the stable lanes fits. When `other` grows past 20 notes, audit it and either refile items into existing tags or introduce a genuinely reusable new category.
- Never put `reading-log`, `x-post`, `article`, `historical-backfill`, `digest`, `weekly-reading`, or host/domain slugs in `taxonomies.tags`.
- Prefer at most 2 to 4 meaningful topical tags per note.
- Create a new topical tag only when it is likely to group several current or future notes in a way a reader would actually browse.
- Avoid host/domain tags unless the publisher or product itself is the point of the note and is likely to recur.
- If a note only weakly fits a tag, leave it out. Sparse but reliable tagging is better than noisy coverage.
- Before introducing a new tag, search the repo for close existing tags and pick the closest stable term if it is good enough.
- Use `references/tagging-guidance.md` as the longer-lived taxonomy policy.
- Use `scripts/audit_tags.go` with `go run skills/telegram-reading-flow/scripts/audit_tags.go /root/reading-list-site` when auditing the current tag vocabulary.

## Common Pitfalls

1. Summarizing an X-linked article without actually opening the article.
2. Publishing every captured link without curation.
3. Losing the retrieval note when only partial source access was possible.
4. Writing verbose notes that are hard to scan later.
5. Letting imported historical titles stay too raw when a small editorial cleanup would make the site much more readable.
6. Committing user-facing prose without a humanizer pass, especially when it leaves AI-ish phrasing or em dashes the user dislikes.
7. Stopping after the local reading log and saying "logged" when the expected deliverable is a live public note.
8. Letting a public note depend on a tweet staying live instead of preserving the actual destination link and enough context for link rot.

## Verification Checklist

- [ ] Link accounted for
- [ ] Source actually read or blocker recorded
- [ ] Work reading log updated when applicable
- [ ] Public note is concise and grounded
- [ ] Useful items were promoted to the repo without waiting for a separate publish prompt
- [ ] Historical imports preserve provenance and do not overstate what was actually read
- [ ] Humanizer pass completed before commit
- [ ] Zola build passed
- [ ] Commit pushed and deploy succeeded
- [ ] Live note or `/notes/` page verified
