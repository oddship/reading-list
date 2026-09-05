+++
title = "Anthropic formalizes Fermat's Last Theorem"
slug = "2026-09-05-anthropic-formalizes-fermats-last-theorem"
date = 2026-09-05T10:58:00+05:30
[taxonomies]
tags = ["llm-research", "agents", "developer-tools"]
[extra]
source_url = "https://www.anthropic.com/research/formalizing-fermats-last-theorem"
source_type = "research-post"
newsletter_candidate = true
why_it_matters = "A complete Lean formalization of Fermat's Last Theorem is a milestone for autoformalization, but the useful lesson is the scaffold around the agents: theorem DAGs, reuse, compilation control, and independent checking."
saved_link = "https://x.com/Leonard41111588/status/2095958530125689240"
related_url = "https://xenaproject.wordpress.com/2026/09/04/flt-anthropic-has-beaten-me-to-it/"
related_urls = ["https://github.com/anthropics/fermats-last-theorem", "https://prove2.me/"]
retrieval_note = "Leonardo de Moura's X post was extracted via FXTwitter; Anthropic's announcement, Kevin Buzzard's Xena post, and the public GitHub repository page were fetched directly."
+++
**Logged at IST:** 2026-09-05 10:58 IST

**What it is:** Leonardo de Moura pointing to Anthropic's announcement, Kevin Buzzard's reaction, and the public Lean repository for a complete computer-checked formalization of Fermat's Last Theorem.

**Gist:** Anthropic says Claude worked largely autonomously for 11 days and produced an end-to-end Lean proof of Fermat's Last Theorem. The project wrote about 13 million lines of Lean and used roughly 29,500 intermediate theorems in the final proof. The public repository says the proof builds on Lean 4.33.1 and Mathlib 4.33.0, derives Mathlib's statement of `FermatLastTheorem`, uses Lean's standard axioms, and includes comparator and nanoda verification paths.

The interesting systems lesson is the scaffold, not just the headline. Anthropic says early attempts failed when agents lost track of project state. The successful run used Prove2Me to maintain a directed graph of theorem statements, separate statements from proofs for compilation/resource control, and support search and reuse across a Claude Code-based multi-agent harness. That makes this feel like a large-scale agent coordination result as much as an autoformalization result.

Buzzard's Xena post is the useful human-context counterweight. He says the codebase compiled and comparator checked out, but also that the proof follows the Darmon-Diamond-Taylor exposition rather than the modern proof his project is formalizing. His point is not that this creates new mathematics. It shows that AI autoformalization artifacts are now robust enough to formalize thousands of pages of hard literature, and that future mathematical review may shift toward machine-checkable verification plus human-readable exposition.

**Newsletter angle:** Strong agent-infra and research-process item: the milestone is not “AI proves FLT” so much as “multi-agent theorem-proving scaffolds can turn a giant literature formalization into a checked artifact.” The durable questions are cost, maintainability, proof readability, independent verification, and how human mathematicians use these artifacts after the headline.

## Embedded source

{{ tweet(id="2095958530125689240", url="https://x.com/Leonard41111588/status/2095958530125689240") }}
