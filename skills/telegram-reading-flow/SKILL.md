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
   - If an X post mainly points to an external article, follow the destination and read that when feasible.
   - If only the X post text is accessible, say so explicitly.
   - Completion criterion: the gist is grounded in retrieved source material or the blocker is clearly recorded.

3. Log to the work reading dropbox first.
   - Resolve the dated log file in Asia/Kolkata before writing, not the machine timezone.
   - Append compact entries to `/root/work-wiki/reading-log/YYYY-MM-DD.md`.
   - Completion criterion: the canonical work log contains the new entry.

4. Promote every useful item to the public site.
   - Convert useful items into `content/notes/*.md` with tags, source URL, a short why-it-matters field, and preserve `logged at IST` when available.
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

1. Read the strongest accessible source, including linked articles/blogs/papers when feasible.
2. Append the grounded compact entry to `/root/work-wiki/reading-log/YYYY-MM-DD.md` using the IST timestamp.
3. Dedupe against existing `content/notes/` by source URL and likely title.
4. Create or update the Zola note with full IST datetime frontmatter, approved public tags, `source_url`, `source_type`, `saved_link`, `why_it_matters`, and concise body copy.
5. Run `python3 scripts/humanize_repo_content.py`.
6. Build with Zola. If `zola` is not installed globally, use a downloaded release binary or the repo's available build path instead of skipping verification.
7. Commit with a Conventional Commit and push to `main`.
8. Check the deploy run for the pushed `HEAD` SHA.
9. Verify the live note or `/notes/` page on `https://reading-list.oddship.net/`.

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
