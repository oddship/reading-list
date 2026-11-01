+++
title = "Lean 4 reaches the top of the $12 Server Challenge"
slug = "2026-11-01-lean-4-tops-the-12-server-challenge"
date = 2026-11-01T12:59:00+05:30
[taxonomies]
tags = ["systems", "developer-tools"]
[extra]
source_url = "https://benchmarks.arjaythedev.com/12-dollar-server"
source_title = "The $12 Server Challenge leaderboard"
source_type = "benchmark"
saved_link = "https://x.com/hargup13/status/2116422880221409621?a=4KJXEmcDhhZ3UtOxUew&s=35"
saved_title = "Harsh Gupta on Lean 4's challenge result"
related_url = "https://github.com/arjaythedev/twelve-dollar-server-challenge"
related_title = "Challenge specification and source repository"
related_urls = ["https://benchmarks.arjaythedev.com/12-dollar-server/leaderboard/lean-derive-hargup"]
related_titles = ["Lean 4 submission results"]
newsletter_candidate = true
why_it_matters = "A striking workload-specific result: Lean 4, compiled to C and using io_uring, ties for the leaderboard's top held-user count on a 1-vCPU, 2-GB machine. The shared challenge methodology makes the result more interpretable than an isolated language-performance claim, while still limiting what it says about general-purpose performance."
retrieval_note = "Read the benchmark leaderboard and methodology, challenge repository, and extracted the shared X post via FXTwitter. The post's 92-second video was not inspected; the note relies on the leaderboard for benchmark details."
+++

Harsh Gupta's Lean 4 submission reached the top held-user count in the $12 Server Challenge. The leaderboard reports **280,000 users held for five minutes**, 26,683 requests per second, p95 latency of 141 ms, p99 of 316 ms, and 0% errors for `lean-derive-hargup`, described as Lean 4 compiled to C with `io_uring`.

This is not a standalone win over every systems language: Mojo and Objective-C also reached 280,000 users, while Rust, C, and handwritten x86-64 assembly entries on this leaderboard held fewer. The challenge is a particular SQLite-backed feed API on a 1-vCPU/2-GB Ubuntu VPS, with a defined interactive load mix and pass thresholds; it is useful evidence about this workload and implementation, not a universal ranking of languages. The organizer documents the test setup and scoring protocol on the [leaderboard](https://benchmarks.arjaythedev.com/12-dollar-server) and the [challenge repository](https://github.com/arjaythedev/twelve-dollar-server-challenge).

{{ tweet(id="2116422880221409621", url="https://x.com/hargup13/status/2116422880221409621") }}
