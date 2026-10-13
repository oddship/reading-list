+++
title = "Jinx transpiles Nix and nixpkgs to TypeScript"
slug = "2026-10-13-jinx-nixpkgs-typescript"
date = 2026-10-13T09:17:00+05:30
[taxonomies]
tags = ["systems", "developer-tools"]
[extra]
source_url = "https://fzakaria.com/2026/10/12/nixpkgs-for-the-frontend-impaired"
source_type = "article"
source_title = "Nixpkgs for the frontend impaired"
saved_link = "https://x.com/fmzakari/status/2109831493510160675"
saved_title = "Farid Zakaria's X post about jinx"
related_url = "https://github.com/fzakaria/jinx"
related_title = "fzakaria/jinx"
related_urls = ["https://github.com/fzakaria/jinx-nixpkgs", "https://fzakaria.github.io/jinx/bench/", "https://fzakaria.com/2026/09/11/a-nix-store-is-three-functions", "https://fzakaria.com/2026/09/24/every-package-is-already-installed", "https://fzakaria.com/2026/09/04/any-nix-package-live-in-your-browser"]
related_titles = ["Compiled nixpkgs tree", "jinx benchmark data", "A Nix store is three functions", "Every package is already installed", "Any Nix package, live in your browser"]
newsletter_candidate = true
why_it_matters = "jinx makes the full nixpkgs ecosystem accessible to TypeScript tooling and browser environments by transpiling Nix while preserving derivation-path parity, rather than reimplementing its package universe."
retrieval_note = "Read Farid Zakaria's article, jinx and jinx-nixpkgs GitHub READMEs, and the published benchmark page. The 231,777-attribute parity numbers and performance measurements are claims/results documented by the project; warm jinx runs are still 2.5x–5.1x slower than Nix in the listed probes."
+++
**Logged at IST:** 2026-10-13 09:17 IST

**What it is:** Farid Zakaria's *jinx*, a Nix-to-TypeScript transpiler, with a compiled TypeScript tree for nixpkgs.

**Gist:** The core move is to preserve the compatibility work embodied in nixpkgs instead of rebuilding a package set for a new evaluator. jinx translates Nix expressions, including laziness, into TypeScript modules and computes the same derivation paths as Nix. The project reports parity across all 231,777 attributes in nixpkgs' CI evaluation set: 229,063 identical drvPaths, 2,714 failing on both sides, and none that differ or fail on only one side.

The payoff is access to TypeScript's debugger, profiler, editor tooling, scripts and browser runtime, including evaluating the compiled nixpkgs tree in a browser. This is not a speedup: the published warm benchmarks show jinx about 2.5x–5.1x slower than Nix on the listed probes, with higher memory use. The pitch is ecosystem reach and inspectability, while retaining Nix store compatibility.

**Newsletter angle:** A striking compatibility strategy for infrastructure tooling: translate the evaluator and keep the hard-won package ecosystem, instead of starting a competing ecosystem from zero.
