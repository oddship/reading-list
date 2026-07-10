+++
title = "agent principal-agent problem"
slug = "2026-05-07-agent-principal-agent-problem"
date = 2026-05-07
[taxonomies]
tags = ["reading-log", "article", "crawshaw-io", "historical-backfill", "agents", "org-design", "llm-research"]
[extra]
source_url = "https://crawshaw.io/blog/agent-principal-agent"
source_type = "article"
newsletter_candidate = true
why_it_matters = "this is one of the clearest process-level arguments for why agent productivity gains may accrue unevenly, favoring small trusted teams over large review-heavy orgs."
saved_link = "https://crawshaw.io/blog/agent-principal-agent"
+++
Imported from historical reading log.
- Read `The agent principal-agent problem` by David Crawshaw.
- Core claim: classic review-before-commit code review assumed a human contributor whose effort and understanding could be inferred from the code; agent-mediated contribution breaks that signal and creates a principal-agent problem where reviewers absorb heavy load from low-effort, lightly-validated `slop PRs`.
- The useful distinction is not just `agents good/bad`, but `high-trust small teams` versus `low-trust large organizations`: small teams can collapse review and let the human prompter own deployment, while big companies remain bottlenecked by review bandwidth and blame-management.
- The strongest practical point is that agents increase both the volume of changes and the temptation to offload reviewer feedback straight back into the model, which compounds review work instead of shrinking it.
- Why it matters: this is one of the clearest process-level arguments for why agent productivity gains may accrue unevenly, favoring small trusted teams over large review-heavy orgs.
- Good angle: `agents may be a force multiplier mostly where trust is already high; in low-trust orgs they amplify review economics instead`.
