+++
title = "Softer Software"
slug = "2026-08-16-softer-software"
date = 2026-08-16T13:20:00+05:30
[taxonomies]
tags = ["agents", "developer-tools"]
[extra]
source_url = "https://plugyawn.com/language-as-software/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "A useful frame for treating LLM prompts and harnesses as a probabilistic programming layer rather than as magic or mere chat."
saved_link = "https://plugyawn.com/language-as-software/"
retrieval_note = "Article fetched directly from the Bear Blog page and parsed from the page body."
+++
**Logged at IST:** 2026-08-16 13:20 IST

**What it is:** plugyawn's essay arguing that LLM prompts and agent harnesses can be understood as a softer generalization of software.

**Gist:** The piece starts from SICP's definition of a program as a precise description of a process, then asks whether software can have the same kind of relaxed version that hard functions get in softmax or other continuous approximations. The proposed answer is that an LLM is a stochastic interpreter for informal language. A prompt describes a computational process, the model searches programspace, and the output is the execution trace.

The interesting part is the agent-harness framing. Once models can write and run Python, spawn subagents, gather results, and loop over prompt-search algorithms such as MAP-Elites, English begins to look less like a UI and more like a higher-level programming substrate. The tradeoff is not that it stops being software. It is that the guarantees become probabilistic.

That makes deterministic software more important, not less. Traditional code becomes the first layer of compilation and constraint for a softer, more flexible layer above it.

**Newsletter angle:** Strong agents/programming-language item: useful language for explaining why English-plus-harness workflows may sit alongside deterministic code as a probabilistic programming layer.
