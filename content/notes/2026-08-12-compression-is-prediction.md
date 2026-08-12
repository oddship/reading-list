+++
title = "Compression is prediction"
slug = "2026-08-12-compression-is-prediction"
date = 2026-08-12T19:00:00+05:30
[taxonomies]
tags = ["llm-research", "systems"]
[extra]
source_url = "https://ngrok.com/blog/compression-is-prediction"
source_type = "article"
newsletter_candidate = true
why_it_matters = "A clean, teachable bridge between compression and language modeling: better probabilities reduce bits in arithmetic coding, and LLM training optimizes the same prediction-shaped quantity through cross-entropy."
saved_link = "https://x.com/i/status/2087523924351369599"
related_url = "https://x.com/mitsuhiko/status/2087523924351369599"
retrieval_note = "Tweet extracted via FXTwitter; linked ngrok article fetched via direct HTML and Jina reader fallback for clean article text."
+++
**Logged at IST:** 2026-08-12 19:00 IST

**What it is:** Armin Ronacher recommending Annie Sexton’s ngrok explainer, “Compression is prediction.”

**Gist:** The piece explains compression through the same lens as language modeling: a model predicts symbol probabilities, and an entropy coder turns those probabilities into a bitstream. Arithmetic coding makes the connection especially clear: high-probability symbols keep the encoded range wider and cost fewer bits; low-probability misses shrink the range and require more precision.

The useful bridge to LLMs is that language models are also next-token probability machines. For compression, you do not sample the next token; you already know the real next token and pay `-log2(probability)` bits for whatever probability the model assigned it. A better predictor gives lower bits per symbol. That is why GPT-2 plus arithmetic coding can compress a Dickens quote much better than a simple order-1 model in the article’s example.

The caveat is operational, not mathematical. LLMs are excellent predictors, but using a multi-gigabyte model to compress HTTP payloads is absurd once model size, CPU/GPU cost, memory, and latency are counted. Ordinary gzip/Brotli-style compressors win in practice because their models and decoders are tiny and fast enough for the job.

**Newsletter angle:** Good foundations item for LLM intuition: cross-entropy training, next-token prediction, and lossless compression are all different faces of the same “assign better probabilities to what comes next” problem.
