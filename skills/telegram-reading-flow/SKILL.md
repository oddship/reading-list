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
Links arrive in Telegram first, get grounded against the actual source when feasible, are logged compactly in the work reading log, and only then are selected items promoted into the public site.

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
   - Tag thoughtfully: prefer reusing existing topical tags before inventing new ones, keep source-mechanics tags (`x-post`, `article`, `historical-backfill`) separate from topic tags, and only create a new topic tag when several future notes are likely to benefit from the same bucket.
   - Avoid host/domain tags unless the source itself is the story or the host is a meaningful recurring lens.
   - Completion criterion: the Zola note is concise, grounded, tagged deliberately, and committed to the repo without waiting for a separate publish decision.

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

## Tagging guidance

- Reuse existing topic tags whenever they fit cleanly. Prefer a stable small vocabulary over one-off novelty tags.
- Treat `reading-log`, `x-post`, `article`, and `historical-backfill` as mechanics/provenance tags, not the main topical taxonomy.
- Prefer at most 2 to 4 meaningful topical tags per note.
- Create a new topical tag only when it is likely to group several current or future notes in a way a reader would actually browse.
- Avoid host/domain tags unless the publisher or product itself is the point of the note and is likely to recur.
- If a note only weakly fits a tag, leave it out. Sparse but reliable tagging is better than noisy coverage.
- Before introducing a new tag, search the repo for close existing tags and pick the closest stable term if it is good enough.

## Common Pitfalls

1. Summarizing an X-linked article without actually opening the article.
2. Publishing every captured link without curation.
3. Losing the retrieval note when only partial source access was possible.
4. Writing verbose notes that are hard to scan later.
5. Letting imported historical titles stay too raw when a small editorial cleanup would make the site much more readable.
6. Committing user-facing prose without a humanizer pass, especially when it leaves AI-ish phrasing or em dashes the user dislikes.

## Verification Checklist

- [ ] Link accounted for
- [ ] Source actually read or blocker recorded
- [ ] Work reading log updated when applicable
- [ ] Public note is concise and grounded
- [ ] Useful items were promoted to the repo without waiting for a separate publish prompt
- [ ] Historical imports preserve provenance and do not overstate what was actually read
- [ ] Humanizer pass completed before commit
