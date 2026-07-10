# Repo-local agent skills

This directory stores repo-local `SKILL.md` files so the maintenance workflow, ingest flow, and skill-authoring guidance are versioned alongside the site itself.

## Included skills

- `reading-list-repo-maintenance/`
  - repo operations, Zola edits, Pages verification, live-site checks, and pre-commit humanizer discipline
- `telegram-reading-flow/`
  - Telegram ingest, source grounding, work-log capture, immediate promotion of useful notes, tag discipline, and historical import hygiene
- `agent-skills-authoring/`
  - meta guidance for creating/updating repo-local skills, syncing local-vs-repo workflow knowledge, and using references/scripts cleanly

## Why keep them in-repo

- operational knowledge evolves with the repo
- curation and publishing conventions stay reviewable in git
- future automation can clone one repo and recover both content and process
- cron-driven publishing can follow the same checked-in rules as manual maintenance

## Format

Each skill lives in its own directory with a `SKILL.md` file using frontmatter plus a markdown body, following the Agent Skills pattern at `https://agentskills.io/specification`.

When a skill grows beyond its always-needed instructions, prefer:
- `references/` for longer policy notes and examples
- `scripts/` for reusable helpers, with `go run` preferred in this repo when practical
