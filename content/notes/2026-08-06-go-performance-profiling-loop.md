+++
title = "Go performance as a profiling loop, not an assembly debate"
slug = "2026-08-06-go-performance-profiling-loop"
date = 2026-08-06T18:30:00+05:30
[taxonomies]
tags = ["developer-tools", "systems"]
[extra]
source_url = "https://x.com/valyala/status/2085328770383106104"
source_type = "x-thread"
newsletter_candidate = true
why_it_matters = "The useful claim is not that Go always emits faster machine code than C or Rust. It is that production profiling, allocation removal, CPU hot-path refactoring, and fast rebuilds often dominate the practical optimization loop."
saved_link = "https://x.com/i/status/2085328770383106104"
related_url = "https://x.com/valyala/status/2084981019422150709"
related_urls = ["https://x.com/vasilios_s/status/2085005610970652917", "https://x.com/Sebishogun10/status/2085235687826100644", "https://pkg.go.dev/runtime/pprof", "https://go.dev/blog/pprof", "https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#profiling"]
retrieval_note = "Extracted the shared status, quoted reply, and parent thread via FXTwitter; followed the chain back to the root Go-vs-Rust claim; read Go runtime/pprof, Go blog pprof, and VictoriaMetrics profiling docs for context on the profiler claims."
+++
**Logged at IST:** 2026-08-06 18:30 IST

**What it is:** Aliaksandr Valialkin’s X conversation chain about Go, C, Rust, and practical optimization, with context from Go and VictoriaMetrics profiling docs.

**Gist:** The chain starts with a deliberately provocative claim: “Go is faster than Rust.” Valialkin’s actual argument is about the whole optimization loop, not a universal language benchmark. He points to two practical advantages: every Go program can expose low-overhead CPU and memory profiling, and Go rebuilds large services such as VictoriaMetrics in seconds rather than minutes.

The replies then force the claim through two narrower versions. One reply asks whether that also means Go is faster than C. Valialkin answers that Go programs are easier to optimize for high performance and low resource usage because CPU-time and allocation profilers are built in. Another reply pushes back that C programs are already likely optimized and that serious optimization means inspecting assembly, especially because Go lacks some compiler optimizations such as loop unrolling or autovectorization.

Valialkin’s final answer is the useful part: optimize from production evidence outward. First collect CPU and memory profiles under production workload. Then remove allocations from hot paths according to the memory profile. Then refactor hot-path code according to the CPU profile. Only after those steps fail to produce enough improvement should you consider assembly-level tuning. His claim is that the last step is unnecessary in most practical cases, which is why Go works well for fast and lean VictoriaMetrics-family systems.

The supporting docs line up with that framing. Go’s `runtime/pprof` writes runtime profiling data in the pprof format, `go test` has standard `-cpuprofile` and `-memprofile` paths, and the Go pprof blog uses profiling to turn a slow program into one that is much faster and uses far less memory. VictoriaMetrics’ own docs expose `/debug/pprof/heap` and `/debug/pprof/profile` endpoints for memory and CPU profiling.

**Newsletter angle:** Useful antidote to language-war benchmarking. The better question is not “which language is faster in the abstract?” but “which stack makes it cheap to observe the real production bottleneck, change the hot path, rebuild, and repeat?”
