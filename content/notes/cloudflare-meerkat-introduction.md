+++
title = "Cloudflare Meerkat Introduction"
date = 2026-07-08
[taxonomies]
tags = ["distributed-systems", "consensus", "cloudflare", "infrastructure"]
[extra]
source_url = "https://blog.cloudflare.com/meerkat-introduction/"
source_type = "article"
status = "published"
newsletter_candidate = true
why_it_matters = "A notable real-world consensus design story beyond the usual Raft framing."
+++

Cloudflare is building Meerkat for strongly consistent control-plane state across 330+ data centers, arguing that leader-and-timeout-heavy approaches like Raft are a poor fit for hostile WAN conditions and that QuePaxa's all-replicas-can-write model better matches their network.

**Newsletter angle:** Notable systems/infrastructure piece on consensus design beyond Raft, especially for globally distributed control planes.
