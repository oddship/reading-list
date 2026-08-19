+++
title = "Incus looks like a better sandbox shape for coding agents"
slug = "2026-08-08-incus-agent-sandboxes"
date = 2026-08-08T19:05:00+05:30
[taxonomies]
tags = ["agents", "ai-infra", "systems"]
[extra]
source_url = "https://linuxcontainers.org/incus/"
source_type = "project"
saved_link = "https://linuxcontainers.org/incus/"
related_url = "https://x.com/shantanugoel/status/2086061269522739695"
related_urls = ["https://x.com/i/status/2086061269522739695", "https://github.com/shantanugoel/incus-manager", "https://raw.githubusercontent.com/shantanugoel/incus-manager/main/README.md", "https://x.com/shantanugoel/status/2085737841301299494"]
newsletter_candidate = true
why_it_matters = "Incus system containers give agent sandboxes a full-OS, systemd-capable, persistent, snapshotable workspace without handing agents the host filesystem."
retrieval_note = "Read the Incus project page and incus-manager README; extracted Shantanu Goel's X post and quoted repo link through FXTwitter; inspected the attached terminal screenshot."
+++
**Logged at IST:** 2026-08-08 19:05 IST

**What it is:** Incus is the Linux Containers project's system container, application container, and VM manager. Shantanu Goel's linked post applies it to AI agent sandboxes through a small `incus-manager` setup repo.

**Gist:** Incus gives a public-cloud-like interface for running system containers, application containers, and virtual machines on shared storage and networking. It was created as a community-driven alternative to Canonical's LXD and is maintained by many of the same people who created LXD.

For coding agents, the interesting mode is the system container: a full Linux userspace with systemd, persistent storage, resource limits, snapshots, profiles/projects, device controls, and a command-line/API control plane. That is closer to a disposable development VM than a Docker app container, while still staying lighter than a full VM for many local workflows.

Shantanu's `incus-manager` repo is a concrete version of that pattern. It provisions persistent Ubuntu agent containers, keeps the host filesystem out of reach, gives each container an isolated UID range, wraps common Incus commands in `agentctl`, supports snapshots/restores/clones, and documents sharp edges like Docker's FORWARD policy blocking Incus bridge traffic.

The security posture is the useful part. Projects and restricted devices are the boundary, code is copied or cloned into `/workspace`, credentials are authenticated inside the container, and the README explicitly says not to mount `~/.ssh`, cloud config, the home directory, Docker socket, or an Incus socket. Snapshots also preserve credentials, so the suggested baseline snapshot happens before agent logins.

**Newsletter angle:** This is a good agent-infra note: as agents get more autonomous, the sandbox wants to look less like a stateless Docker container and more like a persistent, snapshotable OS workspace with narrow host access and separate credentials.

## Embedded source

{{<tweet id="2086061269522739695" url="https://x.com/shantanugoel/status/2086061269522739695"/>}}

{{<tweet id="2085737841301299494" url="https://x.com/shantanugoel/status/2085737841301299494"/>}}
