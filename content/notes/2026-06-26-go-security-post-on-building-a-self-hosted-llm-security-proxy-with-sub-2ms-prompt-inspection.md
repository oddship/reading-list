+++
title = "Go/security post on building a self-hosted LLM security proxy with sub-2ms prompt inspection"
slug = "2026-06-26-go-security-post-on-building-a-self-hosted-llm-security-proxy-with-sub-2ms-prompt-inspection"
date = 2026-06-26
[taxonomies]
tags = ["reading-log", "x-post", "historical-backfill", "agents", "ai-infra", "security", "llm-research"]
[extra]
source_url = "https://x.com/i/status/2070417322842747145"
source_type = "x-post"
status = "reviewed"
newsletter_candidate = true
why_it_matters = "useful practical architecture for regulated multi-provider LLM deployments where cloud gateways or provider-native guardrails are insufficient"
saved_link = "https://x.com/i/status/2070417322842747145"
+++
**What it is:** Go/security post on building a self-hosted LLM security proxy with sub-2ms prompt inspection

**Gist:** author built an OpenAI-compatible reverse proxy (“Tamga”) that scans prompts for PII, secrets, and prompt-injection patterns before forwarding to providers; key engineering lesson is a hybrid scan pipeline where cheap CPU-bound detectors run sequentially while slower network/model-backed scanners run in parallel, because goroutine orchestration overhead dominated when everything fanned out

**Newsletter angle:** concrete infra pattern for “LLM middleware” that is more about latency budgets and data residency than model eval hype
