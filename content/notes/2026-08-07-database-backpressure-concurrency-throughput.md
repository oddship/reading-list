+++
title = "Database backpressure beats unlimited concurrency"
slug = "2026-08-07-database-backpressure-concurrency-throughput"
date = 2026-08-07T21:46:00+05:30
[taxonomies]
tags = ["systems", "ai-infra"]
[extra]
source_url = "https://planetscale.com/blog/concurrency-vs-throughput-vitess-mysql"
source_type = "article"
newsletter_candidate = true
why_it_matters = "A clean production database story showing why higher admitted concurrency can reduce throughput, and why bounded queueing/backpressure can be safer than raising limits until errors disappear."
saved_link = "https://x.com/i/status/2085748307322909157"
related_url = "https://x.com/samlambert/status/2085748307322909157"
related_urls = ["https://vitess.io/docs/reference/programs/vttablet/", "https://www.perfdynamics.com/Manifesto/USLscalability.html", "https://planetscale.com/docs/postgres/connecting/pgbouncer"]
retrieval_note = "Extracted Sam Lambert’s X post via FXTwitter and read the linked PlanetScale article directly."
+++
**Logged at IST:** 2026-08-07 21:46 IST

**What it is:** Sam Lambert’s X post recommending Liz van Dijk’s PlanetScale engineering post on concurrency, throughput, Vitess, and MySQL.

**Gist:** PlanetScale describes a production MySQL database that melted down for sixteen minutes after a batch job opened a transaction against a hot table, took row locks, and held them without committing. The obvious story would be “lock contention,” but the useful point is subtler. Many reads were not waiting on the locked rows. They were doing snapshot reads through an increasingly long version history, blowing past execution ceilings, getting retried, and piling more work into InnoDB.

The migration context mattered. The workload had previously sat behind Cloud SQL managed connection pooling, which capped concurrent statements and queued the rest. On PlanetScale, Vitess vttablet had a transaction pool that failed requests when full. The first mitigation raised the pool cap to roughly ten thousand and increased the timeout because that made errors disappear. It also removed an important backpressure point, allowing the database to admit far more concurrent work than it could process efficiently.

The post frames this with Little’s Law and Gunther’s Universal Scalability Law. More work in flight only increases throughput while per-request time stays stable. Once requests start making each other slower, the coherency term grows roughly with pairs of requests. Past that point, more parallelism can cause retrograde scaling: admitting more work lowers total throughput.

The fix was intentionally boring: reduce the Vitess transaction pool size back toward the old thread-pool scale, and queue at the pool with a bounded timeout instead of admitting everything or erroring immediately. In a later burst, the pool saw tens of thousands of slot requests per second while keeping MySQL execution concurrency under a few hundred statements, no meaningful error spike, and steady query throughput.

**Newsletter angle:** Strong backpressure example. For contended workloads with hot rows, long transactions, `SELECT ... FOR UPDATE`, counters, balances, or queues, the answer is not always “raise the limit.” Sometimes the fastest way to make a busy database do more total work is to let less happen at once.

## Embedded source

{{ tweet(id="2085748307322909157", url="https://x.com/i/status/2085748307322909157") }}
