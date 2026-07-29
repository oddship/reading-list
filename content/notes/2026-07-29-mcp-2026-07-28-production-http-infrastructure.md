+++
title = "MCP 2026-07-28 turns MCP into production HTTP infrastructure"
slug = "2026-07-29-mcp-2026-07-28-production-http-infrastructure"
date = 2026-07-29T18:30:00+05:30
[taxonomies]
tags = ["agents", "ai-infra", "developer-tools"]
[extra]
source_url = "https://modelcontextprotocol.io/specification/2026-07-28"
source_type = "specification"
newsletter_candidate = true
why_it_matters = "A major agent-infra protocol release: MCP is moving from a stateful integration protocol toward stateless, scalable, gateway-friendly HTTP infrastructure."
saved_link = "https://claude.com/blog/bringing-mcp-2026-07-28-to-claude"
related_url = "https://blog.modelcontextprotocol.io/posts/2026-07-28/"
retrieval_note = "Read the official spec page, the MCP release announcement, and Anthropic’s Claude product announcement directly."
+++
**Logged at IST:** 2026-07-29 18:30 IST

**What it is:** Anthropic’s Claude product note, paired with the official MCP 2026-07-28 specification and release announcement.

**Gist:** MCP 2026-07-28 is the release where MCP starts looking less like a demo-era integration protocol and more like ordinary production HTTP infrastructure. The core change is statelessness: the spec removes the `initialize` / `initialized` handshake and `Mcp-Session-Id`, makes each request self-contained with protocol version, client identity, and capabilities in `_meta`, and adds optional `server/discover` for clients that want server capabilities up front.

That design shift matters operationally. Any request can land on any server instance behind a normal load balancer. `Mcp-Method` and `Mcp-Name` headers let gateways, WAFs, and rate limiters route or authorize without parsing JSON bodies. List and read responses can carry cache hints, which helps clients cache tool catalogs and keep upstream prompt caches more stable across reconnects.

The release also cleans up the shape of advanced MCP behavior. Multi Round-Trip Requests replace server-initiated elicitation, sampling, and roots calls that used to need a held-open stream. Tasks move into the formal extension framework, alongside MCP Apps and enterprise-managed authorization. Auth gets harder production edges too: RFC 9207 issuer validation, issuer-bound credentials, and a move away from Dynamic Client Registration toward Client ID Metadata Documents. Roots, Sampling, Logging, and legacy HTTP+SSE are deprecated with at least a twelve-month window.

Anthropic’s Claude announcement frames the same release from the product side: Claude has 950+ MCP servers in its connector directory, and is pairing the new stateless core with MCP Apps, enterprise-managed auth, connector observability, and research-preview MCP tunnels for private-network servers.

**Newsletter angle:** Strong agent-infra item because MCP is crossing a line from “standard way to wire tools into agents” to “standard deployable substrate for agent integrations.” The interesting bits are not just statelessness, but the surrounding production affordances: gateway routing, cacheable tool catalogs, explicit extensions for UI and long-running work, hardened auth, and predictable deprecation windows.
