+++
title = "PrismML's Bonsai 2 27B pushes ternary local models toward lossless"
slug = "2026-09-18-prismml-bonsai-2-27b"
date = 2026-09-18T10:58:00+05:30
[taxonomies]
tags = ["ai-infra", "systems"]
[extra]
source_url = "https://prismml.com/news/bonsai-2-27b"
source_type = "model-release"
newsletter_candidate = true
why_it_matters = "If the reported retention holds up, 27B-class reasoning and multimodal models are getting small enough for local assistants, private workflows, and single-GPU serving without a large quality cliff."
saved_link = "https://x.com/PrismML/status/2100692248480596348"
related_urls = ["https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf", "https://techcrunch.com/2026/09/17/prismml-hopes-its-tiny-llm-could-change-how-we-all-use-ai", "https://prismml.com/", "https://github.com/PrismML-Eng/Bonsai-demo/blob/main/bonsai-2-27b-whitepaper.pdf"]
retrieval_note = "PrismML X launch post was extracted via FXTwitter; the attached benchmark image was OCR'd; PrismML's launch post, Hugging Face model card, and TechCrunch coverage were read directly."
+++

**Logged at IST:** 2026-09-18 10:58 IST

**What it is:** PrismML's launch of Ternary Bonsai 2 27B, a compressed Qwen3.8-27B-derived multimodal model released under Apache 2.0.

**Gist:** PrismML says Bonsai 2 27B uses ternary `{−1, 0, +1}` weights with FP16 group-wise scaling, landing around **1.76 effective bits per weight** and a **5.9 GB** footprint. The company claims this is more than **9x smaller** than the full-precision Qwen3.8 27B counterpart while retaining **98.2%** of aggregate benchmark performance.

The headline table is useful because it shows where the loss remains. Overall score is **83.9** versus Qwen3.8 27B at **85.4**; math is nearly preserved (**96.57** versus **97.06**), coding is close (**81.58** versus **82.17** in the launch table), agentic/tool calling drops more (**77.57** versus **79.74**), and vision drops from **81.64** to **78.59**. Instruction-following is reported as slightly above the base model at **82.66** versus **81.25**.

The Hugging Face card adds the deployment shape: GGUF packs for PrismML's `llama.cpp` fork, MLX companion weights for Apple Silicon, 262K context inherited from the Qwen3.8-27B hybrid-attention backbone, and benchmark comparisons against conventional low-bit quantizations. PrismML frames the result as an intelligence-density gain rather than only a size reduction: a 27B-class model that fits on a normal laptop or a single consumer/datacenter GPU.

**Newsletter angle:** Local AI is moving from "small model because hardware is constrained" toward "large model behaviour under a small memory and power budget." The interesting metric is becoming useful capability per GB / joule, not only benchmark score at full precision.
