+++
title = "Who should pay for source code availability?"
slug = "2026-08-10-source-code-availability"
date = 2026-08-10T16:19:00+05:30
[taxonomies]
tags = ["developer-tools", "systems"]
[extra]
source_url = "https://kristoff.it/blog/source-code-availability/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "A useful systems-and-economics frame for source availability: reliable code hosting is not just a reliability problem, but a question of who pays for redundancy."
saved_link = "https://kristoff.it/blog/source-code-availability/"
retrieval_note = "Direct article HTML fetched successfully and read; Jina reader also checked as fallback for clean text."
+++
**Logged at IST:** 2026-08-10 16:19 IST

**What it is:** Loris Cro’s long essay on source-code availability, using Zine, Zig, Radicle, Codeberg, Tangled, community mirrors, and package registries as examples.

**Gist:** Cro starts from a practical build problem: if a project’s dependencies live across GitHub, Codeberg, and small self-hosted forges, fresh builds can fail whenever any host is down. Forking and vendoring solve this locally, but they do not make the copied code discoverable or automatically useful as shared redundancy.

The core argument is that source availability is a cost-allocation problem. Centralized platforms and package registries make availability feel free by hiding the cost behind big tech sponsorship, donations, volunteers, or eventual monetization. Cro is drawn to Radicle because its p2p seeding model lets the people who depend on a repository also help keep it available, while still preserving discoverability and collaboration data through Git objects.

The Zig-specific angle is practical: Radicle repository IDs are location-independent, but Zig should remain dependency-zero, so direct Radicle support is not straightforward. Cro suggests mirror support in `build.zig.zon` as the immediate bridge: Radicle-aware tooling could resolve a repository ID into HTTP mirrors, while ordinary Zig users could still fetch over normal URLs.

**Newsletter angle:** Strong systems/economics piece for open-source infrastructure. The useful frame is that reliability gets better when dependency consumers help pay or seed the redundancy they benefit from, instead of relying on centralized registries or free big-tech hosting.
