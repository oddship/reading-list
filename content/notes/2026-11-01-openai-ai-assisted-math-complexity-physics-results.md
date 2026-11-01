+++
title = "OpenAI's AI-assisted research results: striking claims, open questions"
slug = "2026-11-01-openai-ai-assisted-math-complexity-physics-results"
date = 2026-11-01T17:39:00+05:30
[taxonomies]
tags = ["llm-research", "org-design"]
[extra]
source_url = "https://openai.com/index/building-scientific-understanding-with-academic-communities/"
source_title = "Working with academic communities to build scientific understanding"
source_type = "research-announcement"
saved_link = "https://news.ycombinator.com/item?id=50251344"
saved_title = "Hacker News: Three new discoveries in mathematics, computer science, and physics"
related_urls = ["https://github.com/openai/math", "https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf", "https://github.com/openai/math/blob/main/lean/docs/378.md", "https://news.ycombinator.com/item?id=50251661"]
related_titles = ["OpenAI math repository and proof artifacts", "ETH preprint", "Lean formalization of the ETH result", "Hacker News discussion focused on the ETH paper"]
newsletter_candidate = true
why_it_matters = "A significant test of AI-assisted research, and of the institutions around it. OpenAI reports three major results and describes distinct release/verification arrangements, while the mathematical claims, their practical implications, and questions of credit and access deserve separate scrutiny."
retrieval_note = "Read OpenAI's announcement, the openai/math repository README, and the ETH preprint text extracted from the repository PDF. The ETH claim is an asymptotic result, not a practical SAT-solving breakthrough or a resolution of P vs NP. Linked the companion HN discussion as discourse, not independent verification."
+++

OpenAI's announcement describes three model-produced research results: a proof of the local smoothing conjecture in every dimension (with consequences for the Kakeya and Stein restriction conjectures), a formalized refutation of the Exponential Time Hypothesis (ETH), and a mathematical existence proof concerning QCD and related quantum field theories. The company says the ETH result is being shepherded by complexity theorists Russell Impagliazzo, Ramamohan Paturi, and Ryan Williams, with raw artifacts released for independent examination. For the mathematics and physics results, it describes different release arrangements shaped with external experts.

The ETH paper gives a deterministic subexponential-time algorithm for counting satisfying assignments of fixed-width CNF formulas and says this refutes ETH. That is a theoretical asymptotic result, not a claim that SAT is practically easy, and not a resolution of P vs. NP. OpenAI itself says finding algorithms that turn the theoretical advance into practical improvements will require substantial further research. Its public repository describes the materials as raw research data, notes that results are at different verification stages, and says some unformalized results could have issues.

The announcement is also notable for its proposed collaboration principles: transparency, no academic credit claimed for the model's discoveries, recognition for collaborators' explanatory work, and independence. Those commitments do not settle broader questions raised by the release, including how prior community knowledge, credit, access, and the choice of initial reviewers should be handled. The companion [Hacker News discussion](https://news.ycombinator.com/item?id=50251661) focuses on the ETH paper; it is discussion, not independent verification.
