+++
title = "How Razorpay refreshes its data warehouse 10x faster"
slug = "2026-07-15-how-razorpay-refreshes-its-data-warehouse-10x-faster"
date = 2026-07-15T10:45:00+05:30
[taxonomies]
tags = ["systems", "ai-infra", "developer-tools"]
[extra]
source_url = "https://engineering.razorpay.com/how-we-refresh-razorpays-data-warehouse-10x-faster-with-graphs-and-indexes-538abc244703"
source_type = "x-post"
newsletter_candidate = true
why_it_matters = "Strong data-infra example of reframing materialized-table refresh as graph maintenance, plus a nice case for batch-plus-incremental beating naive streaming when stateful joins get too expensive."
saved_link = "https://x.com/i/status/2077208966820712893"
+++
**Logged at IST:** 2026-07-15 10:45 IST

**What it is:** Piyush Goel sharing Razorpay Engineering’s writeup on refreshing warehouse facts 10x faster with graphs and indexes

**Gist:** Razorpay moved from expensive full-refresh fact generation toward incremental fact maintenance by treating each denormalized fact as a dependency graph. They pair change-driven processing with secondary indexes on the lake, graph traversal to discover affected ancestors and descendants, and selective runtime joins for high-cardinality dimensions. The result is much faster warehouse refreshes with lower compute cost, restored historical coverage, and less dependency on the warm store.

**Newsletter angle:** Strong data-infra example of reframing materialized-table refresh as graph maintenance, plus a nice case for batch-plus-incremental beating naive streaming when stateful joins get too expensive.
