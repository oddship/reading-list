+++
title = "Open Generative UI"
slug = "2026-05-07-open-generative-ui"
date = 2026-05-07
[taxonomies]
tags = ["reading-log", "x-post", "historical-backfill", "agents", "ai-infra"]
[extra]
source_url = "https://x.com/i/status/2052299884817240444"
source_type = "x-post"
newsletter_candidate = true
why_it_matters = "this is a good signal that `agent UX` is shifting from text-plus-tools toward runtime-generated interfaces, with skills/specs becoming the control layer over unconstrained visual output."
saved_link = "https://x.com/i/status/2052299884817240444"
+++
Imported from historical reading log.
- Extracted main post via `api.fxtwitter.com` fallback and checked the linked repos/docs for `CopilotKit/generative-ui` and `CopilotKit/OpenGenerativeUI`.
- Akshay Pachaar highlights `Open Generative UI`, an open-source take on Claude-style artifacts: the agent streams HTML/SVG token-by-token into a sandboxed iframe so the UI visibly assembles live in chat.
- The interesting implementation choice is that this is not component selection but open-ended UI generation from scratch, with safety coming from iframe isolation and quality steered by skill/prompt layers.
- Repo framing broadens it beyond one demo: CopilotKit positions generative UI as three patterns (`controlled`, `declarative`, `open-ended`) across AG-UI, A2UI/Open-JSON-UI, and MCP Apps, with OpenGenerativeUI as the high-freedom showcase.
- Why it matters: this is a good signal that `agent UX` is shifting from text-plus-tools toward runtime-generated interfaces, with skills/specs becoming the control layer over unconstrained visual output.
- Good angle: `artifacts are escaping proprietary chat apps and turning into an open protocol/framework battle around agent-native UI`.
