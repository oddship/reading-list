+++
title = "Earendil argues AI sessions are becoming provider-sealed state"
slug = "2026-07-30-earendil-session-portability-provider-lock-in"
date = 2026-07-30T22:04:00+05:30
[taxonomies]
tags = ["agents", "ai-infra"]
[extra]
source_url = "https://earendil.com/posts/session-portability/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "A crisp way to judge stateful agent APIs: if the local transcript cannot let another model continue, the provider owns part of the session."
saved_link = "https://x.com/i/status/2082838283520786748"
related_url = "https://x.com/mitsuhiko/status/2082838283520786748"
+++
**Logged at IST:** 2026-07-30 22:04 IST

**What it is:** Earendil Engineering, shared by Armin Ronacher, on AI session portability and the quiet lock-in created by provider-bound state.

**Gist:** The useful test is simple: can I export the session, revoke the old provider, and ask another model to continue from a self-contained transcript? Earendil argues that many modern inference features fail that test. Encrypted reasoning, hosted web search, response IDs, opaque compaction, hidden subagent messages, and provider-managed file/cache references can all leave the local transcript as only a partial view of what actually happened.

The essay is careful about the trade-off: provider-sealed state can improve continuity and may help privacy when `store: false` avoids server-side retention. The problem is ownership. If the only durable meaning is an unreadable blob, a server-side foreign key, or a hosted search context the client never saw, the user cannot inspect, export, replay, audit, or delete the full session.

**Newsletter angle:** This is a strong agents/AI-infra item because it reframes lock-in as an event-log problem. Stateful APIs, retained reasoning, compaction, hosted search, and subagents can make agents much better, but the portable version needs readable handoff summaries, full-fidelity hosted-tool logs, auditable inter-agent communication, inspectable compaction, and exportable artifacts. Better performance should not require giving up the ability to leave.

## Embedded source

{{< tweet id="2082838283520786748" url="https://x.com/i/status/2082838283520786748" >}}
