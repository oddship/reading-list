+++
title = "Diffusing Blame"
slug = "2026-07-18-diffusing-blame"
date = 2026-07-18T21:31:00+05:30
[taxonomies]
tags = ["llm-research", "systems"]
[extra]
source_url = "https://arxiv.org/abs/2606.31700"
source_type = "paper"
newsletter_candidate = true
why_it_matters = "Interesting biologically plausible learning result because it treats credit assignment as an architecture-and-routing problem rather than assuming backprop’s exact weight transport is the only path to useful learning."
saved_link = "https://x.com/i/status/2078136419521048905"
+++
**Logged at IST:** 2026-07-18 21:31 IST

**What it is:** Sakana AI sharing its ALIFE 2026 paper `Diffusing Blame`, about learning in Dale-constrained dual-stream neural networks without weight transport.

**Gist:** The paper asks whether networks can learn competitively while respecting Dale’s principle, where each neuron is either excitatory or inhibitory, and without backprop’s biologically implausible weight transport. Their method extends Error Diffusion with modulo error routing for multi-class settings, splitting layers into excitatory and inhibitory streams with non-negative weights. The results show Dale-constrained networks can still learn on image classification and reinforcement-learning tasks, including MNIST, CIFAR-10, PPO on Brax continuous-control tasks, and Craftax.

**Newsletter angle:** Interesting biologically plausible learning result because it treats credit assignment as an architecture-and-routing problem rather than assuming backprop’s exact weight transport is the only path to useful learning.
