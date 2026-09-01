+++
title = "matklad on cancellation terminology and crash-only shutdown"
slug = "2026-09-01-matklad-cancelation-terminology"
date = 2026-09-01T21:29:00+05:30
[taxonomies]
tags = ["systems", "developer-tools"]
[extra]
source_url = "https://matklad.github.io/2026/08/31/cancelation-terminology.html"
source_type = "article"
newsletter_candidate = true
why_it_matters = "The post gives crisp names to three often-confused shutdown/cancellation ideas, then grounds the distinction in TigerBeetle's crash-only distributed-systems design."
saved_link = "https://x.com/TigerBeetleDB/status/2094709033139626008"
related_url = "https://x.com/TigerBeetleDB/status/2094709033139626008"
related_urls = ["https://github.com/tigerbeetle/tigerbeetle/blob/47aeb2212a255273dda508288412e537d11e4b7c/src/vsr/grid.zig#L589", "https://github.com/tigerbeetle/tigerbeetle/blob/47aeb2212a255273dda508288412e537d11e4b7c/src/state_machine.zig#L942", "https://github.com/tigerbeetle/tigerbeetle/blob/47aeb2212a255273dda508288412e537d11e4b7c/src/vsr/client.zig#L194-L203", "https://www.usenix.org/legacy/events/hotos03/tech/full_papers/candea/candea_html/index.html", "https://www.microsoft.com/en-us/research/wp-content/uploads/2017/06/paper-1.pdf", "https://pbs.twimg.com/media/HRHmv_vWMAAb7Sz.jpg?name=orig"]
retrieval_note = "FXTwitter extracted TigerBeetle's quote tweet, the linked matklad article, and one screenshot. The article was read directly; the screenshot shows the top of the post and the synchronous-cancellation example."
+++
**Logged at IST:** 2026-09-01 21:29 IST

**What it is:** matklad's short terminology note separating synchronous cancellation, asynchronous cancellation, and graceful shutdown, shared by TigerBeetle for its crash-only design angle.

**Gist:** The post's useful move is to stop using “cancellation” and “shutdown” as one blob. Synchronous cancellation is a control-flow operation: canceling means the task has already finished by the next line, like stack unwinding through exceptions, returned errors, RAII, `finally`, `with`/`try` resources, or `defer`.

Asynchronous cancellation is different: it is a communication protocol. One party asks another party to stop, but the work may still be running until it acknowledges and joins. matklad's examples are CPU thread-pool jobs and `io_uring` operations, where buffers and OS resources must remain owned until outstanding work is actually done.

Graceful shutdown sits higher up as an application-level service pattern: stop accepting new connections, keep serving existing ones, and let a load balancer route new work elsewhere. The TigerBeetle section then makes the distributed-systems point. `Grid.cancel` is asynchronous cancellation, `StateMachine.reset` is synchronous cancellation, and a client shutdown comment calls something “graceful shutdown” even though matklad now thinks that name is wrong. TigerBeetle itself is crash-only: if the system must survive SIGKILL and power loss anyway, then intentionally exercising crash paths can simplify implementation and improve coverage. Tail-latency tolerance also handles gray failures, because a very slow node and a crashed node can look equivalent from the outside.

**Newsletter angle:** Sharp distributed-systems terminology note: don't call every cleanup path “graceful shutdown”; distinguish stack unwinding, async resource ownership, and app-level connection draining.

{{ tweet(id="2094709033139626008", url="https://x.com/TigerBeetleDB/status/2094709033139626008") }}
