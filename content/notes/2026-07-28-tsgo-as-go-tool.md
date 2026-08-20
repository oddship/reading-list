+++
title = "Running TypeScript's Go port as a Go tool"
slug = "2026-07-28-tsgo-as-go-tool"
date = 2026-07-28T20:59:00+05:30
[taxonomies]
tags = ["developer-tools", "systems"]
[extra]
source_url = "https://x.com/its_bvisness/status/2081963692300612066"
source_type = "x-post"
newsletter_candidate = true
why_it_matters = "A small but telling developer-tools detail: TypeScript's Go-native port can be pinned and invoked through Go's own tool dependency flow."
saved_link = "https://x.com/i/status/2081963692300612066"
related_url = "https://github.com/microsoft/typescript-go"
retrieval_note = "Grounded from FXTwitter text, attached screenshot OCR, and the public microsoft/typescript-go repository metadata/go.mod."
+++
**Logged at IST:** 2026-07-28 20:59 IST

**What it is:** Ben Visness points out that Microsoft’s Go-native TypeScript port can be added to a `go.mod` file and run with `go tool tsgo`.

**Gist:** The screenshot shows this Go tool directive:

```go
tool github.com/microsoft/typescript-go/cmd/tsgo
```

The practical point is that a Go project can pin and invoke `tsgo` through Go’s own tool dependency workflow, without installing npm just to run TypeScript. The `microsoft/typescript-go` repository describes itself as the staging repo for the native port of TypeScript, and its own `go.mod` is already structured as a normal Go module.

**Newsletter angle:** Small developer-tools item, but a nice one: language tooling is becoming portable across package-manager boundaries. TypeScript-as-a-Go-tool makes TS checking feel like normal Go project infrastructure instead of a separate Node/npm island.

**Retrieval note:** Grounded from FXTwitter text, attached screenshot OCR, and the public `microsoft/typescript-go` repository metadata/go.mod.

## Embedded source

{{ tweet(id="2081963692300612066", url="https://x.com/its_bvisness/status/2081963692300612066") }}
