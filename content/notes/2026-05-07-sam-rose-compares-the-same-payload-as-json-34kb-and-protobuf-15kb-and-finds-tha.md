+++
title = "Sam Rose compares the same payload as JSON (34kb) and protobuf (15kb) and finds that after compression, JSO..."
date = 2026-05-07
[taxonomies]
tags = ["reading-log", "x-post", "x-com", "historical-backfill"]
[extra]
source_url = "https://x.com/i/status/2051977984148467890"
source_type = "x-post"
status = "published"
newsletter_candidate = true
why_it_matters = ""
saved_link = "https://x.com/i/status/2051977984148467890"
+++
Imported from historical reading log.
- Extracted main post via `api.fxtwitter.com` fallback; the attached image includes the concrete compression results.
- Sam Rose compares the same payload as JSON (`34kb`) and protobuf (`15kb`) and finds that after compression, JSON is often slightly smaller than protobuf for Brotli, Zstd, gzip, and bzip2; protobuf only wins clearly for lz4 and barely for lzma in his sample.
- Concrete reported sizes from the screenshot: Brotli `json 4237 < bin 4279`, Zstd `4484 < 4702`, gzip `4766 < 4949`, bzip2 `5208 < 5302`, lzma `4500 > 4484`, lz4 `6245 > 5832`.
- Why it is interesting: it is a good reminder that `binary format smaller on disk/wire` and `binary format compresses smaller` are different questions; verbose JSON field names and repeated structure can give compressors more redundancy to exploit.
- Good discussion angle: `protobuf vs JSON size intuition breaks once a strong general-purpose compressor enters the picture`.
