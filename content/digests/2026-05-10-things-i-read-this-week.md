+++
title = "Things I read this week"
date = 2026-05-10
[taxonomies]
tags = ["digest", "newsletter", "historical-backfill"]
[extra]
source_file = "/root/.openclaw/workspace-rohan-work/tmp/newsletter-draft-2026-05-10-weekly.md"
status = "published"
+++
## Intro

I have been collecting a lot of links lately: blog posts, product launches, research notes, tweets, and side threads that felt worth saving.

So instead of forcing them into one big argument, I wanted to do a simpler weekly roundup: what I read, what stood out, and why each link felt worth keeping.

A few themes did repeat in the background — agent workflow design, review loops, tooling surfaces, and infrastructure — but I have tried to keep this mostly focused on the links themselves.

## AI coding and workflow design

### antirez on building Redis Array
<https://antirez.com/news/164>

A very grounded write-up from antirez on building Redis Array over about four months with heavy AI assistance. What I liked here is that AI shows up throughout the process — spec iteration, implementation, testing, review, and follow-on tooling work — without the post ever pretending the system built itself.

Mitchell Hashimoto highlighted it too:
<https://x.com/i/status/2051684321732530680>

### Anthropic's managed agents update
<https://claude.com/blog/new-in-claude-managed-agents>

Anthropic added three notable ideas to managed agents: memory cleanup (`dreaming`), explicit artifact goals plus grading (`outcomes`), and multi-agent orchestration. Worth reading as a product signal: more of the harness layer is becoming explicit.

### Rach on Autodata-style loops for software agents
<https://x.com/i/status/2052209530801668262>

This connects Meta's Autodata framing to software work: hypothesis, generate data, test, validate, learn, repeat. The linked `devswarm` repo is useful context too, since it shows what these reviewer/fixer loops look like in a more concrete software setting.

### MetaSKILLs
<https://swival.dev/pages/metaskills.html>

A nice framing from Frank/jedisct1: some agent workflows are not just instructions, but loops. This feels especially relevant if you think of skills as workflow structures rather than just prompt files.

### David Crawshaw on the principal-agent problem for code review
<https://crawshaw.io/blog/agent-principal-agent>

One of the better process-level essays I read this week. The core point is that agent-generated code changes review economics, especially in larger organizations where review bandwidth is already scarce.

### Mitchell Hashimoto on “AI slop” as exploratory scaffolding
<https://x.com/i/status/2052397933522506079>

This was more nuanced than the phrase suggests. The useful framing is that rough generated code can still be valuable for reversible exploration: prototype UIs, disposable plugins, temporary surfaces, and internal experimentation.

### Firefox security bug-fix spike with Claude assistance
<https://x.com/i/status/2052468573516513762>

Anthropic shared a chart claiming Firefox fixed more security bugs in April 2026 than in the previous fifteen months combined, with help from Claude Mythos Preview. Caveats aside, it is an interesting datapoint for AI-assisted maintenance and security work.

## Tooling around agents

### Hunk: a diff viewer built for agent-authored changes
<https://x.com/i/status/2052128048288567617>

Mitchell Hashimoto recommended Hunk pretty strongly. It looks like a review-first terminal diff tool with a lot of attention paid to multi-file review, annotations, and agent-generated changesets.

### Mirage: unified filesystem interface for agents
<https://x.com/i/status/2052105012172792061>

Mirage mounts systems like S3, Drive, Slack, Gmail, GitHub, Linear, Notion, databases, and SSH behind a single filesystem abstraction. Interesting if you like the idea of Unix and file semantics as the control plane for cross-service agent work.

### Printing Press: agent-native CLI generation
<https://x.com/i/status/2052422567181611010>

This pitches a library/factory for generating agent-native CLIs, skills, and MCP servers from external services. The interface choice is the interesting bit here: local denormalized command surfaces instead of raw remote APIs.

### Auth for MCP from Auth0
<https://x.com/i/status/2052138238111068277>

A sign that MCP is moving beyond toy demos. Auth0 is pitching this as the missing identity and authorization layer for more serious deployments.

## Search, inference, and model plumbing

### Entire on agentic search
<https://x.com/i/status/2052437618416025846>

One of my favorite links from the week. Entire looked at a large volume of coding-agent tool calls and found that search made up a huge chunk of behavior; the most useful finding was that better ranking seemed to matter more than just faster search latency.

### SubQ sparse-attention claims
Main post:
<https://x.com/i/status/2051663268704636937>

