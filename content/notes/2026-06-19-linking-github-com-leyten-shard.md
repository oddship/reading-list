+++
title = "linking github.com/leyten/shard"
slug = "2026-06-19-linking-github-com-leyten-shard"
date = 2026-06-19
[taxonomies]
tags = ["reading-log", "x-post", "historical-backfill", "ai-infra", "developer-tools", "llm-research", "systems"]
[extra]
source_url = "https://x.com/i/status/2067222629421895939"
source_type = "x-post"
newsletter_candidate = true
why_it_matters = "concrete datapoint that internet-scale multi-host inference may be usable, not just a curiosity."
saved_link = "https://x.com/i/status/2067222629421895939"
+++
**What it is:** X post by @leyten linking `github.com/leyten/shard`

**Gist:** Shard is a WAN-distributed pipeline-parallel LLM inference engine that splits a frontier-size model across GPUs on separate machines; claim is ~30 tok/s for GLM-5.2 744B across 6 RTX PRO 6000s in 6 US states using speculative decoding, async pipelining, and a CUDA-graphed draft model.

**Newsletter angle:** “frontier inference without a datacenter” / distributed serving as systems engineering rather than centralized infra.

**Notes:** extracted via FXTwitter API + GitHub README.
