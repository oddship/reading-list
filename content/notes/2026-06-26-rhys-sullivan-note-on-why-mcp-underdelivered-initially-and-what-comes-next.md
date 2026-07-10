+++
title = "Rhys Sullivan note on why MCP underdelivered initially and what comes next"
slug = "2026-06-26-rhys-sullivan-note-on-why-mcp-underdelivered-initially-and-what-comes-next"
date = 2026-06-26
[taxonomies]
tags = ["reading-log", "x-post", "historical-backfill", "agents", "ai-infra", "developer-tools"]
[extra]
source_url = "https://x.com/RhysSullivan/status/2070311929038680262?s=20"
source_type = "x-post"
status = "reviewed"
newsletter_candidate = true
why_it_matters = "useful framing for the current agent-tooling stack wars—less about MCP vs CLI ideology, more about reducing friction while preserving structure and semantics"
saved_link = "https://x.com/RhysSullivan/status/2070311929038680262?s=20"
+++
**What it is:** Rhys Sullivan note on why MCP underdelivered initially and what comes next

**Gist:** argues MCP launched in the GPT-4o / Sonnet 3.5 era before good agent/tooling patterns were understood, so many servers exposed too few capabilities and clients added too much friction; meanwhile bash/CLI-based agents won because they could chain commands, install tools dynamically, and lean on mature shell primitives. His pushback is that this should not end in “just use CLIs”: CLIs hide action semantics and add statefulness, while the better end-state is harnesses that can expose APIs, MCP, CLIs, GraphQL, etc. through one tool catalog

**Newsletter angle:** crisp explanation of why shell-first agents surged, and why the next layer probably needs to unify API/CLI/MCP rather than pick one
