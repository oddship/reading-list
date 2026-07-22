+++
title = "A history of IDEs at Google"
slug = "2026-07-22-history-of-ides-at-google"
date = 2026-07-22T16:07:00+05:30
[taxonomies]
tags = ["developer-tools", "systems", "org-design"]
[extra]
source_url = "https://laurent.le-brun.eu/blog/a-history-of-ides-at-google"
source_type = "article"
newsletter_candidate = true
why_it_matters = "Strong developer-tools and org-design item because it shows how standard internal tooling creates leverage: integrations can be built once, extension work moves to product teams, and AI features become easier to ship on a common platform."
saved_link = "https://laurent.le-brun.eu/blog/a-history-of-ides-at-google"
+++
**Logged at IST:** 2026-07-22 16:07 IST

**What it is:** Laurent Le Brun’s history of IDEs at Google, focused on google3, Cider, and Cider V.

**Gist:** Le Brun traces Google’s shift from editor pluralism to a de facto standard internal IDE. The core constraint was scale: local IDE assumptions broke against a billion-file monorepo, shared build, search, review tooling, and a language graph that had to match each developer’s sync state. Cider solved much of this with a web editor backed by centralized indexing, then Cider V adopted VS Code as the frontend so Google-specific backend investment could combine with a mature editor and extension ecosystem.

**Newsletter angle:** Strong developer-tools and org-design item because it shows how standard internal tooling creates leverage: integrations can be built once, extension work moves to product teams, and AI features become easier to ship on a common platform.
