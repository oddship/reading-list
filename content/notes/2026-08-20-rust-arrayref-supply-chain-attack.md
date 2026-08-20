+++
title = "Rust warns about a supply chain attack on arrayref"
slug = "2026-08-20-rust-arrayref-supply-chain-attack"
date = 2026-08-20T17:58:00+05:30
[taxonomies]
tags = ["security", "developer-tools"]
[extra]
source_url = "https://blog.rust-lang.org/2026/08/20/supply-chain-attack-on-arrayref/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "This is a live Rust crates.io supply-chain incident involving malicious crate publication, yanked-version repair, and a concrete local cache check for affected developers."
saved_link = "https://x.com/marcoieni/status/2090385832918335824"
related_url = "https://x.com/marcoieni/status/2090385832918335824"
retrieval_note = "FXTwitter extraction retrieved Marco Ieni's post and expanded the Rust Blog URL. The durable note is grounded in the Rust Security Response Team advisory, not just the X post."
+++
**Logged at IST:** 2026-08-20 17:58 IST

**What it is:** A Rust Security Response Team advisory about a supply-chain attack involving `arrayref` and several malicious crates on crates.io.

**Gist:** Rust's security-response team says it received a report at 2026-08-20 07:15 UTC that the `proc-macro1` crate was malicious. The team verified that the crate's build script downloaded a malicious payload, then deleted `proc-macro1` and related crates including `proc-macro-en`, `aovine`, `arone`, `aronenao`, and `tinymember`.

The incident also touched real ecosystem packages. `arrayref@0.3.10` had been republished to depend on the malicious crate, with other versions yanked; Rust removed the malicious version and unyanked the wrongly-yanked versions. `internment@0.8.7` and `append-only-vec@0.1.9` were handled the same way, and the account was locked because the maintainer's machine or credentials were likely compromised.

The advisory gives a concrete local check: inspect `~/.cargo/registry/cache` for `arrayref-0.3.10.crate`, `internment-0.8.7.crate`, `append-only-vec-0.1.9.crate`, or any of the malicious crate names. The exposure window was short, roughly 86 to 107 minutes for the compromised legitimate package releases, but this is exactly the kind of incident where cached dependencies and CI artifacts matter.

**Newsletter angle:** Strong Rust/package-registry supply-chain item: quick incident response, yanked-version repair, account lockdown, and a practical developer-side cache audit.

{{ tweet(id="2090385832918335824", url="https://x.com/marcoieni/status/2090385832918335824") }}
