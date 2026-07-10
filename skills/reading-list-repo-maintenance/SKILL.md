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

2a. Preserve stable note URLs.
   - When importer-driven historical notes are regenerated, keep explicit slugs in frontmatter so title cleanup does not create Zola path collisions or unstable permalinks.
   - Completion criterion: Zola builds without path-collision errors and historical URLs remain deterministic.

3. Keep hosting context straight.
   - While GitHub Pages is the active host, `config.toml` should use `https://oddship.github.io/reading-list` as `base_url`.
   - After custom-domain cutover, switch `base_url` to `https://reading-list.oddship.net`.
   - Completion criterion: generated URLs match the active deploy target.

4. Push and verify, not just commit.
   - Use Conventional Commit messages, push to `main`, inspect the latest GitHub Actions run, and check the live page.
   - Completion criterion: the latest deploy workflow succeeded and the rendered page reflects the change.

5. Keep homepage and list UX intentional.
   - Notes pagination, digest listing, and homepage summaries should keep working after content-shape changes.
   - Completion criterion: homepage, `/notes/`, and `/digests/` render the expected cards and navigation.

6. Keep auth scoped.
   - Use the dedicated repo token env var and path-scoped git credentials for this repo only.
   - Completion criterion: automation can push without broadening GitHub access unnecessarily.

## Common Pitfalls

1. Forgetting that `base_url` controls generated links.
2. Declaring success after a push without checking the Pages workflow.
3. Checking the repo diff but not the live rendered site.
4. Mixing private reading-log concerns with public note rendering concerns.
5. Cleaning up titles without preserving slug stability, causing Zola path collisions.

## Verification Checklist

- [ ] Correct files edited
- [ ] `base_url` matches current hosting target
- [ ] Historical note slugs remain stable / collision-free
- [ ] Changes committed and pushed
- [ ] Latest Pages workflow succeeded
- [ ] Live page matches the expected output
