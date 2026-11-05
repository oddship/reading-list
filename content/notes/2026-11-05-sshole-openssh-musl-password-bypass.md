+++
title = "*sshole: a reported OpenSSH password-authentication bypass on musl systems"
slug = "2026-11-05-sshole-openssh-musl-password-bypass"
date = 2026-11-05T18:24:00+00:00
[taxonomies]
tags = ["security", "systems"]
[extra]
source_url = "https://sshhole.com/"
source_title = "*sshole: the star that let you in"
source_type = "security-research"
newsletter_candidate = true
why_it_matters = "The researcher reports a narrow password-authentication bypass caused by an interaction among musl crypt(), locked-account markers, and OpenSSH's non-PAM password path. The claimed exposure depends on a specific combination of platform, configuration, account state, and password length; it is not a general OpenSSH bypass."
saved_link = "https://sshhole.com/"
saved_title = "*sshole: OpenSSH/musl password-authentication bypass report"
related_urls = ["https://lists.mindrot.org/pipermail/openssh-commits/2026-October/013271.html", "https://cybersecuritynews.com/openssh-flaw-bypass-password-authentication/", "https://pasqualepillitteri.it/en/news/30344/openssh-alpine-bug-long-password-unlocks-locked-accounts"]
related_titles = ["OpenSSH commit cited by the researcher (fixes fake bcrypt salt generation)", "Secondary report on the claimed authentication bypass", "Secondary report on affected configurations and response"]
retrieval_note = "Read the researcher's page, including its source receipts and interactive demonstration, plus the cited OpenSSH mailing-list commit and two secondary reports. The commit cited on the page describes a separate fake-salt/timing issue for bcrypt hashes; it does not itself substantiate the reported bypass or its claimed fix. The exact official Alpine advisory and the fix diff for this issue were not independently located in sources checked, so impact and remediation claims here are attributed to the researcher and reporting, not presented as independently verified. Do not infer exposure outside the narrow conditions described."
+++
**Logged at IST:** 2026-11-05 23:54 IST

**What it is:** Security researcher Özgün Kültekin's report of an authentication bypass involving OpenSSH's password-authentication path on musl-based systems, published as *sshole.

**Gist:** The researcher describes a specific interaction: musl's `crypt()` returns `*` when it cannot process a password beyond its 256-byte limit, while `*` is also used as a locked/no-password marker in account records. In the reported non-PAM OpenSSH path, a password is checked against a salt borrowed from another account. Under the researcher's stated conditions, a 257–1024-byte password can therefore produce the same marker as a locked account's stored field and be accepted. The report says the affected configuration requires musl, OpenSSH without PAM, password authentication enabled, a target account with `*`, and another account with a supported real password hash. It identifies Alpine as a likely deployment context; it does not describe a general bypass affecting glibc systems, PAM-based authentication, or all OpenSSH deployments.

The page provides historical receipts for the behavior and a browser-based demonstration. It also says OpenSSH 10.6p2 fixes the issue and recommends disabling password authentication if an update is not yet available. I could not independently verify the exact vendor advisory or fix diff: the OpenSSH commit linked on the page is specifically about fake bcrypt salt generation for invalid users and restoring timing protection, not the reported `*` comparison. Treat the fix/version and impact statements as researcher-reported pending confirmation from the relevant distro/OpenSSH advisory.

**Source read:** https://sshhole.com/

**Related:** [OpenSSH commit cited on the page](https://lists.mindrot.org/pipermail/openssh-commits/2026-October/013271.html); [secondary coverage](https://cybersecuritynews.com/openssh-flaw-bypass-password-authentication/).

**Newsletter angle:** A useful example of a security failure emerging at a boundary between libc error handling, account-state conventions, and an SSH daemon's authentication logic, with an important caveat that the cited OpenSSH commit does not establish the specific fix claimed by the research page.
