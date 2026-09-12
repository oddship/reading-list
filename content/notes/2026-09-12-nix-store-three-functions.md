+++
title = "A Nix store is three functions"
slug = "2026-09-12-nix-store-three-functions"
date = 2026-09-12T22:55:00+05:30
[taxonomies]
tags = ["developer-tools", "systems"]
[extra]
source_url = "https://fzakaria.com/2026/09/11/a-nix-store-is-three-functions"
source_type = "blog-post"
newsletter_candidate = true
why_it_matters = "Farid Zakaria reduces Nix binary caches to a tiny content-addressed interface, which makes it obvious why static hosts, package registries, OCI, DNS, or stranger media can act as store backends while Nix keeps integrity checks local."
saved_link = "https://x.com/fmzakari/status/2098648298236313942"
related_url = "https://fzakaria.com/2026/09/04/any-nix-package-live-in-your-browser"
related_urls = ["https://github.com/fzakaria/trynix/tree/main/site/examples/cache", "https://github.com/tomberek/github-store", "https://github.com/EphraimSiegfried/gachix", "https://github.com/cmspam/nixcache-oci", "https://www.npmjs.com/package/@fzakaria/hello-nix-cache"]
retrieval_note = "Tweet extracted via FXTwitter; linked Farid Zakaria blog post fetched directly; related trynix note already exists in the reading-list site."
+++

**Logged at IST:** 2026-09-12 22:55 IST

**What it is:** Farid Zakaria follows up on trynix by showing that a Nix binary cache is just a small static-file interface, not something intrinsically tied to the official Nix cache infrastructure.

**Gist:** To act as a remote Nix store, a service only needs to answer three requests: `nix-cache-info`, a `<store-hash>.narinfo` metadata file, and the compressed archive named by the narinfo's `URL` field. GitHub Pages works for trynix because it is a static file server with permissive CORS; GitHub Releases can work too, with small narinfo URL adjustments.

The integrity model is the useful bit. Nix does not need to trust the transport because the narinfo signature covers the store path, NAR hash, NAR size, and references, while the fetched archive is checked against the NAR hash after decompression. The `URL` itself is not covered, so the archive can come from another host, protocol, or backing medium and still validate if the content matches.

Zakaria surveys alternative stores, including git object databases, DNS TXT records, pastebins, OCI registries, and even video-encoded storage. The worked example uses npm: `nix copy --to file://` emits the cache shape, `npm publish` turns it into a package, and `unpkg.com/@fzakaria/hello-nix-cache@latest/` can be passed to `nix copy --from` as a substituter.

The npm trick also shows registry semantics leaking into build distribution. Dist-tags such as `latest`, `staging`, and `production` become channel-like pointers, while immutable package versions can pin exact closures. The catch is duplication: npm publishes whole tarballs, so shared dependencies such as glibc get uploaded repeatedly unless each store path becomes its own package plus an index.

**Newsletter angle:** This is a clean mental model for Nix caches: content-addressed package distribution can ride on almost any dumb storage layer, as long as the client keeps verification strict. That opens fun demos like browser Nix, but also raises etiquette and ecosystem-boundary questions when public registries are repurposed as binary caches.
