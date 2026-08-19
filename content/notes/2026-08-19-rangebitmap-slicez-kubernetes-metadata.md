+++
title = "RangeBitmap, SliceZ, and Kubernetes Metadata at Yandex"
slug = "2026-08-19-rangebitmap-slicez-kubernetes-metadata"
date = 2026-08-19T14:28:00+05:30
[taxonomies]
tags = ["systems", "developer-tools"]
[extra]
source_url = "https://habr.com/ru/companies/yandex_cloud_and_infra/articles/1055120/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "A concrete observability storage case where the right bitmap index turns time filtering from a linear scan into a production-scale metadata query path."
saved_link = "https://x.com/richardstartin/status/2089847854953103434?s=20"
related_url = "https://x.com/richardstartin/status/2089847854953103434"
related_urls = ["https://x.com/richardstartin/status/2089849607945654683", "https://github.com/richardstartin/slicez", "https://richardstartin.github.io/posts/range-bitmap-index"]
retrieval_note = "X thread extracted via FXTwitter. Attached images were OCR'd. Habr AMP article and SliceZ README/GitHub metadata were read directly."
+++
**Logged at IST:** 2026-08-19 14:28 IST

**What it is:** Richard Startin points to a Yandex Monium write-up using `RangeBitmap`, a range-encoded bit-sliced index he designed for Apache Pinot and which is available in RoaringBitmap. His follow-up links `SliceZ`, his newer Java successor for range and point queries over unsorted numeric data.

**Gist:** Yandex Monium stores billions of metrics, processes about 50 GB/s of logs, and serves around 16,000 internal users. Kubernetes broke an old metadata assumption: pod labels are short-lived, but historical label values accumulate. After a few weeks, selectors can hit "too many metrics" because the metadata service sees all historical pods, not just the currently active ones.

The practical fix was to add time filtering without physically segmenting the shard by time. Monium already had an inverted bitmap index over labels. They added `RangeBitmap` indexes over `created_at_seconds` and `last_point_seconds`, then used the inverted index result as a narrowing context for range queries. That made wide metadata filtering scale where a linear scan could not.

The reported result is typical speedups of 6-20x, with up to two orders of magnitude in favorable cases. The conclusion is also useful because it names the constraints: `RangeBitmap` rebuild costs need amortization, which Monium handles with LSM-like structures; batch loading and widened query ranges reduce rebuild pressure; binary search still wins when the data can be sorted; and small scans can be cheaper than the index overhead. With those trade-offs, Monium handles 650K-850K metadata queries/sec carrying time-range information.

Startin's follow-up is the next step: `SliceZ` is a Z-layout bit-sliced index for unsorted numeric data. It supports equality, ranges, `between`, `in`, counts, sums, means, and top/bottom-k queries, with persistence and memory mapping. He describes it as usually faster than `RangeBitmap` and as carrying the same filter-pushdown direction that made the Yandex use case work.

**Newsletter angle:** Good systems/data-structures piece. It shows bitmap indexes as a way to add logical time segmentation and filter pushdown to an observability metadata path without rebuilding the physical storage model.

## Embedded source

{{<tweet id="2089847854953103434" url="https://x.com/richardstartin/status/2089847854953103434?s=20"/>}}

{{<tweet id="2089849607945654683" url="https://x.com/richardstartin/status/2089849607945654683"/>}}
