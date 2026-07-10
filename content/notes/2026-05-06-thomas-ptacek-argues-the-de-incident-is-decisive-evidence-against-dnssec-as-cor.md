+++
title = "Thomas Ptacek argues the .de incident is decisive evidence against DNSSEC as core Internet security functio..."
date = 2026-05-06
[taxonomies]
tags = ["reading-log", "x-post", "x-com", "historical-backfill"]
[extra]
source_url = "https://x.com/i/status/2051802131636592846"
source_type = "x-post"
status = "published"
newsletter_candidate = true
why_it_matters = "this is the sharper, event-driven version of the previous anti-DNSSEC thesis — if a major resolver bypasses validation during a registry signing failure, the operational model looks fragile."
saved_link = "https://x.com/i/status/2051802131636592846"
+++
Imported from historical reading log.
- Extracted main post via `api.fxtwitter.com` fallback; inspected attached screenshot separately.
- Thomas Ptacek argues the `.de` incident is decisive evidence against DNSSEC as `core Internet security functionality`.
- Attached screenshot captures Cloudflare status text saying it temporarily disabled DNSSEC validation on `1.1.1.1` so `.de` names would continue resolving while DENIC fixed a DNSSEC signing problem.
- Why it matters: this is the sharper, event-driven version of the previous anti-DNSSEC thesis — if a major resolver bypasses validation during a registry signing failure, the operational model looks fragile.
- Useful paired angle with the linked essay: `theory from 2015` plus `real outage behavior in 2026`.
