+++
title = "Hobby programming, craft, and the LLM collision"
slug = "2026-08-06-hobby-programming-llms-craft"
date = 2026-08-06T18:52:00+05:30
[taxonomies]
tags = ["agents", "developer-tools", "org-design"]
[extra]
source_url = "https://blog.fogus.me/llm/born-against.html"
source_type = "article-plus-discussion-plus-essay"
newsletter_candidate = true
why_it_matters = "This is a clean chain for why agentic coding lands differently in hobby communities: the thing being defended is often the learning, authorship, provenance, and shared craft process, not merely the existence of working code."
saved_link = "https://blog.fogus.me/llm/born-against.html"
related_url = "https://news.ycombinator.com/item?id=49187061"
related_urls = ["https://github.com/adamtwiss/coda/issues/15", "https://rohanverma.net/pages/essays/hobbyist-programmers-gaslit/"]
retrieval_note = "Read the Fogus post in browser, fetched the HN story and top discussion via HN/API, read the linked Coda GitHub issue/comments, and added Rohan Verma’s related essay on hobbyist programmers as a broader personal/community frame."
+++
**Logged at IST:** 2026-08-06 18:52 IST

**What it is:** Fogus’s short essay on why niche hobby programming communities are hostile to LLM-generated development, paired with the Hacker News discussion, the linked Coda chess-engine GitHub issue, and Rohan Verma’s adjacent essay on hobbyist programmers being pressured to turn computing into career, monetization, or public validation.

**Gist:** Fogus’s operative claim is concrete: in communities like OSDev, LangDev, TxtDev, EmuDev, RLDev, the demoscene, chess engines, and code golf, the process of mastering a difficult field is often the product. A working program is not enough. The community wants to see that the author knows why and how the thing works. In that frame, using an LLM as a surrogate does not look like productivity. It looks like skipping the very activity the hobby exists to practice.

The underlying GitHub issue makes the conflict sharper than a generic “LLMs in hobbies” debate. The objection to Coda, an agentically developed chess engine, is partly about craft and partly about community provenance: developers accused it of taking hard-won optimizations without enough credit, copy-washing or re-expressing ideas through agents, creating licensing uncertainty around GPL/AGPL engines, and then being taken seriously by rating lists. The Coda maintainer’s reply is the opposite frame: the project is openly agentic, GPL-3.0, trying to explore what is possible, and willing to add attribution or remove specific unfair uses when shown.

HN broadened this into a useful taxonomy. One strong comment split programming into phases: choosing the problem, figuring out the solution, implementing it, seeing it work, and shipping it. Entrepreneurial/product people may value the outer phases and treat implementation as a chore. Tinkerers often value the middle phases, sometimes even without shipping. For them, LLMs automate the best part of the dish and leave the less interesting residue.

The maintenance angle also matters. Several commenters argued that doing the design and implementation by hand is what lets you later fix or extend the thing without fumbling. Others pushed back that human-written spaghetti is common too, and that LLMs can produce maintainable code if kept on a short leash. That disagreement is the real control surface: not whether AI is “allowed,” but whether the user remains responsible for understanding, review, provenance, and long-term ownership.

Rohan’s older essay adds a useful pre-LLM layer: programming was already an awkward hobby because it is visibly productive. That productivity attracts pressure to monetize, grow a GitHub following, build a career, treat side projects as serious products, or seek open-source validation. His point is not anti-ambition. It is that computing as play gets delegitimized when every act of building is judged by career or market logic. The Fogus/HN thread is downstream of the same tension, with LLMs making the pressure sharper: if the world already undervalues hobby programming as craft, agents can make the craft look even more like an inefficient route to an artifact.

**Newsletter angle:** Good companion to agentic coding discourse. The conflict is less “AI yes/no” and more “what is being valued here?” Outcome, learning, authorship, provenance, maintenance, play, and community standing are different goals. LLMs can be a force multiplier when the goal is an artifact, but they become culturally abrasive when the shared norm is that craft and earned understanding are the artifact.
