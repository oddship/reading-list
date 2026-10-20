+++
title = "Clairic brings typed extraction to Workers AI"
slug = "2026-10-20-cloudflare-clairic-extraction-model"
date = 2026-10-20T09:19:00+05:30
[taxonomies]
tags = ["ai-infra", "developer-tools", "systems"]
[extra]
source_url = "https://blog.cloudflare.com/clairic-extraction-model/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "Clairic separates structured extraction and estimation from free-form generation, returning typed answers with source spans or uncertainty information for applications that need machine-consumable values."
source_title = "Introducing Clairic, a new System One class of extraction models"
saved_link = "https://x.com/Cloudflare/status/2112244042658423149"
saved_title = "Cloudflare announces Clairic"
+++
**Logged at IST:** 2026-10-20 09:19 IST

**What it is:** Cloudflare's preview announcement for Clairic, a hosted Workers AI model for extracting, computing, estimating, and forecasting typed values from unstructured inputs.

**Gist:** A request supplies text (and optionally images) plus a schema of named fields. Clairic can return text spans with offsets, typed values such as numbers and dates, estimates with a median and 80% interval, and forecasts. Cloudflare says it runs in a single forward pass without generating output tokens; its docs list input-token pricing of $0.10 per million tokens. The model is in preview on Workers AI, and Cloudflare says it intends to release open weights soon.

**Why it matters:** For extraction or bounded prediction, a typed answer with provenance or uncertainty may be easier to validate and cheaper to integrate than asking a general LLM to emit free-form JSON. Cloudflare's speed, accuracy, and cost comparisons are vendor claims; the model can still make mistakes, and the announcement is a preview rather than independent evaluation.

**Source:** https://blog.cloudflare.com/clairic-extraction-model/
**Docs:** https://developers.cloudflare.com/workers-ai/models/clairic/
**Saved link:** https://x.com/Cloudflare/status/2112244042658423149
