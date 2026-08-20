+++
title = "The end of no-code as agentic Linux"
slug = "2026-08-07-end-of-no-code-agentic-linux"
date = 2026-08-07T03:03:00+05:30
[taxonomies]
tags = ["agents", "developer-tools", "systems"]
[extra]
source_url = "https://blog.exe.dev/the-end-of-no-code"
source_type = "article"
newsletter_candidate = true
why_it_matters = "A sharp post-no-code argument: coding agents make custom internal tools cheap enough that the next low-floor/high-ceiling platform may be boring Linux plus open-source stacks, not proprietary no-code builders."
saved_link = "https://x.com/i/status/2085394068771893725"
related_url = "https://x.com/davidcrawshaw/status/2085394068771893725"
related_urls = ["https://exe.dev/", "https://sketch.dev/blog/agent-loop", "https://boringtechnology.club/"]
retrieval_note = "Extracted David Crawshaw’s X post via FXTwitter and read the linked exe.dev essay directly plus reader fallback."
+++
**Logged at IST:** 2026-08-07 03:03 IST

**What it is:** David Crawshaw’s X post saying “the age of no code has passed,” pointing to Philip Zeyliger / exe.dev’s essay “The End of No Code.”

**Gist:** The essay argues that no-code and low-code platforms solved a real organizational problem: business teams needed better structure than spreadsheets, but buying or deploying custom software was blocked by procurement, IT, infrastructure, or engineering scarcity. Airtable’s core insight was that letting users express tables and data types directly lets them model their business without writing `ALTER TABLE` statements.

The claim is that coding agents change the economics underneath that compromise. If an agent can take a business data model, workflows, a spreadsheet, or an API key and turn it into a small usable web app, then proprietary no-code platforms are no longer the obvious low-floor solution. The replacement Zeyliger argues for is intentionally boring: Linux, open-source stacks, SQLite or Postgres, Go/TypeScript or LAMP, and a VM that is already on the internet.

The useful part is the lock-in argument. A Linux VM with code and data can move to AWS, GCP, Render, Railway, Hetzner, OCI, or a miniPC with relatively weak platform lock-in. A no-code platform can also be migrated by an agent eventually, but the substrate is still less inspectable and less portable than boring files, code, and databases.

There is also an operational stance embedded here: build small internal tools “right there in prod” with a coding agent, iterate until usable, let coworkers sand down edges, and only graduate to heavier software-development ceremony when a tool becomes truly business-critical. The essay is partly an exe.dev product argument, but the broader thesis is clear: the low floor is no longer a proprietary builder. It is an agent on a Linux machine.

**Newsletter angle:** Useful post-no-code framing. Not “everyone becomes a software engineer,” but “custom internal software stops needing a bespoke platform to be viable.” If agents can safely operate on boring infrastructure, the new no-code may be agent-assisted Linux with a database, auth, cron/systemd, backups, and a browser loop.

## Embedded source

{{< tweet id="2085394068771893725" url="https://x.com/i/status/2085394068771893725" >}}
