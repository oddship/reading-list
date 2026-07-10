---
name: agent-skills-authoring
description: Use when creating or updating repo-local skills for this reading-list repo and you want them aligned with the Agent Skills specification, recent workflow learnings, and reusable references/scripts.
version: 1.0.0
author: Bosun
license: MIT
metadata:
  hermes:
    tags: [skills, authoring, agentskills, repo-maintenance]
    related_skills: [reading-list-repo-maintenance, telegram-reading-flow]
---

# Agent Skills Authoring

## Overview

This skill governs how Bosun should create and maintain repo-local skills in this repo.
It is the meta layer for keeping process documentation clean, reusable, and consistent with the Agent Skills specification at `https://agentskills.io/specification`.

Use this when adding a new repo-local skill, restructuring an existing one, or syncing local workflow learnings back into the checked-in skills.

## When to Use

Use when:
- a workflow lesson should be captured in a repo-local skill
- an existing skill has drifted from how the repo is actually maintained
- a skill should gain reusable `references/` docs or `scripts/` helpers
- a local-only skill and its repo-local counterpart need to stay aligned

Do not use when:
- the task is a one-off repo edit with no reusable workflow lesson
- the change belongs only in content/docs and does not alter how Bosun should operate

## Workflow

1. Inspect the existing skill surface first.
   - Read the current `SKILL.md`, linked references, and any sibling skill that overlaps.
   - For reading-list workflow changes, check both the repo-local skill and the local `work-reading-dropbox` skill when relevant.
   - Completion criterion: you can point to the exact files that should change.

2. Align with the Agent Skills spec before adding repo-local conventions.
   - Follow the required `SKILL.md` frontmatter and directory layout from the spec.
   - Prefer putting stable instructions in `SKILL.md`, longer rationale in `references/`, and reusable code in `scripts/`.
   - Completion criterion: the skill shape would still make sense to a reader who only knows the upstream Agent Skills specification.

3. Keep skills progressively disclosed.
   - Put trigger conditions, workflow steps, pitfalls, and verification in `SKILL.md`.
   - Move examples, policy notes, tagging guidance, schema details, or command recipes into `references/` when they are useful but not always needed.
   - Add a reusable helper under `scripts/` when a repeated analysis or validation step is likely to come up again.
   - Completion criterion: the main skill stays readable without losing important detail.

4. Prefer reusable scripts invoked with `go run`.
   - In this repo, prefer checked-in Go helpers for lightweight reusable scripts because `go` is available locally and `uvx` is currently unavailable.
   - If Python is the better fit, keep it as a secondary option and document why.
   - Completion criterion: any new helper script has a clear invocation example and a plausible reuse case.

5. Keep local and repo-local workflow skills in sync.
   - When the Telegram-to-reading-list workflow changes, patch both the repo-local skill(s) and the local `work-reading-dropbox` skill unless the difference is intentionally repo-specific.
   - If there is intentional divergence, say so explicitly in the repo skill or reference notes.
   - Completion criterion: future Bosun sessions do not learn conflicting versions of the same workflow.

6. Verify the skill as an artifact.
   - Check frontmatter shape, linked-file references, and script paths.
   - Run the reusable validator script when editing repo-local skills.
   - Completion criterion: the skill directory is internally consistent and committed with the repo changes it documents.

## References and Scripts

- Read `references/agentskills-spec-notes.md` for the repo's distilled interpretation of the Agent Skills specification.
- Use `scripts/validate_skill.go` to sanity-check a repo-local skill directory.

## Common Pitfalls

1. Keeping all knowledge in `SKILL.md` and turning it into a wall of text.
2. Adding one-off advice without deciding whether it belongs in docs, a skill, or a helper script.
3. Forgetting to sync the local `work-reading-dropbox` skill after changing the repo-local workflow.
4. Creating tags, policies, or file layouts inside one skill that silently disagree with another.
5. Writing a helper script with no documented invocation or no realistic reuse path.

## Verification Checklist

- [ ] Skill frontmatter matches the Agent Skills naming/description conventions
- [ ] `SKILL.md` contains only always-needed operational guidance
- [ ] Longer or branch-specific guidance is moved to `references/` when appropriate
- [ ] Reusable automation is checked into `scripts/` when it will save repeated effort
- [ ] Repo-local and local workflow skills were compared when relevant
- [ ] Skill references and script paths are valid
- [ ] Repo changes were committed alongside the skill update
