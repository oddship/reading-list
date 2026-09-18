+++
title = "Cactus Needle 3 squeezes tool calling into an 8-29 MB local model"
slug = "2026-09-18-cactus-needle-3"
date = 2026-09-18T14:35:00+05:30
[taxonomies]
tags = ["ai-infra", "developer-tools", "agents", "systems"]
[extra]
source_url = "https://cactuscompute.com/needle"
source_type = "model-release"
source_title = "Cactus: Needle 3 - 8-29 MB foundation model for tiny devices"
saved_title = "Cactus Compute launch post for Needle 3"
related_titles = ["GitHub: cactus-compute/needle", "Needle API docs", "Show HN: Cactus Needle 3", "Hugging Face: Cactus-Compute/needle"]
newsletter_candidate = true
why_it_matters = "Needle 3 is a good example of specialized local models replacing chat with constrained tool calls, schema extraction, embeddings, and confidence-gated refusal on tiny devices."
saved_link = "https://x.com/cactuscompute/status/2100685924401295764"
related_urls = ["https://github.com/cactus-compute/needle", "https://github.com/cactus-compute/needle/blob/main/doc/apis.md", "https://news.ycombinator.com/item?id=49748553", "https://huggingface.co/Cactus-Compute/needle"]
retrieval_note = "Cactus launch page, FXTwitter post, GitHub README/API docs, Hugging Face page, and sampled frames from the attached launch video were read or inspected. Some supporting pages still describe Needle 2, so the Needle 3 claims are grounded mainly in the launch page, X post, HN launch comment, and launch video frames."
+++

**Logged at IST:** 2026-09-18 14:35 IST

**What it is:** Cactus Compute's Needle 3, a tiny local model family for function calling, structured extraction, and embeddings rather than open-ended chat.

{{ tweet(id="2100685924401295764", url="https://x.com/cactuscompute/status/2100685924401295764") }}

**Gist:** Needle 3 trades away general chat and makes every turn a constrained action: given tool definitions, it returns ordered function calls and arguments; given a schema, it returns a typed record; if no declared tool fits, the intended result is an empty list rather than a guess.

The headline is the deployment shape. Cactus says one laddered set of Simple Attention Network weights can be sliced from **2 to 20 layers**, covering roughly **25-121M parameters** in **8-29 MB** CQ2-bit binaries. The launch page claims **400-4k tokens/s decode** and **1-10k tokens/s prefill** on a Raspberry Pi 5, with engines for macOS, Linux, Windows, Android, iOS, watchOS, tvOS, browser WebAssembly, and WASI hosts.

The interesting product bet is that edge assistants do not always need a chat model. Needle's contract is closer to a local automation router: byte-level grammar for valid JSON, calibrated confidence, tool triggers for required routes, schema extraction, embeddings for local search/routing, and small enough binaries for phones, wearables, smart-home devices, robots, and microcontrollers.

The launch material reports that the 20-layer 121M model scores **86.0** on Mobile Actions exact-call accuracy, versus **82.4** for LFM2.5 1.2B, **76.0** for Qwen3.5 0.8B, **65.1** for FunctionGemma 270M, and **57.6** for Apple FM 3B, with DeepSeek V4 Flash at **88.4**. It also claims a 4-layer fine-tuned subnetwork can pass DeepSeek V4 Flash on a narrow downstream task.

**Newsletter angle:** The local-agent stack may split into tiny, task-specialized control models plus cloud fallback, not just smaller chatbots. Needle is interesting because it treats refusal, JSON validity, confidence, and tool routing as first-class runtime guarantees for edge automation.
