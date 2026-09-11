+++
title = "OpenAI scaled Habitat from Python library to storage platform"
slug = "2026-09-12-openai-habitat-storage-scaling"
date = 2026-09-12T03:42:00+05:30
[taxonomies]
tags = ["systems", "ai-infra", "developer-tools"]
[extra]
source_url = "https://openai.com/index/scaling-storage-one-billion-users-part-one"
source_type = "article"
newsletter_candidate = true
why_it_matters = "OpenAI's Habitat write-up is a concrete frontier-scale storage-platform case study: Python pushed surprisingly far, but only with careful event-loop, pooling, load-balancing, and API-shape decisions."
saved_link = "https://x.com/OpenAIDevs/status/2098502031338340416"
related_url = "https://x.com/OpenAIDevs/status/2098502006935814272"
retrieval_note = "Tweet thread extracted via FXTwitter; linked OpenAI article fetched directly; attached diagram inspected and mirrors the article's Habitat overview."
+++

**Logged at IST:** 2026-09-12 03:42 IST

**What it is:** OpenAI’s engineering write-up on Habitat, the online storage platform behind ChatGPT, API, Codex, and internal services.

**Gist:** Habitat started in mid-2024 as a Python client library over Azure Cosmos DB so product teams would not have to own database details like schema lookup, routing, authorization, encryption, serialization, request shaping, and connection pooling. As OpenAI’s product surface grew, client-side logic became too brittle to coordinate across dozens of services, so Habitat moved into a centralized service that could enforce deployments, observability, access control, audit logging, and storage routing in one place.

The scale is the hook: Habitat now handles more than 70 million requests per second, supports products used by over 1 billion people each week, spans almost 40 regions, and serves more than 500 PB of data. Before the Rust rewrite, the Python service handled more than 20 million requests per second at peak.

The Python lessons are the most reusable part. Asyncio concurrency is not CPU parallelism, so CPU-heavy work like routing, compression, encryption, checksumming, health checks, shadowing, and hedging can turn event-loop scheduling delay into tail latency. OpenAI measured loop delay directly, kept per-process concurrency low, and scaled out many Python worker processes.

There are also sharp operational details: Statsig feature-flag parsing caused synchronized CPU stalls until configs were reduced, polling intervals lengthened, and jitter added; Python `aiohttp` LIFO connection reuse contributed to a metastable failure where overloaded servers kept receiving more traffic; switching to FIFO helped break that feedback loop. Envoy and Istio then provided connection fan-in, HTTP/2 multiplexing, rate limits, and circuit breakers to keep Python process counts from overwhelming downstream storage.

Habitat’s API design is intentionally constrained. Instead of arbitrary SQL or graph traversal, it exposes predictable NoSQL-style object and edge operations inspired by TAO. That makes expensive operations obvious and keeps online storage isolated from analytical/search workloads, which are handled through CDC into Rockset.

OpenAI has now rewritten Habitat in Rust with two engineers using Codex and GPT-5.5. The Rust service handles 95% of production requests and is reported as 6× more CPU efficient and 15× more memory efficient than the Python version.

**Newsletter angle:** This is a useful counterweight to “rewrite it in Rust” as a slogan. The real story is sequencing: accept Python as strategic debt to stabilize APIs and product velocity, measure its actual failure modes, use infrastructure to contain them, then rewrite when the platform shape is clear and the efficiency payoff is obvious.
