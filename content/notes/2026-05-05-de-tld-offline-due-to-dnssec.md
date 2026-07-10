+++
title = "de TLD offline due to DNSSEC?"
date = 2026-05-05
[taxonomies]
tags = ["reading-log", "article", "captnemo-in", "news-ycombinator-com", "historical-backfill", "ai-infra", "systems"]
[extra]
source_url = "https://captnemo.in/blog/2026/05/05/namecheap-whois/"
source_type = "article"
status = "published"
newsletter_candidate = true
why_it_matters = ""
saved_link = "https://news.ycombinator.com/item?id=48027897"
+++
Imported from historical reading log.
- HN thread title: `.de TLD offline due to DNSSEC?`
- Most useful technical claim in the thread: this looked like a DNSSEC validation failure rather than a nameserver outage, with malformed/bad RRSIGs causing validating resolvers to return SERVFAIL for `.de` domains.
- Extra color from discussion: intermittency may have come from anycast nodes serving mixed good/bad signatures or cached answers; some users recovered temporarily via cached resolvers or by disabling validation.
- Useful because it adds a plausible technical explanation to the broader ccTLD-risk theme, not just anecdotal frustration.
- Follow-up source from Nemo: https://x.com/i/status/2051756854275964996 linking blog post https://captnemo.in/blog/2026/05/05/namecheap-whois/
