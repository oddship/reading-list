+++
title = "Metabase critical security update"
slug = "2026-08-08-metabase-critical-security-update"
date = 2026-08-08T00:24:00+05:30
[taxonomies]
tags = ["security", "systems"]
[extra]
source_url = "https://www.metabase.com/blog/security-update"
source_type = "article"
newsletter_candidate = true
why_it_matters = "A high-blast-radius BI security incident: a Metabase application-database SQL injection can become admin access, stored credential exposure, and downstream data access for connected warehouses."
saved_link = "https://www.metabase.com/blog/security-update"
related_url = "https://github.com/metabase/metabase/security/advisories/GHSA-vwf4-m7j8-wcjf"
related_urls = ["https://github.com/metabase/metabase/security/advisories/GHSA-vwf4-m7j8-wcjf"]
retrieval_note = "Read the Metabase blog post directly and fetched the linked GitHub security advisory via the GitHub API."
+++
**Logged at IST:** 2026-08-08 00:24 IST

**What it is:** Metabase’s security update for a critical actively exploited 0-day affecting Metabase versions 1.58 and above.

**Gist:** Metabase says its Cloud service was attacked through an unknown security vulnerability in versions 1.58 and above. They blocked the endpoints used for the attack, identified the issue, and shipped patches. Metabase Cloud customers are already upgraded, but self-hosted instances may still be vulnerable.

The linked advisory describes the bug as unauthenticated arbitrary SQL injection against the Metabase application database. That is a high-blast-radius failure mode: after gaining access, an attacker could get administrator access to the instance, change application configuration, steal stored credentials for connected databases, read data available through those connections, and export data.

Metabase recommends immediate upgrades to the latest safe point release for each supported line: 0.63.5, 0.62.9, 0.61.11, 0.60.17, 0.59.21, or 0.58.24. Versions below 58 are described as not vulnerable. If the `/api/session/reset_password` endpoint is publicly accessible, they also recommend revoking active sessions, reviewing API keys and administrator accounts, rotating connected-database credentials, checking warehouse logs, and reviewing Metabase activity/query history.

The attack pattern to look for is a `POST /api/session/reset_password` returning 400 followed by `GET /api/user/current` returning 200. If upgrading is not immediately possible, the temporary workaround is to block `/api/session/reset_password`.

**Newsletter angle:** Useful incident/advisory example for why BI tools are high-blast-radius infrastructure. A compromise of the analytics app is not contained to dashboards. It can become credential exposure, warehouse access, and broad data exfiltration unless the deployment model limits what the app can reach.
