+++
title = "packetio pushes Go packet I/O toward line rate"
slug = "2026-09-01-packetio-go-dpdk-line-rate"
date = 2026-09-01T08:42:00+05:30
[taxonomies]
tags = ["developer-tools", "systems"]
[extra]
source_url = "https://github.com/atoonk/packetio"
source_type = "repo"
newsletter_candidate = true
why_it_matters = "packetio puts mlx5 Direct Verbs, DPDK, AF_XDP, and AF_PACKET behind one Go API, making line-rate packet generation and forwarding feel closer to normal Go code without hiding backend semantics."
saved_link = "https://x.com/atoonk/status/2094300060964237673"
related_url = "https://x.com/atoonk/status/2094300060964237673"
related_urls = ["https://gist.github.com/atoonk/63ad7ca0c7e4c0e0b167695b311a455e", "https://raw.githubusercontent.com/atoonk/packetio/main/README.md"]
retrieval_note = "FXTwitter extracted Andree Toonk's tweet and its two links. The DPDK example gist and packetio README/GitHub repo were read directly."
+++
**Logged at IST:** 2026-09-01 08:42 IST

**What it is:** packetio is a high-performance packet I/O library for Go. It offers one API over four ways of reaching a NIC: mlx5 Direct Verbs, DPDK, AF_XDP, and AF_PACKET.

**Gist:** The linked example is the sharp demo: a small Go program driving DPDK through packetio sends 64-byte packets at roughly 148M packets/sec on four queues and four cores, reaching 100G line rate on a ConnectX-6 Dx. The same loop can target other backends by changing the import and open call, so the app-level packet loop does not have to be rewritten for every NIC path.

The README makes the design tradeoff clear. packetio tries to hide the boring machinery of mempools, rings, UMEM, Direct Verbs queues, hugepages, and ownership handoff, but it does not pretend all backends are identical. Queue counts, frame ownership, steering, kernel coexistence, and unsupported capabilities remain explicit. That is the part that makes it systems-interesting rather than just a benchmark wrapper.

The performance tables are useful too: mlx5 and DPDK can transmit 64-byte 100G line rate in three cores; AF_XDP gets there with more queues and visible softirq cost; AF_PACKET is the portable floor. It is a concrete snapshot of where Go can sit in the packet-processing stack when the abstraction is built around the real hardware path.

**Newsletter angle:** Go packet processing is getting closer to line-rate NIC work while still feeling like a normal Go library, not a DPDK apprenticeship.

{{ tweet(id="2094300060964237673", url="https://x.com/atoonk/status/2094300060964237673") }}
