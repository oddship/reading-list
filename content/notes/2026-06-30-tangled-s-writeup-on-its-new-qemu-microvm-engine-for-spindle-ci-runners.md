+++
title = "Tangled’s writeup on its new QEMU microVM engine for Spindle CI runners"
date = 2026-06-30
[taxonomies]
tags = ["reading-log", "x-post", "historical-backfill", "agents", "ai-infra", "systems"]
[extra]
source_url = "https://x.com/i/status/2071966840801185811"
source_type = "x-post"
status = "reviewed"
newsletter_candidate = true
why_it_matters = "strong reference for agent/container sandbox UX, network lockdown, and self-hosted CI isolation tradeoffs."
saved_link = "https://x.com/i/status/2071966840801185811"
+++
**Gist:** each workflow runs in its own microVM; guest agent talks back over vsock; NixOS-based workflow config can declaratively enable services like Postgres and Docker; cache/proxy design keeps guests isolated from direct network/cache credentials while still reusing built artifacts.

**Newsletter angle:** “microVMs as the unit of CI isolation, with NixOS as workflow-defined machine config” is a solid hook.

**Retrieval note:** extracted via FXTwitter API + linked article fetch.
