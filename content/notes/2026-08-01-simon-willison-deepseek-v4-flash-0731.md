+++
title = "Simon Willison frames DeepSeek-V4-Flash-0731 as a value-per-intelligence jump"
slug = "2026-08-01-simon-willison-deepseek-v4-flash-0731"
date = 2026-08-01T12:48:00+05:30
[taxonomies]
tags = ["ai-infra", "developer-tools", "llm-research"]
[extra]
source_url = "https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/"
source_type = "article"
saved_link = "https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/"
related_url = "https://reading-list.oddship.net/notes/2026-08-01-deepseek-v4-flash-high-frontend-code-arena/"
related_source_url = "https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731"
newsletter_candidate = true
why_it_matters = "This adds a broader value-per-intelligence read to the earlier Arena price-performance note, and points at reasoning-effort settings as a practical quality lever."
retrieval_note = "Direct page HTML was accessible. The Hugging Face model card was also read for model-size and capability details."
+++
**Logged at IST:** 2026-08-01 12:48 IST

**What it is:** Simon Willison's link-blog note on `deepseek-ai/DeepSeek-V4-Flash-0731`, pointing to the Hugging Face release and Artificial Analysis' pricing/intelligence view.

**Gist:** Simon highlights DeepSeek-V4-Flash-0731 as the latest V4-family release with “substantially enhanced agentic capabilities.” The model card says it is a 304B-parameter release, about 167GB on Hugging Face, that outperforms the V4-Pro preview on listed agent/code benchmarks despite a much smaller activated-parameter count.

The important framing is value, not just model size. Simon notes that Artificial Analysis ranks it ahead of MiniMax M3, a larger 428B model, and that pricing around $0.14/M input and $0.27/M output may make it the best value-per-intelligence model currently available.

There is also a practical harness detail. Simon tried his standard pelican prompt through OpenRouter and got a weak result at the default reasoning level, then a much better one after setting `reasoning_effort=high`. That is a useful reminder that cheap agent/coding models may need the right reasoning-effort configuration before judging their quality.

**Newsletter angle:** Pairs well with the Arena.ai note. Together they say: DeepSeek is showing up not only as a cheap frontend-code arena outlier, but as a broader price/intelligence story with enough API compatibility and reasoning-control surface to matter in real coding-agent setups.
