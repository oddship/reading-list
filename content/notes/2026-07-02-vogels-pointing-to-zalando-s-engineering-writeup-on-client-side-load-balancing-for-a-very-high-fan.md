+++
title = "Vogels pointing to Zalando’s engineering writeup on client-side load balancing for a very high fan-out API..."
slug = "2026-07-02-vogels-pointing-to-zalando-s-engineering-writeup-on-client-side-load-balancing-for-a-very-high-fan"
date = 2026-07-02
[taxonomies]
tags = ["reading-log", "x-post", "historical-backfill", "ai-infra", "developer-tools", "systems"]
[extra]
source_url = "https://x.com/i/status/2072652797603176572"
source_type = "x-post"
newsletter_candidate = true
why_it_matters = "strong real-world systems piece on when client-side LB is worth the complexity, especially for cache-sensitive, high-RPS fan-out services where shared routers distort latency and ownership."
saved_link = "https://x.com/i/status/2072652797603176572"
+++
**Gist:** Zalando moved internal fan-out traffic off shared ingress and into an in-process client-side load balancer to preserve consistent-hash cache locality, cut latency spikes, improve debuggability, and reduce shared infra cost. The interesting details are the safety/operability work: exact hash parity with Skipper, informer-based pod discovery, N-ring fade-in for scale-ups, and bounded-load routing using occupancy plus latency instead of naive in-flight/request-rate signals.

**Newsletter angle:** “own the routing decision in-process” or “occupancy beats request-rate for bounded load” as the memorable lesson.

**Retrieval note:** X post extracted via FXTwitter API; linked Zalando article fetched directly and partially read successfully.
