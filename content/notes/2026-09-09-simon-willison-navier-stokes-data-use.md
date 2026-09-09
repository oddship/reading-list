+++
title = "Simon Willison on Navier-Stokes and AI training-data ambiguity"
slug = "2026-09-09-simon-willison-navier-stokes-data-use"
date = 2026-09-09T18:24:00+05:30
[taxonomies]
tags = ["llm-research", "agents", "org-design"]
[extra]
source_url = "https://simonwillison.net/2026/Sep/8/on-navier-stokes/"
source_type = "blog-post"
newsletter_candidate = true
why_it_matters = "The Navier-Stokes controversy makes AI product data-use policies concrete: private research traces and even rumors can become competitive signal when agentic systems can spend massive compute to reproduce a result."
saved_link = "https://x.com/simonw/status/2097474703380365698"
related_url = "https://x.com/simonw/status/2097474703380365698"
related_urls = ["https://openai.com/index/navier-stokes-solution/", "https://cims.nyu.edu/~tristanb/statement.pdf", "https://anil.recoil.org/notes/rumour-is-the-exploit"]
retrieval_note = "Original X post extracted via FXTwitter; Simon Willison's article, OpenAI's Navier-Stokes announcement, Tristan Buckmaster's statement PDF, and Anil Madhavapeddy's related security post were fetched directly."
+++
**Logged at IST:** 2026-09-09 18:24 IST

**What it is:** Simon Willison's commentary on OpenAI's announced AI-produced resolution of the Navier-Stokes Millennium Prize Problem, and on the dispute around Tristan Buckmaster and Levent Alpöge's related work.

**Gist:** Simon's useful framing is that the controversy is not only about whether OpenAI scooped another team. It is also about the ambiguous promise that user data may be "used to improve model performance." OpenAI says its researchers and agents did not access Buckmaster and Alpöge's work or any specific user data, but also says it cannot rule out de-identified data derived from their product usage having helped improve models.

That turns a vague data-policy clause into a concrete scientific-credit problem. If someone uses Codex or ChatGPT while developing a valuable result, could traces of that work later improve a model that helps someone else finish first? Even if the answer is "unlikely," the lack of auditability is now part of the story.

The article also connects this to Anil Madhavapeddy's "rumour is the exploit" argument in security: once a high-value direction is known, agents plus compute can rapidly search the space. In math and research, the leaked signal may be not a vulnerability class but the fact that a promising path exists.

**Newsletter angle:** A strong item on AI data governance and research norms: competitive agentic systems make private tool use, model-improvement clauses, and rumor-driven solution races part of the same credit-and-disclosure problem.

## Embedded source

{{ tweet(id="2097474703380365698", url="https://x.com/simonw/status/2097474703380365698") }}
