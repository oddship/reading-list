+++
title = "Deer Workflow as code-led agent orchestration"
slug = "2026-07-27-deer-workflow-dynamic-workflow-runtime"
date = 2026-07-27T04:40:00+05:30
[taxonomies]
tags = ["agents", "developer-tools"]
[extra]
source_url = "https://deerwork-ai.github.io/deer-workflow/"
source_type = "project"
newsletter_candidate = true
why_it_matters = "Useful agent-infra item because it puts workflow control back in TypeScript while reserving model calls for judgment-heavy steps."
saved_link = "https://x.com/i/status/2081313440573137291"
retrieval_note = "Grounded from the X post, project landing page, repository README, API docs, and selected source files at deerwork-ai/deer-workflow commit db77223."
+++
**Logged at IST:** 2026-07-27 04:40 IST

**What it is:** Deer Workflow is an open-source Dynamic Workflow runtime for AI agents, published as `@deerwork-ai/deer-workflow` with a `deer-workflow` CLI.

**Gist:** The project argues for a middle ground between traditional workflows and autonomous agents: keep orchestration, order, concurrency, phases, and schemas in ordinary TypeScript, and call an agent only where judgment is needed. Its visible slogan captures the split: “Let code drive the flow. Agents handle judgment.”

The implementation matches that framing. Workflow modules export a handler and optional static `meta`; `phase()` emits lifecycle events; `parallel()` starts lazy tasks concurrently and returns `null` for failed branches; `pipeline()` moves each item independently through typed stages; and the default `agent()` runtime wraps non-interactive `codex exec`. The CLI can generate workflows from prompts, run workflow files with JSON input, and expose a JSONL event stream for automation.

**Newsletter angle:** Useful agent-infra item because it makes the control boundary explicit: code owns deterministic orchestration, while models are replaceable judgment calls inside that structure.

**Retrieval note:** Grounded from the X post, project landing page, repository README, API docs, and selected source files at `deerwork-ai/deer-workflow` commit `db77223`.

## Embedded source

{{<tweet id="2081313440573137291" url="https://x.com/i/status/2081313440573137291"/>}}
