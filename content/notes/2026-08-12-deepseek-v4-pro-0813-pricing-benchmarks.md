+++
title = "DeepSeek V4 Pro 0813 pricing and unverified agent benchmarks"
slug = "2026-08-12-deepseek-v4-pro-0813-pricing-benchmarks"
date = 2026-08-12T22:47:00+05:30
[taxonomies]
tags = ["ai-infra", "agents", "llm-research"]
[extra]
source_url = "https://api-docs.deepseek.com/quick_start/pricing/"
source_type = "docs"
newsletter_candidate = true
why_it_matters = "DeepSeek's official API docs now list V4 Pro 0813 with 1M context, 384K max output, OpenAI/Anthropic-compatible surfaces, and still-low token pricing, while a circulating screenshot claims large agent-benchmark gains that should be treated as unverified until official or third-party results appear."
saved_link = "https://x.com/i/status/2087568202452926622"
related_url = "https://x.com/AndrewCurran_/status/2087568202452926622"
related_urls = ["https://x.com/AndrewCurran_/status/2087565280457461917", "https://api-docs.deepseek.com/quick_start/pricing/", "https://reading-list.oddship.net/notes/2026-08-01-simon-willison-deepseek-v4-flash-0731/", "https://reading-list.oddship.net/notes/2026-08-08-arc-prize-deepseek-v4-flash-0731/"]
retrieval_note = "Tweet and quoted post extracted via FXTwitter. Pricing/features were verified against the live DeepSeek API docs and Jina reader output. Benchmark table and API-doc screenshot were inspected directly as attached X media; benchmark results remain unverified screenshot claims."
+++
**Logged at IST:** 2026-08-12 22:47 IST

**What it is:** Andrew Curran sharing an unverified benchmark screenshot for DeepSeek-V4-Pro-0813, plus a quoted screenshot of the DeepSeek API docs showing the model listed publicly.

**Gist:** The verified part is the API-docs update. DeepSeek’s live pricing page lists `deepseek-v4-pro` with model version `DeepSeek-V4-Pro-0813`, 1M context, maximum 384K output, thinking and non-thinking modes, JSON output, tool calls, Responses API, Anthropic API, chat-prefix completion beta, and FIM in non-thinking mode. Pricing shown in the docs: $0.003625/M input tokens on cache hit, $0.435/M input tokens on cache miss, and $0.87/M output tokens, with a 500 concurrency limit. The docs also warn that DeepSeek plans a significant overall API price increase in the near future.

The unverified screenshot claims large agent-benchmark gains for V4 Pro 0813. It shows, among others: HLE 42.7/60.0, Terminal Bench 2.1 87.9, NL2Repo 61.5, Cybergym 83.3, DeepSWE 62.7, Toolathlon-Verified 74.1, Agents’ Last Exam 25.7, AutomationBench 31.8, DSBench-FullStack 71.1, and DSBench-Hard 67.2. The tweet itself caveats these as “as yet unverified” WeChat-origin benchmarks, so this should be treated as a watch item, not a settled leaderboard result.

If the numbers hold up, the interesting continuation from V4 Flash is that DeepSeek may be moving from price-performance disruption into more direct agent-benchmark competitiveness, while still listing low API prices relative to frontier closed models. But the right stance for now is: official docs confirm V4 Pro 0813 exists and is priced; benchmark claims need confirmation.

**Newsletter angle:** Watch-list item for agentic model economics: verified pricing plus unverified benchmark claims suggest a potentially important DeepSeek release, but the benchmark table needs third-party or official reproducibility before treating it as fact.
