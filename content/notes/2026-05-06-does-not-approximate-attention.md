+++
title = "does not approximate attention"
slug = "2026-05-06-does-not-approximate-attention"
date = 2026-05-06
[taxonomies]
tags = ["reading-log", "x-post", "historical-backfill", "llm-research"]
[extra]
source_url = "https://x.com/badlogicgames/status/2051936321610842245"
source_type = "x-post"
newsletter_candidate = true
why_it_matters = ""
saved_link = "https://x.com/badlogicgames/status/2051936321610842245"
+++
Imported from historical reading log.
- Extracted main post via `api.fxtwitter.com` fallback and checked the linked SubQ technical post.
- Mario Zechner is skeptical of SubQ’s claim that SSA `does not approximate attention`; his objection is that unless ignored query-key pairs are provably zero-contribution, selective sparsification is still an approximation.
- He also flags the missing detail that really matters: how the model chooses which query-key pairs to keep.
- The linked SubQ write-up claims `content-dependent selection` routes attention only to positions that carry signal, yielding linear scaling and large prefill speedups at long context lengths.
- Useful counterweight to the earlier SubQ hype post: the key technical question is not just benchmark wins, but whether the selection mechanism preserves retrieval quality without hiding approximation debt.
- Good angle: `skeptic check on flashy sparse-attention claims`.
