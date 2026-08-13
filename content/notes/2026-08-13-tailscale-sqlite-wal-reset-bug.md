+++
title = "How Tailscale tracked down the SQLite WAL-Reset bug"
slug = "2026-08-13-tailscale-sqlite-wal-reset-bug"
date = 2026-08-13T08:09:00+05:30
[taxonomies]
tags = ["systems", "ai-infra"]
[extra]
source_url = "https://tailscale.com/blog/sqlite-wal-reset-bug"
source_type = "article"
newsletter_candidate = true
why_it_matters = "A rare production-scale debugging story: Tailscale was using boring SQLite in a documented but non-standard way, hit a 16-year-old WAL checkpoint race, and helped SQLite ship a fix. The lesson is about operational paths, observability, recovery design, and open-source support contracts."
saved_link = "https://tailscale.com/blog/sqlite-wal-reset-bug"
related_urls = ["https://sqlite.org/wal.html#the_wal_reset_bug", "https://sqlite.org/changes.html#version_3_51_3", "https://sqlite.org/staleexpridx.html", "https://sqlite.org/src/info/7168988acbec2d8d", "https://sqlite.org/src/file/ext/misc/tmstmpvfs.c?proof=394548354"]
retrieval_note = "Article fetched directly from Tailscale and cross-checked through Jina reader output for clean text."
+++
**Logged at IST:** 2026-08-13 08:09 IST

**What it is:** Tailscale’s postmortem on months of control-plane instability caused by a rare SQLite WAL checkpoint race, and the follow-on false alarm from stale expression indexes.

**Gist:** Tailscale runs its control plane as isolated shards, each backed by a single-writer SQLite database. That architecture was supposed to be boring, but their backup pipeline started finding corrupted SQLite files. Over six months they saw 19 corruption incidents, causing shard-local control-plane downtime and occasional loss of recent configuration metadata. The bug had no easy reproduction, so they added live forensic telemetry, built transaction replay logs, contracted directly with the SQLite developers, and progressively ruled out their own misuse theories.

The key clue was that replay logs sometimes showed committed writes becoming invisible to later transactions. SQLite’s developers built a `tmstmpvfs` tracing shim, which exposed a rare race between a checkpoint and a write transaction. Under a precise timing window, checkpointing could believe pages had been copied from the WAL into the main DB when they had not, leaving references to missing pages and corrupting the database. SQLite named it the “WAL-Reset bug”; it had existed for at least 16 years, but Tailscale’s aggressive manual checkpointing made the rare path likely enough to surface.

There is a second useful lesson in the rollout. SQLite 3.52.0 fixed the race, but also changed floating-point conversion behavior enough to make Tailscale’s expression indexes look corrupt under `PRAGMA integrity_check`. SQLite withdrew 3.52.0 and shipped 3.51.3 with only the WAL fix; Tailscale changed timestamp precision to integer seconds, and SQLite later added self-healing for stale expression indexes.

**Newsletter angle:** “Boring technology” is safest on the well-trodden path. Tailscale’s setup was public and supported, but manual, aggressive checkpoints moved them into a rare operational corner where only production-scale forensics and upstream SQLite expertise could close the loop.
