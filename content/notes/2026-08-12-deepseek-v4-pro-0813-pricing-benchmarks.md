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
related_urls = ["https://x.com/AndrewCurran_/status/2087565280457461917", "https://x.com/pilvar222/status/2087691659953815783", "https://x.com/ValsAI/status/2087697657301279220", "https://x.com/arena/status/2087784211642192332", "https://x.com/arena/status/2087767198974533648", "https://www.vals.ai/benchmarks/vals_index", "https://api-docs.deepseek.com/quick_start/pricing/", "https://reading-list.oddship.net/notes/2026-08-01-simon-willison-deepseek-v4-flash-0731/", "https://reading-list.oddship.net/notes/2026-08-08-arc-prize-deepseek-v4-flash-0731/"]
retrieval_note = "Original tweet and quoted post extracted via FXTwitter. Pricing/features were verified against the live DeepSeek API docs and Jina reader output. Benchmark table and API-doc screenshot were inspected directly as attached X media; benchmark results remain unverified screenshot claims. Updated 2026-08-13 with Aikido cybersecurity benchmark tweet text extracted via FXTwitter and attached cost-vs-recall chart inspected directly; also updated with Vals AI tweet JSON, attached open-weight chart inspection, and Vals Index page data for the relevant rows. Updated again with Arena.ai Code Arena WebDev tweet/quoted tweet via FXTwitter and both attached chart images inspected directly."
+++
**Logged at IST:** 2026-08-12 22:47 IST

**What it is:** Andrew Curran sharing an unverified benchmark screenshot for DeepSeek-V4-Pro-0813, plus a quoted screenshot of the DeepSeek API docs showing the model listed publicly.

**Gist:** The verified part is the API-docs update. DeepSeek’s live pricing page lists `deepseek-v4-pro` with model version `DeepSeek-V4-Pro-0813`, 1M context, maximum 384K output, thinking and non-thinking modes, JSON output, tool calls, Responses API, Anthropic API, chat-prefix completion beta, and FIM in non-thinking mode. Pricing shown in the docs: $0.003625/M input tokens on cache hit, $0.435/M input tokens on cache miss, and $0.87/M output tokens, with a 500 concurrency limit. The docs also warn that DeepSeek plans a significant overall API price increase in the near future.

The unverified screenshot claims large agent-benchmark gains for V4 Pro 0813. It shows, among others: HLE 42.7/60.0, Terminal Bench 2.1 87.9, NL2Repo 61.5, Cybergym 83.3, DeepSWE 62.7, Toolathlon-Verified 74.1, Agents’ Last Exam 25.7, AutomationBench 31.8, DSBench-FullStack 71.1, and DSBench-Hard 67.2. The tweet itself caveats these as “as yet unverified” WeChat-origin benchmarks, so this should be treated as a watch item, not a settled leaderboard result.

If the numbers hold up, the interesting continuation from V4 Flash is that DeepSeek may be moving from price-performance disruption into more direct agent-benchmark competitiveness, while still listing low API prices relative to frontier closed models. But the right stance for now is: official docs confirm V4 Pro 0813 exists and is priced; benchmark claims need confirmation.

**Update, 2026-08-13:** Aikido Research’s Philippe Dourassov posted a separate cybersecurity-benchmark result for DeepSeek v4 Pro 0813. The tweet claims 87.5% benchmark-CVE rediscovery at pass@3, above Claude Opus 5 and Qwen3.8 Max at 81.3%, but with a precision tradeoff: 65.6% of DeepSeek-reported vulnerabilities were valid, below GPT-5.6-Sol’s 86.4%. He also notes run variance: the model finds 58.3% of vulnerabilities on an average single run, so its best result comes from combining findings across runs. The attached Aikido/research chart frames this as cost vs. recall over 1→2→3 runs, with DeepSeek v4 Pro 0813 on the high-recall side of the Pareto frontier.

This strengthens the “watch this release” case, but it is still benchmark-by-post rather than a fully published reproducible report. The useful caveat is recall versus precision: DeepSeek may be very good at surfacing candidate vulnerabilities, while still needing triage discipline because its false-positive rate is high.

**Update, 2026-08-13:** Vals AI posted Vals Index v1.2 open-weight results for DeepSeek V4 Pro 0813. Their tweet says the model jumped 11 points and is now the #2 open-weight model on the index, behind Kimi K3. The attached chart shows Kimi K3 at 74.70% accuracy, $2.34/test, 1224s latency; DeepSeek V4 Pro 0813 at 66.25%, $0.14/test, 1135s; Qwen 3.8 Max at 65.47%, $2.68/test; GLM 5.2 at 65.02%, $2.08/test; DeepSeek V4 Flash 0731 at 63.95%, $0.06/test; and older DeepSeek V4 at 55.62%, $0.83/test. The live Vals Index page also lists Pro 0813 at 66.251% accuracy, $0.135/test, and 1134.51s latency in the overall task view.

This is a cleaner third-party benchmark anchor than the circulating WeChat screenshot, though still one benchmark's methodology. The pattern across the posts is now sharper: V4 Pro 0813 is not simply winning every leaderboard, but it is repeatedly showing up as unusually cheap for its capability band. On Vals, it sits well below Kimi K3 in accuracy, but is roughly 17x cheaper per test.

**Update, 2026-08-13:** Arena.ai posted a Code Arena: WebDev follow-up for DeepSeek-V4-Pro (Max). Arena says the upcoming open-weight model is around #8 overall on early AutoEval at 1607 points, and #2 among open models after Kimi K3 Max at 1674. The quoted top-15 chart places it just below GPT-5.6 Sol xHigh at 1622 and ahead of GLM-5.2 Max at 1587, DeepSeek V4 Flash High at 1582, and Claude Opus 4.8 High at 1564.

The second Arena chart makes the price/performance story explicit. It marks `deepseek-v4-pro-max-20260813` as DeepSeek/MIT, score 1607, at about $0.76/M blended tokens using a 3:1 ratio, while the tweet cites $0.435/M input and $0.87/M output. Arena claims it outperforms models beyond its price tier, including Opus 4.8 at $5/$25 and GLM-5.2 at $1.4/$4.4. The caveat matters: this is early AutoEval, where a reward model trained on Arena human-preference data casts automatic votes, so the score may move as live human votes arrive.

**Newsletter angle:** Combine the DeepSeek Pro threads as an agentic-model-economics watch item: official pricing plus early third-party benchmark posts suggest an important capability-per-dollar shift. The emerging story is not "DeepSeek tops every leaderboard". It is that an open-weight model is repeatedly landing close enough to expensive frontier coding and agent models to change routing, evaluation, and cost assumptions.
