+++
title = "How I work with Agents"
slug = "2026-10-26-how-i-work-with-agents-thorsten-ball"
date = 2026-10-26T07:01:00+05:30
[taxonomies]
tags = ["agents", "developer-tools", "ai-infra"]
[extra]
source_url = "https://x.com/i/article/2114385531811319808"
source_title = "How I work with Agents"
source_type = "social"
saved_link = "https://x.com/badlogicgames/status/2114414124042219969"
saved_title = "Mario Zechner recommends Thorsten Ball's agent workflow essay"
related_url = "https://x.com/thorstenball/status/2114386050638336082"
related_title = "Thorsten Ball's announcement of the article"
newsletter_candidate = true
why_it_matters = "A concrete set of agent-workflow principles from Amp: make the full SDLC observable and actionable to agents, test the value of accumulated knowledge, ask agents to build tools for exploration, demand evidence, and delegate larger asynchronous tasks."
retrieval_note = "Read the full X article body, including its 16 recommendations, from the FXTwitter API response for the sharing post. Direct extraction of the X article URL returned HTTP 403; this note is grounded in the complete article payload exposed by that API, not title metadata alone."
+++

Thorsten Ball’s October 2026 guide describes how his team works with coding agents at Amp. The recommendations treat agents less like autocomplete and more like workers that need a visible environment, usable tools, feedback, and clear evidence of completion.

Several ideas stand out:

- **Use the strongest available models.** Ball argues that a model’s error rate compounds into repeated attempts and wasted time, so a cheaper but less capable model may not be a real saving.
- **Prompt for the outcome, not the implementation.** State what success should look like and let the agent choose how to get there.
- **Make the whole software lifecycle legible and actionable.** Agents should be able to run what they build, inspect production logs, deploy, watch rollouts, release, flip flags, and triage reports. If they cannot see something, they may invent it.
- **Test whether accumulated agent knowledge works.** Treat instructions, skills, scripts, and docs as hypotheses: compare agents with and without that context rather than assuming it helps.
- **Have agents build tools for iteration.** Generate variations or competing explanations and create a way to evaluate them, instead of steering every attempt by hand.
- **Ask for evidence, not assurances.** End-to-end walkthroughs, demos, and before/after measurements can help establish whether a change works. Ball cautions against treating unsupported claims as proof.
- **Lean into asynchronous, larger tasks.** Batch work, let agents run independently, and use schedules or wake-ups to return when follow-up is needed rather than hovering over each step.

The piece also recommends reducing anxiety about code accumulation and reviewing selectively, with attention concentrated on high-blast-radius areas. Those are Ball’s judgments from his current workflow, not universal rules: the right review threshold depends on the consequences of failure and how well a project can verify changes.

The connecting theme is to make the agent’s working environment and the result observable. More autonomy is useful when the agent can operate the system end to end and return evidence that a human can assess.

**Source retrieval note:** The X article itself was inaccessible to direct extraction (HTTP 403). Its complete article text was available in the FXTwitter API response for the post that recommended it.

## Shared post

{{ tweet(id="2114414124042219969", url="https://x.com/badlogicgames/status/2114414124042219969") }}
