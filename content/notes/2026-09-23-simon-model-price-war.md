+++
title = "Simon Willison on the latest model price war"
slug = "2026-09-23-simon-model-price-war"
date = 2026-09-23T09:51:00+05:30
[taxonomies]
tags = ["llm-research", "ai-infra"]
[extra]
source_url = "https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/"
source_title = "Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, and a new price war"
source_type = "article"
newsletter_candidate = true
why_it_matters = "A practical snapshot of LLM API competition: frontier-ish models are getting cheaper fast, while expensive high-reasoning modes still need operational guardrails."
saved_link = "https://x.com/simonw/status/2102546103984079131"
saved_title = "Simon Willison sharing his Opus 5.5 / GPT-6 Sol / GPT-6 Luna write-up"
related_url = "https://x.com/simonw/status/2102546103984079131"
related_title = "Announcement post on X"
retrieval_note = "X post extracted via FXTwitter; linked Simon Willison article read directly."
+++

**Logged at IST:** 2026-09-23 09:51 IST

**What it is:** Simon Willison's early read on a cluster of model launches: Anthropic's Claude Opus 5.5 and OpenAI's GPT-6 Sol and GPT-6 Luna.

**Gist:** The most important part is pricing. Simon notes that GPT-6 Luna is half the price of GPT-5.6 Luna, at $0.10/M input and $0.50/M output, while GPT-6 Sol also halves the GPT-5.6 Sol tier. Claude Opus 5.5 gets a smaller but still meaningful cut from the earlier Opus price level, with input at $4/M and output at $20/M, plus much cheaper cache reads for long agentic conversations.

The qualitative picture is more mixed. Simon is moving Codex and Claude Code defaults to GPT-6 Sol and Claude Opus 5.5, and has upgraded his Datasette Agent demo to GPT-6 Luna. But his pelican SVG test exposed a failure mode for Opus 5.5 at max reasoning: it over-thought the task until it hit the 128,000 output-token limit without returning a finished SVG, twice.

The useful takeaway is not just that models are getting cheaper. It is that the operating envelope is moving quickly: cheap models may become good enough for more production agent paths, while expensive reasoning modes still need explicit cost, latency, and completion guardrails.

{{ tweet(id="2102546103984079131", url="https://x.com/simonw/status/2102546103984079131") }}

**Newsletter angle:** Good pricing/agent-ops item on how model defaults can change when capability moves down the cost curve, and why high-reasoning modes still need reliability controls.
