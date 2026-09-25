+++
title = "Go experiments with platform-independent SIMD"
slug = "2026-09-25-go-platform-independent-simd"
date = 2026-09-25T19:01:00+05:30
[taxonomies]
tags = ["developer-tools", "systems"]
[extra]
source_url = "https://go.dev/blog/simd-experiment"
source_title = "Platform-independent SIMD in Go"
source_type = "blog-post"
newsletter_candidate = true
why_it_matters = "Go is trying to expose SIMD as portable, readable Go rather than architecture-specific assembly, using compiler specialization and runtime dispatch to preserve performance where hardware support exists."
saved_link = "https://go.dev/blog/simd-experiment"
saved_title = "Platform-independent SIMD in Go"
related_urls = ["https://go.dev/blog/greenteagc", "https://google.github.io/highway/en/master/index.html"]
related_titles = ["Green Tea garbage collector", "Highway portable SIMD library"]
retrieval_note = "Go blog post fetched directly; article describes the experimental Go 1.26/1.27 SIMD APIs and planned Go 1.28 extensions."
+++

**Logged at IST:** 2026-09-25 19:01 IST

**What it is:** David Chase and Junyang Shao describe Go's experimental SIMD APIs: architecture-dependent `archsimd`, plus a portable `simd` package added across Go 1.26 and 1.27.

**Gist:** Before this work, Go programs mostly had to drop to Go assembly to use CPU SIMD instructions directly. The new API stack gives performance-sensitive code a way to express vector operations in Go, while accounting for the messy reality that SIMD varies by platform: amd64 has AVX widths and features, arm64 has NEON and SVE, wasm has fixed 128-bit vectors, and mask semantics differ across families.

The portable `simd` package takes a conservative route. It removes fixed vector sizes from the public type system, exposes size-agnostic vector types such as `simd.Uint8s` and `simd.Float32s`, and supports operations that can be mapped across amd64 AVX/AVX2/AVX512, arm64 NEON, wasm SIMD, or emulated when native support is missing. Code opts in with `GOEXPERIMENT=simd`, and `GODEBUG=simd=...` can force emulation or specific vector widths for testing.

The implementation is also interesting compiler work. Go rewrites functions that mention `simd` types into specialized versions for vector lengths such as 128, 256, 512, or emulation, then dispatches at runtime high enough in the call graph to avoid per-operation overhead. The design goal is portable code that is still close to assembly performance when the source operations match the hardware.

**Newsletter angle:** A serious attempt to make SIMD feel like ordinary portable Go: architecture-aware under the hood, readable enough for humans and LLMs, and explicit about the abstraction/performance tradeoff.
