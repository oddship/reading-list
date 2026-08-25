+++
title = "llama.cpp as a pure Go library"
slug = "2026-08-25-go-llama-pure-go-local-inference"
date = 2026-08-25T20:15:00+05:30
[taxonomies]
tags = ["ai-infra", "developer-tools", "systems"]
[extra]
source_url = "https://github.com/goccy/go-llama"
source_type = "repo"
newsletter_candidate = true
why_it_matters = "A useful example of local inference becoming importable infrastructure for Go services, without cgo, shared libraries, or a separate wasm runtime."
saved_link = "https://x.com/goccy54/status/2092156440786186315"
related_url = "https://x.com/goccy54/status/2092156440786186315"
related_urls = ["https://raw.githubusercontent.com/goccy/go-llama/main/README.md", "https://github.com/goccy/llama-wasm", "https://github.com/goccy/wasm2go", "https://github.com/goccy/llamawasm2go"]
retrieval_note = "FXTwitter extraction succeeded and resolved the GitHub repo. The go-llama README/API metadata, go.mod, llama-wasm README, wasm2go README, and llamawasm2go repo metadata were read directly."
+++
**Logged at IST:** 2026-08-25 20:15 IST

**What it is:** `goccy/go-llama`, a pure-Go llama.cpp-style inference library for running GGUF models from Go applications.

**Gist:** The interesting bit is the packaging path. `go-llama` does not bind to llama.cpp through cgo, and it does not embed a wasm runtime. Instead, llama.cpp is compiled to WASI WebAssembly, then translated ahead-of-time into standalone Go through `wasm2go` and `llamawasm2go`. The result is meant to be a normal Go dependency: no shared library, no cgo, and static-binary friendly.

The README claims a fairly complete local-inference surface: model/context management, streaming, interruption, sampling controls, speculative decoding, LoRA adapters, chat templates, embeddings, scoring, and state save/load. It also exposes sandbox-ish knobs around preopened directories, memory caps, in-memory filesystems, and stdio capture.

The caveat is also clear: wasm32 linear memory caps the engine at 4 GiB, so this is for small quantized models, roughly the README's “3B parameters at Q4” target, not giant local serving. But that is still a useful deployment shape: embedding small LLM-derived features directly inside Go services without shipping a C++ runtime edge.

**Newsletter angle:** Good AI-infra/developer-tools item: local inference is becoming something a Go service can import like a library, not a sidecar process or cgo deployment project.

{{ tweet(id="2092156440786186315", url="https://x.com/goccy54/status/2092156440786186315") }}
