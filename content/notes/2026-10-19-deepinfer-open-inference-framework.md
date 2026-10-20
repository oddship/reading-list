+++
title = "DeepInfer: DeepSeek's open inference framework"
slug = "2026-10-19-deepinfer-open-inference-framework"
date = 2026-10-19T23:59:00+05:30
[taxonomies]
tags = ["ai-infra", "systems"]
[extra]
source_url = "https://github.com/deepseek-ai/DeepInfer"
source_title = "DeepInfer: High-performance, large-scale inference framework for DeepSeek models"
source_type = "repository"
saved_link = "https://x.com/deepseek_ai/status/2112476496283775135"
saved_title = "DeepSeek announces DeepInfer"
related_url = "https://x.com/deepseek_ai/status/2112476496283775135"
related_urls = ["https://github.com/deepseek-ai/DeepInfer/blob/main/doc/README.md", "https://github.com/deepseek-ai/DeepInfer/blob/main/examples/sweep/run_sweep.sh"]
related_titles = ["DeepInfer documentation", "Reproduce the published performance sweeps"]
newsletter_candidate = true
why_it_matters = "DeepSeek has released the inference stack behind its large-scale services, exposing specialized scheduling, parallelism, and decoding techniques, but the current release is model- and hardware-specific and does not include every component needed for a complete service."
retrieval_note = "Extracted DeepSeek's X announcement and read the repository README, including supported features, hardware, benchmark setup, and explicitly missing service components. Benchmark results are project-reported and tied to stated GPU configurations."
+++
**Logged at IST:** 2026-10-20

**What it is:** DeepSeek has open-sourced DeepInfer, the inference framework it says powers its large-scale production services. The repository currently supports DeepSeek-V4.1-Flash and describes the release as an offline-inference stack with core serving features.

**Gist:** The implementation combines optimized model/runtime kernels with attention and expert parallelism, asynchronous scheduling, multi-token draft verification, structured outputs, and options for batch-invariant inference and deterministic sampling. The README lists NVIDIA SM100 GPUs and Huawei Ascend 950 NPUs as supported hardware, with platform-specific prerequisites.

DeepSeek publishes prefill and decode performance charts, measured on four SM100 GPUs for prefill and 64 for decode within one scale-up domain. Those are project-reported results, and the repository provides a sweep script for reproducing them. DeepInfer is Apache-2.0 and acknowledges that it builds primarily on vLLM, with inspiration from SGLang and TensorRT-LLM.

**Caveat:** This is not a turnkey, general-purpose serving platform yet. The repository says a KV-cache system, prefill/decode disaggregation, and load balancing across data-parallel replicas are not included in this release. Its supported model and accelerator matrix is also narrow.

**Source:** https://github.com/deepseek-ai/DeepInfer
**Saved X post:** https://x.com/deepseek_ai/status/2112476496283775135
