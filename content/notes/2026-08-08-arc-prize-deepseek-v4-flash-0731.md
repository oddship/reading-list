+++
title = "ARC Prize verifies DeepSeek V4 Flash 0731 on ARC-AGI"
slug = "2026-08-08-arc-prize-deepseek-v4-flash-0731"
date = 2026-08-08T11:56:00+05:30
[taxonomies]
tags = ["ai-infra", "developer-tools", "llm-research"]
[extra]
source_url = "https://arcprize.org/results/deepseek-v4-flash-0731"
source_type = "benchmark"
saved_link = "https://news.ycombinator.com/item?id=49214008"
related_url = "https://arcprize.org/results/deepseek-v4-flash-0731"
related_urls = ["https://news.ycombinator.com/item?id=49214008", "https://hn.algolia.com/api/v1/items/49214008", "https://reading-list.oddship.net/notes/2026-08-01-simon-willison-deepseek-v4-flash-0731/"]
newsletter_candidate = true
why_it_matters = "This gives the DeepSeek V4 Flash price-performance story a verified ARC-AGI anchor, not just anecdotal coding-agent reports."
retrieval_note = "Read the ARC Prize result page directly and used the Hacker News Algolia item API for discussion context."
+++
**Logged at IST:** 2026-08-08 11:56 IST

**What it is:** ARC Prize's verified result page for `DeepSeek V4 Flash 0731`, plus the Hacker News discussion around it.

**Gist:** ARC Prize reports DeepSeek V4 Flash 0731 at max effort scoring 89.0% on ARC-AGI-1 Semi-Private at about $0.02 per task and 61.4% on ARC-AGI-2 Semi-Private at about $0.04 per task. The high and low reasoning variants step down to 87.0%/56.0% and 84.0%/46.0%.

That makes the result interesting as a cost-to-capability marker. The HN discussion is mostly reading it as a practical threshold moment: not necessarily frontier SOTA, but cheap enough that many coding-agent, CI-agent, monitoring, and bulk-analysis workflows become easier to justify.

There is a caveat worth keeping attached to the result. Several commenters point out that API price is not a clean efficiency measure because subsidies, scale, and inference optimizations can distort it. Active parameters per token, flops, or joules would be better metrics, but they are not consistently available across models.

**Newsletter angle:** This pairs with the earlier DeepSeek V4 Flash notes as the benchmark anchor. The larger story is not just cheaper chat, it is the point where multi-stream agentic work starts to look operationally cheap enough to run by default.
