+++
title = "tsrs: a Rust port of the TypeScript compiler"
slug = "2026-10-19-tsrs-rust-typescript-compiler"
date = 2026-10-19T23:59:00+05:30
[taxonomies]
tags = ["developer-tools", "systems"]
[extra]
source_url = "https://blog.cloudflare.com/typescript-rust-port/"
source_title = "Introducing tsrs: a Port of TypeScript to Rust"
source_type = "article"
saved_link = "https://x.com/voidzerodev/status/2112531443591020965"
saved_title = "VoidZero introduces tsrs"
related_url = "https://x.com/voidzerodev/status/2112531443591020965"
related_urls = ["https://github.com/oxc-project/tsrs", "https://github.com/oxc-project/tsrs/tree/main/bench"]
related_titles = ["tsrs source repository and current status", "tsrs benchmark methodology and results"]
newsletter_candidate = true
why_it_matters = "tsrs is an attempt to make TypeScript type-checking faster and more memory-efficient while staying aligned with TypeScript's design, and to run the toolchain in WebAssembly environments such as browsers and Workers."
retrieval_note = "Read Cloudflare's announcement and the tsrs repository README. The up-to-8x speed and ~70% lower-memory figures are the authors' early benchmark claims versus TypeScript 7.0 under matched worker counts; the project remains experimental and its README lists compatibility gaps."
+++
**Logged at IST:** 2026-10-20

**What it is:** Cloudflare, VoidZero, and Max Schwenk of Owner.com are developing `tsrs`, a Rust port of the TypeScript compiler, in collaboration with the TypeScript team and within the Oxc toolchain.

**Gist:** The project is explicitly not a fork intended to take over TypeScript's direction. Its stated aim is a faithful port that tracks the upstream team's language and implementation decisions. Cloudflare's early benchmarks report up to 8× faster checking and about 70% less memory than TypeScript 7.0 at the same number of checker workers; the announcement notes that TypeScript 7.1 beta itself is already up to 2.5× faster than 7.0, with some optimizations upstreamed from `tsrs`.

The Rust implementation is also motivated by WebAssembly: the team says its memory model makes it easier to integrate with a Wasm host, enabling uses in browsers and Workers. The project repository currently describes `tsrs` as an experimental replacement for the TypeScript 7 compiler and language server, with a browser playground and a goal of full conformance. Its README also documents unsupported options and known differences, so this is not yet a drop-in replacement to assume without testing.

**Why it matters:** A compiler port can be more than a language rewrite: the pitch combines faster checking with a smaller memory footprint and new deployment targets. The harder long-term question is whether the port can stay behaviorally aligned with TypeScript as the upstream compiler and language evolve.

**Source:** https://blog.cloudflare.com/typescript-rust-port/
**Code and current status:** https://github.com/oxc-project/tsrs
**Saved X post:** https://x.com/voidzerodev/status/2112531443591020965
