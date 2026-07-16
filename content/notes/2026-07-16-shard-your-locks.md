+++
title = "Shard your locks"
slug = "2026-07-16-shard-your-locks"
date = 2026-07-16T23:42:00+05:30
[taxonomies]
tags = ["systems", "developer-tools"]
[extra]
source_url = "https://strebkov.dev/posts/shard-your-locks/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "Strong practical concurrency piece because it turns a familiar rule of thumb into a measurable systems lesson: lock striping usually beats reflexive RWMutex usage once core counts and contention rise."
saved_link = "https://strebkov.dev/posts/shard-your-locks/"
+++
**Logged at IST:** 2026-07-16 23:42 IST

**What it is:** Misha Strebkov benchmarking six Go in-memory cache designs under different read/write mixes and core counts.

**Gist:** The sharp result is that the boring “just use RWMutex for read-heavy caches” instinct does not hold up well under contention. A 256-shard striped map was the best all-around design, scaling up to about 8x faster than a single mutex at 8 cores, while RWMutex plateaued early and could even lose to a plain mutex on writes. The broader lesson is to reason about contention topology, cache-line movement, and workload skew, not just read/write ratios.

**Newsletter angle:** Strong practical concurrency piece because it turns a familiar rule of thumb into a measurable systems lesson: lock striping usually beats reflexive RWMutex usage once core counts and contention rise.
