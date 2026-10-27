+++
title = "Reforging the workflow for agents"
slug = "2026-10-27-reforging-the-workflow"
date = 2026-10-27T18:22:30+05:30
[taxonomies]
tags = ["agents", "developer-tools"]
[extra]
source_url = "https://mgratzer.com/posts/reforging-the-workflow/"
source_title = "Reforging the Workflow: Where the Human Goes When Agents Ship"
source_type = "article"
saved_link = "https://x.com/mgratzer/status/2114726996869595265"
saved_title = "Martin Gratzer on how his work with agents changed"
related_url = "https://x.com/mgratzer/status/2114726996869595265"
related_title = "Martin Gratzer’s workflow diagram and summary"
newsletter_candidate = true
why_it_matters = "A concrete account of shifting engineering attention from line-by-line review to problem shaping, independent checks, risk triage, and guardrails, with important caveats about project risk and organizational context."
+++

Martin Gratzer describes moving from reviewing each agent-written diff to shaping the work before it starts and improving the system around the agent. He still breaks work into independently shippable vertical slices. Fresh-context reviews, exercised changes, mechanical checks, and risk assessment catch issues; low-risk pull requests can merge automatically, while higher-risk changes come with a focused list of where a person should look.

The key shift is not simply trusting agents more. It is making trust depend on structure: repositories and workflow tooling encode guardrails, and mistakes become reasons to improve those guardrails. Human attention moves toward framing the problem, judging domain-specific questions, and spotting patterns across failures. The author is explicit that this setup does not transfer unchanged to every team: compliance, shared understanding, and higher-stakes production contexts still matter.

{{ tweet(id="2114726996869595265", url="https://x.com/mgratzer/status/2114726996869595265") }}