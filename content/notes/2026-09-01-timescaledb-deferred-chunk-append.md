+++
title = "TimescaleDB defers chunk expansion for LIMIT queries"
slug = "2026-09-01-timescaledb-deferred-chunk-append"
date = 2026-09-01T08:54:00+05:30
[taxonomies]
tags = ["systems", "developer-tools"]
[extra]
source_url = "https://www.tigerdata.com/blog/faster-planning-for-limit-queries-on-hypertables"
source_type = "article"
newsletter_candidate = true
why_it_matters = "DeferredChunkAppend is a clean database planning lesson: a LIMIT can make execution cheap while planning still scales with partitions, so TimescaleDB moves chunk expansion to execution where the limit can stop it early."
saved_link = "https://x.com/michaelfreedman/status/2094531186643402933"
related_url = "https://x.com/michaelfreedman/status/2094531186643402933"
retrieval_note = "FXTwitter extracted Mike Freedman's note tweet and linked Tiger Data article. The Tiger Data engineering post was read directly."
+++
**Logged at IST:** 2026-09-01 08:54 IST

**What it is:** Tiger Data's engineering note on `DeferredChunkAppend`, a TimescaleDB 2.30 optimization for `ORDER BY time LIMIT` queries on hypertables with many chunks.

**Gist:** The subtle bug is not query execution, but query planning. A latest-row query such as `SELECT * FROM metrics WHERE device = 'D001' ORDER BY time DESC LIMIT 1` should usually read one recent chunk. Existing `ChunkAppend` execution already visits chunks in order and stops once the limit is satisfied. But before execution can do that, the planner still expands the hypertable into thousands of chunk scans, opens and locks chunks, reads statistics, and builds the append plan.

`DeferredChunkAppend` changes the plan shape. Instead of expanding every chunk during planning, it leaves the hypertable as a single custom scan node and fetches chunks lazily during execution, in the order the query requires. Each chunk is queried normally, but the `LIMIT` can stop the process after the first few chunks.

The reported numbers are stark. On 10,000 chunks with PostgreSQL 18, hypertable planning time drops from 202 ms with `ChunkAppend` to 0.013 ms with `DeferredChunkAppend`; on PostgreSQL 17 it drops from 3660 ms to 0.013 ms. The broader lesson is that `LIMIT` bounds what comes back, not what has to be planned, unless the planner itself is shaped to defer work.

**Newsletter angle:** Database performance is often hidden in planning, not execution: partition-scale systems need plan shapes that avoid paying per-partition costs for point-like queries.

{{ tweet(id="2094531186643402933", url="https://x.com/michaelfreedman/status/2094531186643402933") }}
