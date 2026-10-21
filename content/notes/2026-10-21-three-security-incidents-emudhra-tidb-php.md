+++
title = "Three security incidents: eMudhra, TiDB Cloud, and PHP"
slug = "2026-10-21-three-security-incidents-emudhra-tidb-php"
date = 2026-10-21T19:20:00+05:30
[taxonomies]
tags = ["security", "systems"]
[extra]
source_url = "https://x.com/AnzalAbidi/status/2112802425052754183"
source_title = "Anzal Abidi's security-incident roundup"
source_type = "social"
saved_link = "https://x.com/AnzalAbidi/status/2112802425052754183"
saved_title = "Three incidents in 72 hours: eMudhra, TiDB Cloud, and PHP"
related_url = "https://x.com/itszn13/status/2112908489198903680"
related_title = "PHP researcher on coordinated disclosure"
related_urls = ["https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/", "https://bugzilla.mozilla.org/show_bug.cgi?id=2083449", "https://www.pingcap.com/security/", "https://cryptobriefing.com/bitget-no-user-data-tidb-cloud-breach", "https://www.php.net/archive/2026.php", "https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w", "https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp", "https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/", "https://github.com/openai/php2shell-checker"]
related_titles = ["Google's eMudhra response", "Mozilla's eMudhra incident tracker", "PingCAP security guidelines", "Reporting on the alleged TiDB Cloud breach", "PHP official release and security guidance", "CVE-2026-109618: PHP advisory", "CVE-2026-109619: PHP advisory", "OpenAI's account of the coordinated response", "OpenAI PHP version checker"]
newsletter_candidate = true
why_it_matters = "The roundup is a useful prompt to check certificate trust stores, cloud-provider incident notices, and PHP patch status, but confidence differs by incident: eMudhra and the PHP vulnerabilities are confirmed by primary sources, while the detailed TiDB breach claims remain allegations in sources checked."
retrieval_note = "Read both X posts, including the attached screenshots, and checked Google/Mozilla eMudhra materials, PingCAP's public security page and secondary breach reporting, PHP's official release notice and two GitHub advisories, OpenAI's disclosure account, and its version checker. The PHP advisories confirm two critical RCEs (CVE-2026-109618 and CVE-2026-109619) and patched versions 8.2.35, 8.3.36, 8.4.27, and 8.5.12. The PHP project says updating is the only complete mitigation; its interim mitigations reduce specific paths but do not make installations safe. The enumerated TiDB breach contents and customer impacts remain allegations in sources checked; official PingCAP breach confirmation was not found."
+++
**Logged at IST:** 2026-10-21 19:20 IST

**What it is:** An X roundup of three security stories: weak eMudhra intermediate-CA keys, an alleged TiDB Cloud data theft, and critical PHP remote-code-execution vulnerabilities.

**Gist:** The eMudhra incident is confirmed: eight subordinate CA keys were generated with insufficient randomness, and browser/root-program responses followed. Google says Chrome blocked the affected keys; Mozilla's tracker documents the incident. Operators should ensure trust stores and runtimes are updated rather than assuming every client handles revocation equally.

The post's detailed TiDB Cloud breach narrative, including the 10.6 TB figure, customer-secret counts, and named tenants, was not independently confirmed in the public sources checked. PingCAP's security page describes vulnerability reporting, not this incident; published breach figures remain attributed allegations. TiDB Cloud users should look for provider communications and rotate credentials that may have been exposed through their own support workflows.

**PHP2Shell is now confirmed by PHP's official security notice.** PHP describes two critical unauthenticated RCE vulnerabilities: CVE-2026-109618 (OOM corruption) and CVE-2026-109619 (stale global state). The PHP project lists PHP 8.2.35, 8.3.36, 8.4.27, and 8.5.12 as fixed releases; PHP 8.1 and older are no longer maintained upstream, though some distributors may backport fixes. Update promptly and verify the effective package version with your distribution/vendor.

If an immediate update is not possible, PHP's advisory gives interim mitigations for specific paths. For CVE-2026-109618, it recommends administratively enforcing `memory_limit=-1`, keeping `post_max_size` conservative, and bounding decoded request size and multipart inputs at the frontend. For CVE-2026-109619, disable `session.upload_progress.enabled` before request parsing and restart workers; on PHP 8.5, also set `fatal_error_backtraces=0` and restart workers. These are partial risk reductions, not complete fixes: PHP says only updating is complete mitigation. The separate checker published by OpenAI estimates server/URL PHP versions but explicitly does not verify that a security fix is applied; distro backports complicate version-only checks.

OpenAI says a model used in its Patch the Planet initiative helped identify one flaw, and that Wiz independently found and reported both; the PHP maintainers led the fixes and release. The follow-up researcher's post and screenshot credit reporters and remediation developers, but do not replace the maintainers' advisories as the source for patch guidance.

**Sources:** https://www.php.net/archive/2026.php · https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w · https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp · https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/
**Caveat:** Confidence still varies across stories: eMudhra and PHP are corroborated by primary sources; the detailed TiDB impact list remains unverified in sources checked.
