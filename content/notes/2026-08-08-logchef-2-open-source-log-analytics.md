+++
title = "Logchef 2.0 turns log search into an operational workspace"
slug = "2026-08-08-logchef-2-open-source-log-analytics"
date = 2026-08-08T19:00:00+05:30
[taxonomies]
tags = ["developer-tools", "systems", "ai-infra"]
[extra]
source_url = "https://logchef.app"
source_type = "product"
saved_link = "https://x.com/i/status/2086066533286183137"
related_url = "https://x.com/mrkaran_/status/2086066533286183137"
related_urls = ["https://github.com/mr-karan/logchef", "https://raw.githubusercontent.com/mr-karan/logchef/main/README.md", "https://x.com/mrkaran_/status/2086066533286183137"]
newsletter_candidate = true
why_it_matters = "Logchef is a good example of an ops tool becoming a query and control plane over existing storage, with CLI and MCP interfaces for agent-driven investigations."
retrieval_note = "Extracted the X post through FXTwitter, read the Logchef site and GitHub README, and inspected frames from the launch video."
+++
**Logged at IST:** 2026-08-08 19:00 IST

**What it is:** Karan Sharma's launch thread for Logchef 2.0, an open-source, self-hosted log analytics workspace for ClickHouse and VictoriaLogs.

**Gist:** Logchef 2.0 expands the project from a fast ClickHouse log explorer into a broader operational workspace. The new shape is search, live tail, dashboards, alerts, RBAC, CLI, AI query assistant, and MCP integration in one self-hosted binary.

The product choice I like here is that Logchef does not try to become another storage layer. It queries ClickHouse and VictoriaLogs directly, so existing ingestion, retention, schemas, and operations stay where they already are. Logchef becomes the investigation and control plane in front of them.

The 2.0 additions are mostly about making that control plane complete: VictoriaLogs as a first-class datasource, cross-source dashboards, live tail from browser or terminal, local auth as an alternative to OIDC, scoped service tokens, query limits, dashboard caching, and rate limits for shared deployments.

There is also an agent angle. The site explicitly pitches the CLI and MCP server as ways for coding agents and assistants to investigate logs through a schema-aware interface. That is a useful pattern: give agents stable query tools, scoped tokens, JSON/JSONL output, and version-matched skill instructions instead of expecting them to scrape dashboards.

**Newsletter angle:** Nice systems/tooling example of the "control plane over existing infrastructure" pattern. It also fits the agent-infra thread: operational tools are starting to expose first-class CLI and MCP surfaces, not just human dashboards.

## Embedded source

{{< tweet id="2086066533286183137" url="https://x.com/i/status/2086066533286183137" >}}
