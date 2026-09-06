+++
title = "Go adds a production goroutine leak profiler"
slug = "2026-09-04-go-goroutine-leak-profiler"
date = 2026-09-04T19:16:00+05:30
[taxonomies]
tags = ["systems", "developer-tools"]
[extra]
source_url = "https://go.dev/blog/goroutine-leak-profiles"
source_type = "x-post"
newsletter_candidate = true
why_it_matters = "Runtime-level leak detection can catch production concurrency failures that tests and ordinary goroutine profiles miss."
saved_link = "https://x.com/rseroter/status/2095574797342146630"
retrieval_note = "Tweet extracted via FXTwitter; linked Go blog fetched directly; attached GIF thumbnail inspected and found decorative, not substantive."
+++

**Logged at IST:** 2026-09-04 19:16 IST

**What it is:** Richard Seroter pointed to the Go blog post announcing Go 1.27's goroutine leak profiler.

**Gist:** Go 1.27 adds a `goroutineleak` profile through `runtime/pprof`, and through `/debug/pprof/goroutineleak` when `net/http/pprof` is installed. It targets goroutines permanently blocked on channels or standard `sync` primitives, using GC reachability and liveness analysis to keep false positives low.

The important caveat is scope. It does not cover file or network I/O, direct syscalls, custom primitives, or cases where leaked primitives remain reachable from globals or runnable goroutines.

**Newsletter angle:** Runtime diagnostics are moving closer to the failure modes people actually hit in long-running services.
