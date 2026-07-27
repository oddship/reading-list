+++
title = "Auto Trees prime and pi-weaver as context-control primitives"
slug = "2026-07-27-auto-trees-prime-vs-pi-weaver"
date = 2026-07-27T04:37:00+05:30
[taxonomies]
tags = ["agents", "developer-tools"]
[extra]
source_url = "https://github.com/IgorWarzocha/howaboua-pi-stuff/tree/main/packages/pi-auto-trees"
source_type = "project"
newsletter_candidate = true
why_it_matters = "Useful agent-harness item because it contrasts human-triggered clean context boundaries with model-triggered branch pruning."
saved_link = "https://x.com/i/status/2081329769069572363"
related_url = "https://rohanverma.net/pages/harness-engineering/research/pi-weaver/"
retrieval_note = "Grounded from the X post, screenshot, Auto Trees source at commit 341cab6, package metadata for @howaboua/pi-auto-trees v0.1.10, and Rohan's pi-weaver architecture write-up/site source. I did not find a public pi-weaver package or repo, so pi-weaver implementation details come from the write-up rather than source code inspection."
+++
**Logged at IST:** 2026-07-27 04:37 IST

**What it is:** A comparison between Auto Trees' new `/prime <scope>` command for Pi and Rohan's pi-weaver research write-up.

**Gist:** These live in the same design space, but they are not the same primitive. Auto Trees asks, “Where should the next clean working context start?” Pi-weaver asks, “When should this failed branch stop existing?”

Auto Trees is a human-triggered session hygiene tool. `/prime <scope>` sends Pi a scoped orientation prompt, asks it to map only relevant code, avoid dependency and README detours, and stop at the boundary. The implementation waits for `agent_settled`, including retries and compaction, then automatically places a marker. Later `/end` summarizes back to that marker and advances it.

The inspected implementation is small and operational: marker state is stored as a custom branch entry, semantic leaf detection skips bookkeeping entries, `/marker` labels the current semantic point, `/prime` schedules auto-marking after the agent settles, and `/end` calls `navigateTree(markerId, { summarize: true, ... })`.

Pi-weaver is a more invasive recovery harness. The write-up describes three tools: `checkpoint`, `time_lapse`, and `done`. `time_lapse(label, steering)` sets a pending rewind; a later context event truncates everything after the checkpoint and injects steering before the next model call. That lets the model throw away a bad branch rather than merely summarize it.

So Auto Trees preserves a good branch compactly. Pi-weaver deliberately discards a bad branch. The first is safer production workflow ergonomics. The second is more interesting research machinery for failure recovery, but needs guardrails to avoid expensive, disciplined grinding.

**Newsletter angle:** Strong agent-harness note because it draws a useful control-surface distinction: human-triggered clean context boundaries versus model-triggered branch pruning.

**Retrieval note:** Grounded from the X post, screenshot, Auto Trees source at commit `341cab6`, package metadata for `@howaboua/pi-auto-trees` v0.1.10, and Rohan's pi-weaver architecture write-up/site source. I did not find a public pi-weaver package or repo, so pi-weaver implementation details come from the write-up rather than source code inspection.
