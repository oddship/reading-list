+++
title = "Alexandru Nedelcu on AI, wisdom, and maintainable code"
slug = "2026-09-22-ai-has-no-wisdom"
date = 2026-09-22T21:59:00+05:30
[taxonomies]
tags = ["agents", "developer-tools"]
[extra]
source_url = "https://alexn.org/blog/2026/09/22/ai-has-no-wisdom-and-neither-will-you/"
source_title = "AI Has No Wisdom and Neither Will You"
source_type = "article"
newsletter_candidate = true
why_it_matters = "A sharp counterweight to AI-coding optimism: maintainability and architecture are slow-feedback skills, and teams can lose judgment if they stop reading and writing code themselves."
saved_link = "https://x.com/badlogicgames/status/2102374897649647627"
saved_title = "Mario Zechner recommending AI Has No Wisdom and Neither Will You"
related_url = "https://x.com/badlogicgames/status/2102374897649647627"
related_title = "Recommendation post on X"
retrieval_note = "X post extracted via FXTwitter; linked Alexandru Nedelcu essay read directly. The recommender tweet is provenance, not the primary source."
+++

**Logged at IST:** 2026-09-22 21:59 IST

**What it is:** Alexandru Nedelcu's critique of the idea that programmers can safely stop reading or writing code because AI agents will handle it.

**Gist:** Nedelcu's argument is not that LLMs are useless. He uses them himself for boring work. His objection is to treating AI-generated code as a replacement for human responsibility, code-reading, and architectural judgment.

The core point is about feedback loops. Maintainability, good architecture, clear invariants, and code that remains easy to evolve are hard to measure immediately. Bad architecture often takes months or years to reveal itself. That makes it a poor fit for reinforcement signals and rulebooks: models can optimize for things that pass tests or look plausible now, while missing the slow-burn consequences that experienced engineers learn to smell through painful production work.

He is especially worried about mastery. If developers stop making choices, stop reading the code, and stop owning mistakes, they also stop building the judgment that lets them know when rules should be bent or replaced. In that world the AI makes mistakes, the person does not learn from them, and the organization quietly loses taste.

{{ tweet(id="2102374897649647627", url="https://x.com/badlogicgames/status/2102374897649647627") }}

**Newsletter angle:** Useful counterpoint to the AI optimization / software-factory items: AI can accelerate work, but teams still need humans building taste, architecture judgment, and code-reading skill.
