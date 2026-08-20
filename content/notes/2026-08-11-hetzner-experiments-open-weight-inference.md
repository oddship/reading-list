+++
title = "Hetzner experiments with open-weight LLM inference"
slug = "2026-08-11-hetzner-experiments-open-weight-inference"
date = 2026-08-11T20:03:00+05:30
[taxonomies]
tags = ["ai-infra", "systems"]
[extra]
source_url = "https://experiments.hetzner.com/"
source_type = "product"
newsletter_candidate = true
why_it_matters = "Hetzner testing a free, no-SLA open-weight inference API is a useful signal that commodity infra providers are probing hosted LLM inference as an infrastructure product, not only renting GPUs."
saved_link = "https://x.com/i/status/2087099126760501364"
related_url = "https://x.com/Hetzner_Online/status/2087099126760501364"
related_urls = ["https://inference.hetzner.com/api/v1/models", "https://pbs.twimg.com/media/HPbdfUqWYAAjNVP.jpg?name=orig"]
retrieval_note = "Tweet extracted via FXTwitter; linked short URL resolved to Hetzner Experiments; static app shell and JS bundle inspected because browser hit bot-check; inference API /api/v1/models endpoint checked and returned 401 unauthorized; launch image inspected visually."
+++
**Logged at IST:** 2026-08-11 20:03 IST

**What it is:** Hetzner's exploratory Experiments platform with an experimental open-weight LLM inference API.

**Gist:** Hetzner says the API is free for now, has no SLAs, and is meant for users to test their own workloads and report what works. They are explicit that this may not become a permanent product.

The linked site resolves to `experiments.hetzner.com`; the app exposes an `AI Inference · Hetzner Experiments` area, API-token creation, docs links, and an inference endpoint at `https://inference.hetzner.com/api/v1`. The unauthenticated `/models` endpoint returns `401 unauthorized`, so the actual model list was not visible without a token.

**Newsletter angle:** Good ai-infra item: a traditional hosting provider is testing LLM inference as a managed API, not just selling GPU servers. The cautious `free, no SLA, maybe not permanent` framing makes it useful market signal rather than a finished product launch.

## Embedded source

{{< tweet id="2087099126760501364" url="https://x.com/i/status/2087099126760501364" >}}
