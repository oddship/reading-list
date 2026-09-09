+++
title = "trynix runs Nix packages in a browser tab"
slug = "2026-09-09-trynix-browser-nix-package-runner"
date = 2026-09-09T19:24:00+05:30
[taxonomies]
tags = ["developer-tools", "systems", "ai-infra"]
[extra]
source_url = "https://fzakaria.com/2026/09/04/any-nix-package-live-in-your-browser"
source_type = "blog-post"
newsletter_candidate = true
why_it_matters = "trynix turns Nix store paths into shareable, runnable browser artifacts, which makes review builds, bug reports, tutorials, and agent-produced binaries much easier to hand to humans or other agents."
saved_link = "https://fzakaria.com/2026/09/04/any-nix-package-live-in-your-browser"
related_urls = ["https://trynix.dev/", "https://github.com/fzakaria/trynix", "https://nixmultiverse.com/"]
retrieval_note = "Farid Zakaria's blog post was fetched directly; the note also records the linked trynix homepage, source repository, and nixpkgs-multiverse dependency."
+++
**Logged at IST:** 2026-09-09 19:24 IST

**What it is:** Farid Zakaria introducing [trynix](https://trynix.dev/), a browser-based runner for arbitrary Nix package closures.

**Gist:** trynix lets a web page boot a Linux machine inside the browser and put selected Nix packages on `PATH`. It uses nixpkgs-multiverse to map package/version requests to exact store paths, fetches closures from CORS-accessible Nix binary caches, mounts an in-memory Nix store into an x86_64 Linux VM running under qemu-wasm, and presents a shell in the page.

The neat systems trick is that there is no backend server in the normal path: the page is static, the store paths come from public caches, and the VM lives inside the browser tab. It also avoids slow cold boots by prefetching the engine and resuming from a pre-booted VM snapshot taken just before mounting the store.

The practical angle is stronger than the demo. A CI system can publish PR artifacts to a cache and leave a link that boots exactly those artifacts. A bug report can carry its own reproducible environment. Documentation can link to a shell with the exact tool version already available. Agents can hand around runnable Nix store paths instead of screenshots or vague build instructions.

**Newsletter angle:** A browser URL becomes a runnable artifact boundary: useful for PR review, reproducible bug reports, executable docs, and agent-to-agent handoff of build outputs.
