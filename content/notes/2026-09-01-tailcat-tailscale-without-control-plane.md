+++
title = "Tailcat uses Tailscale's data plane without its control plane"
slug = "2026-09-01-tailcat-tailscale-without-control-plane"
date = 2026-09-01T08:22:00+05:30
[taxonomies]
tags = ["developer-tools", "systems", "agents"]
[extra]
source_url = "https://tailscale.com/blog/tailcat"
source_type = "article"
newsletter_candidate = true
why_it_matters = "Tailcat turns Tailscale's WireGuard, NAT traversal, and DERP data plane into a short-lived, accountless capability tool for ad-hoc machine access, agent sandboxes, file transfer, and remote development."
saved_link = "https://x.com/Tailscale/status/2094485903016177871"
related_url = "https://x.com/Tailscale/status/2094485903016177871"
related_urls = ["https://tailscale.com/tailcat", "https://github.com/tailscale/tailcat", "https://raw.githubusercontent.com/tailscale/tailcat/main/README.md"]
retrieval_note = "FXTwitter extracted the Tailscale launch tweet and linked blog URL. The Tailscale blog, product page, and Tailcat README were read directly. The attached tweet image was inspected; it is mostly launch branding with the title and a small terminal snippet."
+++
**Logged at IST:** 2026-09-01 08:22 IST

**What it is:** Tailscale's Tailcat is an open-source Go package and CLI that acts like netcat over Tailscale's data plane, without using Tailscale's control plane.

**Gist:** Tailcat splits the stack in an interesting way. It keeps the WireGuard encryption, magicsock NAT traversal, and DERP rendezvous/fallback pieces, but removes tailnets, accounts, logins, users, admins, policy, IP management, and OS-level network configuration. One side starts a listener and gets a shareable tailcat address; the other side uses that address to connect.

The CLI is broader than a simple pipe. It can forward ports, run no-auth SSH/SFTP for temporary access, copy files, serve directories, run a SOCKS proxy for tailcat-oblivious tools, or act as an exit node. The default hosted relays are rate-limited and not positioned as private or high-throughput infrastructure, but users can run their own `derper` if they want more control.

The agent angle is explicit. Brad Fitzpatrick describes using Tailcat to give sandboxed AI agents temporary access to test machines, nested VMs, exotic hardware, and remote environments without enrolling them into a persistent governed network. That makes Tailcat a useful artifact to watch: a small capability-style connectivity primitive for ephemeral work, rather than a replacement for a managed tailnet.

**Newsletter angle:** Tailscale is productizing the boundary between data plane and control plane: accountless, short-lived secure connectivity for agents, sandboxes, file transfer, and remote dev.

{{ tweet(id="2094485903016177871", url="https://x.com/Tailscale/status/2094485903016177871") }}
