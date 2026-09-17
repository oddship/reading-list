+++
title = "Cadence argues for embodied AGI without transformer-style attention"
slug = "2026-09-17-cadence-embodied-agi-without-attention"
date = 2026-09-17T19:34:00+05:30
[taxonomies]
tags = ["agents", "llm-research", "systems"]
[extra]
source_url = "https://muellerberndt.medium.com/you-dont-need-attention-after-all-the-road-to-embodied-agi-with-cadence-8606a64e40df"
source_type = "article"
newsletter_candidate = true
why_it_matters = "Cadence is a concrete open-source attempt to make embodied learning about persistent local state, writable records, and online adaptation rather than ever-longer attention over history."
saved_link = "https://muellerberndt.medium.com/you-dont-need-attention-after-all-the-road-to-embodied-agi-with-cadence-8606a64e40df"
related_urls = ["https://github.com/muellerberndt/cadence", "https://floatingpragma.io/cadence/paper.pdf", "https://floatingpragma.io/cadence-examples/"]
retrieval_note = "Medium article, GitHub README, and draft paper were extracted directly. The note uses the public article as the saved source and the paper/README for technical grounding."
+++

**Logged at IST:** 2026-09-17 19:34 IST

**What it is:** Bernhard Mueller's long-form introduction to Cadence, an open-source neural architecture from Pragma Research aimed at embodied AGI.

**Gist:** Cadence argues that a robot brain should not be organized around a frozen transformer stack attending over a growing history. Its proposed alternative is a mesh of bounded recurrent patches that settle into local agreement, keep state across moments, write experience into sparse records, and update synapses while the machine continues acting.

The Medium article frames the motivation in embodied terms: a household robot needs to learn its body, its surroundings, and the consequences of actions without a separate train-then-freeze lifecycle. The draft paper sharpens the claim: Cadence combines recurrent settling, local equilibrium contrast, sparse record memory, and configurable wiring. Reported experiments include simulated arms and artists that learn from record writes, memory-world interventions where erasing records damages behavior, and localized solver repairs that can be cheaper than recomputing the whole network. The paper is careful that conventional methods still win some latency, language, and music comparisons, and that physical-robot transfer and lower total resource cost are the decisive tests.

The useful signal is not "attention is dead." It is a testable architectural bet: for embodied agents, memory should live in persistent state, writable records, and local repair loops, not only in a context window or external transcript.

**Newsletter angle:** A good research counterpoint to transformer-first AGI stories: if intelligence is embedded in a body, the hard system problem may be continual consequence learning under energy, memory, and validation budgets.
