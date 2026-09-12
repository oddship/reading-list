+++
title = "The browser's main thread is expensive"
slug = "2026-09-12-browser-main-thread-expensive"
date = 2026-09-12T22:57:00+05:30
[taxonomies]
tags = ["frontend", "systems", "performance"]
[extra]
source_url = "https://kciter.so/posts/the-expensive-main-thread/en"
source_type = "article"
newsletter_candidate = true
why_it_matters = "The article is a practical browser-performance mental model: user-perceived smoothness is mostly about how carefully an app spends, avoids, or moves work off the single main thread."
saved_link = "https://x.com/jh3yy/status/2098382395426611397"
related_url = "https://x.com/jh3yy/status/2098382395426611397"
retrieval_note = "Tweet extracted via FXTwitter; linked article fetched directly; attached X demo video sampled into a contact sheet and confirmed it shows the article's immediate-render versus yielding-render chat demo."
+++

**Logged at IST:** 2026-09-12 22:57 IST

**What it is:** kciter’s interactive article on why browser main-thread time is the scarce resource behind jank, slow input, and broken animation.

**Gist:** The core model is simple: JavaScript, event handlers, framework internals, style calculation, layout, paint, and most of the rendering pipeline all compete on one main thread. At 60Hz there are only about 16.6ms per frame, and less than that in practice; a long task blocks input and paint, so “my code is fast enough” is the wrong frame if it monopolizes the thread.

The article organizes the fixes into two families. First, use the main thread wisely: split long work into smaller tasks, batch high-frequency work, prioritize urgent interactions over background updates, and defer non-visible or non-urgent rendering. The demos make the trade-off concrete: yielding can make an interface feel smooth even if the total work takes longer, while batching once per frame can preserve throughput when data arrives faster than the UI should redraw.

Second, avoid the main thread when possible. Animations that stay in compositor-friendly properties such as `transform` and `opacity` can keep running when JS is blocked. Heavy computation should move to workers, using transferable buffers when copying would dominate. The strongest optimization is still eliminating work: drop stale streams, merge updates where only the latest value matters, skip invisible rendering, and memoize repeated computation.

The attached X video is a short capture of the article’s chat demo, showing “Immediate render” versus “Yielding render”: the visible lesson is that task boundaries, not just raw algorithm speed, determine whether typing and animation remain responsive.

**Newsletter angle:** Good systems thinking for frontend work. The browser is a scheduler and rendering pipeline, not just a JS runtime; performance comes from respecting the scarce shared resource and deciding what work should run now, later, elsewhere, or never.
