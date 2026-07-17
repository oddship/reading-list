+++
title = "Running LLM inference on AWS: Bedrock vs SageMaker vs self-hosted on EKS"
slug = "2026-07-17-running-llm-inference-on-aws-bedrock-vs-sagemaker-vs-self-hosted-on-eks"
date = 2026-07-17T15:43:00+05:30
[taxonomies]
tags = ["ai-infra", "systems", "agents"]
[extra]
source_url = "https://devopsity.com/blog/running-llm-inference-on-aws-bedrock-vs-sagemaker-vs-self-hosted-eks/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "Good companion to the self-hosting pieces because it turns the ‘rent vs own’ question into an explicit AWS migration path, with concrete crossover points and infra patterns like Karpenter, vLLM, and mixed spot/on-demand GPU pools."
saved_link = "https://devopsity.com/blog/running-llm-inference-on-aws-bedrock-vs-sagemaker-vs-self-hosted-eks/"
+++
**Logged at IST:** 2026-07-17 15:43 IST

**What it is:** Devopsity’s comparison of three AWS inference patterns: Bedrock, SageMaker endpoints, and self-hosted GPU serving on EKS.

**Gist:** The useful part is not the cloud-brand framing but the workload segmentation. Bedrock wins at low volume and low ops burden, SageMaker sits in the middle for fine-tuned models and predictable dedicated capacity, and self-hosted EKS wins once utilization is high enough that GPU spot economics and batching dominate per-token pricing. The stronger systems lesson is that the architecture choice is really about traffic shape, latency SLOs, compliance boundaries, and whether you want to pay in tokens, instance-hours, or platform complexity.

**Newsletter angle:** Good companion to the self-hosting pieces because it turns the "rent vs own" question into an explicit AWS migration path, with concrete crossover points and infra patterns like Karpenter, vLLM, and mixed spot/on-demand GPU pools.
