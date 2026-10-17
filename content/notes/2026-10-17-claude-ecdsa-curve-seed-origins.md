+++
title = "Claude traces the origins of NIST's ECDSA curve seeds"
slug = "2026-10-17-claude-ecdsa-curve-seed-origins"
date = 2026-10-17T09:17:00+05:30
[taxonomies]
tags = ["cryptography", "ai", "research", "security"]
[extra]
source_url = "https://www.anthropic.com/research/ecdsa-curve-origins"
source_type = "research"
newsletter_candidate = true
why_it_matters = "An AI-assisted investigation connects opaque cryptographic-standard parameters to a reproducible weak-PRNG process, reducing some backdoor concerns while leaving specific curve-selection questions open."
source_title = "Claude reveals ECDSA curve origins"
saved_link = "https://x.com/sweis/status/2111165738836717980"
saved_title = "Steve Weis: Claude found the seeds"
related_url = "https://x.com/sweis/status/2111165738836717980"
related_title = "Steve Weis's X post and thread"
related_urls = ["https://saweis.net/posts/nist-curve-seed-origins.html", "https://blog.cryptographyengineering.com/2015/10/22/a-riddle-wrapped-in-curve/"]
related_titles = ["Stephen Weis's investigation of NIST curve seed origins", "Matthew Green: A riddle wrapped in a curve"]
+++
**Logged at IST:** 2026-10-17 09:17 IST

**What it is:** Anthropic's account of how Claude traced the origins of NIST ECDSA curve seeds, shared by cryptographer Steve Weis, whose earlier investigation documented the mystery.

**Gist:** Anthropic reports that Claude identified the NIST prime-curve seeds as outputs of the `lrand48` pseudorandom-number generator initialized from Unix timestamps. It also traced some older ANSI X9.62 base points to a generator used in the FreeLIP arithmetic package. Anthropic says these findings are not a cryptographic break and make deliberate backdooring of the seeds less plausible. Questions remain: some viable candidate curves appear to have been skipped, and the origins of several base points are still unexplained.

Weis's 2023 investigation captured the uncertainty before this result, including the widely repeated but incorrect lost-passphrase story; Matthew Green's 2015 article provides historical context for the distrust surrounding NIST's curve parameters.

**Why it matters:** A memorable example of AI-assisted cryptanalytic archaeology: recognizing the fingerprints of a weak 1990s PRNG helped resolve a decades-old provenance question, while leaving concrete details open to further scrutiny.

**Sources:**
- [Anthropic's research write-up](https://www.anthropic.com/research/ecdsa-curve-origins)
- [Stephen Weis's investigation](https://saweis.net/posts/nist-curve-seed-origins.html)
- [Matthew Green's historical overview](https://blog.cryptographyengineering.com/2015/10/22/a-riddle-wrapped-in-curve/)

{{ tweet(id="2111165738836717980", url="https://x.com/sweis/status/2111165738836717980") }}
