---
name: work-reading-dropbox
description: Capture and promote reading links shared for the Reading List project. Use for link drops and compact reading-log entries, not unsolicited newsletter drafting.
---

# Reading link capture

Resolve the current day in Asia/Kolkata and append a compact entry to `data/reading-log/YYYY-MM-DD.md`. Include the saved URL, logged-at IST timestamp, source type, gist, source actually read, and any retrieval blocker.

Follow linked articles, papers or repositories when feasible. A social card or title alone does not justify a public note. Keep weakly grounded or explicitly private items in the log.

Dedupe by URL and title. Promote useful grounded entries to `content/notes/` with full IST datetime frontmatter, approved topic tags and provenance. Preserve existing slugs. Add readable source titles and archive URLs when available. Link matching digest citations with `python3 scripts/link_digest_notes.py`.

Follow `docs/link-drop-playbook.md` through build, commit, push and deployment verification. Keep the reply brief and state the exact partial state if blocked. Detailed historical capture references are retained privately under `data/previous-agent-skills/work-reading-dropbox/`.

Read `AGENTS.md` first. Use paths relative to the project root. Load `skills/humanizer/SKILL.md` before publishing prose. Never use em dashes in outgoing writing.
