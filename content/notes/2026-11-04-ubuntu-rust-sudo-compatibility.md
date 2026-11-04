+++
title = "Ubuntu’s Rust sudo breaks compatibility with argument wildcards"
slug = "2026-11-04-ubuntu-rust-sudo-compatibility"
date = 2026-11-04T05:25:00+00:00
[taxonomies]
tags = ["systems", "security"]
[extra]
source_url = "https://utcc.utoronto.ca/~cks/space/blog/linux/Ubuntu2604RustSudoNotCompatible"
source_type = "article"
newsletter_candidate = true
why_it_matters = "A concrete sudoers portability trap for administrators moving to sudo-rs: argument wildcard rules accepted by standard sudo may be rejected or interpreted differently, changing what commands a policy actually permits."
saved_link = "https://utcc.utoronto.ca/~cks/space/blog/linux/Ubuntu2604RustSudoNotCompatible"
source_title = "The Ubuntu 26.04 Rust sudo is not compatible with standard sudo"
saved_title = "The Ubuntu 26.04 Rust sudo is not compatible with standard sudo"
+++
**Logged at IST:** 2026-11-04 10:55 IST

**What it is:** Chris Siebenmann’s report of a sudoers compatibility difference between standard sudo and Ubuntu 26.04’s sudo-rs.

**Gist:** A long-standing rule uses `-bp[acru]` to permit a narrow set of Exim queue options. The author reports that standard sudo treats the bracket expression as a wildcard, while sudo-rs does not support wildcards inside command-line arguments, so the rule no longer permits the intended invocations. Ubuntu’s sudo-rs manpage confirms that argument wildcards are unsupported (with a limited exception for a final `*`). The practical lesson is to audit and test sudoers policies during migration rather than assuming syntax compatibility means behavioral compatibility.

**Source read:** https://utcc.utoronto.ca/~cks/space/blog/linux/Ubuntu2604RustSudoNotCompatible

**Cross-check:** https://manpages.ubuntu.com/manpages/stonking/man5/sudoers-rs.5.html, Ubuntu manpage for sudo-rs 0.2.14-1ubuntu4.1; explicitly documents the argument-wildcard limitation.

**Newsletter angle:** Rust reimplementations can preserve familiar configuration syntax while changing policy semantics; test real sudoers rules against the exact implementation and version you deploy.
