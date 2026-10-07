+++
title = "Hooking into the Go toolchain with -toolexec"
slug = "2026-10-06-hooking-into-go-toolchain"
date = 2026-10-06T17:03:00+05:30
[taxonomies]
tags = ["developer-tools", "systems"]
[extra]
source_url = "https://internals-for-interns.com/posts/hooking-into-the-go-toolchain/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "The Go command exposes a powerful interception point for observing and rewriting compiler inputs without modifying the compiler, with practical caveats around build-cache correctness."
source_title = "Hooking into the Go Toolchain"
saved_link = "https://x.com/jespinog/status/2107071564025905583"
saved_title = "Jesús Espino shares a guest post on Go's -toolexec"
related_urls = ["https://github.com/kakkoyun/hooking-into-the-go-toolchain", "https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation"]
related_titles = ["Companion repo with runnable experiments", "OpenTelemetry Go compile-time instrumentation (otelc)"]
retrieval_note = "Read the article and companion repository. The article's experiments use Go 1.27.1 on macOS and require Go 1.25 or newer; source rewriting through -toolexec is a workaround, not a supported dedicated compiler extension point."
+++
**Logged at IST:** 2026-10-06 17:03 IST

**What it is:** A hands-on explanation of `go build -toolexec`, written by Kemal Akkoyun and hosted by Jesús Espino.

**Gist:** `-toolexec` routes each compiler, assembler, and linker invocation through a wrapper you choose. The article builds from a simple build-time stopwatch to source rewriting, injecting imports, `//go:linkname` hooks, and cache pitfalls, then connects the techniques to `otelc`. The build cache can make rewritten builds surprising, so the experiments isolate their caches and discuss keeping cache identity honest.

**Why it matters:** This is a surprisingly capable seam for build instrumentation and experiments, but it is not a stable, first-class source-rewriting API. The runnable examples make the risks concrete rather than hiding them behind an abstraction.

**Source read:** https://internals-for-interns.com/posts/hooking-into-the-go-toolchain/; https://github.com/kakkoyun/hooking-into-the-go-toolchain

{{ tweet(id="2107071564025905583", url="https://x.com/jespinog/status/2107071564025905583") }}
