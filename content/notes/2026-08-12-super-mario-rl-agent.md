+++
title = "Training an RL agent to beat Super Mario Bros. World 1-1"
slug = "2026-08-12-super-mario-rl-agent"
date = 2026-08-12T18:56:00+05:30
[taxonomies]
tags = ["agents", "llm-research", "developer-tools"]
[extra]
source_url = "https://shantanugoel.com/2026/08/12/teach-machines-super-mario/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "A concrete reinforcement-learning experiment where the lessons are less about Mario and more about observation design, reward shaping, checkpoint selection, and the amount of iteration hidden behind a clean result."
saved_link = "https://x.com/i/status/2087529937272267261"
related_url = "https://x.com/shantanugoel/status/2087529937272267261"
related_urls = ["https://x.com/shantanugoel/status/2087452030000615560", "https://github.com/shantanugoel/super-mario-bros-rl"]
retrieval_note = "Tweet and quoted post extracted via FXTwitter; quoted media inspected directly. Linked Shantanu Goel article was fetched directly and read from rendered article HTML; GitHub README and repo metadata were fetched separately."
+++
**Logged at IST:** 2026-08-12 18:56 IST

**What it is:** Shantanu Goel’s writeup on training a PPO reinforcement-learning agent, using stable-retro and stable-baselines3, to beat World 1-1 of NES Super Mario Bros.

**Gist:** The interesting part is the debugging path. Early attempts failed because the agent saw only stacked 84×84 grayscale frames, produced too-short jumps, and treated three Mario lives as one long episode. Moving to one-life episodes helped, but the bigger fixes were reward shaping and observation design: dense rewards for forward progress, coins, score, time pressure, and a modest flag bonus, plus going back from fast memory-coordinate observations to pixels so the policy could actually see pits, pipes, and goombas.

The final numbers are strong but honestly caveated: 97/100 one-life stochastic clears, 92.3% over 300, 93.8% over 500, best streak of 58, and 300/300 deterministic clears from the final checkpoint. Goel also notes that training from scratch remained seed-sensitive, with runs ranging from about 94% down to 50%, so the reproducible artifact is the selected checkpoint and harness rather than a fully reliable recipe.

The quoted post adds the practical experiment bill: a laptop RTX 3070m, 3.5 days and nights of experiments, about $6.58 of DeepSeek V4 Flash tokens through OpenRouter, and roughly 187M LLM-side tokens across the workspace while iterating.

**Newsletter angle:** Good agent-systems item: clean demo results hide a lot of harness work, reward design, observation choices, evaluation modes, seed sensitivity, and checkpoint curation.
