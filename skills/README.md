# Project agent skills

Each directory contains a `SKILL.md` with Agent Skills frontmatter and Markdown
instructions. Agents can read these files directly, and `AGENTS.md` routes the
main reading workflows to them.

- `work-reading-dropbox`: capture links in the private reading log and promote grounded notes.
- `reading-list-curator`: source extraction, provenance and thematic curation.
- `reading-list-site-operations`: content, taxonomy, feeds and routine publication.
- `reading-list-zola-publishing`: Zola builds, templates and deployment.
- `reading-list-zola-publish-verification`: verify generated pages and the exact deployed commit.
- `humanizer`: review outgoing prose.
- `reading-list-repo-maintenance`, `telegram-reading-flow`, and `agent-skills-authoring`: existing repository-specific guides. The Telegram guide applies only when that transport is explicitly configured.

Historical Hermes skill references remain private in
`data/previous-agent-skills/` and `data/original-hermes-skills/`. Current root
instructions take precedence over their old commands and paths.

BB can load these same files through optional symlinks created by
`python3 scripts/setup_bb_adapter.py`. Another agent can use the root files
directly. See `docs/portability.md` for host migration and private data handling.
