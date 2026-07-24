+++
title = "Watching Go's Green Tea GC move through the heap"
slug = "2026-07-24-observing-go-green-tea-gc"
date = 2026-07-24T23:44:00+05:30
[taxonomies]
tags = ["systems", "developer-tools"]
[extra]
source_url = "https://theconsensus.dev/p/2026/07/19/observing-gos-garbage-collector-old-and-new.html"
source_type = "article"
newsletter_candidate = true
why_it_matters = "Strong systems item because it makes GC behavior visible with small experiments instead of only runtime documentation, and separates Green Tea's cache-locality win from Go's remaining fragmentation limits."
saved_link = "https://theconsensus.dev/p/2026/07/19/observing-gos-garbage-collector-old-and-new.html"
retrieval_note = "Direct fetch and browser access were blocked by Cloudflare; this note is grounded in the Jina reader copy of the canonical page."
+++
**Logged at IST:** 2026-07-24 23:44 IST

**What it is:** Phil Eaton / The Consensus deep dive on observing Go’s Green Tea garbage collector and Go’s non-moving heap behavior.

**Gist:** The article starts by making Go’s heap layout visible. Small, medium, and large objects are allocated into size-segregated spans, so randomly allocated objects end up grouped by size. C# is used as a contrast: its objects are not arranged the same way, and later examples show its compacting collector moving survivors together after cleanup.

The Green Tea part is about cache locality. Go 1.26’s default collector scans spans and queues future spans rather than following every pointer as it sees one. On pointer-heavy workloads, that speeds up runs substantially. The interesting measurement lesson is that L3 cache counters alone are misleading: the useful signal shows up when the author moves to bare metal and looks at L1 MPKI, where Green Tea’s lower-level locality win becomes clear.

The remaining Go limitation is fragmentation. Because Go’s collector does not move objects, freeing 90% of objects can still leave survivors pinning almost the same number of 8KiB spans. Manual packing, or C#’s compaction, recovers the density that Go’s GC cannot recover automatically.

**Newsletter angle:** Strong systems item because it makes GC behavior visible with small experiments instead of only runtime documentation, and cleanly separates Green Tea’s cache-locality win from Go’s remaining fragmentation limits.

**Retrieval note:** Direct fetch and browser access were blocked by Cloudflare; this note is grounded in the Jina reader copy of the canonical page.
