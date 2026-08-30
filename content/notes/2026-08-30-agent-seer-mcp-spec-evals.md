+++
title = "Agent Seer turns MCP specs into agent evals"
slug = "2026-08-30-agent-seer-mcp-spec-evals"
date = 2026-08-30T12:51:00+05:30
[taxonomies]
tags = ["agents", "developer-tools", "llm-research"]
[extra]
source_url = "https://arxiv.org/abs/2608.26133"
source_type = "paper"
newsletter_candidate = true
why_it_matters = "If agent evals can be derived from the live MCP spec, private and fast-changing tool suites get a plausible cold-start evaluation path instead of stale hand-written tests."
saved_link = "https://x.com/omarsar0/status/2093741222443786244"
related_url = "https://x.com/omarsar0/status/2093741222443786244"
retrieval_note = "FXTwitter extraction resolved the linked arXiv paper and DAIR.AI paper page. The arXiv abstract/full paper extract was read, and the attached X image was inspected; it is the paper's first page."
+++
**Logged at IST:** 2026-08-30 12:51 IST

**What it is:** Apple's Agent Seer paper, shared by Omar Sanseviero, on synthesizing MCP agent evaluation scenarios from the tool spec itself.

**Gist:** Agent Seer treats an MCP specification as enough raw material to build a self-contained evaluation harness. It enriches tool descriptions, generates expected tool-call workflows, synthesizes mock outputs, and expands those into multi-turn dialogues grounded in the synthetic data. The pipeline needs no examples, no live tool access, and no domain-specific tuning.

The useful framing is the cold-start problem for agent evals. New private APIs, internal MCP servers, and rapidly changing tool suites usually have no durable benchmark. Hand-written evals also go stale as soon as the tool surface changes. Agent Seer shifts the work from manual curation to structured extraction from the live spec.

The empirical result is directionally promising, but the caveat matters. Across seven MCP specs, the paper reports strong tool-calling and coherence scores with complete coverage on small and medium specs. Quality varies more with parameter schema complexity than with tool-suite size, and the main failure mode is wrong argument values. That is exactly the kind of error coarse tool-name matching can miss.

**Newsletter angle:** Strong agents/evaluation item: MCP servers may be able to ship with generated eval suites that track the current spec, especially for private or fast-moving enterprise tools.

{{ tweet(id="2093741222443786244", url="https://x.com/omarsar0/status/2093741222443786244") }}
