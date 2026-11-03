+++
title = "Weight-space programming: LLMs reading and editing neural network weights"
slug = "2026-11-03-weight-space-programming"
date = 2026-11-03T00:00:00+05:30
[taxonomies]
tags = ["llm-research"]
[extra]
source_url = "https://rikiyat.github.io/blog/weight-space-programming/"
source_title = "Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights"
source_type = "research-blog"
saved_link = "https://x.com/AlexKrentsel/status/2117376683724660898"
saved_title = "Alex Krentsel: reproducing the weight-space programming results"
related_url = "https://x.com/rikiyatakehi/status/2117313742891327994"
related_title = "Rikiya Takehi: Weight-Space Programming announcement"
related_urls = ["https://x.com/badlogicgames/status/2117355349967544808"]
related_titles = ["Mario Zechner's recommended reading post"]
newsletter_candidate = true
why_it_matters = "A striking early report that frontier LLMs may inspect and directly edit neural-network parameters, extending model-assisted optimization beyond prompts and code."
retrieval_note = "Read the full MIT CSAIL authors' blog post and extracted both X posts via FXTwitter. Alex Krentsel says he reproduced the reported results and argues the capability is a recent step change; this is a personal reproduction report, not independent peer-reviewed validation. The MIT post itself describes its findings as very early results."
+++

MIT CSAIL researchers Rikiya Takehi, Jayden Teoh, Alex Zhang, and Omar Khattab introduce **weight-space programming**: asking a general-purpose LLM to inspect or directly edit neural-network weights to meet a natural-language goal, without gradient descent or training loops. Their early experiments include identifying what small networks do from their raw weights, writing small game-playing networks, and modifying a language model.

For Qwen3.5-0.8B, the authors report that GPT-6 Astra identified weights associated with reasoning loops and changed 0.016% of the parameters. Under the same sampling settings, they report MATH-500 rising from 7.9% to 48.1%, with IFEval instruction-following performance also increasing threefold. The authors call these very early results, not an established general method. Alex Krentsel separately says he reproduced the results and characterizes the capability as a recent step change; that is a researcher’s reproduction claim, not peer-reviewed independent validation.

The paper’s broader proposal is that language models may reason directly about parameter values, not only about prompts, code, or training procedures. If robust, this could affect both optimization and interpretability; the scope, reproducibility, and generality of the reported experiments remain open questions.

{{ tweet(id="2117313742891327994", url="https://x.com/rikiyatakehi/status/2117313742891327994") }}
{{ tweet(id="2117376683724660898", url="https://x.com/AlexKrentsel/status/2117376683724660898") }}