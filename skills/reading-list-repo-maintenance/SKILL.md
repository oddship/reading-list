---
name: reading-list-repo-maintenance
description: Use when maintaining the Zola reading-list repo, publishing notes, fixing templates, or verifying GitHub Pages deploys.
version: 1.1.0
author: Bosun
license: MIT
metadata:
  hermes:
    tags: [zola, github-pages, reading-list, repo-maintenance]
    related_skills: [telegram-reading-flow]
---

# Reading List Repo Maintenance

## Overview

This skill is for working inside the `oddship/reading-list` repo that powers the reading-list site.
It assumes the repo is a Zola site deployed through GitHub Pages and that content updates are made by editing markdown files and pushing to `main`.

## When to Use

Use when:
- adding or editing note files under `content/notes/`
- changing Zola templates or config
- fixing broken site links or rendering issues
- verifying a GitHub Pages deployment after a push

Do not use when:
- the task is only to log links privately in the work reading dropbox
- the user wants DNS or domain-management work outside the repo itself

## Workflow

1. Inspect the repo state first.
   - Read the relevant content/template/config files before editing.
   - Completion criterion: the files governing the current bug or content change are identified.

2. Make the smallest correct repo change.
   - Prefer compact markdown notes and minimal template edits.
   - Completion criterion: the repo reflects the intended user-visible change.

3. Preserve stable note URLs and keep tags coherent.
   - When importer-driven historical notes are regenerated, keep explicit slugs in frontmatter so title cleanup does not create Zola path collisions or unstable permalinks.
   - Use only the compact public topic vocabulary by default: `agents`, `ai-infra`, `developer-tools`, `llm-research`, `org-design`, `security`, `systems`, `other`.
   - Use `other` only as a temporary holding lane; if it grows past 20 notes, refile items or introduce a genuinely reusable new category.
   - Keep source type, import state, digest grouping, and host/domain labels out of `taxonomies.tags`; put them in `[extra]` metadata instead.
   - Completion criterion: Zola builds without path-collision errors and the tag vocabulary stays compact and intentional.

4. Keep hosting context straight.
   - While GitHub Pages is the active host, `config.toml` should use `https://oddship.github.io/reading-list` as `base_url`.
   - After custom-domain cutover, switch `base_url` to `https://reading-list.oddship.net`.
   - Completion criterion: generated URLs match the active deploy target.

5. Push and verify, not just commit.
   - Use Conventional Commit messages, push to `main`, inspect the latest GitHub Actions run, and check the live page.
   - Completion criterion: the latest deploy workflow succeeded and the rendered page reflects the change.

6. Keep homepage, archive UX, and feeds intentional.
   - Notes pagination, digest listing, and homepage summaries should keep working after content-shape changes.
   - Keep tiered feeds live: all-site `/rss.xml`, notes `/notes/rss.xml`, digests `/digests/rss.xml`, and per-tag `/tags/<tag>/rss.xml`.
   - Completion criterion: homepage, `/notes/`, `/digests/`, `/tags/`, and representative feeds render the expected content.

7. Run a humanizer pass before every commit.
   - Remove AI-sounding phrasing where practical, and specifically eliminate em dashes from user-facing prose unless the user asked for them.
   - Completion criterion: staged user-facing text has had a cleanup pass for voice and punctuation before commit.

8. Keep auth scoped.
   - Use the dedicated repo token env var and path-scoped git credentials for this repo only.
   - Completion criterion: automation can push without broadening GitHub access unnecessarily.

9. Keep repo-local skills in sync with live practice.
   - When a recurring workflow changes, patch the repo-local skills/docs in the same commit rather than leaving the process layer stale.
   - If the local `work-reading-dropbox` skill also changed, sync it in the same pass unless the difference is intentionally local-only.
   - Completion criterion: the repo remains a trustworthy upstream source for the workflow it describes.

## Common Pitfalls

1. Forgetting that `base_url` controls generated links.
2. Declaring success after a push without checking the Pages workflow.
3. Checking the repo diff but not the live rendered site.
4. Mixing private reading-log concerns with public note rendering concerns.
5. Cleaning up titles without preserving slug stability, causing Zola path collisions.
6. Committing user-facing prose without a humanizer pass.

## Verification Checklist

- [ ] Correct files edited
- [ ] `base_url` matches current hosting target
- [ ] Historical note slugs remain stable and collision-free
- [ ] User-facing prose got a humanizer pass
- [ ] Changes committed and pushed
- [ ] Latest Pages workflow succeeded
- [ ] Live page matches the expected output
