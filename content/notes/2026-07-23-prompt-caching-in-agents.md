+++
title = "Prompt caching in agents"
slug = "2026-07-23-prompt-caching-in-agents"
date = 2026-07-23T17:46:00+05:30
[taxonomies]
tags = ["agents", "ai-infra", "systems"]
[extra]
source_url = "https://earendil.com/posts/prompt-caching/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "Strong agents and AI-infra item because it makes cache-hit behavior part of agent product design, not just provider-side optimization."
saved_link = "https://earendil.com/posts/prompt-caching/"
+++
**Logged at IST:** 2026-07-23 17:46 IST

**What it is:** Earendil Engineering post explaining why prompt caching is a first-order systems concern for coding agents.

**Gist:** The post grounds prompt caching in KV-cache reuse: agents mostly append to a stable prompt, so latency and cost depend on preserving an identical token prefix. It walks through session affinity versus distributed cache storage, branch and tree sessions, automatic versus explicit caching, fragile tool loadouts, TTL misses, gateway incentives, and why Pi prefers stable append-oriented transcripts over aggressive pruning.

**Newsletter angle:** Strong agents and AI-infra item because it makes cache-hit behavior part of agent product design, not just provider-side optimization.
