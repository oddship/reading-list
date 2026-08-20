+++
title = "Poisoned Postgres Connection Pools"
slug = "2026-08-19-postgres-poisoned-connection-pools"
date = 2026-08-19T09:33:00+05:30
[taxonomies]
tags = ["systems", "developer-tools"]
[extra]
source_url = "https://planetscale.com/blog/postgres-poisoned-connection-pools"
source_type = "article"
newsletter_candidate = true
why_it_matters = "Connection pooling bugs often look like database failures, but the real issue can be leaked session state moving between clients through PgBouncer."
saved_link = "https://x.com/i/status/2089776662791786675"
related_url = "https://x.com/BenjDicken/status/2089776662791786675"
retrieval_note = "X post extracted via FXTwitter. The linked PlanetScale article HTML was read directly."
+++
**Logged at IST:** 2026-08-19 09:33 IST

**What it is:** PlanetScale's debugging note on poisoned Postgres connection pools, shared by Ben Dicken.

**Gist:** The failure mode is simple and nasty: PgBouncer transaction pooling reuses underlying database connections across clients. If one client leaves session state behind, the next client can inherit it.

The concrete example is read-only state. Application code used `SET SESSION CHARACTERISTICS AS TRANSACTION READ ONLY` for a read-only transaction, but that changed the session rather than only the transaction. Later requests reused that same underlying connection and started failing writes with Postgres error `25006` or `ERROR: cannot execute INSERT in a read-only transaction`.

The immediate antidote is to reset affected pooled connections with `DISCARD ALL` or kill/reset the pooler sessions. The durable fix is in application behavior: avoid session-level flags through PgBouncer, prefer transaction-scoped read-only settings with strict cleanup and timeouts, or route read traffic to replicas instead.

**Newsletter angle:** Useful database reliability story. Connection pools are not transparent plumbing; they preserve enough state that bugs in transaction boundaries, cleanup paths, and ORM behavior can escape one request and poison the next.

## Embedded source

{{ tweet(id="2089776662791786675", url="https://x.com/i/status/2089776662791786675") }}
