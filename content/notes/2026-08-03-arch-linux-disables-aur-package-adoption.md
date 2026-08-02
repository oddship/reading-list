+++
title = "Arch Linux disables AUR package adoption after malware attacks"
slug = "2026-08-03-arch-linux-disables-aur-package-adoption"
date = 2026-08-03T03:38:00+05:30
[taxonomies]
tags = ["security", "systems"]
[extra]
source_url = "https://lwn.net/Articles/1086489/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "A concrete supply-chain security case: community package repositories can be attacked through abandoned-package adoption, not only through new account abuse or compromised maintainers."
saved_link = "https://lwn.net/Articles/1086489/"
+++
**Logged at IST:** 2026-08-03 03:38 IST

**What it is:** LWN news item on Arch Linux disabling adoption of orphaned AUR packages after another malware campaign.

**Gist:** Arch's DevOps team disabled orphaned-package adoption in the AUR after an influx of malicious package adoptions and follow-up commits. The linked analysis describes the payload as a Tor-controlled remote-access trojan that tries to upload a broad range of user data.

The important detail is the failure mode: the attacker path runs through abandoned community packages. Arch had already suspended new account registration in June after a similar campaign, then reopened registration in July with minor restrictions. This new round suggests that package-adoption workflow itself is part of the attack surface.

**Newsletter angle:** Useful supply-chain security case study for community package repositories: abandoned-package takeover is a governance and workflow problem, not just a malware-detection problem.
