+++
title = "Appwrite rewrites its CLI from TypeScript to Go"
slug = "2026-08-13-appwrite-cli-go-rewrite"
date = 2026-08-13T09:59:00+05:30
[taxonomies]
tags = ["developer-tools", "systems"]
[extra]
source_url = "https://appwrite.io/blog/post/rewriting-the-appwrite-cli-in-go"
source_type = "article"
newsletter_candidate = true
why_it_matters = "A concrete developer-tools rewrite story where the useful result is less about language ideology and more about startup time, install surface, memory use, release targets, and compatibility discipline."
saved_link = "https://x.com/i/status/2087622396769657336"
related_url = "https://x.com/rseroter/status/2087622396769657336"
retrieval_note = "Tweet extracted via FXTwitter. Appwrite article fetched directly; metadata/FAQ and article body snippets inspected for measurements, migration constraints, and Go-versus-Rust rationale."
+++
**Logged at IST:** 2026-08-13 09:59 IST

**What it is:** Richard Seroter pointing to Appwrite's rewrite of its CLI from TypeScript/Bun to Go.

**Gist:** Appwrite says the user-facing contract stays the same: npm package name, `appwrite` binary, flags, scripts, CI behavior, exit codes, and JSON output. The internals changed from a JavaScript bundle on a runtime plus 189 packages underneath to a native Go binary.

The measured deltas are the useful part: startup went from 207.6ms to 11.1ms, install dependency count from 330 packages to 2, on-disk install from 209MB to 13MB, memory during push from 283.5MB to 28.0MB, and binary size from 66MB to 14MB. Appwrite frames the memory drop as an implementation change too: the new CLI streams the archive instead of holding it in memory.

The Go-versus-Rust rationale is pragmatic rather than ideological. Appwrite says both languages would have solved the ~200ms startup cost, but Go fit because the CLI mostly does parallel network operations, the first-party Appwrite Go SDK already comes from the same generator, GOOS/GOARCH covers their six release targets, and community contributors can ramp quickly. They kept the TypeScript CLI installable for at least one minor cycle and used parity tests to compare the two implementations command by command.

**Newsletter angle:** Useful developer-tools systems item: CLIs are part of product latency and dependency surface. Rewrites are risky, but generated parity tests plus API-spec-derived commands make this a cleaner example than a generic "rewrite in Go" victory lap.

## Embedded source

{{< tweet id="2087622396769657336" url="https://x.com/i/status/2087622396769657336" >}}
