+++
title = "Why Software Factories Fail"
slug = "2026-07-24-why-software-factories-fail"
date = 2026-07-24T17:32:00+05:30
[taxonomies]
tags = ["agents", "developer-tools", "org-design"]
[extra]
source_url = "https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/wsff.md"
source_type = "article"
newsletter_candidate = true
why_it_matters = "Useful agents and developer-tools item because it gives a concrete frame for why more coding-agent loops are not enough, and why teams should move review effort earlier into specs and design instead of deleting it."
saved_link = "https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/wsff.md"
+++
**Logged at IST:** 2026-07-24 17:32 IST

**What it is:** Dex Horthy / HumanLayer essay arguing against lights-off coding-agent software factories.

**Gist:** The post argues that harness engineering, loop engineering, and benchmark-driven agent gains make agents much faster at producing code, but they do not solve long-term maintainability. Current coding-agent training and evaluation reward short-horizon success, mostly “did the tests pass?”, while bad design shows up weeks or months later as shotgun surgery, slow review, and fragile systems.

The practical answer is not to abandon agents, but to turn the lights back on: keep humans in the loop for product review, architecture, program design, vertical slices, and code review. The leverage move is to shift review earlier into specs and design, so teams can still move faster without filling the codebase with hard-to-change agent slop.

**Newsletter angle:** Useful agents and developer-tools item because it gives a concrete frame for why “more loops” is not enough, and why review bottlenecks should be moved earlier rather than deleted.
