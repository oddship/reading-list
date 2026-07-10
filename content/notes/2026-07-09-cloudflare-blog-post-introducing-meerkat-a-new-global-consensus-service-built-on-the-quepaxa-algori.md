+++
title = "Cloudflare introduces Meerkat"
slug = "2026-07-09-cloudflare-blog-post-introducing-meerkat-a-new-global-consensus-service-built-on-the-quepaxa-algori"
date = 2026-07-09
[taxonomies]
tags = ["reading-log", "article", "blog-cloudflare-com", "ai-infra", "llm-research", "systems"]
[extra]
source_url = "https://blog.cloudflare.com/meerkat-introduction/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "Notable systems/infrastructure piece on consensus design beyond Raft, especially for globally distributed control planes."
saved_link = "https://blog.cloudflare.com/meerkat-introduction/"
+++
**Logged at IST:** 2026-07-09 23:10 IST

**What it is:** Cloudflare blog post introducing Meerkat, a new global consensus service built on the QuePaxa algorithm

**Gist:** Cloudflare is building Meerkat for strongly consistent control-plane state across 330+ data centers, arguing that leader-and-timeout-heavy approaches like Raft are a poor fit for hostile WAN conditions and that QuePaxa’s all-replicas-can-write model better matches their network.

**Newsletter angle:** Notable systems/infrastructure piece on consensus design beyond Raft, especially for globally distributed control planes.
