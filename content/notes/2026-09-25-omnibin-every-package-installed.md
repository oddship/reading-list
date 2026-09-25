+++
title = "omnibin makes nixpkgs feel already installed"
slug = "2026-09-25-omnibin-every-package-installed"
date = 2026-09-25T18:20:00+05:30
[taxonomies]
tags = ["developer-tools", "systems", "ai-infra"]
[extra]
source_url = "https://fzakaria.com/2026/09/24/every-package-is-already-installed"
source_title = "Every package is already installed"
source_type = "blog-post"
newsletter_candidate = true
why_it_matters = "omnibin reframes package management as a lazy, indexed namespace: expose every historical nixpkgs binary on PATH, fetch only what is touched, and give agents a queryable universe of tools without pre-installing them."
saved_link = "https://fzakaria.com/2026/09/24/every-package-is-already-installed"
saved_title = "Every package is already installed"
related_urls = ["https://github.com/fzakaria/omnibin", "https://hub.docker.com/r/fmzakari/omnibin", "https://fzakaria.com/2026/08/09/nixpkgs-multiverse-every-version-that-ever-existed"]
related_titles = ["omnibin source repository", "fmzakari/omnibin Docker image", "nixpkgs-multiverse: every version that ever existed"]
retrieval_note = "Farid Zakaria's blog post was fetched directly; related links include the omnibin repository, Docker image, and nixpkgs-multiverse dependency."
+++

**Logged at IST:** 2026-09-25 18:20 IST

**What it is:** Farid Zakaria introduces [omnibin](https://github.com/fzakaria/omnibin), a FUSE filesystem that makes every binary ever shipped by nixpkgs appear available on `PATH` without installing all of it first.

**Gist:** omnibin combines [nixpkgs-multiverse](https://fzakaria.com/2026/08/09/nixpkgs-multiverse-every-version-that-ever-existed) with the `.ls` metadata that Hydra publishes next to Nix cache narinfos. That index lets the filesystem answer questions such as "where is `python3@3.6.2`?" from metadata, then lazily fetch and unpack the needed NAR only when something actually opens the file.

The result is deliberately absurd and useful: tens of thousands of top-level binaries, and hundreds of thousands of versioned binary names, are visible without occupying disk until first use. The Docker image makes the same idea available as an agent harness: start from a container where old Python, `jq`, GCC, and other tools can be invoked by name or version without curating a base image first.

The caution is also part of the design. Agents should not blindly `ls` and stat the whole tree; omnibin exposes an index database and CLI queries so tooling can ask for the relevant binary/version instead of crawling nearly 900k entries.

**Newsletter angle:** Package management as lazy namespace design: make the universe visible, fetch only what is touched, and teach agents to query the index instead of exploring the filesystem.
