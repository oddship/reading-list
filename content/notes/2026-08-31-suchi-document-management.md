+++
title = "Suchi: document management as one Go binary"
slug = "2026-08-31-suchi-document-management"
date = 2026-08-31T20:03:00+05:30
[taxonomies]
tags = ["developer-tools", "systems"]
[extra]
source_url = "https://github.com/johnnybravo-xyz/suchi"
source_type = "repo"
newsletter_candidate = true
why_it_matters = "Suchi is an interesting small-footprint document-management stack: SQLite-first, content-addressed blobs, broad intake, explicit egress, and integration boundaries via HTTP API and MCP."
saved_link = "https://github.com/johnnybravo-xyz/suchi"
related_url = "https://docs.suchi.page/"
retrieval_note = "GitHub README and public documentation home were read directly."
+++
**Logged at IST:** 2026-08-31 20:03 IST

**What it is:** Suchi is a self-hosted document-management system delivered as a single Go binary. It uses SQLite, content-addressed storage, a Svelte interface, and an HTTP API, with a v0.1 beta positioned for evaluation and non-critical archives.

**Gist:** The appeal is the operational shape: no separate database server, queue, cache, telemetry service, or remote UI assets by default. It still covers the expected document-management surface area: PDFs and images with OCR, office formats, mail intake, full-text search, Johnny.Decimal filing, saved views, automations, ACLs, OIDC, share links, backups, and restore tooling.

The integration story is also explicit. Suchi exposes a scoped HTTP API and MCP over stdio or HTTP, while optional integrations such as mail, identity, and OpenAI-compatible classification are operator-controlled and visible as egress. That makes it worth watching as a compact personal or office DMS design rather than another heavy service stack.

**Newsletter angle:** Small-footprint self-hosted DMS with clean systems taste: one static Go binary, SQLite/CAS storage, explicit egress, and API/MCP boundaries.
