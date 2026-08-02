+++
title = "Devtools must be open source"
slug = "2026-08-03-devtools-must-be-open-source"
date = 2026-08-03T01:28:00+05:30
[taxonomies]
tags = ["agents", "developer-tools"]
[extra]
source_url = "https://blog.exe.dev/devtools-must-be-open-source"
source_type = "article"
newsletter_candidate = true
why_it_matters = "Clear agent-era argument for open-source devtools: source access is not just trust or ideology, it is what lets agents personalize tools and maintain those changes over time."
saved_link = "https://blog.exe.dev/devtools-must-be-open-source"
+++
**Logged at IST:** 2026-08-03 01:28 IST

**What it is:** David Crawshaw / exe.dev essay arguing that developer tools need to be open source because agent-driven personalization depends on editable source.

**Gist:** Crawshaw’s core claim is that agents change the ROI of customizing software twice over: they make it cheap to start modifying a tool, and they can automate the ongoing work of rebasing those changes on upstream releases. In that world, source code becomes the extension system. Config files, plugin APIs, and vendor-provided hooks still help, but they are the old constrained surface; the powerful path is to give an agent the source and ask for the exact tool behavior you want.

The Shelley/meat.dev example is the concrete version of the argument: adding background diff reduction directly into the devtool is far more natural when the agent can edit the product itself than when a user has to fight a generic extension API. That makes closed-source tools like Claude Code less personalizable by default, while open agents can absorb skills and local changes directly.

**Newsletter angle:** Useful framing for why open-source AI devtools matter beyond trust: agent-era personalization needs source-level editability and maintainable local divergence.
