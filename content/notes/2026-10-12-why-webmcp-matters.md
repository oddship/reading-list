+++
title = "Why WebMCP matters: agentic web performance and co-browsing"
slug = "2026-10-12-why-webmcp-matters"
date = 2026-10-12T16:29:00+05:30
[taxonomies]
tags = ["agents", "developer-tools"]
[extra]
source_url = "https://blog.yoav.ws/posts/why_webmcp_matters/"
source_type = "article"
source_title = "Why WebMCP matters"
saved_link = "https://blog.yoav.ws/posts/why_webmcp_matters/"
saved_title = "Why WebMCP matters"
newsletter_candidate = true
why_it_matters = "A practitioner argues that site-provided WebMCP tools can make agent-assisted co-browsing faster and more reliable while keeping the user in control of the familiar web experience."
related_urls = ["https://webmachinelearning.github.io/webmcp/", "https://webmcp.com/benchmark", "https://shopify.dev/changelog/webmcp-liquid-hydrogen", "https://shopify.dev/docs/agents/carts-and-checkout/checkout-webmcp"]
related_titles = ["WebMCP proposal", "WebMCP benchmark", "Shopify storefront WebMCP announcement", "Shopify Checkout WebMCP docs"]
retrieval_note = "Read Yoav Weiss's full article directly. The author describes his work shipping Shopify storefront WebMCP and discusses the proposal's open questions. Performance and cost figures are attributed to the cited Nekuda and Shopify experiments; they are not independent measurements in this note."
+++
**Logged at IST:** 2026-10-12 16:29 IST

**What it is:** Yoav Weiss's practitioner case for WebMCP, written after helping ship Shopify storefront tools.

**Gist:** Weiss argues that WebMCP lets a site expose explicit JavaScript tools to an agent working alongside the user's browser session. Compared with DOM- or screenshot-driven clicking, those tools can make co-browsing faster, cheaper, and less awkward while leaving the site's developer and the user in control; the user can take over at any point. He calls this “web performance for AI agents.”

He sees WebMCP as a way for a merchant's site to contribute domain-specific help to a user's existing agent, rather than requiring every merchant to build its own assistant. He also argues imperative tools complement declarative/form-based semantics for multi-step tasks and agent-consumed context, while acknowledging unresolved questions around tool registration, permissions, user intent, security, evaluation, and semantic divergence. His cited speed/cost results come from experiments by Nekuda and Shopify, not a universal guarantee.

**Newsletter angle:** A clear product-level argument for website-first agent integration: expose useful capabilities to the user's agent without replacing the human-facing site or forcing the merchant to own the whole assistant.
