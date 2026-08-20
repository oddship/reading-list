+++
title = "AI Plays Age of Empires II"
slug = "2026-08-18-ai-plays-age-of-empires-ii"
date = 2026-08-18T16:47:00+05:30
[taxonomies]
tags = ["agents", "developer-tools", "systems"]
[extra]
source_url = "https://www.youtube.com/watch?v=ZBdAe3ZwKds"
source_type = "video"
newsletter_candidate = true
why_it_matters = "A concrete toy environment for agentic coding loops: generate game scripts, run matches, measure outcomes, then tune strategy against an executable environment."
saved_link = "https://youtu.be/ZBdAe3ZwKds?si=edzNtcTa31asTSBR"
related_url = "https://github.com/MaxRobinsonTheGreat/AgentsOfEmpires"
related_urls = ["https://github.com/mboop127/AutoDE"]
retrieval_note = "YouTube oEmbed, page metadata, video description, timestamps, and thumbnail were read. Transcript fetch was blocked by YouTube cloud/IP restrictions, so this note is not grounded in a full transcript. The linked AgentsOfEmpires README and GitHub metadata were read directly."
+++
**Logged at IST:** 2026-08-18 16:47 IST

**What it is:** Emergent Garden's video on using modern AI agents to play Age of Empires II, along with the linked `AgentsOfEmpires` runner repo.

**Gist:** The video description says the creator used LLM-powered agents, including Claude, GPT, Gemini, and Kimi K3, to write custom Age of Empires II AI scripts, make them fight, and then tune strategies over repeated runs. The listed chapters move from "Agents of Empires" into playing the game, model comparisons, strategy optimization, and battle optimization.

The linked GitHub repo is useful context because it shows the loop around the video. `AgentsOfEmpires` is a rough AoE2 DE runner that uses screen capture rather than a background API. It can run smoke tests and tournaments, write status JSON, archive strategies, save recordings, and parse match outputs such as duration, resignations, age-up times, command counts, and inferred winners.

That makes this more interesting than a one-off "AI plays a game" demo. It is a small agent evaluation harness: generate scripts, run them in a real environment, observe outcomes, and iterate.

**Newsletter angle:** Good agent-systems example for the theme that AI coding gets more powerful when paired with executable environments and feedback loops, even messy ones.

## Embedded source

{{< youtube id="ZBdAe3ZwKds" url="https://www.youtube.com/watch?v=ZBdAe3ZwKds" >}}
