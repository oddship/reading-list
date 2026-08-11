+++
title = "DeepSeek V4 Flash across four agent harnesses"
slug = "2026-08-11-deepseek-v4-flash-agent-harnesses"
date = 2026-08-11T09:50:00+05:30
[taxonomies]
tags = ["agents", "developer-tools"]
[extra]
source_url = "https://x.com/composio/status/2086814488162972027"
source_type = "x-post"
newsletter_candidate = true
why_it_matters = "A small but useful reminder that agent harnesses are now part of model performance: the same model can show different pass rates, costs, and latencies depending on the runtime wrapped around it."
saved_link = "https://x.com/i/status/2086814488162972027"
related_url = "https://pbs.twimg.com/media/HPXZaY5XUAAmz_p.jpg?name=orig"
retrieval_note = "Tweet extracted via FXTwitter; attached benchmark image inspected/OCRed. No non-X article, repo, or paper destination was present in the post."
+++
**Logged at IST:** 2026-08-11 09:50 IST

**What it is:** Composio's benchmark image comparing DeepSeek V4 Flash on four agent harnesses: Pi Agent, Prime Agent, Deep Agents, and Hermes Agent.

**Gist:** The post says Composio ran DeepSeek V4 Flash through 30 challenging agentic tasks on four more harnesses. The headline result is that Pi Agent had the best reported combination: 66.7% pass rate, $0.012 median cost per task, and 132s median time per task.

The chart's other reported figures are Prime Agent at 62.5% pass, $0.045, 242s; Deep Agents at 53.3%, $0.018, 187s; and Hermes Agent at 50.0%, $0.017, 176s. Treat this as vendor-published eval signal rather than an independent benchmark, but it is still useful because it frames the harness itself as a material variable in agent performance.

**Newsletter angle:** Good short item for the agent-infra lane: model evals are increasingly runtime evals too, and cost/pass-rate/time can move based on the surrounding agent harness.
