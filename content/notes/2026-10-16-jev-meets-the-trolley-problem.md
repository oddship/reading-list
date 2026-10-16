+++
title = "Jev meets the trolley problem"
slug = "2026-10-16-jev-meets-the-trolley-problem"
date = 2026-10-16T13:11:00+05:30
[taxonomies]
tags = ["agents", "ai", "evaluation", "ethics"]
[extra]
source_url = "https://zachlandes.com/trolley-problem/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "A large, inspectable experiment shows that decision-model outputs can vary with scenario framing and wording, while reported confidence should not be mistaken for moral correctness or calibrated certainty."
source_title = "Jev Meets the Trolley Problem"
+++
**Logged at IST:** 2026-10-16 13:11 IST

**What it is:** Zach Landes's interactive comparison of Jev, OpenAI's Decisions API (GPT-6 Luna), and twelve local decision models on trolley-problem scenarios.

**Gist:** Across 5,240 setups, the experiment varies scenario, wording, description order, and crowd size. Most models pull the lever to save five people at the cost of one, but choices shift in variants involving a model's own server or developer, and as the number of people changes. The results are a useful reminder that a decision model's probability is not a measure of moral correctness; some repeated runs straddle the decision threshold, and wording can materially affect choices.

The author reports important limits: comparisons depend on the tested prompts and model versions, some Jev-format findings are exploratory, and the results do not rank moral choices. The interactive page and frozen prompt/results data make the experiment inspectable.

**Why it matters:** Decision models expose choices and confidence directly, but this study demonstrates how sensitive those choices can be to framing, and why a confidence score should not be confused with sound judgment.

**Source:** https://zachlandes.com/trolley-problem/
