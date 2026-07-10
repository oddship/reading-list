+++
title = "cursed code"
slug = "2026-06-26-cursed-code"
date = 2026-06-26T19:23:00+05:30
[taxonomies]
tags = []
[extra]
source_url = "https://x.com/i/status/2070308475603951723"
source_type = "x-post"
newsletter_candidate = true
why_it_matters = "delightful example of language/compiler design used for computational theater, more about quines, staged codegen, and expressive weirdness than practical software"
saved_link = "https://x.com/i/status/2070308475603951723"
+++
**What it is:** Tim McNamara sharing an IOCCC-winning “cursed code” project where Pong advances by rewriting its own source each frame

**Gist:** the linked repo, `uellenberg/Insert`, is a small language for self-modifying code; programs can access their own source as string fragments, overwrite marked values, print the next version of themselves, and in the Pong demo each run emits the source for the next frame before recompiling

**Newsletter angle:** “playful programming systems” / self-modifying code as art rather than anti-pattern
