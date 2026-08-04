+++
title = "Herdr Cuts Multi-Agent CPU by Rendering Less"
slug = "2026-08-04-herdr-95-percent-less-cpu"
date = 2026-08-04T11:57:00+05:30
[taxonomies]
tags = ["agents", "developer-tools", "systems"]
[extra]
source_url = "https://herdr.dev/blog/ten-agents-three-clients-95-percent-less-cpu/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "Agent workspaces multiply UI cost across panes, sessions, and attached clients. Herdr's result is a useful reminder that the biggest performance win can be refusing to render unchanged or invisible state."
saved_link = "https://herdr.dev/blog/ten-agents-three-clients-95-percent-less-cpu/"
retrieval_note = "Read the source article directly from herdr.dev."
+++
**Logged at IST:** 2026-08-04 11:57 IST

**What it is:** Can Celik's Herdr engineering post on cutting CPU use in multi-agent terminal sessions by avoiding frames that do not carry new information.

**Gist:** The headline claim is not that Herdr's renderer became dramatically faster. It is that Herdr asks the renderer to do much less work. Across workloads dominated by unnecessary rendering, total CPU for the server plus attached clients fell by 89 to 95 percent.

The three changes are nicely concrete. First, Herdr removed animated sidebar spinners for working agents. The static coloured state mark still tells you what is happening, while avoiding eight animation-driven redraws per second. Second, PTY render requests now carry the source pane, so output from a hidden background pane can update terminal state without forcing every attached client to receive and apply a frame nobody can see. Third, passive mouse movement no longer redraws Herdr's own frame unless one of Herdr's hover-sensitive modes is active. The mouse events still reach the pane.

The scaling point is the useful part. Skipping one server render also skips frame prep, serialization, network transmission, and client-side frame handling. With ten agents and three clients, that fanout is where the saving compounds. The post is also careful about limits: if forty-nine hidden panes are all writing at 60Hz, Herdr still has to read and parse the PTYs so the panes are correct when opened.

**Newsletter angle:** Good systems material for agent tooling: in multi-agent UIs, performance is partly an information-design problem. Motion should mean something changed, hidden output should not redraw visible clients, and unchanged frames should not exist.
