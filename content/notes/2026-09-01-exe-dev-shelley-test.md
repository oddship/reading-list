+++
title = "exe.dev's Shelley Test for agent-era software teams"
slug = "2026-09-01-exe-dev-shelley-test"
date = 2026-09-01T08:50:00+05:30
[taxonomies]
tags = ["agents", "developer-tools", "org-design"]
[extra]
source_url = "https://blog.exe.dev/revisiting-joel"
source_type = "article"
newsletter_candidate = true
why_it_matters = "The Shelley Test reframes software-team quality for agent-heavy engineering: CI latency, observability access, deployment loops, code review, internal tooling, and agent-legible products become first-class team capabilities."
saved_link = "https://x.com/ssh_exe_dev/status/2094432562378895655"
related_url = "https://x.com/ssh_exe_dev/status/2094432562378895655"
retrieval_note = "FXTwitter extracted exe.dev's launch tweet and linked blog URL. The article was read directly."
+++
**Logged at IST:** 2026-09-01 08:50 IST

**What it is:** exe.dev revisits Joel Spolsky's classic Joel Test and proposes a nine-question “Shelley Test” for software teams working with coding agents.

**Gist:** The post argues that Joel's original checklist still matters, but agent-heavy software work changes which team capabilities compound. The new questions ask whether the team uses agentic code review, deploys continuously with LLM supervision, has trustworthy end-to-end tests, gives humans and agents easy access to observability, can use the best current models, and keeps merge queues under about three minutes.

The second half is more organizational than technical. exe.dev wants teams to make it easy to stand up new tools and agents, regularly discuss and revise their workflows, and make their products legible to coding agents as users. That last point is sharp: docs such as `llms.txt`, usable auth, and APIs become product surface area because users increasingly judge software by whether their agent can operate it.

The useful frame is that “using AI” is too vague. In practice, agent-era engineering quality depends on feedback-loop latency, deployment confidence, queryable production context, cheap internal tooling, and product affordances that let agents act safely and effectively.

**Newsletter angle:** A compact checklist for agent-era engineering orgs: not vibe-coding, but fast merge queues, trustworthy deploys, observability in the loop, tool-building capacity, and agent-legible product surfaces.

{{ tweet(id="2094432562378895655", url="https://x.com/ssh_exe_dev/status/2094432562378895655") }}
