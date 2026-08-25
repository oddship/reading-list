+++
title = "Speculative tool calls for code-as-action agents"
slug = "2026-08-25-speculative-programmatic-tool-calling"
date = 2026-08-25T12:48:00+05:30
[taxonomies]
tags = ["agents", "developer-tools", "ai-infra"]
[extra]
source_url = "https://alexzhang13.github.io/blog/2026/spec-ptc/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "A concrete harness-level optimization for agents that treat code execution as the main tool, and an early sign that agent runtimes may start borrowing JIT/speculative-execution ideas."
saved_link = "https://x.com/a1zhang/status/2091938825580716079"
related_url = "https://x.com/a1zhang/status/2091938825580716079"
related_urls = ["https://github.com/alexzhang13/spec-ptc", "https://arxiv.org/abs/2512.24601", "https://arxiv.org/abs/2402.01030"]
retrieval_note = "FXTwitter extraction succeeded and resolved the blog URL. The blog HTML plus GitHub README/API metadata were read directly; the attached image was inspected and shows the main sPTC timeline example."
+++
**Logged at IST:** 2026-08-25 12:48 IST

**What it is:** Alex Zhang's post and reference implementation for Speculative Programmatic Tool Calling, or sPTC.

**Gist:** sPTC is a latency trick for agents where the model's main action is code in a REPL. Instead of waiting for the whole generated program to finish before running tools, the harness watches the code stream, speculatively parses likely tool calls, launches expensive sub-agent or sub-LLM calls early, and then lets the real execution claim those cached futures if the calls actually happen.

The idea matters because programmatic tool calling makes the harness more like a runtime than a thin JSON-tool dispatcher. Once tools are functions in generated code, the runtime can overlap root-model decoding with sub-call execution, parallelize blocking calls the model wrote serially, and use a shadow REPL to safely evaluate enough partial state to know which calls are worth launching.

Zhang is careful about the trade-offs: the gains depend on token-generation latency, tool latency, serving-engine load, and how aggressive the speculation is. His reported RLM speedups are modest in the benchmark setting, around 1-1.2x, but the important pattern is broader: agent harnesses are starting to absorb compiler/runtime ideas like speculation, futures, purity contracts, and scheduling.

**Newsletter angle:** Good developer-tools item: code-as-action agents may need runtimes that optimize generated programs underneath the model, not just better prompts or bigger context windows.

{{ tweet(id="2091938825580716079", url="https://x.com/a1zhang/status/2091938825580716079") }}
