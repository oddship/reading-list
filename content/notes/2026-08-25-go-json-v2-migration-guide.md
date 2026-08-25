+++
title = "Go's json/v2 migration surface"
slug = "2026-08-25-go-json-v2-migration-guide"
date = 2026-08-25T20:19:00+05:30
[taxonomies]
tags = ["developer-tools", "systems"]
[extra]
source_url = "https://antonz.org/go-json-v2"
source_type = "article"
newsletter_candidate = true
why_it_matters = "A practical map of a standard-library migration where correctness defaults, streaming APIs, compatibility options, and performance trade-offs all change together."
saved_link = "https://x.com/ohmypy/status/2092210706137374961"
related_url = "https://x.com/ohmypy/status/2092210706137374961"
retrieval_note = "FXTwitter extraction succeeded and resolved the Antonz article; the article HTML was read directly."
+++
**Logged at IST:** 2026-08-25 20:19 IST

**What it is:** Anton Zhiyanov's interactive guide to Go's new `json/v2` package.

**Gist:** The guide is a migration map from `encoding/json` v1 to `json/v2`. The basics still look familiar, but the surrounding API changes a lot: direct `MarshalWrite` and `UnmarshalRead`, streaming encode/decode through `jsontext`, composable options instead of many one-off functions, new struct tags like `case` and `embed`, and streaming custom marshaling through `MarshalJSONTo` / `UnmarshalJSONFrom`.

The defaults also change in ways that will matter in real services. Nil slices encode as `[]` instead of `null`, nil maps as `{}`, byte arrays as base64 strings, invalid UTF-8 is rejected by default, duplicate object names are rejected, and unmarshaling is exact/case-sensitive unless configured otherwise.

The useful framing: `json/v2` is more explicit, more flexible, and much better for some streaming/custom-marshaling performance cases, but it is also more complex. This is the kind of standard-library migration where the compatibility options matter as much as the shiny API.

**Newsletter angle:** Good Go/developer-tools item: correctness defaults, API ergonomics, and streaming performance are all moving together in one of Go's most heavily used packages.

{{ tweet(id="2092210706137374961", url="https://x.com/ohmypy/status/2092210706137374961") }}
