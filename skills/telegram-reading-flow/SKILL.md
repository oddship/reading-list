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
   - Append compact entries to `/root/work-wiki/reading-log/YYYY-MM-DD.md`.
   - Completion criterion: the canonical work log contains the new entry.

4. Promote selectively to the public site.
   - Convert chosen items into `content/notes/*.md` with tags, source URL, status, and a short why-it-matters field.
   - Completion criterion: the Zola note is concise, grounded, and publication-ready.

5. Preserve the distinction between capture and publication.
   - Not everything logged needs to be public immediately.
   - Completion criterion: the public site stays curated rather than becoming a raw dump.

6. Treat historical imports differently from live curation.
   - For older OpenClaw or Drive-era backfills, prefer local work-reading logs first, then missing OpenClaw memory files, then weekly draft markdowns for digest pages.
   - Preserve provenance when the historical wording is imported as-is.
   - Completion criterion: old material is recoverable in the site without pretending every item was freshly curated by hand.

7. Run a humanizer pass before committing public-facing prose.
   - Clean up AI-ish phrasing and strip em dashes unless the user explicitly asked for them.
   - Completion criterion: content promoted into the repo reads naturally and respects the user's punctuation preferences.

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
- [ ] Publication decision is explicit rather than accidental
- [ ] Historical imports preserve provenance and do not overstate what was actually read
- [ ] Humanizer pass completed before commit
