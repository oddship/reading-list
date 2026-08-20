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
related_url = "https://github.com/oddship/bosun/tree/main/packages/pi-weaver"
retrieval_note = "Grounded from the X post, screenshot, Auto Trees source at commit 341cab6, package metadata for @howaboua/pi-auto-trees v0.1.10, Rohan's pi-weaver write-up, and oddship/bosun packages/pi-weaver source at commit f857b23."
+++
**Logged at IST:** 2026-07-27 04:37 IST

**What it is:** A comparison between Auto Trees' new `/prime <scope>` command for Pi and pi-weaver, using the public `oddship/bosun/packages/pi-weaver` implementation Rohan pointed me to.

**Gist:** These live in the same design space, but they are not the same primitive. Auto Trees asks, “Where should the next clean working context start?” Pi-weaver asks, “When should this failed branch stop existing?”

Auto Trees is a human-triggered session hygiene tool. `/prime <scope>` sends Pi a scoped orientation prompt, asks it to map only relevant code, avoid dependency and README detours, and stop at the boundary. The implementation waits for `agent_settled`, including retries and compaction, then automatically places a marker. Later `/end` summarizes back to that marker and advances it.

The inspected implementation is small and operational: marker state is stored as a custom branch entry, semantic leaf detection skips bookkeeping entries, `/marker` labels the current semantic point, `/prime` schedules auto-marking after the agent settles, and `/end` calls `navigateTree(markerId, { summarize: true, ... })`.

Pi-weaver is a more invasive recovery harness. The public implementation registers three tools: `checkpoint`, `time_lapse`, and `done`. The extension only fully activates when `PI_AGENT=weaver`, injects `WEAVER_PROMPT` before the agent starts, stores checkpoints as `weaver-checkpoint` custom entries, tracks failed bash results after edits, and uses a `context` event to rewrite the next model context. `time_lapse(target, steering)` sets `pendingRewind`; later, the context hook finds the matching checkpoint tool result, slices the message array to that point, and appends steering plus checkpoint state as a fresh user message. It also blocks later batched tool calls while the rewind is pending.

So Auto Trees preserves a good branch compactly. Pi-weaver deliberately discards a bad branch by editing the agent's next context directly. Auto Trees mainly wraps session-tree and summarization ergonomics; pi-weaver changes the control loop with tool registration, prompt policy, context-event pruning, failure reminders, and eval/Harbor adapters. The first is safer production workflow ergonomics. The second is more interesting research machinery for failure recovery, but needs guardrails to avoid expensive, disciplined grinding.

**Newsletter angle:** Strong agent-harness note because it draws a useful control-surface distinction: human-triggered clean context boundaries versus model-triggered branch pruning.

**Retrieval note:** Grounded from the X post, screenshot, Auto Trees source at commit `341cab6`, package metadata for `@howaboua/pi-auto-trees` v0.1.10, Rohan's pi-weaver write-up, and `oddship/bosun/packages/pi-weaver` source at commit `f857b23`.

## Embedded source

{{ tweet(id="2081329769069572363", url="https://x.com/i/status/2081329769069572363") }}
