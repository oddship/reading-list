+++
title = "SQLite inside Nix through exec, native imports, and Wasm"
slug = "2026-08-20-sqlite-in-nix-wasm"
date = 2026-08-20T11:17:00+05:30
[taxonomies]
tags = ["developer-tools", "systems"]
[extra]
source_url = "https://fzakaria.com/2026/08/19/three-ways-to-smuggle-sqlite-into-nix"
source_type = "article"
newsletter_candidate = true
why_it_matters = "The post is a concrete cost-model tour of how far Nix evaluator extensibility can go, from unsafe process/native escapes to sandboxed Wasm, and why the practical answer can still be JSON."
saved_link = "https://x.com/fmzakari/status/2090300767148396570"
related_url = "https://x.com/fmzakari/status/2090300767148396570"
retrieval_note = "FXTwitter extraction retrieved Farid Zakaria's post and expanded the blog URL. The durable note is grounded in the destination blog HTML, not just the X post."
+++
**Logged at IST:** 2026-08-20 11:17 IST

**What it is:** Farid Zakaria's write-up on trying to expose SQLite-backed queries to Nix for `nixpkgs-multiverse`.

**Gist:** `nixpkgs-multiverse` currently carries JSON indexes, but `builtins.fromJSON` is eager: one lookup pays the cost of parsing and materializing the whole file. Zakaria uses that as the setup for three SQLite-in-Nix experiments.

`builtins.exec` is the simple unsafe escape hatch: ask `sqlite3` to print a Nix expression and let the evaluator parse it. `builtins.importNative` goes further by loading a shared object that can cache SQLite handles and build Nix values directly, which makes repeated queries much cheaper, but still requires native code during evaluation.

The most interesting path is `builtins.wasm`. With Determinate's Wasm builtin, a module can build real Nix values inside a sandboxed deterministic runtime. Zakaria patches the API with a `read_file_range` helper, wires SQLite's VFS to read database pages from a Nix store path, and gets a real SQLite query running through WebAssembly inside the evaluator.

The punchline is practical rather than triumphalist: `importNative` is fastest, Wasm is safer but currently dominated by about 2.5 seconds of Cranelift startup/JIT cost, and for a modest lockfile query count the current JSON index still wins. The piece is useful because it separates the architectural possibility from the deployment cost model.

**Newsletter angle:** Good systems/developer-tools item on Nix evaluator extensibility, deterministic Wasm as a safer escape hatch, and the mundane performance trade-offs that decide whether elegant infrastructure ideas actually ship.

{{< tweet id="2090300767148396570" url="https://x.com/fmzakari/status/2090300767148396570" >}}
