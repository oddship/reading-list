This is the weekly Sunday-night reading-list publishing run for the Reading List project. The goal is to proactively keep the reading-list repository and public site up to date.

Primary sources of truth and working files:
- Canonical reading log folder: data/reading-log/
- Repo checkout: the project root
- Historical importer script: scripts/import_historical_reading.py
- Repo humanizer helper: scripts/humanize_repo_content.py
- Historical OpenClaw draft folder (for older reference only when needed): data/legacy-workspace/tmp/

What to do on each run:
1. Inspect the current reading-log index and the most recent dated reading-log files under data/reading-log/.
2. When logging any new items, resolve the target day file in Asia/Kolkata, not the machine timezone, and record a `logged at IST: YYYY-MM-DD HH:MM IST` line on each new entry.
3. Ensure the repo reflects the latest local history by running the historical importer if needed (`python3 scripts/import_historical_reading.py` from the project root). This keeps notes and historical digests in sync with the local logs.
4. Create or update the current weekly digest in content/digests/ for the Monday review window immediately following this Sunday run. Base it on the week's reading-log entries. If a suitable local weekly draft already exists, reuse and refine it; otherwise draft directly from the reading logs. Keep the digest concise, publishable, and thematic.
5. If useful, make small editorial cleanups to newly affected notes/digests so titles are readable and the site stays coherent. Preserve provenance; do not claim a downstream article was read if only the X post text was available.
6. Before any commit, run the repo humanizer helper (`python3 scripts/humanize_repo_content.py`) or an equivalent pass over changed user-facing prose. Never use em dashes in outgoing writing.
7. Commit any repo changes with Conventional Commit messages.
8. Push to origin main.
9. Verify the latest s3site deploy succeeded and check the live homepage, /notes/, and /digests/ pages.
10. Report in the current execution session with a concise summary: what changed in the repo/site, what digest was created or updated, whether deploy succeeded, and whether there were no changes.

Rules:
- Treat the repo as something to keep proactively current, not just a one-off publish destination.
- Prefer the local work reading log over old Google Doc / Drive-era flow. Do not create or update Google Docs in this job.
- Preserve stable note/digest slugs when editing existing content.
- If there are no content changes, still verify and report that the repo/site were already up to date.
- Be honest about blockers.

Read AGENTS.md first. Run from the project root with its private data folder available. Load skills/humanizer/SKILL.md before publishing prose. Use the authenticated gh CLI for GitHub checks. Deployment is the Deploy via s3site Actions workflow. Report the exact commit, deployment and live-check state. Do not send external messages without an explicit delivery configuration. Do not manufacture a fresh digest when the week has no new reading; verify and report no changes.
