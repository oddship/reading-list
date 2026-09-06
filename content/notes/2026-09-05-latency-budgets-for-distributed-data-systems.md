+++
title = "Latency is a budget, not a virtue"
slug = "2026-09-05-latency-budgets-for-distributed-data-systems"
date = 2026-09-05T09:16:00+05:30
[taxonomies]
tags = ["systems"]
[extra]
source_url = "https://www.bitsxpages.com/p/lessons-in-latency"
source_type = "x-post"
newsletter_candidate = true
why_it_matters = "S3-style storage tradeoffs only make sense against latency budgets, p99 targets, average-latency capacity, cache tiering, and request-cost economics."
saved_link = "https://x.com/almoggavra/status/2095894755129618905"
retrieval_note = "Tweet extracted via FXTwitter; linked Substack article fetched directly; no substantive attached media beyond the article card."
+++

**Logged at IST:** 2026-09-05 09:16 IST

**What it is:** Almog Gavra's Bits & Pages post giving a framework for reasoning about latency in distributed data systems, framed around the S3-versus-performance tradeoff.

**Gist:** Gavra treats latency as a product budget. Below the acceptable threshold, shaving latency is mainly a capacity and cost question rather than a user-experience win. Little's Law connects average latency to throughput capacity, while p99 latency consumes the user-visible budget.

For storage choices, the answer depends on whether cheaper, slower media plus more concurrency or replicas beats faster, more expensive media. Caches matter because hot data lowers average latency. Object storage adds its own economics: per-request cost, write batching, durability, and read freshness become part of the design.

**Newsletter angle:** Stop arguing “S3 good” or “S3 bad” in the abstract. Compare budgets, tails, caches, and costs.
