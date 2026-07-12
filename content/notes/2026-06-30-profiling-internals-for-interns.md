+++
title = "Profiling | Internals for Interns"
slug = "2026-06-30-profiling-internals-for-interns"
date = 2026-06-30
[taxonomies]
tags = ["reading-log", "x-post", "historical-backfill", "ai-infra", "llm-research", "systems"]
[extra]
source_url = "https://x.com/i/status/2071530061727949272"
source_type = "x-post"
newsletter_candidate = true
why_it_matters = "strong runtime internals explainer; useful for debugging/perf literacy and for understanding what pprof is actually showing."
saved_link = "https://x.com/i/status/2071530061727949272"
+++
**Gist:** all five profiles emit the same pprof structure; the core difference is collection model, CPU samples asynchronously via signal + ring buffer, heap/block/mutex aggregate in per-stack tables in place, goroutine snapshots stacks on demand.

**Newsletter angle:** “pprof is one file format over three collection strategies” is a clean framing hook.

**Retrieval note:** extracted via FXTwitter API + linked article fetch.
