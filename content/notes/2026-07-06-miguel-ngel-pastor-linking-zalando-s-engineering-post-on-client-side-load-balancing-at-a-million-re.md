+++
title = "Miguel Ángel Pastor linking Zalando’s engineering post on client-side load balancing at a million requests..."
slug = "2026-07-06-miguel-ngel-pastor-linking-zalando-s-engineering-post-on-client-side-load-balancing-at-a-million-re"
date = 2026-07-06T00:07:00+05:30
[taxonomies]
tags = ["developer-tools", "systems"]
[extra]
source_url = "https://x.com/i/status/2073796043230052472"
source_type = "x-post"
newsletter_candidate = true
why_it_matters = "own the routing decision in-process when cache-sensitive fanout paths make shared infra the bottleneck"
saved_link = "https://x.com/i/status/2073796043230052472"
+++
**What it is:** Miguel Ángel Pastor linking Zalando’s engineering post on client-side load balancing at a million requests per second

**Gist:** argues high-fanout internal traffic benefited from moving load balancing into the client process to preserve cache locality, improve debuggability, and avoid shared-ingress distortions; highlights safety work like bounded-load routing and rollout fade-in

**Newsletter angle:** own the routing decision in-process when cache-sensitive fanout paths make shared infra the bottleneck

**Retrieval note:** extracted cleanly via FXTwitter API; card points to the Zalando engineering article

**Note:** overlaps with the same Zalando piece already logged earlier via Werner Vogels on 2026-07-02, but this direct share is now recorded too
