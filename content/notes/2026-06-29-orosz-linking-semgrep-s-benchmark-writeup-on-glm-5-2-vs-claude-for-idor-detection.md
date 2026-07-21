+++
title = "Orosz linking Semgrep’s benchmark writeup on GLM 5.2 vs Claude for IDOR detection"
slug = "2026-06-29-orosz-linking-semgrep-s-benchmark-writeup-on-glm-5-2-vs-claude-for-idor-detection"
date = 2026-06-29
[taxonomies]
tags = ["agents", "security", "llm-research"]
[extra]
source_url = "https://x.com/i/status/2071378924462911870"
source_type = "x-post"
newsletter_candidate = true
why_it_matters = "good evidence that harness design still dominates raw model choice, but also that at least one open-weight coding model has crossed into “serious default option” territory for security work on both performance and cost."
saved_link = "https://x.com/i/status/2071378924462911870"
+++
**Gist:** on Semgrep’s IDOR benchmark, GLM 5.2 scored 39% F1 in a simple prompt-only PydanticAI harness, beating Claude Code’s 32% while costing roughly $0.17 per vulnerability found; Semgrep’s own endpoint-discovery multimodal harness still led overall at 53–61% F1.

**Newsletter angle:** “the harness matters more than the model, until a cheap open model gets good enough to change the default stack.”
