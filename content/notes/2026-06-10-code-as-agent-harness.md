+++
title = "Code as Agent Harness"
slug = "2026-06-10-code-as-agent-harness"
date = 2026-06-10
[taxonomies]
tags = ["agents", "ai-infra", "llm-research"]
[extra]
source_url = "https://x.com/i/status/2064234290511331676"
source_type = "x-post"
newsletter_candidate = true
why_it_matters = "a clean articulation of the shift from prompt engineering toward harness/system design, reliability coming from execution, verification, and environment structure, not just smarter base models."
saved_link = "https://x.com/i/status/2064234290511331676"
+++
**What it is:** How To AI thread summarizing the Stanford + Meta “Code as Agent Harness” paper.

**Gist:** the core claim is that reliable agents should externalize reasoning into executable code instead of relying on free-form natural-language chain-of-thought. In this framing, code becomes the agent harness: scripts hold state, tests/verifiers provide feedback, execution logs become memory, and the environment constrains behavior through real runtime errors rather than vague self-talk.

**Newsletter angle:** “the important unit of agent capability is the harness, not the prompt” or “code is becoming the runtime substrate for agent reasoning.”

**Note:** extracted via FXTwitter note-tweet payload; saved as a secondary summary/interpretation of the paper rather than a direct read of the paper itself.
