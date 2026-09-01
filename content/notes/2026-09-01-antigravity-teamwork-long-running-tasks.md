+++
title = "Antigravity Teamwork for long-running agent tasks"
slug = "2026-09-01-antigravity-teamwork-long-running-tasks"
date = 2026-09-01T09:01:00+05:30
[taxonomies]
tags = ["agents", "developer-tools", "ai-infra"]
[extra]
source_url = "https://g.dev/cloud/ksp-agy-teamwork"
source_type = "article"
newsletter_candidate = true
why_it_matters = "A hands-on Antigravity Teamwork report shows long-running multi-agent coding becoming productized around spec refinement, milestone artifacts, adversarial review, liveness checks, and final verification."
saved_link = "https://x.com/ksprashu/status/2094497945232323003"
related_url = "https://x.com/ksprashu/status/2094497945232323003"
related_urls = ["https://antigravity.google/blog/teamwork-when-ai-becomes-a-research-partner", "https://antigravity.google/docs/teamwork/", "https://github.com/ksprashu/anotato", "https://anotato-powot63zaa-uc.a.run.app/"]
retrieval_note = "FXTwitter extracted Prashanth Subrahmanyam's tweet and linked g.dev/Medium URL. The Medium walkthrough plus official Antigravity Teamwork launch blog and docs were read directly. The linked demo app and repo were recorded from the article, not deeply audited."
+++
**Logged at IST:** 2026-09-01 09:01 IST

**What it is:** Prashanth Subrahmanyam's hands-on walkthrough of Google Antigravity's `/teamwork-preview`, using it to run a long multi-agent coding task.

**Gist:** The post is useful because it shows the product shape, not just the launch claim. Teamwork first rewrites the user's rough requirement into a spec, asks clarifying questions, defines acceptance criteria, and presents an approval artifact. After approval, it delegates to a team-lead/orchestrator setup that breaks the work into milestones and spins up implementation, challenger, reviewer, forensic auditor, and final victory-auditor subagents.

The concrete test project was Anotato: a small app for pasting screenshots, adding visual annotations, and copying an annotated image plus textual notes back into a coding harness. Prashanth says the build ran for a little over two hours, needed no further human intervention after plan approval, and produced a working deployed app and source repo. His visible workflow notes match the official Antigravity docs: Teamwork is designed for long-running projects, structured handoffs, milestone artifacts, isolated workspaces, and independent verification gates.

The broader signal is that multi-agent coding is becoming a productized harness pattern. The interesting parts are not just “more agents,” but spec refinement before execution, adaptive team composition, liveness monitoring, explicit challenger/auditor roles, and a final artifact that summarizes tests and run instructions.

**Newsletter angle:** Long-running agent work is moving toward managed teams: approval-gated specs, milestone plans, subagent handoffs, adversarial verification, and final “prove it works” audits.

{{ tweet(id="2094497945232323003", url="https://x.com/ksprashu/status/2094497945232323003") }}
