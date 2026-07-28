+++
title = "Ghostty's 8-byte terminal grid cells"
slug = "2026-07-28-ghostty-alacritty-terminal-grid-memory"
date = 2026-07-28T13:27:00+05:30
[taxonomies]
tags = ["systems", "developer-tools"]
[extra]
source_url = "https://x.com/mitchellh/status/2081833183835013618"
source_type = "x-post"
newsletter_candidate = true
why_it_matters = "A concrete example of reducing memory by designing data structures around the common terminal-cell cases instead of paying per-cell costs for rare state."
saved_link = "https://x.com/mitchellh/status/2081833183835013618?s=20"
related_url = "https://x.com/mitchellh/status/2081788657078505732"
retrieval_note = "Grounded from FXTwitter text for the post and quoted context."
+++
**Logged at IST:** 2026-07-28 13:27 IST

**What it is:** Mitchell Hashimoto explains why Ghostty/libghostty's terminal grid is much more memory-efficient than Alacritty's terminal crate in his benchmark.

**Gist:** The core comparison is simple: Alacritty stores 32 bytes of metadata per row and 24 bytes per cell, while Ghostty represents each row and each cell in 8 bytes. Mitchell says around 95% of the uncompressed memory-usage difference comes from a few data-structure choices.

Ghostty does not store the full style beside every cell. It stores a 16-bit style ID and dedupes styles in a look-aside, reference-counted hash table. That matches the distribution Mitchell calls out: most cells are unstyled, styled cells often share styles, and shared styles usually appear in runs.

For text content, Ghostty stores single codepoints inline and moves multi-codepoint graphemes into a look-aside table backed by a bitmap-tracked chunk allocator. A 2-bit tag in the packed 64-bit cell marks the content shape. The 16-bit limits are handled by keeping the grid as a linked list of contiguous ~400KB chunks, each limited to 2^16 values before moving to the next chunk.

**Newsletter angle:** Good systems note on making the hot representation fit the domain. The win is not just compression, it is avoiding persistent per-cell costs for rare styles and rare grapheme cases.

**Retrieval note:** Grounded from FXTwitter text for the post and quoted context. The quoted post says Ghostty's scrollback compression is on by default, the benchmark uses the same Rust binary to compare libghostty and Alacritty terminal state, and a longer blog post may follow.
