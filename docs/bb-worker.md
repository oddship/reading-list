# BB scheduler adapter

The workflow is defined by the root `AGENTS.md`, `skills/`, and `automation/`
files. Private source data lives in `data/`. See `portability.md` to move it.

BB loads `.bb/AGENTS.md`, a symlink to the root instructions, and project skill
symlinks under `.bb/skills/`. These links stay inside the repository. They contain
no independent workflow rules. The local adapter is ignored by Git.

The Reading List BB automation runs Sunday at 23:00 in Asia/Kolkata and reads
`AGENTS.md` and `automation/weekly-reading.md` from the existing project checkout.
The host must supply authenticated `gh` access to the scheduled process. Run
reports appear in the scheduler's execution thread.

To recreate the adapter after a move, run `python3 scripts/setup_bb_adapter.py`.
The task and private data remain usable without BB.
