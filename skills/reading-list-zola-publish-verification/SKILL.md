---
name: reading-list-zola-publish-verification
description: Verify generated and deployed Reading List pages for the exact published commit. Use after content, shortcode, template or deployment changes.
---

# Publication verification

A local build alone does not verify publication. Confirm `public/<route>/index.html` exists for every changed page and that social shortcodes rendered into embed markup. Check dates in Asia/Kolkata and UTC when future-dated content is omitted.

Use the authenticated `gh` CLI to locate the `Deploy via s3site` Actions run whose `headSha` matches the full pushed commit. Wait for a successful conclusion. Check the live changed page, homepage, `/notes/` and `/digests/` as appropriate. Inspect rendered HTML when embeds or feeds changed.

Report the exact state: logged but not published, build failed, pushed but deploy failed, deploy passed but live verification blocked, or fully verified. Do not report success from an older deployment or a successful push alone.

Read `AGENTS.md` first. Use paths relative to the project root. Load `skills/humanizer/SKILL.md` before publishing prose. Never use em dashes in outgoing writing.
