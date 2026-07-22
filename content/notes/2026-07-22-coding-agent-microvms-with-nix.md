+++
title = "Coding agent MicroVMs with Nix"
slug = "2026-07-22-coding-agent-microvms-with-nix"
date = 2026-07-22T16:10:00+05:30
[taxonomies]
tags = ["agents", "security", "developer-tools", "systems"]
[extra]
source_url = "https://michael.stapelberg.ch/posts/2026-02-01-coding-agent-microvm-nix/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "Strong agent-security and developer-tools item because it turns the lethal-trifecta mitigation into a reproducible local workflow: remove private data from the agent environment, make state disposable, and use Nix to make new sandboxes cheap enough to create per project."
saved_link = "https://michael.stapelberg.ch/posts/2026-02-01-coding-agent-microvm-nix/"
+++
**Logged at IST:** 2026-07-22 16:10 IST

**What it is:** Michael Stapelberg’s NixOS and microvm.nix setup for running coding agents inside ephemeral MicroVMs.

**Gist:** Stapelberg wants coding agents to run without per-command review while keeping them away from personal files and making compromise disposable. His setup uses NixOS, microvm.nix, a NATed bridge, shared project workspaces, shared Claude credentials, cloud-hypervisor, and home-manager so each project gets a reproducible ephemeral VM. He also shows a Claude Skill that creates new project MicroVM definitions, picks free IPs, clones repositories, adds build dependencies, creates SSH keys, and verifies the Nix config.

**Newsletter angle:** Strong agent-security and developer-tools item because it turns the lethal-trifecta mitigation into a reproducible local workflow: remove private data from the agent environment, make state disposable, and use Nix to make new sandboxes cheap enough to create per project.
