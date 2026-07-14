+++
title = "Using uvx in GitHub Actions in a cache-friendly way"
slug = "2026-07-14-using-uvx-in-github-actions-in-a-cache-friendly-way"
date = 2026-07-14T08:12:00+05:30
[taxonomies]
tags = ["developer-tools", "systems"]
[extra]
source_url = "https://til.simonwillison.net/github-actions/uvx-github-actions-cache"
source_type = "article"
newsletter_candidate = true
why_it_matters = "Nice practical CI pattern for teams using uvx as disposable tooling glue, especially because it avoids adding fake dependency files just to drive cache keys."
saved_link = "https://x.com/i/status/2076836099910193484"
+++
**Logged at IST:** 2026-07-14 08:12 IST

**What it is:** Simon Willison linking to his TIL on running `uvx` in GitHub Actions without re-downloading the package every run

**Gist:** The useful trick is to pin `UV_EXCLUDE_NEWER` to a date, use that same date in the GitHub Actions cache key, and set `UV_OFFLINE=1` on cache hits. That gives a lightweight, file-free way to make `uvx tool-name` workflows cacheable, reproducible enough, and intentionally bustable by changing one date.

**Newsletter angle:** Nice practical CI pattern for teams using `uvx` as disposable tooling glue, especially because it avoids adding fake dependency files just to drive cache keys.
