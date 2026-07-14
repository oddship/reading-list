+++
title = "iximiuz on Januscape and the limits of microVM safety claims"
slug = "2026-07-14-iximiuz-on-januscape-and-the-limits-of-microvm-safety-claims"
date = 2026-07-14T11:05:00+05:30
[taxonomies]
tags = ["security", "systems", "ai-infra"]
[extra]
source_url = "https://www.openwall.com/lists/oss-security/2026/07/06/7"
source_type = "x-post"
newsletter_candidate = true
why_it_matters = "Useful corrective to simplistic microVMs-are-always-safer narratives, because the real boundary depends on what kernel and hardware virtualization surfaces you expose."
saved_link = "https://x.com/i/status/2076674329694150780"
+++
**Logged at IST:** 2026-07-14 11:05 IST

**What it is:** iximiuz warning that VMs and microVMs exposing `/dev/kvm` to untrusted guests were hit by the Januscape guest-to-host breakout class

**Gist:** The key update is that KVM-based isolation is not a free safety upgrade over containers if you hand untrusted guests nested virtualization. The disclosed Januscape bug is a guest-to-host KVM/x86 escape affecting systems that accept untrusted guests and expose nested virt, with mitigations including disabling nested virtualization until downstream kernels catch up.

**Newsletter angle:** Useful corrective to simplistic "microVMs are always safer" narratives, because the real boundary depends on what kernel and hardware virtualization surfaces you expose.

**Supporting source:** Canonical also published mitigation guidance: `https://canonical.com/blog/januscape-linux-vulnerability-mitigations-available`
