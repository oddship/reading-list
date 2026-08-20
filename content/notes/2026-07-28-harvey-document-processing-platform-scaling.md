+++
title = "Harvey's document processing platform at 24.8M docs a week"
slug = "2026-07-28-harvey-document-processing-platform-scaling"
date = 2026-07-28T10:05:00+05:30
[taxonomies]
tags = ["ai-infra", "systems"]
[extra]
source_url = "https://x.com/i/article/2081784796863254528"
source_type = "x-article"
newsletter_candidate = true
why_it_matters = "A concrete scaling story for AI products where document ingestion and retrieval become the core production path, not a background utility."
saved_link = "https://x.com/i/status/2081787028891394186"
retrieval_note = "Grounded from the public X post and X Article rendered in the browser. xurl was unavailable in this environment."
+++
**Logged at IST:** 2026-07-28 10:05 IST

**What it is:** Gary Lam shared Harvey’s article on the infrastructure changes behind its document-processing platform.

**Gist:** Harvey says the platform went from just under one million documents in a busy week to 24.8 million documents and 56 TB of original file data in the latest complete week. The article is useful because it frames document processing as the hot path for an AI legal product: every query over customer data depends on fetch, extraction, chunking, embedding, indexing, storage, and retrieval staying reliable.

The architectural move was to stop treating this as one broad pipeline. Harvey split the work by bottleneck and failure mode: dedicated extraction capacity for OCR and conversion-heavy files, separate chunk/embed and indexing lanes, durable workflows with file-level failures, regional worker management, vector-store migration paths, Arrow IPC in the embed-to-index handoff, stage-specific queues, retry budgets, memory sizing, and backpressure controls.

**Newsletter angle:** Good systems read on the point where ingestion becomes product infrastructure. The interesting bit is not “we scaled a queue,” but that each stage started behaving like a different system with its own capacity model.

**Retrieval note:** Grounded from the public X post and X Article rendered in the browser. `xurl` was unavailable in this environment.

## Embedded source

{{ tweet(id="2081787028891394186", url="https://x.com/i/status/2081787028891394186") }}
