+++
title = "Wafer Serving Kimi K3 on AMD MI355X"
slug = "2026-08-03-wafer-kimi-k3-mi355x"
date = 2026-08-03T09:51:00+05:30
[taxonomies]
tags = ["ai-infra", "systems"]
[extra]
source_url = "https://www.wafer.ai/blog/kimi-k3-mi355x"
source_type = "article"
newsletter_candidate = true
why_it_matters = "A concrete serving-economics data point for frontier-scale open models on AMD: HBM capacity can change the node topology, but the software path still decides whether the economics show up in practice."
saved_link = "https://x.com/i/status/2084000214281822637"
related_url = "https://x.com/wafer_ai/status/2084000214281822637"
related_urls = ["https://news.ycombinator.com/item?id=49141073"]
hn_url = "https://news.ycombinator.com/item?id=49141073"
retrieval_note = "Read the Wafer article directly, extracted the shared X post through FXTwitter, inspected the attached screenshot as Hacker News context, and found the matching HN item through Algolia. No independent benchmark reproduction."
+++
**Logged at IST:** 2026-08-03 09:51 IST

**What it is:** Wafer's write-up on serving Moonshot's 2.8T-parameter Kimi K3 on 8x AMD MI355X, with a performance-per-dollar comparison against Nvidia B200 and B300 nodes.

**Gist:** Wafer argues this is one of the first model-serving cases where MI355X's 288 GB HBM per GPU changes the practical topology. Kimi K3 needs more memory than a single 8x B200 node can provide once weights and a 1M-token KV pool are included, so their B200 comparison spans two nodes. The MI355X TP8 setup reaches 952 tok/s/node and 118 tok/s single-stream decode on a 1,024-token input / 400-token output benchmark. Wafer reports that as about 3.8x the per-node aggregate throughput of their TP16 B200 deployment, with 48 tok/s per dollar versus 7 for B200 and 33 for B300 using their cited GPU-hour prices.

The engineering details are the useful part. Speculative decoding needed a ROCm fix for `top_k_renorm_prob`, which Wafer handled with a small PyTorch top-k renormalization path rather than a custom kernel; that reportedly gave about 2.2x single-stream performance, 1.7x at moderate load, and 18% higher peak aggregate. Prefill remained a separate bottleneck: a 172k-token cold prefill was about 51s on MI355X versus 23s on B300 until they got the AITER MLA prefill path working by padding K3's 12 attention heads per rank to a 16-head shape.

**Newsletter angle:** This is a better "CUDA moat" datapoint than a raw benchmark chart because the claimed win comes from capacity-driven topology plus boring software fixes, not from pretending AMD kernels are magically caught up everywhere.

## Embedded source

{{< tweet id="2084000214281822637" url="https://x.com/i/status/2084000214281822637" >}}
