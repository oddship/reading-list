+++
title = "AI Is Removing the Middle Class of Software Engineering"
slug = "2026-08-19-ai-removing-middle-class-software-engineering"
date = 2026-08-19T11:10:00+05:30
[taxonomies]
tags = ["agents", "developer-tools", "org-design"]
[extra]
source_url = "https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html"
source_type = "article"
newsletter_candidate = true
why_it_matters = "This is a sharp version of the agent-era engineering management problem: implementation gets cheaper, but understanding, review, validation, and ownership do not automatically get cheaper with it."
retrieval_note = "Article HTML and metadata were read directly."
+++
**Logged at IST:** 2026-08-19 11:10 IST

**What it is:** Florian Herrengt's essay arguing that AI is removing the middle class of software engineering.

**Gist:** The core claim is not "AI is bad". Herrengt says he uses AI heavily. The warning is that AI removes the speed limit from weak engineering culture.

Before AI, bad decisions compounded slowly because implementation was expensive. Now someone can generate a 25,000-line PR, add services, change schemas, and ship plausible-looking functionality before anyone has built a real mental model of what changed. The output may work at first, but the debt is hidden until a bug appears and nobody can explain where the data comes from or why the architecture looks the way it does.

That shifts the bottleneck from producing code to understanding and owning it. Code review, CI, and architectural process still matter, but many of those practices were designed for a world where producing huge amounts of change was hard. If people can generate faster than the team can understand or validate, the real options are to generate less, find better validation, or accept lower quality.

The essay's labor-market point follows from that: good engineers become more valuable because AI lets them move faster while applying judgment. Engineers who use AI as a substitute for understanding become more expensive liabilities, because they can now create more complexity than the team can realistically absorb.

**Newsletter angle:** Good org/engineering-culture piece for the agent era. It draws the practical line around judgment, review discipline, system understanding, and accountability for design decisions, not around whether engineers should use AI at all.
