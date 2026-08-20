+++
title = "Git at Any Scale"
slug = "2026-08-19-git-at-any-scale-cursor"
date = 2026-08-19T09:51:00+05:30
[taxonomies]
tags = ["systems", "ai-infra", "developer-tools"]
[extra]
source_url = "https://cursor.com/blog/git-at-any-scale"
source_type = "article"
newsletter_candidate = true
why_it_matters = "Git hosting is becoming AI infrastructure: agents create more repositories, pushes, clones, and CI pressure, so version-control storage needs database-like durability and scaling properties."
saved_link = "https://x.com/i/status/2089758713183613266"
related_url = "https://x.com/cursor_ai/status/2089758713183613266"
retrieval_note = "X post extracted via FXTwitter. The linked Cursor article HTML was read directly."
+++
**Logged at IST:** 2026-08-19 09:51 IST

**What it is:** Vicent Martí's Cursor post on the storage system behind Origin, Cursor's Git hosting product.

**Gist:** The useful framing is that Git hosting is hard because Git was designed so every repository copy is equivalent. That makes the local developer workflow great, but it makes server-side scaling awkward: packfiles are optimized for local disk and Git clients still expect packfiles over the network.

The post walks through prior approaches. Object-level distributed stores map nicely to content-addressed Git objects, but DAG walks become round-trip-heavy and clone still needs packfiles. Distributed filesystems preserve the normal Git layout but run into filesystem semantics and performance issues. GitHub's Spokes-style design works better by keeping real Git repos on local NVMe and replicating packfiles consistently, but its 3PC shape struggles when repositories need many replicas or when agents create many small, mostly idle repositories.

Cursor's Continuity keeps the good part, normal Git repositories on fast local disks, but moves truth into an S3-backed write-ahead log. Pushes are persisted as WAL entries before acknowledgement, visibility is controlled through a WAL index, and any node can materialize a repository from the WAL. Local repositories become warm cache rather than pets. S3 compare-and-swap gives linearizable pushes, while fully consistent replicas scale read-heavy Git operations, API reads, UI interactions, and agent workflows.

**Newsletter angle:** Strong systems design read on treating source control like a database: WAL as truth, local disk as cache, linearizable writes, compaction as part of replication, and AI-agent traffic changing both the floor and ceiling of Git infrastructure.

## Embedded source

{{< tweet id="2089758713183613266" url="https://x.com/i/status/2089758713183613266" >}}
