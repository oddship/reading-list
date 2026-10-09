+++
title = "Deno's team joins Cloudflare to make self-hosted Workers a first-class path"
slug = "2026-10-09-deno-team-joins-cloudflare-self-hosting"
date = 2026-10-09T19:42:00+05:30
[taxonomies]
tags = ["systems", "developer-tools"]
[extra]
source_url = "https://deno.com/blog/cloudflare"
source_type = "article"
newsletter_candidate = true
why_it_matters = "The move combines Deno's self-hosting work on celld with Cloudflare's workerd and Durable Objects, while materially changing the roadmap for Deno runtime and Deno Deploy users."
saved_link = "https://x.com/badlogicgames/status/2108546982637973670"
saved_title = "Mario Zechner reacting to the announcement"
source_title = "Deno is joining Cloudflare"
related_url = "https://blog.cloudflare.com/deno-joins-cloudflare/"
related_title = "Deno is joining Cloudflare: Cloudflare Blog"
related_urls = ["https://x.com/KentonVarda/status/2108546700239368289", "https://celld.dev/", "https://github.com/cloudflare/workerd"]
related_titles = ["Kenton Varda's announcement", "celld", "workerd"]
retrieval_note = "Extracted the shared X post through FXTwitter, including its quoted Kenton Varda post, then read both Ryan Dahl's Deno announcement and Cloudflare's joint post."
+++
**Logged at IST:** 2026-10-09 19:42 IST

**What it is:** Ryan Dahl announced that the Deno team is joining Cloudflare and will work with the Workers and Durable Objects teams to make self-hosted Workers a first-class, supported way to run applications.

**Gist:** The plan is to bring ideas and code from Deno's celld project into workerd, combining the Workers programming model with a scalable, self-hostable runtime and Durable Objects. Ryan Dahl frames this as continuing a longer effort to simplify server software: compute, storage, and communication primitives built into the programming model rather than assembled as separate infrastructure. Cloudflare says its earlier workerd release lacked scalable multi-instance Durable Objects and the surrounding tooling needed to make self-hosting practical.

**User impact and caveats:** This is also a consequential roadmap change for Deno users. Deno says it will provide monthly bug-fix and security releases for the Deno runtime for one year, then end its own runtime development; the runtime remains open source. Deno Deploy will operate for six more months before shutdown, with migration help for paying customers. JSR will continue, with infrastructure moving to Cloudflare, and rusty_v8 support will continue with a goal of integrating it into workerd. These are announced plans, not a completed merged self-hosting product; the post says more details will follow.

**Context:** The quoted Cloudflare announcement presents workerd's open-source status as an escape hatch rather than lock-in, arguing that compatibility with a different programming model has trade-offs and that openness helped win customers. Mario Zechner's shared “wow” reaction points to this announcement; it adds no separate technical claim.
