+++
title = "Entire's core claim is useful: from ~202k real tool calls across ~1,983 public coding-agent checkpoints, ab..."
date = 2026-05-07
[taxonomies]
tags = ["reading-log", "x-post", "historical-backfill", "agents", "ai-infra", "developer-tools", "llm-research"]
[extra]
source_url = "https://x.com/i/status/2052437618416025846"
source_type = "x-post"
status = "reviewed"
newsletter_candidate = true
why_it_matters = "this is a strong correction to the instinct that agent tooling wins mainly through lower tool latency; the bigger win may be reducing search thrash by improving first-query usefulness."
saved_link = "https://x.com/i/status/2052437618416025846"
+++
Imported from historical reading log.
- Extracted Mario Zechner's quote-post via `api.fxtwitter.com` fallback and checked the linked Entire blog post on agentic search.
- Entire's core claim is useful: from ~202k real tool calls across ~1,983 public coding-agent checkpoints, about `48.8%` were search-related, so search is a first-order agent behavior rather than a side utility.
- Their more interesting finding is that raw speed is not the main bottleneck. Making search dramatically faster (`ripgrep` → `fff`) only modestly improved end-to-end run time because tool latency was a tiny fraction of total wall clock; ranking better results mattered more than shaving milliseconds.
- Mario's gloss is the punchline: there is still low-hanging fruit in `agentic search` if builders remember older information-retrieval lessons instead of treating the problem as just faster grep.
- Why it matters: this is a strong correction to the instinct that agent tooling wins mainly through lower tool latency; the bigger win may be reducing search thrash by improving first-query usefulness.
- Good angle: `agent search looks less like a systems-speed problem and more like a ranking/IR problem from 2004 wearing an LLM hat`.
