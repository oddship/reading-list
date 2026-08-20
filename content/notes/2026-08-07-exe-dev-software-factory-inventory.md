+++
title = "exe.dev's software factory inventory"
slug = "2026-08-07-exe-dev-software-factory-inventory"
date = 2026-08-07T16:17:00+05:30
[taxonomies]
tags = ["agents", "ai-infra", "developer-tools", "systems"]
[extra]
source_url = "https://blog.exe.dev/inventory"
source_type = "article"
newsletter_candidate = true
why_it_matters = "A concrete inventory of the agentic internal tools exe.dev uses for security, ops, CI, deploys, publishing, and reporting, useful as a map of where agents can become production operating leverage rather than demos."
saved_link = "https://x.com/i/status/2085567322606178476"
related_url = "https://x.com/ssh_exe_dev/status/2085567322606178476"
related_urls = ["https://status.exe.dev/", "https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/", "https://sketch.dev/blog/agent-loop"]
retrieval_note = "Extracted exe.dev’s X post via FXTwitter and read the linked exe.dev blog post directly."
+++
**Logged at IST:** 2026-08-07 16:17 IST

**What it is:** exe.dev’s X post pointing to Philip Zeyliger’s inventory of the internal agents, bots, and operational tools they use to run exe.

**Gist:** The post is useful because it lists the actual places where exe.dev has put agents and small internal systems into its operating loop. They have agents for systematic security review, alert investigation, daily log-trend emails, and deploy supervision. They also have bots that look for flaky or slow tests, a homegrown status page, Pushover-based phone paging, and daily Slack reports about git commits and support/help threads.

The more interesting entries are about company workflow, not just infrastructure. Their blog has moved from Markdown in git to a full CMS with collaborative editing, comments, revision history, embargoes, a content calendar, and an agent that can import a post from pasted content. Their UI tests are drifting away from hand-maintained Playwright scripts toward textual paragraphs that materialize into browser instructions, cache the generated steps, and self-heal in CI when they fail.

There is a security caveat baked into the post: agents that read untrusted data while holding private context and external communication tools are in Simon Willison’s “lethal trifecta” danger zone. exe.dev’s answer is to isolate these loops in VMs and sharply limit what their tools can do.

**Newsletter angle:** Good concrete inventory for what “agentic internal tooling” looks like after the demo phase. The pattern is not one giant autonomous engineer. It is a patchwork of narrowly scoped loops around security, observability, CI, deploys, publishing, and reporting, with isolation and tool limits as part of the operating model.

## Embedded source

{{< tweet id="2085567322606178476" url="https://x.com/i/status/2085567322606178476" >}}
