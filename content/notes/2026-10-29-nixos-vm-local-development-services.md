+++
title = "Run local development services with NixOS and systemd"
slug = "2026-10-29-nixos-vm-local-development-services"
date = 2026-10-29T22:01:00+05:30
[taxonomies]
tags = ["developer-tools", "systems"]
[extra]
source_url = "https://www.tweag.io/blog/2026-10-29-running-local-dev-services-with-nix"
source_type = "blog-post"
source_title = "Running local development services"
saved_link = "https://x.com/tweagio/status/2115836678313046307?a=juYBoDSMJhm-1c-XBog&s=35"
saved_title = "Tweag on running local development services with Nix"
related_url = "https://github.com/tweag/dev-services-nix-demo"
related_title = "Tweag's dev-services-nix-demo repository"
newsletter_candidate = true
why_it_matters = "A practical Nix dev-environment pattern that reuses standard NixOS service modules and systemd for local backing services, narrowing the gap between development and production configuration."
retrieval_note = "Read Tweag's tutorial and inspected the linked GitHub repository metadata and README. The article's example assumes a Linux host; its footnote points macOS readers to a separate Darwin branch and Linux builder setup."
+++
**What it is:** Tweag's tutorial for running local databases and other backing services inside a small NixOS VM launched from a Nix development shell.

**Gist:** Rather than reimplementing service definitions or introducing a development-only process manager, the setup uses standard NixOS modules from Nixpkgs and systemd inside a local QEMU VM. A `vm` command added to the dev shell starts the VM; project-specific modules configure services, while production service configuration can be shared where appropriate. The article also describes forwarding services to the host and extending the VM with tools such as `lazyjournal` for systemd logs.

This trades some memory and boot time for isolation, reproducibility, and production-like systemd behavior. The tutorial assumes Linux; it points macOS users to a separate Darwin branch and notes the additional Linux-builder setup. The linked repository is a demo for the article.

**Newsletter angle:** A useful middle ground for Nix teams that want realistic local dependencies without maintaining a second service configuration and process-management stack just for development.