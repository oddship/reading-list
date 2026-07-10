+++
title = "Sebastian Raschka summarizing a paper on whether repository-level context files like AGENTS.md actually hel..."
slug = "2026-06-08-sebastian-raschka-summarizing-a-paper-on-whether-repository-level-context-files-like-agents-md-actu"
date = 2026-06-08
[taxonomies]
tags = ["reading-log", "x-post", "historical-backfill", "agents", "llm-research"]
[extra]
source_url = "https://x.com/rasbt/status/2063649136323252397"
source_type = "x-post"
status = "reviewed"
newsletter_candidate = true
why_it_matters = "useful empirical pushback against overstuffed agent instruction files; supports keeping repo guidance short, specific, and preferably written by humans with real domain context."
saved_link = "https://x.com/rasbt/status/2063649136323252397"
+++
**What it is:** Sebastian Raschka summarizing a paper on whether repository-level context files like `AGENTS.md` actually help coding agents.

**Gist:** in the reported benchmarks, LLM-generated context files were neutral-to-slightly-worse versus no context file, developer-written ones were better than LLM-written ones, and surprisingly the no-context condition was often cheaper/more efficient.

**Newsletter angle:** more agent context is not automatically better — extra instructions can increase exploration cost without improving task success.

**Note:** extracted from the FXTwitter API `article` body; links to arXiv paper `2602.11988`.
