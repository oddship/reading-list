+++
title = "OpenAI says retained reasoning and compaction tripled ARC-AGI-3 scores"
slug = "2026-07-30-openai-arc-agi-3-retained-reasoning-compaction"
date = 2026-07-30T07:15:00+05:30
[taxonomies]
tags = ["agents", "ai-infra", "llm-research"]
[extra]
source_url = "https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "A useful reminder that agent benchmarks often measure harness memory and API choices, not only raw model capability."
retrieval_note = "OpenAI page was Cloudflare-blocked in browser/direct fetch; content was extracted via Jina Reader and grounded against the original URL."
+++
**Logged at IST:** 2026-07-30 07:15 IST

**What it is:** OpenAI explaining why GPT-5.6 Sol’s ARC-AGI-3 score jumped when they changed the evaluation harness to match their production Responses API setup.

**Gist:** The central claim is not “the model got better,” but “the harness was dropping the parts of the interaction that make long-running agents work.” In the official ARC-AGI-3 public-set harness, GPT-5.6 Sol scored 13.3% RHAE. With two settings enabled, retained reasoning and compaction, OpenAI reports 38.3%, about 3x higher, while cutting output tokens by 6x.

The failure mode is familiar: after each game action, the original harness discarded private reasoning, so the model had to rediscover its strategy each turn. Then, as runs grew, rolling truncation discarded older actions and observations too. OpenAI’s Responses API setup keeps reasoning across turns by passing the previous response ID, then uses compaction instead of rolling truncation so the model can preserve what it learned about the game while staying within context limits.

**Newsletter angle:** Strong evals/agent-infra item because it makes a clean systems point: benchmark scores are partly a measurement of memory architecture. For agents, “same model, different harness” can mean different task competence, token cost, and apparent intelligence. It also pushes the practical recommendation toward Responses API-style retained reasoning plus compaction, and away from generic chat-completions loops that silently erase the agent’s working memory.
