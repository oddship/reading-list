# Agent Skills specification notes for this repo

This repo follows the upstream Agent Skills specification at:
- https://agentskills.io/specification

## What matters most here

- A skill is a directory with at minimum `SKILL.md`.
- `scripts/`, `references/`, and `assets/` are optional and should be used deliberately.
- `SKILL.md` should keep the core trigger, workflow, pitfalls, and verification close at hand.
- Longer policy notes or examples should move into `references/`.
- Reusable helper code should live in `scripts/`.

## Frontmatter rules we should keep honoring

- `name`: lowercase, hyphenated, max 64 chars
- `description`: explain what the skill does and when to use it, max 1024 chars
- `license`: include it even if the validator treats it as optional
- `metadata.hermes.tags` and `metadata.hermes.related_skills`: keep them useful and sparse

## Repo-specific preference

- Prefer `go run` helpers for reusable scripts in repo-local skills because Go is available locally and keeps execution self-contained.
- If a script is Python-only for a good reason, document the reason in the skill.

## Progressive disclosure rule of thumb

Keep in `SKILL.md`:
- when to use the skill
- the numbered workflow
- common pitfalls
- verification checklist

Move to `references/`:
- extended rationale
- taxonomy policy
- schema notes
- examples that are nice to have but not required every time

Move to `scripts/`:
- validators
- audits
- one-off analyses that became repeated tasks
