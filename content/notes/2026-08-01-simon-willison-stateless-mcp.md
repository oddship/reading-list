+++
title = "Simon Willison is interested in MCP again because it is stateless"
slug = "2026-08-01-simon-willison-stateless-mcp"
date = 2026-08-01T11:41:00+05:30
[taxonomies]
tags = ["agents", "ai-infra", "developer-tools"]
[extra]
source_url = "https://simonwillison.net/2026/Jul/31/stateless-mcp/"
source_type = "article"
saved_link = "https://simonwillison.net/2026/Jul/31/stateless-mcp/"
newsletter_candidate = true
why_it_matters = "Stateless MCP lowers the protocol implementation tax and gives agent systems a more auditable capability boundary than arbitrary shell and network access."
retrieval_note = "Direct page HTML was accessible and article text was extracted from Simon Willison's post."
+++
**Logged at IST:** 2026-08-01 11:41 IST

**What it is:** Simon Willison on why the 2026-07-28 stateless MCP specification has renewed his interest in MCP, with three projects he built around it: `mcp-explorer`, `datasette-mcp`, and `llm-mcp-client`.

**Gist:** The technical hook is that stateless MCP collapses the older session flow into a single HTTP request. Instead of initializing a session, storing a `Mcp-Session-Id`, and then routing later tool calls against that state, a client can call a tool directly with an `MCP-Protocol-Version` header. That is cleaner for clients, simpler for servers, and a much better fit for horizontally scaled web services.

Simon uses that simplicity to build `mcp-explorer`, a Python CLI for listing, inspecting, and calling stateless MCP tools; `datasette-mcp`, a Datasette plugin that exposes read-only database tools over MCP; and `llm-mcp-client`, an alpha plugin for wiring MCP servers into his `llm` CLI.

The bigger shift is his security framing. He had cooled on MCP when shell-plus-`curl` agents seemed more flexible, but he now sees MCP as easier to audit and control than arbitrary command execution in an open network environment. Smaller local models can also drive narrow MCP tools more reliably than they can drive a full shell.

**Newsletter angle:** Strong MCP follow-up. The point is not just that the spec changed, but that the stateless shape makes MCP feel more like useful web infrastructure and less like protocol ceremony, especially for sensitive agent applications.
