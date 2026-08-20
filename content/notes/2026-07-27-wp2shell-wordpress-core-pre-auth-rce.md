+++
title = "wp2shell pre-authentication RCE in WordPress Core"
slug = "2026-07-27-wp2shell-wordpress-core-pre-auth-rce"
date = 2026-07-27T21:44:00+05:30
[taxonomies]
tags = ["security"]
[extra]
source_url = "https://slcyber.io/research-center/wp2shell-pre-authentication-rce-in-wordpress-core/"
source_type = "security-advisory"
newsletter_candidate = true
why_it_matters = "High-signal security item because the claimed impact is anonymous pre-authentication RCE on stock WordPress installs, with affected versions and mitigations published while technical details are withheld."
saved_link = "https://x.com/i/status/2078253959018648050"
retrieval_note = "Grounded from the X post and Searchlight Cyber advisory. Technical exploit details were intentionally withheld by the advisory, so this note summarizes impact, affected versions, and mitigation only."
+++
**Logged at IST:** 2026-07-27 21:44 IST

**What it is:** Searchlight Cyber advisory for `wp2shell`, a reported pre-authentication RCE in WordPress Core, shared by the researcher as a patch-now warning.

**Gist:** The claim is severe and concrete: Searchlight Cyber says the issue can be exploited by an anonymous user against a stock WordPress install with no plugins and no preconditions. They are not releasing technical details yet, but they published affected version ranges and a checker at `wp2shell.com`.

Affected versions listed by the advisory: `<= 6.8.5` is not affected; `6.9.0` through `6.9.4` are affected; `7.0.0` through `7.0.1` are affected. Mitigation is to update to WordPress `7.0.2`, or `6.9.5` on the 6.9 branch. As a temporary emergency measure, they suggest blocking anonymous access to the REST batch API, including `/wp-json/batch/v1` and `?rest_route=/batch/v1`, with the caveat that this may break legitimate site behavior.

**Newsletter angle:** Worth tracking as a security item because the advisory is intentionally light on exploit details but strong on operational urgency: stock install, anonymous pre-authentication RCE, patch immediately.

**Retrieval note:** Grounded from the X post and Searchlight Cyber advisory. Technical exploit details were intentionally withheld by the advisory, so this note summarizes impact, affected versions, and mitigation only.

## Embedded source

{{ tweet(id="2078253959018648050", url="https://x.com/i/status/2078253959018648050") }}
