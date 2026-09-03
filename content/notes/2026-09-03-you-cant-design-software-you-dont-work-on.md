+++
title = "You can't design software you don't work on"
slug = "2026-09-03-you-cant-design-software-you-dont-work-on"
date = 2026-09-03T22:11:00+05:30
[taxonomies]
tags = ["org-design", "systems"]
[extra]
source_url = "https://www.seangoedecke.com/you-cant-design-software-you-dont-work-on/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "A sharp reminder that architecture work on large existing systems is mostly codebase-specific judgment, so the people designing changes need implementation proximity and skin in the game."
saved_link = "https://x.com/fhackdroid/status/2095482838498095427?s=20"
related_url = "https://x.com/fhackdroid/status/2095483493438636243?s=20"
retrieval_note = "Both Farhaan Bukhsh X posts extracted via FXTwitter; the screenshot in the first post was inspected; the linked Sean Goedecke article was fetched directly."
+++
**Logged at IST:** 2026-09-03 22:11 IST

**What it is:** Farhaan Bukhsh reacting to Sean Goedecke’s essay on why useful software design requires working knowledge of the codebase, followed by a direct link to the essay.

**Gist:** Goedecke argues that generic design advice is usually too abstract for large existing systems. Real design is dominated by local constraints: what the current code already does, where data is available, how subsystems interact, and which change paths are safe. In that setting, consistency and concrete judgment often matter more than idealized architecture.

The strongest design conversations therefore happen among engineers who actively work on the system. They are often boring to outsiders because they turn on files, interfaces, invariants, migration paths, and recent refactors rather than broad principles. Generic architecture still has a role for brand-new systems, company-wide paved paths, and tie-breakers, but it should not replace implementation-proximate judgment.

Farhaan’s framing is the useful social angle: architects who want to write code and know the codebase can participate in design as a conversation. Architects who only hand off big-picture designs lack skin in the game.

**Newsletter angle:** A good engineering-culture note for the “architecture as implementation-proximate work” lane: design authority should come with codebase context and responsibility for outcomes.

## Embedded source

{{ tweet(id="2095482838498095427", url="https://x.com/fhackdroid/status/2095482838498095427") }}
