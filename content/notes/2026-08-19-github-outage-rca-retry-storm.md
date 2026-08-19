+++
title = "GitHub Outage RCA: Sidecar Limits, Load Balancers, and Retry Storms"
slug = "2026-08-19-github-outage-rca-retry-storm"
date = 2026-08-19T09:31:00+05:30
[taxonomies]
tags = ["systems", "ai-infra"]
[extra]
source_url = "https://www.githubstatus.com/incidents/zkxwbgr0cnmx"
source_type = "incident-rca"
newsletter_candidate = true
why_it_matters = "The outage is a clean example of capacity controls and retry behavior coupling across service mesh, gateways, clients, and regional failover."
saved_link = "https://x.com/i/status/2089797401196290203"
related_url = "https://x.com/cassidoo/status/2089797401196290203"
retrieval_note = "X post extracted via FXTwitter. The linked GitHub Status incident API/page was read directly."
+++
**Logged at IST:** 2026-08-19 09:31 IST

**What it is:** GitHub's RCA for the August 17, 2026 critical GitHub.com incident, shared by Cassidy Williams.

**Gist:** GitHub.com saw elevated errors and latency for 7h47m across Issues, Pull Requests, APIs, Actions, and Copilot. At peak, web and API error rates were around 20%, while archive and raw-content downloads reached around 50%.

The immediate cause was load-balancer saturation in Central US. An Istio sidecar pod hit its concurrency limits and did not autoscale correctly because the policy watched host service capacity but not sidecar capacity. That cascaded until four HAProxy nodes exhausted their flow limits, degrading the gateway auth path and causing broad authentication latency and failures.

The recovery story is the interesting part. Optimistic gateway retries overloaded internal load balancers. A latent VS Code retry bug then amplified Copilot Token Service traffic by roughly 10x, from a normal 7-9K RPS to 70-100K RPS. GitHub mitigated by reducing gateway retries, blocking retry-triggering token requests at load balancers, and gradually ramping traffic back per site.

**Newsletter angle:** Good reliability write-up for the theme that autoscaling, retries, and failover are one coupled system. Capacity accounting has to include sidecars and service-mesh limits, and client retry behavior can dominate recovery once the first failure is fixed.
