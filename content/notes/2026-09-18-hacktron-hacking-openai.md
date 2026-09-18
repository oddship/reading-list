+++
title = "Hacktron's HEIF Heist chain from Discourse to OpenAI Codex"
slug = "2026-09-18-hacktron-hacking-openai"
date = 2026-09-18T10:02:00+05:30
[taxonomies]
tags = ["security", "ai-infra", "agents", "systems"]
[extra]
source_url = "https://www.hacktron.ai/blog/hacking-openai"
source_type = "security-writeup"
newsletter_candidate = true
why_it_matters = "A concrete case study in how agent-assisted exploit work, a native image-decoder bug, and loose identity/connectors can turn into cross-product access quickly."
saved_link = "https://x.com/S1r1u5_/status/2100777801335095383"
related_urls = ["https://heif-heist.com/", "https://github.com/discourse/discourse/security/advisories/GHSA-vhm9-85gw-x335", "https://x.com/rootxharsh/status/2100801820960620574", "https://x.com/LiveOverflow/status/2100768686231499107", "https://www.youtube.com/watch?v=gjHh9g7yo9Y", "https://www.wsj.com/tech/ai/hackers-used-anthropics-claude-to-break-into-openai-b40ba883", "https://github.com/discourse/discourse/commit/a07188016987de1613c961277e2e928aaa7c37ec", "https://vercel.com/changelog/nextjs-august-2026-security-release", "https://docs.github.com/en/enterprise-server@3.21/admin/release-notes#3.21.5-security-fixes"]
retrieval_note = "S1r1us and Harsh Jaiswal X posts were extracted via FXTwitter; attached images and related screenshots were OCR'd; Hacktron's OpenAI write-up, the HEIF Heist site, and Discourse GHSA-vhm9-85gw-x335 were read directly. A related LiveOverflow YouTube explainer was identified via oEmbed/X, but transcript extraction was blocked by YouTube IP restrictions, so the video itself was not summarized."
+++

**Logged at IST:** 2026-09-18 10:02 IST

**What it is:** One combined entry for Hacktron's OpenAI compromise write-up, the broader HEIF Heist research, the Discourse security advisory, and the related LiveOverflow explainer link.

**Gist:** Hacktron says it chained a `libheif`/ImageMagick remote-code-execution path in OpenAI's Discourse forum with an OpenAI SSO flaw. The claimed result was no-interaction takeover of OpenAI employees' ChatGPT/Codex accounts, with potential reach into connected services such as GitHub, Slack, and email.

They demonstrated impact by asking an employee's Codex account to open a harmless pull request in OpenAI's internal `openai/openai` monorepo, then stopped further testing. The write-up says OpenAI fixed the issue the same day, and OpenAI later paid a $6,500 bounty for the OpenAI-side finding.

The Discourse advisory gives the concrete patch hook: **GHSA-vhm9-85gw-x335 / CVE-2026-32882**, high severity **8.8**, describes remote code execution via malformed HEIF image uploads, and lists patched Discourse versions **2026.7.0**, **2026.6.1**, **2026.5.2**, and **2026.1.6**. It also notes that current Discourse core adds image-processing sandboxing as defense in depth.

The broader HEIF Heist site frames the issue as an ecosystem problem rather than a one-off Discourse bug. Many products accept HEIF, HEIC, or AVIF uploads that eventually flow into native decoders such as `libheif` and `libde265` through ImageMagick, libvips, Sharp, distro packages, and container images. Hacktron lists related impact across OpenAI, Slack, Meta, Discourse, Next.js image optimization, GitHub Enterprise, and other frameworks/CMSes.

The deeper point is economic: Hacktron argues that agent-assisted exploit development compressed work that used to require rare expertise and sustained effort into a few days of agent time plus a few hours of human guidance. That makes old assumptions about "known but hard to weaponize" dependency bugs much weaker.

**Newsletter angle:** Treat image decoding as an untrusted native execution boundary. Patch `libheif`/`libde265` and affected applications, but also sandbox or disable untrusted HEIF/AVIF processing where it is not needed, especially when the surrounding product has powerful identity and connector reach.
