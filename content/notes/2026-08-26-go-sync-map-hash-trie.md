+++
title = "Go's sync.Map moves to a hash trie"
slug = "2026-08-26-go-sync-map-hash-trie"
date = 2026-08-26T16:33:00+05:30
[taxonomies]
tags = ["developer-tools", "systems"]
[extra]
source_url = "https://victoriametrics.com/blog/go-sync-map-hash-trie/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "The public sync.Map API stayed stable, but the implementation changed enough to revisit its real performance, memory, and concurrency tradeoffs."
saved_link = "https://x.com/func25/status/2092537534119354879"
related_url = "https://x.com/func25/status/2092537534119354879"
retrieval_note = "FXTwitter extraction resolved the VictoriaMetrics article. The article HTML was read directly, and the X post image was inspected; it shows sync.Map using roughly 3-5x the memory of a plain map across tested entry counts."
+++
**Logged at IST:** 2026-08-26 16:33 IST

**What it is:** Phuong Le's VictoriaMetrics walkthrough of Go's hash-trie-backed `sync.Map` implementation.

**Gist:** The visible API is still the familiar `Load`, `Store`, `Delete`, `LoadOrStore`, `CompareAndSwap`, `Range`, and `Clear`. Underneath, Go moved `sync.Map` to an internal `HashTrieMap`: keys are hashed, the hash is consumed in 4-bit chunks, each indirect node has 16 child slots, and full hash collisions fall back to overflow entries.

The concurrency model is the useful part. `Load` can walk atomic child pointers without taking node mutexes. Writers search without a lock, then lock only the immediate parent indirect node, recheck that the slot is still valid, and publish a replacement entry or subtree with an atomic pointer store. That lets writes to different parts of the trie proceed independently, but it also means the implementation allocates more and has more machinery than a plain map.

The practical guidance stays conservative. `sync.Map` is safe for concurrent calls, but it is not a general replacement for `map[K]V` plus `sync.RWMutex`. It stores keys and values as `any`, gives no snapshot guarantee for `Range`, cannot make multi-key updates atomic, and can use several times more memory than a plain map. It is most worth considering for write-once/read-many maps or workloads where different goroutines mostly touch different keys and a single mutex is a measured bottleneck.

**Newsletter angle:** Good Go/systems item: the standard API did not change, but the implementation shift explains when `sync.Map` wins and why “concurrent-safe” alone is not enough reason to use it.

{{ tweet(id="2092537534119354879", url="https://x.com/func25/status/2092537534119354879") }}
