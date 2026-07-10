+++
title = "is moving its GitHub repo into the"
slug = "2026-05-07-is-moving-its-github-repo-into-the"
date = 2026-05-07
[taxonomies]
tags = ["reading-log", "x-post", "historical-backfill", "agents", "security", "developer-tools", "org-design"]
[extra]
source_url = "https://x.com/i/status/2052337097315381517"
source_type = "x-post"
status = "reviewed"
newsletter_candidate = true
why_it_matters = "this is an ecosystem/ownership cleanup move, but it deliberately forces extension authors to choose between forward compatibility and backward compatibility."
saved_link = "https://x.com/i/status/2052337097315381517"
+++
Imported from historical reading log.
- Extracted main post via `api.fxtwitter.com` fallback.
- Mario Zechner says `pi` is moving its GitHub repo into the `earendil-works` org and will start publishing packages under the `@earendil-works` npm namespace instead of `@mariozechner`.
- Short-term compatibility remains for existing imports, but typed extensions should migrate quickly once the new packages land.
- Breaking edge: extensions switched to `@earendil-works` will stop working on older `pi` versions after today's release.
- Why it matters: this is an ecosystem/ownership cleanup move, but it deliberately forces extension authors to choose between forward compatibility and backward compatibility.
- Good angle: `agent-tooling ecosystems are hitting the boring-but-real package-namespace migration phase, and extension authors absorb the breakage`.
