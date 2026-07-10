# Repo-local agent skills

This directory stores repo-local `SKILL.md` files so the maintenance workflow and Telegram ingest flow are versioned alongside the site itself.

## Included skills

- `reading-list-repo-maintenance/`
  - repo operations, Zola edits, Pages verification, live-site checks
- `telegram-reading-flow/`
  - Telegram ingest, source grounding, work-log capture, selective promotion into public notes

## Why keep them in-repo

- operational knowledge evolves with the repo
- curation/publishing conventions stay reviewable in git
- future automation can clone one repo and recover both content and process

## Format

Each skill lives in its own directory with a `SKILL.md` file using frontmatter plus a markdown body, following the general agent-skills pattern.
