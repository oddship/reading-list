+++
title = "go-perl embeds Perl 5 in pure Go"
slug = "2026-09-01-go-perl-pure-go-perl5"
date = 2026-09-01T08:28:00+05:30
[taxonomies]
tags = ["developer-tools", "systems"]
[extra]
source_url = "https://github.com/goccy/go-perl"
source_type = "repo"
newsletter_candidate = true
why_it_matters = "go-perl is a serious Perl-in-Go embedding attempt: Perl 5.44.0 translated into Go, static-binary friendly, with Go↔Perl calls, PSGI, XS support, sandboxed capabilities, and an accompanying gperl toolchain."
saved_link = "https://x.com/goccy54/status/2094453110681038915"
related_url = "https://x.com/goccy54/status/2094453110681038915"
related_urls = ["https://raw.githubusercontent.com/goccy/go-perl/main/README.md", "https://github.com/goccy/go-perl/releases/tag/v0.2.0"]
retrieval_note = "FXTwitter extracted Masaaki Goshima's Japanese launch tweet and linked GitHub repo. The repository README and v0.2.0 release metadata were read directly."
+++
**Logged at IST:** 2026-09-01 08:28 IST

**What it is:** go-perl is a pure-Go way to embed Perl 5. It uses Perl 5.44.0 compiled to WebAssembly and then translated to Go, so a Go build can produce a single self-contained binary that runs Perl without cgo, an external `perl`, or a runtime wasm engine.

**Gist:** The interesting part is how far past a toy interpreter wrapper this goes. Go code can evaluate Perl and call named Perl subs, while Perl code can call bound Go functions in-process. Values cross as typed handles rather than strings, so Perl objects and aggregates can remain live across the boundary.

The v0.2.0-era feature set also reaches into real application territory. The `psgi` package can serve PSGI/Plack applications on Go's `net/http`; the `gperl` command can run scripts, build self-contained binaries, and compile XS distributions; and native XS support is tested against unmodified CPAN modules such as Moose, Text::Xslate, Devel::NYTProf, DBD::mysql, and Syntax::Keyword::Match. The library default is capability-controlled and sandboxed, while the CLI intentionally behaves more like normal `perl` with host filesystem/environment access.

The packaging story is systems-relevant too: the embedded stdlib and generated bridge come from attested perl-wasm release artifacts, and release binaries are built with provenance. It is another example of old runtime ecosystems becoming importable infrastructure for Go services.

**Newsletter angle:** Perl 5 as embeddable Go infrastructure: static-binary friendly, cross-compilable, and compatible enough to care about PSGI and native XS modules.

{{ tweet(id="2094453110681038915", url="https://x.com/goccy54/status/2094453110681038915") }}
