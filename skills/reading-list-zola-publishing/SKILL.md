---
name: reading-list-zola-publishing
description: Build and publish the Zola Reading List site. Use for template, shortcode, static-page and deployment changes.
---

# Zola publishing

Run commands from the repository root. Use Zola 0.22.1 to match CI and build with `zola build --force`. Inspect HTML for every changed route. Preserve the site's existing config, feeds, taxonomy and opt-in social embed behavior.

Use the repo's function-style tweet and YouTube shortcodes. Check that generated HTML contains the component markup rather than raw template delimiters. Keep custom feed templates and check dated section rules when a page is omitted.

Review user-facing prose, stage only intended public files, use a Conventional Commit, and push to origin main when publication is authorized. The deploy target is s3site through the `Deploy via s3site` GitHub Actions workflow. Use `gh` to verify the run for the pushed full SHA, then check the changed route and relevant index pages.

Read `AGENTS.md` first. Use paths relative to the project root. Load `skills/humanizer/SKILL.md` before publishing prose. Never use em dashes in outgoing writing.
