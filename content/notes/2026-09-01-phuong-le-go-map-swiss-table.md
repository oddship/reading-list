+++
title = "Phuong Le on Go map internals before and after Swiss Table"
slug = "2026-09-01-phuong-le-go-map-swiss-table"
date = 2026-09-01T21:18:00+05:30
[taxonomies]
tags = ["systems", "developer-tools"]
[extra]
source_url = "https://victoriametrics.com/blog/go-map/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "Go 1.24's Swiss Table map change is easier to understand if you first understand the older bucket, overflow, tophash, and evacuation model that VictoriaMetrics explains clearly."
saved_link = "https://x.com/func25/status/2094719411466998208"
related_url = "https://x.com/func25/status/2094719411466998208"
related_urls = ["https://pbs.twimg.com/media/HRHaFJDa0AACHZR.jpg?name=orig"]
retrieval_note = "FXTwitter extracted Phuong Le's tweet, the VictoriaMetrics Go-map article URL, and one attached image. The article was read directly; the image was inspected and contains a draft Swiss Table diagram showing an 8-slot group becoming a table with two groups after a ninth entry."
+++
**Logged at IST:** 2026-09-01 21:18 IST

**What it is:** Phuong Le's teaser for a forthcoming “dead-simple” explanation of Go's Swiss Table map, with a link back to VictoriaMetrics' existing explainer on how Go maps worked before Go 1.24.

**Gist:** The linked article is a clear tour of the old Go-map implementation model. A Go map is backed by an `hmap` pointing at an array of buckets. Each bucket holds up to 8 key/value pairs. Keys are placed by hashing with a per-map seed, which helps explain why two maps with the same logical contents can iterate differently.

The article then builds the performance story: collisions create overflow buckets; the map grows when there are too many overflow buckets or when the load factor crosses roughly 6.5; cached `tophash` values make most key comparisons cheaper; and growth is done incrementally by evacuating old buckets into new buckets during later assignments or deletes. That evacuation model also explains why Go does not let you take the address of a map element: growth can move the element.

The attached teaser image shows the newer Swiss Table vocabulary. It describes a group as having 8 slots; when a ninth entry arrives, Go creates a table with two groups and redistributes the existing entries before storing the new one. The useful setup is that the old bucket/overflow/evacuation mental model gives the contrast needed for understanding Go 1.24+'s group/table design.

**Newsletter angle:** Good Go runtime internals explainer: the older bucket/overflow/evacuation model sets up why Swiss Table's groups/tables matter in Go 1.24+.

{{ tweet(id="2094719411466998208", url="https://x.com/func25/status/2094719411466998208") }}
