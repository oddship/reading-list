+++
title = "Go's json/v2 API becomes generally available"
slug = "2026-08-25-go-json-v2-migration-guide"
date = 2026-08-25T20:19:00+05:30
[taxonomies]
tags = ["developer-tools", "systems"]
[extra]
source_url = "https://go.dev/blog/jsonv2"
source_title = "A new Go API for JSON"
source_type = "article"
newsletter_candidate = true
why_it_matters = "Go 1.27 makes a redesigned JSON API generally available, bringing stricter defaults, composable options, streaming primitives, and room to fix compatibility-constrained behavior without breaking encoding/json users."
saved_link = "https://x.com/golang/status/2118388202327433685?a=0CFY9HLv3YYXm338F7o&s=35"
saved_title = "Go announces a new API for JSON"
related_url = "https://antonz.org/go-json-v2"
related_title = "A practical migration guide to Go's json/v2"
related_urls = ["https://go.dev/doc/go1.27"]
related_titles = ["Go 1.27 release notes"]
retrieval_note = "Read the Go team's announcement and Go 1.27 release notes, as well as Anton Zhiyanov's migration guide already covered in this note. The announcement says encoding/json/v2 and encoding/json/jsontext are stable and generally available in Go 1.27."
+++
**Logged at IST:** 2026-08-25 20:19 IST; updated 2026-11-05

**What it is:** The Go team's announcement that `encoding/json/v2` and `encoding/json/jsontext` are stable and generally available in Go 1.27, alongside a practical migration guide by Anton Zhiyanov.

**Gist:** The v2 API addresses longstanding limitations in the original `encoding/json`: ambiguous or surprising behavior around invalid UTF-8, duplicate object names, nil slices/maps, and case-insensitive field matching; awkward option plumbing; and limitations in streaming and custom-marshaler performance. The lower-level `jsontext` package provides JSON syntax and token-level facilities, while `json/v2` builds Go-value marshaling and unmarshaling on top. A separate `/v2` namespace allows behavior to improve without breaking the Go 1 compatibility promise.

The migration guide maps the changed APIs and defaults, including composable options, streaming custom marshaling, and compatibility considerations. These changes can improve correctness and flexibility, but migration requires checking which v1 behaviors an application relies on and choosing options deliberately.

**Source read:** https://go.dev/blog/jsonv2

**Related:** [Go 1.27 release notes](https://go.dev/doc/go1.27); [Anton Zhiyanov's migration guide](https://antonz.org/go-json-v2).

**Newsletter angle:** A substantial standard-library evolution: stricter JSON behavior and a more composable, streaming API, delivered under a new import path to preserve compatibility for existing Go programs.

{{ tweet(id="2118388202327433685", url="https://x.com/golang/status/2118388202327433685") }}
