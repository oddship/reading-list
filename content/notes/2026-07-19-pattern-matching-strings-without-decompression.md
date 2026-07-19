+++
title = "Pattern matching strings without decompression"
slug = "2026-07-19-pattern-matching-strings-without-decompression"
date = 2026-07-19T23:32:00+05:30
[taxonomies]
tags = ["systems", "developer-tools"]
[extra]
source_url = "https://spiraldb.com/blog/pattern-matching-strings-without-decompression"
source_type = "article"
newsletter_candidate = true
why_it_matters = "Strong database-systems piece because it shows compression as an execution format, not only a storage format: predicate pushdown can operate over encoded data when the codec preserves enough structure."
saved_link = "https://spiraldb.com/blog/pattern-matching-strings-without-decompression"
+++
**Logged at IST:** 2026-07-19 23:32 IST

**What it is:** Spiral/Vortex deep dive on evaluating SQL `LIKE` predicates directly over FSST-compressed strings.

**Gist:** The post explains how Vortex can match string patterns in compressed code space instead of decompressing values first. It builds deterministic finite automata over FSST symbol codes, then uses a SIMD Teddy prefilter to cheaply identify candidate positions before running the verifier. On selective patterns like ClickBench Q20’s `%google%`, the prefilter cuts candidate stops from about ten million to 44,158 and confirms 646 true matches, producing roughly 2.4x to 3.6x single-thread speedups across tested x86 machines, with smaller but still positive wins at high thread counts.

**Newsletter angle:** Strong database-systems piece because it shows compression as an execution format, not only a storage format: predicate pushdown can operate over encoded data when the codec preserves enough structure.
