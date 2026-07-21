+++
title = "agentic-inbox"
slug = "2026-07-06-agentic-inbox"
date = 2026-07-06
[taxonomies]
tags = ["agents", "security", "developer-tools"]
[extra]
source_url = "https://blog.sh1ma.dev/en/articles/20260706_cloudflare_agentic_inbox/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "agentic inboxes are becoming deployable infra products, but the real story is the surrounding control plane and auth plumbing"
saved_link = "https://blog.sh1ma.dev/en/articles/20260706_cloudflare_agentic_inbox/"
+++
**What it is:** hands-on writeup of deploying Cloudflare’s official `agentic-inbox` to run a custom-domain email client on Cloudflare Workers

**Gist:** the stack uses Email Routing for inbound mail, Email Service for sending, Durable Objects + SQLite for mailboxes, R2 for attachments, and Cloudflare Access for auth. Main operational gotcha is that one-click deploy is not enough: you still have to wire the Email Routing catch-all and set the Access secrets or the app won’t work

**Newsletter angle:** agentic inboxes are becoming deployable infra products, but the real story is the surrounding control plane and auth plumbing

**Retrieval note:** article body was embedded in the site JS bundle; direct HTML was mostly a shell page
