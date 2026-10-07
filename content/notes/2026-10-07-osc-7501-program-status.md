+++
title = "OSC 7501: a terminal protocol for program status"
slug = "2026-10-07-osc-7501-program-status"
date = 2026-10-07T02:34:00+05:30
[taxonomies]
tags = ["developer-tools", "agents"]
[extra]
source_url = "https://mitchellh.com/writing/program-status-osc7501"
source_type = "article"
newsletter_candidate = true
why_it_matters = "A terminal-native status protocol could replace brittle screen-reading heuristics and per-dashboard integrations with structured state emitted over the existing PTY."
source_title = "A Terminal Protocol for Program Status (OSC 7501)"
saved_link = "https://x.com/mitchellh/status/2107577887159386152"
saved_title = "Mitchell Hashimoto introduces OSC 7501"
related_urls = ["https://www.superlogical.com/rex/docs/build/program-status", "https://github.com/ghostty-org/ghostty/pull/14560"]
related_titles = ["OSC 7501 Program Status Protocol specification", "libghostty implementation PR"]
retrieval_note = "Read the announcement article and the protocol specification. OSC 7501 is a proposed protocol with prototype implementations; wide terminal and application adoption remains necessary for the ecosystem benefits described."
+++
**Logged at IST:** 2026-10-07 02:34 IST

**What it is:** Mitchell Hashimoto's proposal for OSC 7501, a terminal-native protocol that lets programs report states such as working, blocked, done, or error, with optional context.

**Gist:** Instead of dashboards inferring state from screen text/window titles or requiring each program to integrate with each dashboard's API, a program emits structured status over its existing PTY. The terminal decides how to present it. That makes the same mechanism applicable to agents, builds, package managers, and deployment tools, and naturally works through SSH and containers. The specification also defines state records, feature detection, limits, and security considerations.

**Why it matters:** The idea replaces a growing N-by-N integration and heuristic problem with a shared terminal protocol. The proposal is promising, but its usefulness depends on adoption by terminals and programs; the article reports prototypes, not broad ecosystem support.

**Source read:** https://mitchellh.com/writing/program-status-osc7501; https://www.superlogical.com/rex/docs/build/program-status

{{ tweet(id="2107577887159386152", url="https://x.com/mitchellh/status/2107577887159386152") }}
