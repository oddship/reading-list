+++
title = "DSLs enable reliable use of LLMs"
slug = "2026-07-14-dsls-enable-reliable-use-of-llms"
date = 2026-07-14T20:54:00+05:30
[taxonomies]
tags = ["agents", "developer-tools", "systems"]
[extra]
source_url = "https://martinfowler.com/articles/llm-and-dsls.html"
source_type = "article"
newsletter_candidate = true
why_it_matters = "Strong articulation of a recurring pattern in good AI engineering: move effort from reviewing arbitrary generated code toward building better vocabularies, abstractions, and validators that make generation reliable by construction."
saved_link = "https://x.com/i/status/2077023024155422927"
+++
**Logged at IST:** 2026-07-14 20:54 IST

**What it is:** Martin Fowler sharing Unmesh Joshi’s article on DSLs and LLM reliability

**Gist:** The article’s core claim is that LLMs become much more reliable when they are constrained by domain abstractions and DSLs instead of being asked to directly generate unconstrained general-purpose code. The deeper point is that DSLs do double duty: they help teams discover and stabilize a semantic model during design, and then they become a natural-language target that LLMs can generate against, validate, and repair with much tighter feedback loops.

**Newsletter angle:** Strong articulation of a recurring pattern in good AI engineering: move effort from reviewing arbitrary generated code toward building better vocabularies, abstractions, and validators that make generation reliable by construction.
