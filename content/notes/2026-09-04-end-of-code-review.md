+++
title = "The end of code review?"
slug = "2026-09-04-end-of-code-review"
date = 2026-09-04T04:49:00+05:30
[taxonomies]
tags = ["agents", "org-design", "developer-tools"]
[extra]
source_url = "https://thelastsoftwareengineer.substack.com/p/the-end-of-code-review-or-an-opportunity"
source_type = "article"
newsletter_candidate = true
why_it_matters = "A useful model for separating code review's bug-finding role from its harder-to-replace social roles: coordination, mentorship, shared ownership, and codebase awareness."
saved_link = "https://x.com/p0nk/status/2095569704534364313"
related_url = "https://x.com/p0nk/status/2095569704534364313"
retrieval_note = "Christian Kästner’s X post was extracted via FXTwitter; the linked Substack article was fetched directly."
+++
**Logged at IST:** 2026-09-04 04:49 IST

**What it is:** Christian Kästner launching the CMU “The Last Software Engineer?” Substack with an essay on whether AI-generated code makes modern code review unsustainable.

**Gist:** Kästner argues that modern lightweight code review was probably a reasonable pre-AI equilibrium. It was not especially good at finding deep bugs, but it was cheap enough to run for most changes and provided other benefits: readability pressure, shared ownership, codebase awareness, mentorship, convention-setting, and group problem-solving.

Agentic coding changes the equation all at once. It can lower code production cost, change liability through lower or higher quality, make rework cheaper, create cheaper review substitutes, and weaken human review through volume pressure, automation bias, and reviewer cognitive debt. If agents produce more code than humans can meaningfully review, preserving traditional PR review may just turn it into rubber-stamping.

The useful move is to ask what code review was doing for the organization and then design replacements for those functions. Some bug-finding may move into automated review, tests, static analysis, or agent self-review. The harder questions are about coordination, mentoring, safety, ownership, and where humans should exert control: requirements, architecture, test design, production safeguards, or something else.

**Newsletter angle:** Strong companion to the agentic-engineering/code-review lane: stop defending PR review as a ritual, but be explicit about which social and safety functions must survive in new forms.

## Embedded source

{{ tweet(id="2095569704534364313", url="https://x.com/p0nk/status/2095569704534364313") }}
