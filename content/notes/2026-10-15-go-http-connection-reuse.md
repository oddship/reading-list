+++
title = "Go 1.27 improves HTTP/1 connection reuse"
slug = "2026-10-15-go-http-connection-reuse"
date = 2026-10-15T10:08:00+05:30
[taxonomies]
tags = ["go", "systems", "performance"]
[extra]
source_url = "https://go.dev/blog/http-connection-reuse"
source_type = "article"
newsletter_candidate = true
why_it_matters = "A small Transport change lets ordinary response-body closing preserve more HTTP/1 connections, reducing needless connection churn without requiring callers to adopt a new pattern."
source_title = "HTTP connection reuse improvements in Go 1.27"
+++
**Logged at IST:** 2026-10-15 10:08 IST

**What it is:** A Go blog article by Nicholas Husin and Damien Neil describing improved HTTP/1 connection reuse in Go 1.27.

**Gist:** In earlier Go versions, an HTTP/1 connection could be discarded when a caller closed a response body with unread bytes. Go 1.27's `net/http.Transport` asynchronously drains a limited amount, up to 256 KB or 50 ms, to salvage reuse. The article reports roughly a 5× improvement in its repeated-request benchmark. Callers can keep closing response bodies as usual; HTTP/2 was not affected by this particular issue.

**Why it matters:** A useful performance improvement hidden behind unchanged, idiomatic Go code: fewer unnecessary connection setups, without asking application code to manage a more complicated lifecycle.

**Source:** https://go.dev/blog/http-connection-reuse
