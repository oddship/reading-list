+++
title = "celld: self-hosted Durable Objects"
slug = "2026-08-05-celld-self-hosted-durable-objects"
date = 2026-08-05T20:19:00+05:30
[taxonomies]
tags = ["systems", "ai-infra", "developer-tools"]
[extra]
source_url = "https://github.com/denoland/celld"
source_type = "repository"
newsletter_candidate = true
why_it_matters = "celld is a serious attempt to make the Durable Objects programming model self-hostable: V8 Workers, one SQLite database per object, S3-compatible storage as the durable source of truth, and no separate control plane or consensus service."
saved_link = "https://x.com/i/status/2085001943693549887"
related_url = "https://x.com/rough__sea/status/2085001943693549887"
related_urls = ["https://celld.dev", "https://raw.githubusercontent.com/denoland/celld/main/README.md"]
retrieval_note = "Read Ryan Dahl's X post via FXTwitter, the attached benchmark/characteristics images, and the denoland/celld GitHub README."
+++
**Logged at IST:** 2026-08-05 20:19 IST

**What it is:** Ryan Dahl's launch post for `celld`, a Deno open-source daemon for self-hosted, distributed Durable Objects and Workers.

**Gist:** `celld` aims to run the Cloudflare Workers and Durable Objects programming model on your own machines. Each object is its own SQLite database, addressed by name and replicated to an S3-compatible bucket. The fleet coordinates through that bucket alone, using object-storage compare-and-swap so one node owns a cell at a time without a separate control plane, membership protocol, failure detector, or consensus service.

The tweet's shape is deliberately concrete: V8 + S3 + SQLite + LTX + Tokio, programmed with Cloudflare Workers and Durable Object JavaScript APIs and config. It claims durable writes before acknowledgement, RPO=0, roughly 4 MB memory overhead per resident cell, and near-zero cost for hibernated cells beyond S3 storage.

The attached charts make the cost argument. Dahl compares monthly cost against resident fleet size, showing `celld` staying flat at small fleet sizes and much cheaper at larger resident-cell counts than Cloudflare Durable Objects in the shown model. The characteristics table lists one epoch-fenced writer per cell, zero acknowledged writes lost on kill, about 90 ms region-local durable write latency, about 20 s failover after node loss with no lost writes, 0.2 / 0.3 ms warm stateless p50 / p99, about 94k req/s per worker thread, about 4 ms to wake a hibernated cell, 1,000 resident cells per 8 GB node, and about $0.05 per resident cell-month.

**Newsletter angle:** This is an important systems counterpoint to managed serverless primitives: the Durable Objects model may be escaping Cloudflare as a self-hostable architecture, with object storage as the coordination and durability substrate.

## Embedded source

{{< tweet id="2085001943693549887" url="https://x.com/i/status/2085001943693549887" >}}
