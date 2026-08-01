+++
title = "Agent-era terminal multiplexers should separate sessions from views"
slug = "2026-08-01-terminal-multiplexers-server-session-client-view"
date = 2026-08-01T13:45:00+05:30
[taxonomies]
tags = ["agents", "developer-tools", "systems"]
[extra]
source_url = "https://peterp.org/blog/terminal-multiplexers.html"
source_type = "article"
saved_link = "https://x.com/i/status/2083161617148019025"
related_url = "https://x.com/appfactory/status/2083161617148019025"
newsletter_candidate = true
why_it_matters = "Terminal multiplexing is turning into agent collaboration infrastructure: persistent sessions, shared compute, replayable output, and clients that do not all need the same layout."
retrieval_note = "FXTwitter exposed the linked article; direct article HTML was accessible and read."
+++
**Logged at IST:** 2026-08-01 13:45 IST

**What it is:** Peter Pistorius arguing that the current wave of new terminal multiplexers is about a real shift in how developers use computers, especially with long-running agents and shared remote compute.

**Gist:** The core sentence is: “The server should own the session. The client should own the view.” Traditional multiplexers were designed around a human actively operating a terminal, with server-side windows, panes, focus, and layout. Peter argues that model breaks down when agents work for hours, multiple people or agents need to inspect the same work, and the process may be running on a laptop, office machine, SSH host, VM, or cloud computer.

His proposed boundary is clean. The server owns the PTY, process lifetime, stable session identity, terminal output and checkpoints, connected participants, ordered input, reconnection, and a protocol other software can use. The client owns tabs, panes, spatial windows, focus, scroll position, selection, and viewport. A phone, browser, desktop app, regular terminal, and agent API should be able to compose the same sessions differently.

The hard part is terminal geometry. A generic PTY has one authoritative rows-by-columns size, so a desktop and phone cannot both get independently rendered versions of the same arbitrary terminal app. The practical answer is one canonical grid owned by the session, plus client-specific viewport, pan, crop, or scale behavior. That still keeps layout out of shared server state.

**Newsletter angle:** Strong systems/agent-infra item. It reframes terminal multiplexers as the session layer for humans, agents, and remote compute, not merely as a better `tmux` layout manager.
