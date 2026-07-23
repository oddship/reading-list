+++
title = "Everyone should know SIMD"
slug = "2026-07-23-everyone-should-know-simd"
date = 2026-07-23T07:25:00+05:30
[taxonomies]
tags = ["systems", "developer-tools"]
[extra]
source_url = "https://mitchellh.com/writing/everyone-should-know-simd"
source_type = "article"
newsletter_candidate = true
why_it_matters = "Strong systems and developer-tools item because it makes SIMD approachable as a practical hot-loop pattern, not a specialist-only bag of CPU-specific tricks."
saved_link = "https://x.com/i/status/2079992025261424803"
related_url = "https://x.com/mitchellh/status/2079992025261424803"
+++
**Logged at IST:** 2026-07-23 07:25 IST

**What it is:** Mitchell Hashimoto linking to his practical SIMD introduction, “Everyone Should Know SIMD,” using a Ghostty loop as the worked example.

**Gist:** Hashimoto argues that everyday SIMD should not feel scary: the common “process N values at a time” case follows a repeatable five-step shape: broadcast constants, loop one vector-width chunk at a time, do the parallel operation, reduce or store the vector result, then finish with the scalar tail. His Ghostty example turns a scalar codepoint scan into generic Zig vector code, yielding up to 4x, 8x, or 16x lane-level throughput depending on NEON, AVX2, or AVX-512, and about a 5x real end-to-end speedup on his AVX2 desktop.

**Newsletter angle:** Strong systems and developer-tools item because it makes SIMD approachable as a practical hot-loop pattern, not a specialist-only bag of CPU-specific tricks.
