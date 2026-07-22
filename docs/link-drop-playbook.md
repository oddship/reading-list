# Link Drop Playbook

Use this for normal useful reading links dropped in Rohan's work Telegram thread.

## Default rule

Publish by default. A useful link drop is not complete when it is only logged locally. It is complete when the public reading-list site has the note live, or when a blocker is reported precisely.

Only keep an item log-only when:

- Rohan clearly asks for private/backlog-only capture
- source access is too weak for a grounded public note
- publishing would require an unusual public, destructive, or high-risk change

## Required path

1. Read the strongest accessible source.
   - For X posts, inspect the post and attached media.
   - If the post points to an article, blog, paper, repo, or video, follow that source when feasible.
   - Preserve retrieval blockers instead of pretending the source was read.
2. Append the compact entry to `/root/work-wiki/reading-log/YYYY-MM-DD.md` using the IST date and timestamp.
3. Dedupe against existing `content/notes/` by source URL, saved link, and likely title.
4. Create or update a note under `content/notes/` with:
   - full IST datetime in `date`
   - approved public tags only
   - `[extra].source_url`
   - `[extra].source_type`
   - `[extra].newsletter_candidate`
   - `[extra].why_it_matters`
   - `[extra].saved_link`
5. Run `python3 scripts/humanize_repo_content.py`.
6. Build the site with Zola. If `zola` is not globally installed, use an available release binary or the CI-equivalent build path.
7. Commit with a Conventional Commit.
8. Push to `main`.
9. Check the deploy run for the pushed `HEAD` SHA.
10. Verify the live note URL or `https://reading-list.oddship.net/notes/`.

## Reporting states

Use precise states in chat:

- `logged and published` when the live site was verified
- `logged but not published` when no note reached the repo
- `note written but build failed` when Zola failed
- `pushed but deploy failed` when CI/deploy failed
- `deploy passed but live verification blocked` when the deploy succeeded but the live fetch/browser check failed

Do not say only "logged" for a useful work-thread link unless it was intentionally backlog-only.

## Skill sync rule

When this workflow changes, update all of these in the same commit where practical:

- `skills/telegram-reading-flow/SKILL.md`
- `skills/reading-list-repo-maintenance/SKILL.md`
- `docs/maintainer-guide.md`
- `docs/link-drop-playbook.md`

Also patch the local Hermes skill `work-reading-dropbox` when the change affects Telegram intake behavior.