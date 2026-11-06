+++
title = "100x more programmers"
slug = "2026-11-06-100x-more-programmers"
date = 2026-11-06T06:58:00+05:30
[taxonomies]
tags = ["developer-tools", "systems", "ai-infra"]
[extra]
source_url = "https://tailscale.com/blog/100x-more-programmers"
source_title = "100x more programmers"
source_type = "article"
newsletter_candidate = true
why_it_matters = "Avery Pennarun argues that AI-assisted programming could make small, bespoke software practical for far more people, shifting the bottleneck from code generation to computing, networking, deployment, and ownership, and making open, composable infrastructure more important."
saved_link = "https://tailscale.com/blog/100x-more-programmers?utm_content=buffer7f91d&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer"
saved_title = "100x more programmers"
retrieval_note = "Read the full Tailscale essay. The 100x/billion-person projection and the claims about AI-driven software economics are Avery Pennarun's thesis, not measured forecasts. The article also advances Tailscale's product-adjacent argument for networking and its Aperture platform; that perspective is attributed to the author/company."
+++
**Logged at IST:** 2026-11-06 06:58 IST

**What it is:** Tailscale CEO Avery Pennarun's argument that AI could bring roughly 100 times more people into programming, not necessarily as professional developers, but as people who describe a need and have a computer build a small program for it.

**Gist:** Pennarun's example is a coin-flipping app: making the code was easy for a colleague with an AI coding agent, while getting a Linux VM, connecting to it, and sharing the running app remained awkward. His larger claim is that AI lowers the cost of one-off software, making it reasonable for a teacher, dentist, or small team to build a tool for a tiny audience instead of buying a generic subscription. The “100x” and “about a billion people” are his forecast, not a quantified prediction backed by a model in the post.

That shift makes the rest of computing more visible. Programs still need compute, storage, and networking; deploying and safely sharing a small app can drag in servers, DNS, TLS, authentication, and operations. Pennarun argues for making personal computers, small machines, and cloud VMs easier to use as interchangeable places to run software, and for reducing networking friction.

The essay also warns against replacing today's cloud lock-in with an AI-provider-owned stack spanning models, connectors, sandboxes, identity, and hosting. Pennarun's preferred alternative is an integrated but open system whose components can be replaced, with control over where models run and where data lives. He connects this to Tailscale's networking work and its Aperture product; that commercial perspective is part of the essay's framing. The underlying design tension is broader: make bespoke software easy to run without making one provider the unavoidable owner of its execution environment.

**Source read:** https://tailscale.com/blog/100x-more-programmers

**Newsletter angle:** If coding becomes abundant, deployment and ownership become the constraints. The next wave of “programmers” may need simpler ways to run, connect, and share small programs, without every personal tool turning into a subscription or a vertically integrated platform dependency.
