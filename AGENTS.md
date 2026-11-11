# Reading List

This repository contains a static reading site and its curation workflow. Resolve paths from the repository root, regardless of the host or agent running it.

## Source files

- `data/reading-log/` is the canonical private reading log. Use Asia/Kolkata dates and a `logged at IST: YYYY-MM-DD HH:MM IST` line for new entries.
- `content/notes/` and `content/digests/` contain public content.
- `data/legacy-workspace/` and `data/legacy-hermes-memories/` preserve historical source material.
- `data/previous-agent-skills/` and `data/original-hermes-skills/` preserve detailed historical operating references. They are optional reference material, not current runtime instructions.
- `data/source-path-map.json` maps historical file paths to project-relative locations.
- `data/` contains private logs, snapshots, run history and recovery records. Never commit or publish it. A Git clone alone does not include it; transfer it separately when moving hosts.

## Curation

Read `skills/work-reading-dropbox/SKILL.md` for link drops, `skills/reading-list-curator/SKILL.md` for source extraction, and `skills/reading-list-site-operations/SKILL.md` for publishing. These project instructions take precedence over archived instructions.

Useful, grounded links shared for this reading list should be logged and promoted by default. Preserve stable slugs, source attribution, archive links and IST timestamps. Follow linked articles when possible. Keep blocked or weakly grounded items log-only. Do not claim an article was read when only its social post was accessible.

Use `python3 scripts/import_historical_reading.py` for incremental historical imports and `python3 scripts/link_digest_notes.py` for digest backlinks. Review their diff. Never delete and rebuild the content tree.

Before sending or publishing prose, read `skills/humanizer/SKILL.md` and review the actual text. Never use em dashes in outgoing prose, including replies. Run `python3 scripts/humanize_repo_content.py` before publishing and review its diff for unrelated changes.

## Publishing

Use Python 3, Git, the authenticated `gh` CLI and Zola 0.22.1. Build with `zola build --force` and inspect generated pages for changed notes or digests. Commit selected public files with Conventional Commit messages and push to origin main for authorized link drops and weekly publication. Never commit private logs, secrets or imported session history.

Use the host's existing GitHub authentication. Check `gh auth status` and `gh api repos/oddship/reading-list`. Git may use `gh auth git-credential` through a credential helper. Do not copy or print tokens. Any scheduler must provide GitHub authentication to its job process.

Deployment uses the GitHub Actions workflow `Deploy via s3site`. Match its run to the pushed full commit SHA, wait for success, then check https://reading-list.oddship.net/, /notes/ and /digests/. Do not dispatch a manual deployment without an explicit request.

## Scheduling and delivery

`automation/weekly-reading.md` defines the agent task. `automation/schedule.json` records the cron expression and IANA timezone. Any agent scheduler can use these files from the project root; this task requires reasoning and is not a plain shell cron script.

Reports belong in the current execution session unless another delivery channel is explicitly configured. Historical Telegram metadata does not authorize new messages or supply an active transport.

When moving hosts, copy the repository, the ignored `data/` directory, and any uncommitted files. Install the tools, authenticate `gh`, and point the new scheduler at the task file. `docs/portability.md` explains the optional BB adapter.

Review the source grounding of pre-existing untracked content before including it in a publication.
