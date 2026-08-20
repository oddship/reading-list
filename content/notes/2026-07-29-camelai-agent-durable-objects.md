+++
title = "camelAI moved its coding agent off VMs"
slug = "2026-07-29-camelai-agent-durable-objects"
date = 2026-07-29T01:57:00+05:30
[taxonomies]
tags = ["agents", "ai-infra", "developer-tools"]
[extra]
source_url = "https://x.com/i/article/2082137754788646912"
source_type = "x-article"
newsletter_candidate = true
why_it_matters = "A concrete agent-infra case study on replacing always-on VM sandboxes with Durable Objects, object storage, explicit platform methods, and pay-per-execution Workers."
saved_link = "https://x.com/i/status/2082138839888589200"
related_url = "https://github.com/qaml-ai/camelAI"
retrieval_note = "Grounded from FXTwitter article text and public GitHub repository metadata."
+++
**Logged at IST:** 2026-07-29 01:57 IST

**What it is:** Miguel Salinas explains how camelAI rewrote its coding agent stack to stop running each user on an always-on virtual machine.

**Gist:** The old camelAI setup used the Claude Code harness and a self-built VM/container service. That worked, but always-on machines plus attached disk were too expensive for the scale they wanted. The rewrite moved the “brain” of the agent into a Cloudflare Durable Object first, then removed the VM-backed project runtime entirely.

The current stack stores each project filesystem in Durable Object SQLite, with larger files in R2 and git history through Cloudflare Artifacts. The agent harness uses lower-level pieces from Mario Zechner’s `pi` rather than the full OS-assuming layer. Instead of bash, the agent writes JavaScript that runs through Code Mode and Cloudflare dynamic Workers in fresh V8 isolates.

The tradeoff is explicit capability design. Without bash, the agent can only do what camelAI has provided methods for: file reads/writes/edits, grep/glob, deploys, builds, notebooks, and similar platform actions. Builds and notebooks still use short-lived Linux containers because they genuinely need that environment. The upside is lower cost, lower latency, less infrastructure, controlled credentials, and a smaller action space that cheaper models can handle better.

**Newsletter angle:** Strong agent-infra item because it pushes against the default “coding agent equals Linux sandbox” architecture. The interesting product lesson is that removing open-ended bash can be a feature if it forces capabilities into explicit, safer, cheaper platform methods.

## Embedded source

{{ tweet(id="2082138839888589200", url="https://x.com/i/status/2082138839888589200") }}
