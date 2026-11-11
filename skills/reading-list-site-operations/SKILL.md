---
name: reading-list-site-operations
description: Maintain Reading List notes, digests, taxonomy, feeds and publication. Use when changing site content or carrying out the weekly reading workflow.
---

# Reading site operations

Use `data/reading-log/` as the private source and preserve curated public notes and stable slugs. Assign recurring topical tags from the maintainer guide. Keep source mechanics and domain names out of public taxonomy. Review `other` when it exceeds 20 notes.

Keep homepage, notes, digests, pagination, per-section feeds and tag feeds coherent. Run the incremental importer only when needed and inspect its diff. After digest changes, run `python3 scripts/link_digest_notes.py` to connect citations to existing notes.

For new notes, preserve the incoming link, the source actually read, source titles, archives and retrieval limitations. Render social links using the site's current shortcodes; X embeds must remain opt-in. Avoid broad social-embed backfills for a single note.

Read `docs/maintainer-guide.md` and `docs/link-drop-playbook.md` for the publication contract. Build using Zola 0.22.1, commit selected files, push and verify the exact Actions commit and live pages. Use the current host's authenticated `gh` CLI. Historical operational examples remain in `data/previous-agent-skills/reading-list-site-operations/`.

Read `AGENTS.md` first. Use paths relative to the project root. Load `skills/humanizer/SKILL.md` before publishing prose. Never use em dashes in outgoing writing.
