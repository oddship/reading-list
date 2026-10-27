+++
title = "Egres: a new Postgres-compatible database"
slug = "2026-10-27-egres-postgres-compatible-database"
date = 2026-10-27T21:30:00+05:30
[taxonomies]
tags = ["systems", "developer-tools"]
[extra]
source_url = "https://manishrjain.com/egres/"
source_title = "Egres: A Postgres-compatible database for heavy, multi-tenant workloads"
source_type = "article"
saved_link = "https://x.com/manishrjain/status/2115100275333800108"
saved_title = "Manish R Jain announces Egres"
related_urls = ["https://github.com/manishrjain/egres", "https://egresql.io/docs/benchmarks/", "https://egresql.io/docs/quickstart/"]
related_titles = ["Egres source repository", "Egres benchmark methodology", "Egres quickstart"]
newsletter_candidate = true
why_it_matters = "A ground-up database design aimed at combining Postgres wire compatibility with multi-tenant resource metering, an LSM-forest storage engine, object-storage support, and zero-copy branching. The author publishes detailed comparative benchmarks, while noting the current release is single-node with basic query support."
+++

Manish Jain introduces Egres, a new database that speaks the Postgres protocol but is not a Postgres fork. Its design targets heavy, multi-tenant workloads: a coroutine-based execution system meters CPU, memory, and disk I/O per query and tenant; its zdb storage engine is an LSM forest; and it supports local or object storage, Raft-based replication, and instant zero-copy database or table branches.

The author reports results from a 600-million-row comparison with Postgres 18, including lower disk use and faster results on several read queries. These are the author’s benchmark results, not an independent evaluation; the linked methodology page describes the setup. The trade-offs are material: the current release is single-node, query support is basic (equality predicates, no joins), and its load rate was slower in the reported test. The post says multi-node clustering is planned for a later release.

{{ tweet(id="2115100275333800108", url="https://x.com/manishrjain/status/2115100275333800108") }}