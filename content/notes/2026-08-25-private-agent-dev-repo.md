+++
title = "The private repo as the real agent workspace"
slug = "2026-08-25-private-agent-dev-repo"
date = 2026-08-25T12:35:00+05:30
[taxonomies]
tags = ["agents", "developer-tools", "systems"]
[extra]
source_url = "https://x.com/rough__sea/status/2092091242377265562"
source_type = "x-post"
newsletter_candidate = true
why_it_matters = "A sharp example of open source as an export surface, while the valuable development asset becomes the private agent-readable wiki, specs, tests, and experiment harness."
saved_link = "https://x.com/rough__sea/status/2092091242377265562"
related_urls = ["https://github.com/denoland/celld", "https://celld.dev", "https://gist.github.com/ry/c56dfa7b1b90eeff2d8d0127e45ae3bb/revisions?short_path=4c66555#diff-4c66555dd402cc5d67a52a326ac73c0e13d09c5e3e6e2e32967808d23a576025"]
retrieval_note = "FXTwitter extraction succeeded; the public celld README, GitHub repo metadata, and Ryan Dahl's LLM Wiki gist were read directly. Attached images were inspected and show the private repo layout, wiki/design pages, tests tree, and a Vultr fault-injection latency chart."
+++
**Logged at IST:** 2026-08-25 12:35 IST

**What it is:** Ryan Dahl describing how celld is developed from a larger private `denoland/celld.dev` repo, while the public `denoland/celld` repo stays a lean export.

**Gist:** The useful part is the shape of the working repo. Dahl says the private repo has an LLM-maintained design wiki, a large test suite, a TLA+ spec, website code, cloud experiment scripts, and a speculative managed control plane. The public repo is open source, but the real development loop happens around the richer private artifact.

That feels like an agent-era pattern: code is no longer the only scarce asset. The durable value is the executable and readable context around the code: specs, tests, design pages, operational scripts, and experiment harnesses. If those are strong enough, agents can keep rewriting, porting, or replacing large chunks of the app while the test/spec corpus acts as the contract.

It also changes the open-source boundary. Instead of sharing every commit, a project can publish a clean artifact and keep the private repo as the agent workspace where product strategy, control-plane ideas, tests, and design history live together.

**Newsletter angle:** Strong developer-tools item: in agent-heavy development, the private test/wiki/spec corpus may become the real moat, and the public repository becomes more like a release artifact.

{{ tweet(id="2092091242377265562", url="https://x.com/rough__sea/status/2092091242377265562") }}
