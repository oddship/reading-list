+++
title = "GitHub restricts stargazer data"
slug = "2026-07-22-github-stargazer-api-restriction"
date = 2026-07-22T16:55:00+05:30
[taxonomies]
tags = ["developer-tools", "systems"]
[extra]
source_url = "https://www.star-history.com/blog/github-stargazer-api-restriction/"
source_type = "article"
newsletter_candidate = true
why_it_matters = "Useful developer-tools and API-governance item because it shows how an upstream platform privacy or abuse-control change can quietly break analytics products, badges, and public observability workflows built on previously open metadata."
saved_link = "https://www.star-history.com/blog/github-stargazer-api-restriction/"
+++
**Logged at IST:** 2026-07-22 16:55 IST

**What it is:** Star History’s note on GitHub restricting access to the stargazers API.

**Gist:** GitHub is limiting the endpoint that reveals who starred a repository and when to repository admins and collaborators. Star History depends on exactly that data to reconstruct growth curves, so charts for repositories you do not own or collaborate on are broken, and README-embedded live charts are affected because Star History’s servers are not collaborators on most repos. Owner and collaborator views still work with a readable fine-grained token; old no-scope tokens no longer work.

**Newsletter angle:** Useful developer-tools and API-governance item because it shows how an upstream platform privacy or abuse-control change can quietly break analytics products, badges, and public observability workflows built on previously open metadata.
