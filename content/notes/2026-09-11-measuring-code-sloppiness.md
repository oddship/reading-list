+++
title = "Earendil measures code sloppiness beyond correctness"
slug = "2026-09-11-measuring-code-sloppiness"
date = 2026-09-11T17:42:00+05:30
[taxonomies]
tags = ["agents", "developer-tools", "llm-research"]
[extra]
source_url = "https://earendil.com/posts/measuring-code-sloppiness/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "When coding agents can satisfy tests, the remaining risk is codebase erosion: unnecessary volume, duplication, abstraction, and complexity that make humans lose agency."
saved_link = "https://x.com/pidotdev/status/2098373492362428683"
related_url = "https://x.com/pidotdev/status/2098373491586425056"
retrieval_note = "Tweet and parent post extracted via FXTwitter; linked Earendil article fetched directly. Parent post includes a short launch video, but the article is the primary source."
+++

**Logged at IST:** 2026-09-11 17:42 IST

**What it is:** Sebastian Baye at Earendil asks how to measure the “sloppiness” of code when LLMs can already generate code that often passes tests.

**Gist:** The useful distinction is correctness versus maintainability. Agents can optimize against hidden tests, but formally correct code can still introduce unnecessary abstractions, duplicate logic, excessive volume, and complex functions that make the codebase harder for humans to steer.

Baye is skeptical of simple LLM-as-judge evaluations: scalar ratings are noisy, pairwise preferences can flip under superficial renaming, and rubrics still do not replace human taste. Human review remains the gold standard for readability, but does not scale as a benchmark across providers and harnesses.

The practical metrics he highlights are deliberately imperfect but useful. LOC delta is a crude early warning. SlopCodeBench-style **verbosity** combines AST-grep heuristics and clone detection to estimate duplicated or unnecessary lines. **Erosion** measures how much codebase “mass” is concentrated in large, complex functions using cyclomatic complexity and source lines of code.

The striking result: in the cited comparison, established repos averaged verbosity around 0.15 and erosion around 0.31, while agent-generated code averaged roughly 0.33 and 0.68. In other words, the agent code was about twice as verbose and eroded as human-maintained code by these measures.

**Newsletter angle:** If code generation is becoming abundant, the scarce skill is not just asking for working patches. It is building loops, metrics, and review habits that keep a codebase legible, compact, and human-governable after hundreds of agent iterations.
