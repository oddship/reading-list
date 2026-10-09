+++
title = "Pi's system theme derives color from your terminal and contrast requirements"
slug = "2026-10-09-pi-system-theme-terminal-colors-contrast"
date = 2026-10-09T09:58:00+05:30
[taxonomies]
tags = ["developer-tools", "systems"]
[extra]
source_url = "https://earendil.com/posts/system-theme/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "The theme adapts to a user's terminal palette without blindly reusing colors that may be unreadable: it separates hue/chroma from lightness, then derives role-specific lightness from contrast constraints."
saved_link = "https://x.com/mitsuhiko/status/2108527082070233261"
saved_title = "Armin Ronacher on Pi's new system theme"
source_title = "There are many themes, but this one is yours"
related_url = "https://x.com/mitsuhiko/status/2108527082070233261"
retrieval_note = "Extracted the X post via FXTwitter and read Maximilian Blazek's linked article directly. The post points to the article; no attached media was present."
+++
**Logged at IST:** 2026-10-09 09:58 IST

**What it is:** Maximilian Blazek explains how Pi's new default system theme adapts to the user's terminal colors while preserving readable contrast.

**Gist:** Pi treats the terminal's palette as a source of hue and chroma, not as a finished UI theme. It converts colors into perceptual OKLCH space, then computes each UI role's lightness from explicit constraints describing which foregrounds and panels need to contrast with which backgrounds. The implementation reverses a perceptual contrast algorithm and uses fitted polynomial coefficients, avoiding shipping the reference algorithm itself. At startup Pi asks the terminal for its colors and regenerates the theme, including when the terminal switches between light and dark. The article also explains why ANSI palettes are inconsistent and why simply reusing them can make complex terminal interfaces inaccessible.

**Why it matters:** A practical design pattern for personalization without surrendering legibility: inherit the user's color identity, but derive accessible role colors from the interface's contrast relationships. The author also calls out that contrast is perceptual and invites users to contribute data to an open survey.

**Caveat:** Contrast thresholds are an engineering approximation of perception; the article notes there is no open dataset that fully captures how real people perceive contrast on real screens.

**Embedded source:** [X post](https://x.com/mitsuhiko/status/2108527082070233261)
