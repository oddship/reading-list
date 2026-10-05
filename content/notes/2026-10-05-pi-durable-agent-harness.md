+++
title = "Pi Durable extends a coding harness into long-running agent applications"
slug = "2026-10-05-pi-durable-agent-harness"
date = 2026-10-05T14:38:00+05:30
[taxonomies]
tags = ["agents", "developer-tools"]
[extra]
source_url = "https://earendil.com/posts/pi-durable/"
source_type = "x-post"
newsletter_candidate = true
why_it_matters = "It treats durable agent work as a runtime and storage problem: transcripts, task state, execution environments, restart behavior, and shared human steering are explicit parts of the harness."
saved_link = "https://x.com/badlogicgames/status/2105739632168054992"
saved_title = "Mario Zechner on Pi Durable"
source_title = "Pi Durable"
related_urls = ["https://earendil.com/posts/pi-1-0/", "https://earendil.com/posts/you-said-no-mcp/"]
related_titles = ["Pi 1.0", "You Said No MCP!"]
+++
**Logged at IST:** 2026-10-05 14:38 IST

**What it is:** Pi Durable is an experimental TypeScript harness for building long-running agent applications. It ships alongside Pi 1.0, the hardened coding agent, but is a separate substrate rather than a replacement for that product.

**Gist:** The design starts from the assumption that an agent may need to run across process restarts, use different execution environments, continue long conversations, and be steered by more than one person. The harness combines conversation storage with task execution and tools. The project describes memory, SQLite, and JSONL storage backends, and emphasizes a small, inspectable codebase that agents themselves can work with. Pi 1.0 adds native MCP through codemode, deferred tool loading, virtual model extensions, and transcript-aware system messages.

**Why it matters:** “Agent harness” becomes more than a prompt loop when tasks must survive failures and move between interfaces. Persistence, replayable task state, and human steering are runtime concerns, not features that can safely be left to a long-lived chat session.

**Caveat:** Pi Durable is experimental. The linked launch articles describe the authors’ intended design; the two demo videos attached to the X post were not independently reviewed.
