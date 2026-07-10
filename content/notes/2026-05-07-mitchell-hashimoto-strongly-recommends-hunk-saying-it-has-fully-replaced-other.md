+++
title = "Mitchell Hashimoto strongly recommends Hunk, saying it has fully replaced other local diff viewers for him"
date = 2026-05-07
[taxonomies]
tags = ["reading-log", "x-post", "x-com", "historical-backfill"]
[extra]
source_url = "https://x.com/i/status/2052128048288567617"
source_type = "x-post"
status = "published"
newsletter_candidate = true
why_it_matters = "looks like a purpose-built diff/review surface for AI-assisted coding rather than a prettier plain diff pager."
saved_link = "https://x.com/i/status/2052128048288567617"
+++
Imported from historical reading log.
- Extracted main post via `api.fxtwitter.com` fallback and checked the linked GitHub repo.
- Mitchell Hashimoto strongly recommends `Hunk`, saying it has fully replaced other local diff viewers for him.
- `Hunk` is positioned as a review-first terminal diff viewer for agent-authored changesets.
- Notable capabilities from the repo: multi-file review stream with sidebar navigation, inline AI/agent annotations, split/stack responsive layouts, watch mode, keyboard + mouse support, pager mode, and Git difftool/pager integration.
- Install/use gist: package name `hunkdiff`; commands mirror Git workflows (`hunk diff`, `hunk show`, `hunk patch -`).
- Why it matters: looks like a purpose-built diff/review surface for AI-assisted coding rather than a prettier plain diff pager.
- Good angle: `tooling layer forming around agent-authored code review, not just code generation`.
