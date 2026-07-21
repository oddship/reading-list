+++
title = "Armin Ronacher explaining Pi’s new per-project approval prompt and the security model behind it"
slug = "2026-06-08-armin-ronacher-explaining-pi-s-new-per-project-approval-prompt-and-the-security-model-behind-it"
date = 2026-06-08
[taxonomies]
tags = ["agents", "security", "llm-research"]
[extra]
source_url = "https://x.com/i/status/2064060467975520341"
source_type = "x-post"
newsletter_candidate = true
why_it_matters = "strong practical framing for repo trust boundaries in coding-agent UX, and a good complement to the separate discussion about whether AGENTS files improve task performance."
saved_link = "https://x.com/i/status/2064060467975520341"
+++
**What it is:** Armin Ronacher explaining Pi’s new per-project approval prompt and the security model behind it.

**Gist:** the key argument is that `AGENTS.md` gets injected into the system prompt, so untrusted repo-level instructions can directly influence agent behavior in ways a README usually won’t; Pi added one-time trust prompts to reduce silent execution risk on untrusted repos.

**Newsletter angle:** repo-local agent instructions are becoming both a productivity primitive and a new software supply-chain/security surface.

**Note:** extracted via FXTwitter API from the tweet’s article body; points to GitHub issue `earendil-works/pi#5514` for feedback.
