+++
title = "HTML over the wire: SSE plus POST versus WebSockets"
slug = "2026-08-12-html-over-wire-sse-websockets"
date = 2026-08-12T19:04:00+05:30
[taxonomies]
tags = ["systems", "developer-tools"]
[extra]
source_url = "https://yagni.club/3mstlyuxe5s26"
source_type = "article"
newsletter_candidate = true
why_it_matters = "A practical transport-level argument for hypermedia apps: if you are sending HTML over the wire, SSE plus ordinary POSTs can keep HTTP/2, auth, logging, status codes, and Brotli, while WebSockets may force a second connection and weaker compression."
saved_link = "https://yagni.club/3mstlyuxe5s26"
related_urls = ["https://en.andros.dev/blog/ef4968f5/html-over-websockets-real-time-spas-with-barely-any-javascript/", "https://htmlwire.exe.xyz/", "https://tangled.org/drk.wtf/htmlwire", "https://www.rfc-editor.org/rfc/rfc7692.html"]
retrieval_note = "YAGNI Club page fetched directly; clean article text extracted through Jina reader. Demo page at htmlwire.exe.xyz opened in browser to verify the live WebSocket/SSE comparison UI."
+++
**Logged at IST:** 2026-08-12 19:04 IST

**What it is:** A YAGNI Club response to an “HTML over WebSockets” article, arguing that many HTML-over-the-wire apps should consider SSE plus normal POSTs before reaching for WebSockets.

**Gist:** The core correction is transport-level. The original WebSocket argument says one persistent connection avoids TCP and HTTP overhead, but with HTTP/2 keep-alive the page, CSS, SSE stream, and POST commands can already share the same connection. A WebSocket often means a second TCP/TLS connection plus an HTTP/1.1 upgrade, while command POSTs keep the normal HTTP request lifecycle: auth, rate limits, access logs, status codes, and errors.

The more interesting point is compression. SSE is just an HTTP response, so it can use normal content codings like Brotli. WebSocket compression is negotiated as `permessage-deflate`; the extension framework exists, but in practice Brotli did not become a WebSocket content coding. For HTML-over-the-wire, where each patch often resembles the previous one, that matters because compression can see and exploit repeated HTML, especially when the payload crosses DEFLATE’s smaller window.

The linked demo makes the claim concrete: two panes share one server/session/SQLite database/renderer, one transported over WebSocket and the other over SSE plus POST, with byte-identical HTML applied by Idiomorph. The article says a 66 KB table re-rendered on each keystroke costs about 3.4 KB over WebSocket versus 23 B over SSE, a 153× difference, because the SSE response can benefit from HTTP compression.

**Newsletter angle:** Strong systems note for boring-web/hypermedia design: the question is not “real-time needs WebSockets”, it is whether the UX needs bidirectional transport badly enough to give up HTTP’s existing semantics and compression path.
