+++
title = "Detecting Goroutine Leaks"
slug = "2026-08-18-detecting-goroutine-leaks"
date = 2026-08-18T14:15:00+05:30
[taxonomies]
tags = ["developer-tools", "systems"]
[extra]
source_url = "https://antonz.org/detecting-goroutine-leaks/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "Goroutine leaks are easy to miss in passing tests. Newer Go tooling makes leak checks more deterministic in tests and more visible in running systems."
saved_link = "https://x.com/i/status/2089355447778046064"
related_url = "https://x.com/ohmypy/status/2089355447778046064"
retrieval_note = "X post extracted via FXTwitter. The linked Anton Zhiyanov article was read directly."
+++
**Logged at IST:** 2026-08-18 14:15 IST

**What it is:** Anton Zhiyanov's walkthrough of goroutine leak detection in modern Go, comparing `goleak`, `synctest`, and the experimental `goroutineleak` pprof profile.

**Gist:** The article starts with the practical shape of a goroutine leak: goroutines blocked forever on synchronization primitives while the rest of the program keeps running. That makes leaks quieter than deadlocks and harder to catch than data races.

Zhiyanov walks through a simple unbuffered-channel example, then compares three ways to find the leak. `goleak` works today as a third-party test helper. `synctest`, production-ready in Go 1.25+, can catch blocked goroutines inside deterministic test bubbles without sleep-based timing. The newer `goroutineleak` pprof profile, experimental in Go 1.26, is less ideal for unit tests on its own but useful for inspecting running programs.

The useful distinction is test-time versus runtime detection. `synctest` helps make leak checks part of ordinary tests. The pprof profile helps diagnose leaks in deployed or long-running systems.

**Newsletter angle:** Good Go/concurrency testing note for the broader theme that reliability work improves when failure modes become observable and testable by default.

## Embedded source

{{ tweet(id="2089355447778046064", url="https://x.com/i/status/2089355447778046064") }}
