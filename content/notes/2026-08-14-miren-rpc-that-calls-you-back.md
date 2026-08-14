+++
title = "Miren's RPC that calls you back"
slug = "2026-08-14-miren-rpc-that-calls-you-back"
date = 2026-08-14T10:05:00+05:30
[taxonomies]
tags = ["systems", "developer-tools"]
[extra]
source_url = "https://miren.dev/blog/rpc-that-calls-you-back"
source_type = "article"
newsletter_candidate = true
why_it_matters = "A concrete object-capability RPC design for deployment and control-plane workflows where callbacks, progress updates, and subscriptions should be typed method calls instead of side-channel protocols."
saved_link = "https://miren.dev/blog/rpc-that-calls-you-back"
retrieval_note = "Article fetched directly from Miren and parsed from the page body."
+++
**Logged at IST:** 2026-08-14 10:05 IST

**What it is:** Miren engineering post by Evan Phoenix and Paul Hinze on the RPC layer they built for typed two-way calls across CLI, control plane, and runtime components.

**Gist:** Miren argues that a lot of deployment-platform work does not fit cleanly into one request and one response. A deploy has progress updates, health checks, subscriptions, and callbacks from a server to an ephemeral client. Polling, webhooks, or a separate stream work, but they make the request/response model leak.

Their answer is object-capability RPC. In the IDL, parameters and results can be interfaces, not just structs and scalars. Passing an interface does not serialize object state. It creates a live typed capability, so the receiver can call methods on the object you passed. The example is a client handing the server an `UpdateReceiver`; the server later calls `recv.update(reading)` over the same session.

The post is especially clear on why they did not just use gRPC bidirectional streams. gRPC gives two typed message channels, but not a typed callable object passed as an argument. If the server needs to invoke several methods on something the client owns, you end up building a small dispatch protocol inside the stream. Streams also do not acknowledge peer handling: a send can complete once bytes are buffered, not once the other side has received and acted on the message. Miren wants capability calls to be real calls, where completion is the acknowledgment.

The wire shape is pragmatic. Unary calls are CBOR bodies sent as HTTP/3 `POST /_rpc/call/{oid}/{method}`. Calls that pass capabilities use WebTransport with HTTP `CONNECT /_rpc/callstream/{oid}/{method}`, giving bidirectional QUIC streams inside one session. Generated Go code turns YAML schemas into interfaces, typed clients, adapters, dispatch tables, random 16-byte object IDs, and ref/deref lifetime tracking for capabilities that outlive the original call.

**Newsletter angle:** Useful systems-design piece: object-capability RPC can make callback-heavy control-plane workflows feel like normal APIs, while honestly accepting that you now own transport behavior, reconnection bugs, and distributed capability lifetime.
