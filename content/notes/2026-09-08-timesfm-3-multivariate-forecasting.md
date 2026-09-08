+++
title = "TimesFM-3 brings zero-shot forecasting to multivariate time series"
slug = "2026-09-08-timesfm-3-multivariate-forecasting"
date = 2026-09-08T20:14:00+05:30
[taxonomies]
tags = ["llm-research", "systems", "ai-infra"]
[extra]
source_url = "https://research.google/blog/timesfm-3-a-zero-shot-foundation-model-for-multivariate-forecasting/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "Time-series foundation models are moving from univariate demos toward multivariate, covariate-aware forecasting primitives that can plug into data platforms."
saved_link = "https://research.google/blog/timesfm-3-a-zero-shot-foundation-model-for-multivariate-forecasting/"
related_urls = ["https://huggingface.co/google/timesfm-3.0-pytorch", "https://github.com/google-research/timesfm", "https://huggingface.co/spaces/Salesforce/GIFT-Eval", "https://huggingface.co/spaces/autogluon/fev-bench", "https://huggingface.co/spaces/Real-TSF/TIME-leaderboard"]
retrieval_note = "Google Research post, Hugging Face model card/API, and GitHub README read directly."
+++

**Logged at IST:** 2026-09-08 20:14 IST

**What it is:** Google Research's introduction of TimesFM-3, a 330M-parameter zero-shot time-series foundation model for multivariate forecasting.

**Gist:** TimesFM-3 moves the TimesFM family beyond strictly univariate forecasting. It natively supports forecasting multiple related targets together, past-only covariates, and past-future dynamic covariates such as holidays, promotions, or weather forecasts that are known over the forecast horizon.

The architecture keeps the TimesFM patching idea, grouping time series into patches of 32 steps, but builds multivariate tokens and alternates two kinds of attention. Causal temporal attention looks horizontally through each series' past without leaking future target values. Full variate attention looks vertically across series at the same time step, letting the model capture cross-series relationships.

A practical difference is decode shape. Earlier TimesFM versions forecast one patch at a time; TimesFM-3 uses contiguous patch masking to append masked future placeholders and fill the whole horizon in a single forward pass. It predicts point forecasts plus 9 quantiles, giving a probabilistic forecast for every target and horizon step.

**Benchmarks:** Google reports TimesFM-3 as top-ranked among pre-trained foundation models on Gift-Eval, FEV-Bench, and TIME, in both point and probabilistic forecasting metrics. The post emphasizes that even TimesFM-3's univariate mode matches or beats other replicable time-series foundation models, while full multivariate mode improves further when cross-series information and covariates are available.

**Caveats:** The GitHub README says TimesFM source code is Apache-2.0 and older weights through 2.5 remain Apache-2.0, but TimesFM-3 pretrained weights are currently under a separate non-commercial license restricted to non-commercial, non-production use. The blog says BigQuery integration is coming in the next few weeks, so the open checkpoint is available now but the managed data-platform path is still pending.

**Newsletter angle:** This is another sign that foundation-model patterns are leaking into forecasting and data infrastructure. The interesting product question is not just whether the model tops benchmarks, but whether multivariate zero-shot forecasting becomes a callable primitive inside warehouses, observability systems, retail planning tools, and finance workflows.
