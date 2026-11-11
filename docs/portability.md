# Moving the reading workflow

Copy the repository and its ignored `data/` directory, including any uncommitted
files. `data/` contains private logs and recovery material and must not be
published. Keep a backup before switching the active scheduler.

Install Python 3, Git, GitHub CLI and Zola 0.22.1. Authenticate `gh` on the new
host and configure Git authentication. The job process must have access to that
authentication; an interactive shell and a scheduled process can have different
environments.

Run commands from the repository root. The importer defaults to `data/`; set
`READING_LIST_DATA_DIR` to another absolute path or a path relative to the repo
when needed. Read `AGENTS.md`, discover skills under `skills/`, and use
`automation/weekly-reading.md` as the scheduled agent prompt. The schedule is
recorded in `automation/schedule.json` using five-field cron and an IANA timezone.

The weekly task requires an agent to read and curate sources. A cron or systemd
timer can launch an agent CLI, but cannot perform the task by running the prompt
file as a shell script. Choose the agent and scheduler on the new host, and
have it report in its execution session unless delivery is configured separately.

Verify the private log, import helpers, site build, GitHub access and a read-only
agent run before enabling the new schedule. Pause the old schedule at cutover.
For BB, recreate the optional loader links with
`python3 scripts/setup_bb_adapter.py` and attach the automation to the new host's
project checkout. No workflow logic lives in the adapter.
