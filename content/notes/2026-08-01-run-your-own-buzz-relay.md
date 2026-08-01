+++
title = "Running your own Buzz relay makes self-hosting concrete"
slug = "2026-08-01-run-your-own-buzz-relay"
date = 2026-08-01T11:38:00+05:30
[taxonomies]
tags = ["agents", "ai-infra", "developer-tools"]
[extra]
source_url = "https://engineering.block.xyz/blog/run-your-own-buzz-relay"
source_type = "article"
saved_link = "https://engineering.block.xyz/blog/run-your-own-buzz-relay"
newsletter_candidate = true
why_it_matters = "The post turns Buzz's self-hosted agent workspace pitch into the operational details that matter: keys, relay identity, URL identity, membership, storage, TLS, upgrades, and backups."
retrieval_note = "Direct page HTML was accessible and article text was extracted from the Block Engineering page."
related_url = "https://reading-list.oddship.net/notes/2026-07-22-buzz-channel-driven-agent-workspace/"
project_url = "https://buzz.xyz"
repo_url = "https://github.com/block/buzz"
+++
**Logged at IST:** 2026-08-01 11:38 IST

**What it is:** Block Engineering's practical guide to running a Buzz relay yourself, first on a laptop with Docker Compose and then on Railway or a VPS.

**Gist:** This is the operational counterpart to the Buzz launch post. The relay is a single Rust binary that serves the WebSocket relay, REST API, and web UI, backed by Postgres, Redis, and S3-compatible object storage. The guide walks through the production Compose bundle, local startup, `buzz-admin` membership management, and joining the relay from Buzz Desktop.

The important part is identity. A Buzz relay has its own Nostr signing key, while the owner has a separate public key. The relay advertises its pubkey and signs membership and service events with it, so rotating that key is not a casual secret-refresh operation. The `RELAY_URL` also becomes part of the community identity: scheme, host, and port must match exactly, and changing from a local URL to a public domain creates a fresh community boundary.

The public-hosting section makes the custody tradeoff explicit. Railway can provision the relay, Postgres, Redis, object storage, secrets, migrations, and a public domain, but the relay signing key lives in Railway's variable store unless you copy it out and back it up. The VPS path keeps the same Compose shape, adds Caddy for HTTPS, and calls out the practical backup set: relay private key, Postgres, object-store bucket, git volume, and owner key.

**Newsletter angle:** Good follow-up to the earlier Buzz note. The launch pitch was about channels as a control plane for people and agents; this one shows what "self-hostable" really requires once messages, membership, media, and signed relay identity are yours to operate.
