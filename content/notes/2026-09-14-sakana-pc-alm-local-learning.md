+++
title = "Sakana's PC-ALM trains deep nets with local credit dynamics"
slug = "2026-09-14-sakana-pc-alm-local-learning"
date = 2026-09-14T21:55:00+05:30
[taxonomies]
tags = ["llm-research", "systems"]
[extra]
source_url = "https://pub.sakana.ai/pc-alm/"
source_type = "research-blog"
newsletter_candidate = true
why_it_matters = "PC-ALM reframes multilayer credit assignment as layer-local primal/dual control dynamics, narrowing the gap between predictive coding and backprop on very deep networks."
saved_link = "https://x.com/SakanaAILabs/status/2099468208231399687"
related_url = "https://x.com/SakanaAILabs/status/2099468208231399687"
related_urls = ["https://arxiv.org/abs/2605.31022", "https://github.com/SakanaAI/pc-alm", "https://raw.githubusercontent.com/SakanaAI/pc-alm/main/README.md"]
retrieval_note = "Tweet extracted via FXTwitter; linked Sakana blog, arXiv abstract, GitHub page, and raw README were read. Attached launch video was noted but not sampled because the blog contains the same core claims and figures."
+++

**Logged at IST:** 2026-09-14 21:55 IST

**What it is:** Sakana AI introduces PC-ALM, an augmented-Lagrangian version of predictive coding for training neural networks without a global backpropagation pass.

**Gist:** Standard predictive coding already gives a layer-local learning story, but its credit signal tends to decay in deep, narrow networks. PC-ALM keeps the local-neighbor structure and adds per-layer Lagrange multipliers: “dual neurons” that accumulate local constraint errors during inference.

That turns each layer into something like a PI feedback controller. In linear networks, the dual variables converge to the exact backprop credit signals; in nonlinear experiments, Sakana reports much better signal propagation than standard PC and near-backprop performance on residual MLPs up to 1000 layers on MNIST.

The repo is a minimal JAX reference implementation covering MNIST/Fashion-MNIST width/depth grids for BP, PC, and PC-ALM. Its README includes a reproducible Fashion-MNIST cell where PC-ALM reaches 77.75% test accuracy versus 78.66% for BP and 68.13% for PC, with gradient cosine 0.909 versus PC’s 0.604.

**Newsletter angle:** Useful because it connects NeuroAI’s local-learning motivation to distributed optimization and control theory. The interesting claim is not “the brain runs this exact algorithm,” but that backprop-like credit can emerge from local coupled dynamics rather than an explicit global backward pass.