Skeptical follow-up from Mario Zechner:
<https://x.com/badlogicgames/status/2051936321610842245>

SubQ makes very large claims around sparse attention, long context, and compute savings. Mario's skepticism is useful context: the real question is how the model decides what attention relationships to keep and what gets lost.

### DFlash and speculative decoding infrastructure
<https://x.com/i/status/2051900751673467097>

An open-source speculative decoding project for Gemma 4. Beyond the single project, it is a nice signal that inference acceleration is becoming an ecosystem layer with reusable tooling and backend integrations.

### JSON vs protobuf after compression
<https://x.com/i/status/2051977984148467890>

A fun reminder that raw size and compressed size are different questions. In Sam Rose's example, JSON often ended up slightly smaller than protobuf once strong compression was applied.

### Microwave-noise training-data anecdote
<https://x.com/i/status/2051873677998956851>

A funny post, but also a useful one. The claim is that a GPT-3 training loss spike was traced to weird scraped data from a `microwavegang` community full of repetitive junk text, and the spike disappeared after cleanup.

## Organizations, infrastructure, and the business layer

### Microsoft's Work Trend Index on agentic organizations
<https://x.com/i/status/2051787232043020719>

The packaging is very Microsoft, but the underlying point is worth reading: AI impact inside organizations may depend more on workflow, management, and incentives than on raw model access.

### Simon Willison on the xAI/Anthropic data-center deal
<https://x.com/i/status/2052436629365948920>

A useful note on supply-side dependency, environmental cost, and the awkwardness of one frontier AI company depending on infrastructure controlled by another.

### Gray markets for Claude access in China
<https://x.com/i/status/2052023116348469608>

An interesting ChinaTalk-linked piece on the ecosystem of intermediaries, proxying, payments, and access workarounds that emerge when frontier model access is blocked or restricted.

### Chrome and Gemini Nano silent-install complaints
<https://x.com/i/status/2051630929622311250>

Interesting less as Chrome drama and more as a signal: on-device AI is increasingly showing up as platform behavior, with the usual questions around consent, storage, visibility, and user control.

## India, public infrastructure, and useful software

### ParliamentWatch
<https://x.com/i/status/2052264995787079900>

A very good civic-tech project that makes Indian parliamentary standing committee reports searchable, summarizable, exportable, and easier to track. One of the most obviously useful links in the whole batch.

### Pratilekha
<https://x.com/i/status/2051675299428143565>

An early signal from Bangalore around multilingual AI infrastructure: “one API, every Indian & regional language.” Still early, but worth tracking.

## Internet infrastructure and operational fragility

### The `.de` / DNSSEC outage cluster
HN thread:
<https://news.ycombinator.com/item?id=48027897>

Thomas Ptacek resurfacing *Against DNSSEC*:
<https://sockpuppet.org/blog/2015/01/15/against-dnssec/>

Thomas Ptacek on the specific `.de` incident:
<https://x.com/i/status/2051802131636592846>

This cluster was worth reading together: the outage itself, the older DNSSEC critique, and the real-world resolver behavior during the incident.

### Nemo on the `.in` / Namecheap WHOIS issue
<https://captnemo.in/blog/2026/05/05/namecheap-whois/>

Useful context on the recent `.in` domain suspension incident. The most important detail here is that it appears to involve a registrar-side bug interacting badly with ccTLD policy.

## A few smaller things I bookmarked

- Martin Fowler's `Fragments: May 5`: <https://martinfowler.com/fragments/2026-05-05.html>
- Dell and Lenovo becoming premier sponsors of LVFS: <https://x.com/i/status/2052013565373026679>
- `nless` for exploring logs/CSV/JSON as terminal tables: <https://x.com/i/status/2051733119405817951>
- Ben Holmes on Slate vs TipTap/ProseMirror ergonomics: <https://x.com/i/status/2051492921430384656>

## Closing note

I like this format better for now.

It is closer to how I actually consume this stuff during the week: save a link, read it later, pull out the interesting bit, move on.

Some weeks there will be a stronger theme and that may justify a more opinionated essay. But most weeks probably do not need that. A simple roundup of things read, shipped, argued, or discovered is useful on its own.

If this becomes a recurring thing, I will probably keep the structure lightweight:

- a short intro
- grouped links
- 2–4 lines on why each one was worth saving
- maybe one short closing note

That feels sustainable.

## Possible titles

- Things I read this week
- The week that was: links and notes
- Interesting things I read this week
- Weekly reading list
- Notes from this week's reading pile
