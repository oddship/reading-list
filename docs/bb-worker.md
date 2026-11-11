# BB worker operation

The Reading List BB project runs in `/workspace/reading-list` on `archon-bb-worker`.
It replaces the Hermes weekly reading-list job. The BB schedule runs Sunday at
23:00 in `Asia/Kolkata`.

The private source log is `.reading-list/reading-log/`. Historical work memory,
weekly drafts, imported Hermes skills and prior run output live under
`.reading-list/`. That directory is excluded locally from Git and must remain
private. The original source snapshot and file manifest are retained there for
recovery. Do not use a fresh worktree for scheduled runs because it lacks this
private data.

BB loads project instructions from `.bb/AGENTS.md` and project skills from
`.bb/skills/`. The weekly prompt is `.bb/weekly-reading.md`. Add new reading links
in the BB project. Run reports appear in BB; the old Telegram topic is not a BB
input or delivery transport.

Use `gh` in the authenticated BB execution session. Git uses `gh auth
git-credential`; no Hermes publishing token is needed. Build with Zola 0.22.1,
which matches CI. The site deploys through GitHub Actions to s3site and is served
at https://reading-list.oddship.net/.

The migration retains the source server's unpushed November 9 digest commit and
two untracked October 5 notes. Review them before publishing. Migration checks
do not publish content.
