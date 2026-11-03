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
saved_link = "https://x.com/badlogicgames/status/2117355349967544808"
saved_title = "Mario Zechner's recommended reading post"
related_urls = ["https://x.com/rikiyatakehi/status/2117313742891327994", "https://x.com/AlexKrentsel/status/2117376683724660898", "https://x.com/hosseeb/status/2117380109355352166", "https://x.com/a1zhang/status/2117364329133621614"]
related_titles = ["Rikiya Takehi: Weight-Space Programming announcement", "Alex Krentsel: reported reproduction", "Haseeb Qureshi: clarification on the interpretation", "Alex Zhang: authors' clarification on the method"]
newsletter_candidate = true
why_it_matters = "A striking early report that frontier LLMs may inspect and directly edit neural-network parameters, extending model-assisted optimization beyond prompts and code."
retrieval_note = "Read the full MIT CSAIL authors' blog post; extracted X posts by Mario Zechner, Rikiya Takehi, Alex Krentsel, Haseeb Qureshi, and quoted author Alex Zhang via FXTwitter. The paper authors explain the result used a published activation-steering technique for repetition/looping; Haseeb cautions against interpreting it as RSI or telepathy. Alex Krentsel reports reproduction, not independent peer-reviewed validation. The authors characterize the underlying findings as very early results."
+++

MIT CSAIL researchers Rikiya Takehi, Jayden Teoh, Alex Zhang, and Omar Khattab introduce **weight-space programming**: asking a general-purpose LLM to inspect or directly edit neural-network weights to meet a natural-language goal, without gradient descent or training loops. Their early experiments include identifying what small networks do from their raw weights, writing small game-playing networks, and modifying a language model.

For Qwen3.5-0.8B, the authors report that GPT-6 Astra identified weights associated with reasoning loops and changed 0.016% of the parameters. Under the same sampling settings, they report MATH-500 rising from 7.9% to 48.1%, with IFEval instruction-following performance also increasing threefold. The authors call these very early results, not an established general method. Alex Krentsel separately says he reproduced the results and characterizes the capability as a recent step change; that is a researcher’s reproduction claim, not peer-reviewed independent validation.

The paper’s broader proposal is that language models may reason directly about parameter values, not only about prompts, code, or training procedures. The authors’ follow-up clarification adds important context: Astra’s edit drew on a published activation-steering technique for reducing repetition/looping, rather than evidence of unexplained “X-ray vision” into another model. Their post says the task began from a simple prompt and evolved without human feedback; the researchers recognized the looping explanation after inspecting the result. Haseeb Qureshi emphasizes this is a cool but understandable capability, not recursive self-improvement or “LLM telepathy.” The demonstration remains an early result; its scope and generality are open questions.

{{ tweet(id="2117313742891327994", url="https://x.com/rikiyatakehi/status/2117313742891327994") }}
{{ tweet(id="2117376683724660898", url="https://x.com/AlexKrentsel/status/2117376683724660898") }}
{{ tweet(id="2117380109355352166", url="https://x.com/hosseeb/status/2117380109355352166") }}