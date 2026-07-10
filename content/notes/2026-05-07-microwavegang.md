+++
title = "microwavegang"
slug = "2026-05-07-microwavegang"
date = 2026-05-07
[taxonomies]
tags = ["reading-log", "x-post", "historical-backfill", "llm-research"]
[extra]
source_url = "https://x.com/i/status/2051873677998956851"
source_type = "x-post"
status = "reviewed"
newsletter_candidate = true
why_it_matters = "this is a vivid, shareable example of `data quality showing up directly in loss curves`, which is often easier to remember than abstract warnings about web-scale corpora."
saved_link = "https://x.com/i/status/2051873677998956851"
+++
Imported from historical reading log.
- Extracted main post via `api.fxtwitter.com` fallback; the quoted tweet and attached screenshot provide the actual context.
- Claim: a GPT-3 training loss spike was traced to scraped data from a `microwavegang` subreddit/community full of text like `MMMMMMMMMMMMMM` and `BEEP BEEP BEEP`, and the spike disappeared after dataset cleanup.
- The screenshot is funny but the underlying lesson is serious: weird narrow-distribution junk data can create visible optimization pathologies, and simple data cleaning can remove dramatic training instability.
- Why it matters: this is a vivid, shareable example of `data quality showing up directly in loss curves`, which is often easier to remember than abstract warnings about web-scale corpora.
- Good angle: `sometimes model progress is not smarter optimization but just deleting the internet's microwave noises from the batch`.
