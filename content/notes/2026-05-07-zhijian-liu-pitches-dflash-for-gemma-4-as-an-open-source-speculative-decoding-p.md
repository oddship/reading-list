+++
title = "Zhijian Liu pitches DFlash for Gemma 4 as an open-source speculative decoding path that can push native Gem..."
date = 2026-05-07
[taxonomies]
tags = ["reading-log", "x-post", "x-com", "historical-backfill"]
[extra]
source_url = "https://x.com/i/status/2051900751673467097"
source_type = "x-post"
status = "published"
newsletter_candidate = true
why_it_matters = ""
saved_link = "https://x.com/i/status/2051900751673467097"
+++
Imported from historical reading log.
- Extracted main post via `api.fxtwitter.com` fallback and checked the linked repo `z-lab/dflash`.
- Zhijian Liu pitches `DFlash` for Gemma 4 as an open-source speculative decoding path that can push native Gemma 4 MTP further, claiming up to `6x` faster generation at the same quality.
- Repo framing: `DFlash: Block Diffusion for Flash Speculative Decoding` — a lightweight block-diffusion draft model for speculative decoding, with support across Gemma, Qwen, Llama, GPT-OSS, MLX, vLLM, SGLang, and Transformers backends.
- What seems notable is not just the speed claim, but that speculative-decoding acceleration is turning into a portable ecosystem layer with open models, backend integrations, and per-model draft variants.
- Good angle: `inference-speed competition is moving into open, pluggable speculative-decoding infrastructure`.
