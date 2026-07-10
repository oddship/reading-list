# Repo-local agent skills

This directory stores repo-local `SKILL.md` files so the maintenance workflow and Telegram ingest flow are versioned alongside the site itself.

## Included skills

- `reading-list-repo-maintenance/`
  - repo operations, Zola edits, Pages verification, live-site checks, and pre-commit humanizer discipline
- `telegram-reading-flow/`
  - Telegram ingest, source grounding, work-log capture, selective promotion into public notes, and historical import hygiene

## Why keep them in-repo

- operational knowledge evolves with the repo
- curation and publishing conventions stay reviewable in git
- future automation can clone one repo and recover both content and process
- cron-driven publishing can follow the same checked-in rules as manual maintenance

## Format

Each skill lives in its own directory with a `SKILL.md` file using frontmatter plus a markdown body, following the general agent-skills pattern.
