+++
title = "One month without AI"
slug = "2026-09-26-one-month-without-ai"
date = 2026-09-26T19:31:00+05:30
[taxonomies]
tags = ["agents", "developer-tools"]
[extra]
source_url = "https://blog.bustikiller.com/2026/09/25/one-month-without-ai.html"
source_title = "One month without AI"
source_type = "essay"
newsletter_candidate = true
why_it_matters = "A first-person counterweight to AI-coding productivity stories: the author argues that agentic coding made him faster at producing PRs but worse at owning, reviewing, and learning from the code."
saved_link = "https://x.com/badlogicgames/status/2103844577643831494"
saved_title = "Mario Zechner recommending One month without AI"
related_url = "https://x.com/badlogicgames/status/2103844577643831494"
related_title = "Recommendation post on X"
retrieval_note = "X post extracted via FXTwitter; linked Bustikiller essay read directly. The tweet is provenance, not the primary source."
+++

**Logged at IST:** 2026-09-26 19:31 IST

**What it is:** Bustikiller's personal essay about stopping AI-assisted coding after realizing it was degrading his ownership of code, review quality, and day-to-day satisfaction as a developer.

**Gist:** The arc is familiar and uncomfortable. The author starts with autocomplete and small generated functions, then moves to pasting Jira tickets into agents, running multiple worktrees in parallel, and letting tools write commits and PR descriptions. At first it feels like leverage. Over time it becomes a focus-management problem: many AI-generated PRs still require careful review, fixes, CI follow-up, and context switching. Some tasks that could have been a focused hour turn into days of supervising generated work.

The deeper critique is about judgment. The author says he stopped fully understanding what he was pushing, accepted code he would previously have rejected, and eventually failed a basic test-quality check in review. That shame pushed him to stop using AI, return to TDD, keep PRs small, write terse descriptions, ask peers about architecture, and regain confidence that he understood every changed line.

{{ tweet(id="2103844577643831494", url="https://x.com/badlogicgames/status/2103844577643831494") }}

**Newsletter angle:** A useful human-counterexample to simple AI-productivity narratives. The cost is not only hallucinated code; it is attention fragmentation, review load, diminished code ownership, and slow erosion of engineering taste.
