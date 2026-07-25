+++
title = "Letta trajectory standardizes agent experience data"
slug = "2026-07-25-letta-trajectory-agent-experience-data"
date = 2026-07-25T12:49:00+05:30
[taxonomies]
tags = ["agents", "developer-tools"]
[extra]
source_url = "https://www.letta.com/blog/trajectory/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "Useful agents and developer-tools item because it turns messy local coding-agent transcripts into portable experience data for memory, search, and learning loops."
saved_link = "https://www.letta.com/blog/trajectory/"
retrieval_note = "Grounded from the Letta blog post fetched directly."
+++
**Logged at IST:** 2026-07-25 12:49 IST

**What it is:** Letta blog post introducing `@letta-ai/trajectory`, a normalized format and package for coding-agent session data.

**Gist:** Letta argues that agents can learn from past sessions across Claude Code, Codex, Letta Code, and other harnesses only if the experience is normalized into a token-efficient, agent-readable format. `trajectory` represents user messages, assistant messages, reasoning, tool calls, tool results, and harness metadata in one standard record schema.

The key design choice is to optimize for agents reading past sessions, not full-fidelity replay or benchmarking. The format drops harness bookkeeping, duplicated payloads, UI event streams, encrypted reasoning blobs, and can truncate long tool outputs. Letta says this gives roughly 5x token reduction versus native session formats on sampled coding sessions, and uses it in Letta Code for cross-harness memory search and background "dreaming" over recent work.

**Newsletter angle:** Useful agents and developer-tools item because it turns messy local coding-agent transcripts into portable experience data for memory, search, and learning loops.

**Retrieval note:** Grounded from the Letta blog post fetched directly.
