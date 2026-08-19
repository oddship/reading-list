+++
title = "TigerBeetle object storage clients vs simples3"
slug = "2026-07-27-tigerbeetle-object-storage-vs-simples3"
date = 2026-07-27T04:31:00+05:30
[taxonomies]
tags = ["systems", "developer-tools"]
[extra]
source_url = "https://x.com/TigerBeetleDB/status/2080684469099401247"
source_type = "x-post"
newsletter_candidate = true
why_it_matters = "Useful systems item because it separates small dependency-free cloud clients from deterministic runtime-integrated infrastructure clients."
saved_link = "https://x.com/TigerBeetleDB/status/2080684469099401247"
related_url = "https://github.com/rhnvrm/simples3"
retrieval_note = "Grounded from the X thread metadata, visible YouTube page metadata/chapter list, and rhnvrm/simples3 source at commit 57fa0ec. Full YouTube transcript extraction was blocked by YouTube bot/cloud-IP checks, so this is not a transcript-grounded video summary."
+++
**Logged at IST:** 2026-07-27 04:31 IST

**What it is:** TigerBeetle shared notes around its custom object-storage clients, and I compared that design direction with `rhnvrm/simples3`.

**Gist:** The shared instinct is anti-SDK: avoid a large vendor dependency tree, understand the REST/signing surface directly, and keep the client small enough to reason about. But the two implementations optimize for different worlds.

`simples3` is a pragmatic Go S3 REST client. It is stdlib-only, supports SigV4, custom endpoints, bucket/object/list/multipart/tagging/versioning/SSE/IAM features, and exposes a straightforward blocking `net/http` API. It is small and useful when Go's normal HTTP stack, goroutines, and buffering behavior are acceptable.

TigerBeetle's claim is stricter. Ordinary object-storage SDKs can block, spawn threads, allocate, pull in dependencies, and hide runtime behavior. TigerBeetle says its AWS/GCP/Azure clients fit its single-threaded deterministic style: static allocation, zero-copy, fully async I/O, and deterministic simulation of DNS/TLS/HTTP/S3.

The concrete gap is not “custom S3 client” versus “SDK.” It is application-level convenience versus systems-runtime predictability. `simples3` reads whole payloads in several paths, uses `http.Client.Do`, and supports goroutine-based multipart concurrency. That is idiomatic Go. It is also not the TigerStyle bar of no hidden blocking, no scheduler dependency, static allocation, and deterministic failure simulation.

**Newsletter angle:** Good systems note on a spectrum: dependency-light application library at one end, deterministic runtime-integrated cloud client at the other.

**Retrieval note:** Grounded from the X thread metadata, visible YouTube page metadata/chapter list, and `rhnvrm/simples3` source at commit `57fa0ec`. Full YouTube transcript extraction was blocked by YouTube bot/cloud-IP checks, so this is not a transcript-grounded video summary.

## Embedded source

{{<tweet id="2080684469099401247" url="https://x.com/TigerBeetleDB/status/2080684469099401247"/>}}
