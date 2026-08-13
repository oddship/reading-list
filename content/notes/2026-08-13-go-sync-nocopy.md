+++
title = "How Go's sync.noCopy works"
slug = "2026-08-13-go-sync-nocopy"
date = 2026-08-13T17:56:00+05:30
[taxonomies]
tags = ["systems", "developer-tools"]
[extra]
source_url = "https://func25.dev/posts/go-sync-nocopy/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "A concise example of Go using tooling conventions, not compiler magic, to encode a subtle API contract around values that must not be copied after first use."
saved_link = "https://func25.dev/posts/go-sync-nocopy/"
retrieval_note = "Direct fetch/browser were Cloudflare-blocked; article text was read through Jina Reader from the original URL."
+++
**Logged at IST:** 2026-08-13 17:56 IST

**What it is:** func25.dev explaining Go's internal `sync.noCopy` marker and how `go vet` detects accidental copies of sync-like structs.

**Gist:** `noCopy` is not compiler magic. It is an empty marker with two empty methods on its pointer receiver: `Lock` and `Unlock`. Those names make `*noCopy` satisfy `sync.Locker`, while the value `noCopy` does not. `go vet`'s `copylocks` checker uses that shape: while inspecting copied types, it recursively looks for a type whose pointer implements `sync.Locker` but whose value does not.

That is why `go build` will still accept copying a used `sync.Map`, but `go vet` can report `assignment copies lock value ... contains sync.noCopy`. The explicit marker also makes the warning describe the API contract rather than whichever internal mutex happens to exist, and it decouples detection from implementation details. The post points out a nice Go 1.24 edge case: a new defined type like `type LocalMutex sync.Mutex` loses `Mutex`'s methods, so the embedded `_ noCopy` marker fixes a false negative that method-based detection could miss.

The practical section is useful too. If you want this protection in your own package, define your own unexported `noCopy` marker and put `_ noCopy` in structs that must not be copied after first use. But remember the boundary: default `go test ./...` does not run the `copylocks` checker. Use `go vet ./...`, `go test -vet=copylocks ./...`, or `go test -vet=all ./...` if you want the warning in CI.

One small layout gotcha: `noCopy` has zero size, but a trailing zero-size field can still force padding. On a 64-bit platform, `{ n int64; _ noCopy }` can grow from 8 bytes to 16 bytes, while `{ _ noCopy; n int64 }` stays 8 bytes. Put the marker first.

**Newsletter angle:** Good systems-programming note: a tiny unexported marker encodes an API contract through tooling, not language semantics, and even its field position matters for layout.
