+++
title = "Claude Haiku 5.5: cheap tokens, with a long-prompt catch"
slug = "2026-10-08-claude-haiku-5-5-pricing-and-pelicans"
date = 2026-10-08T02:51:00+05:30
[taxonomies]
tags = ["llm-research", "ai-infra"]
[extra]
source_url = "https://simonwillison.net/2026/Oct/7/claude-haiku-5-5/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "Haiku 5.5's low per-token price looks attractive for short high-volume workloads, but the 100k-token price step and tokenizer change make cost per task a better comparison than headline rates."
source_title = "Introducing Claude Haiku 5.5"
saved_link = "https://x.com/simonw/status/2107938675405586713"
saved_title = "Simon Willison on Haiku 5.5 pricing and pelicans"
related_urls = ["https://www.anthropic.com/claude-haiku-5-5"]
related_titles = ["Anthropic: Claude Haiku 5.5"]
retrieval_note = "Read Simon Willison's article and Anthropic's launch page. Pricing and availability are grounded in Anthropic's announcement; tokenizer observations and pelican-generation costs are Simon's reported tests."
+++
**Logged at IST:** 2026-10-08 02:51 IST

**What it is:** Simon Willison's launch-day notes on Claude Haiku 5.5, including hands-on pelican image-generation tests and a close look at pricing.

**Gist:** Haiku 5.5 is priced at $0.10 per million input tokens and $0.50 per million output tokens for prompts up to 100,000 tokens, with rates 5x higher above that threshold. Willison notes that its updated tokenizer used about 1.25x as many tokens as Haiku 4.5 on the same long prompt, complicating simple per-token comparisons. His tests found the model could generate a low-effort pelican SVG in seven seconds for under a tenth of a cent; a max-effort version took just over five minutes and cost about 3.4 cents. Anthropic positions Haiku for fast, high-volume, narrower tasks and subagent work, while reserving complex agentic coding for larger models. Anthropic also announced lower Sonnet 5.5 cache-read prices and monthly API credits for Max and Team subscribers.

**Why it matters:** The headline token price is only part of the economics. Prompt length, tokenizer efficiency, reasoning effort, and workload fit can change the actual cost and latency tradeoff.

**Sources read:** https://simonwillison.net/2026/Oct/7/claude-haiku-5-5/; https://www.anthropic.com/claude-haiku-5-5
