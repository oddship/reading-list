+++
title = "The data race that wasn't a bug, and the one that was"
slug = "2026-10-06-net-http-request-body-race"
date = 2026-10-06T19:24:00+05:30
[taxonomies]
tags = ["systems"]
[extra]
source_url = "https://victoriametrics.com/blog/http-race-condition/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "An early HTTP response can arrive while Go's transport is still reading a request body, making buffer reuse in retry logic race with the transport goroutine."
source_title = "The Data Race That Wasn't a Bug (and the One That Was)"
saved_link = "https://x.com/valyala/status/2107469590921949645"
saved_title = "VictoriaMetrics on two net/http race-detector findings"
related_urls = ["https://github.com/golang/go/issues/81445", "https://x.com/jespinog/status/2107441828253336046"]
related_titles = ["Go issue #81445", "Jesús Espino's article announcement"]
retrieval_note = "Read the VictoriaMetrics article and the linked Go issue. The post discusses Go 1.27 internals; the benign-vs-bug distinction is specific to the reported use case, not a blanket claim that races are harmless."
+++
**Logged at IST:** 2026-10-06 19:24 IST

**What it is:** A VictoriaMetrics post by Jesús Espino and Vadim Alekseev investigating two race-detector reports involving Go's HTTP client.

**Gist:** With HTTP/1.1, `net/http` has a `writeLoop` that can still be sending a request body after the caller has received an early response. If retry code resets and rewrites a shared buffer backing that body, it can race with that read. The article separates this real buffer-reuse bug from another reported race that was not a problem in their particular use case, and explains why they fixed one but intentionally left the other.

**Why it matters:** `Client.Do` returning a response does not necessarily mean every transport-side read of the request body has finished. Request-body ownership and reuse matter in retry paths; the linked Go issue remains open for investigation in the retrieved version.

**Source read:** https://victoriametrics.com/blog/http-race-condition/; https://github.com/golang/go/issues/81445

{{ tweet(id="2107469590921949645", url="https://x.com/valyala/status/2107469590921949645") }}
