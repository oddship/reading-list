+++
title = "Hacktron's OpenAI forum-to-Codex compromise write-up"
slug = "2026-09-18-hacktron-hacking-openai"
date = 2026-09-18T10:02:00+05:30
[taxonomies]
tags = ["security", "ai-infra", "agents"]
[extra]
source_url = "https://www.hacktron.ai/blog/hacking-openai"
source_type = "security-writeup"
newsletter_candidate = true
why_it_matters = "A concrete case study in how agent-assisted exploit work can turn a dependency bug and identity-boundary mistake into cross-product access quickly."
saved_link = "https://x.com/S1r1u5_/status/2100777801335095383"
related_urls = ["https://x.com/S1r1u5_/status/2100777801335095383", "https://www.wsj.com/tech/ai/hackers-used-anthropics-claude-to-break-into-openai-b40ba883", "https://github.com/discourse/discourse/security/advisories/GHSA-vhm9-85gw-x335", "https://github.com/discourse/discourse/commit/a07188016987de1613c961277e2e928aaa7c37ec"]
retrieval_note = "X post extracted via FXTwitter; attached launch image and related screenshots were OCR'd; the Hacktron write-up was read directly, and a partial WSJ article was available before the subscription wall."
+++

**Logged at IST:** 2026-09-18 10:02 IST

**What it is:** Hacktron's disclosure of a chain from an OpenAI-hosted Discourse forum compromise to OpenAI employee ChatGPT/Codex account access.

**Gist:** Hacktron says it chained a `libheif`/ImageMagick remote-code-execution path in OpenAI's Discourse forum with an OpenAI SSO flaw. The claimed result was no-interaction takeover of OpenAI employees' ChatGPT/Codex accounts, with potential reach into connected services such as GitHub, Slack, and email.

They demonstrated impact by asking an employee's Codex account to open a harmless pull request in OpenAI's internal `openai/openai` monorepo, then stopped further testing. The post says OpenAI fixed the issue the same day, Discourse published advisory GHSA-vhm9-85gw-x335 and added ImageMagick sandboxing, and OpenAI paid a $6,500 bounty for the OpenAI-side finding.

The deeper point is economic: Hacktron argues that agent-assisted exploit development compressed work that used to require rare expertise and sustained effort into a few days of agent time plus a few hours of human guidance. That makes old assumptions about dependency bugs, image parsers, and identity boundaries feel much weaker.

**Newsletter angle:** A sharp security-through-complexity warning: AI-assisted exploit work makes "known but hard to weaponize" bugs look operationally cheap, especially when identity and connector boundaries are loose.
