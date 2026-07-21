# Tagging guidance for reading notes

## Goal

Keep the note taxonomy compact, reusable, and browseable.

## Rules

- Reuse an existing topic tag unless a new tag would clearly organize multiple notes better.
- Keep mechanics and source provenance in `extra.source_type` / `extra.source_url`, not in the public tag taxonomy.
- Prefer 2 to 4 meaningful topic tags per note.
- Avoid host/domain tags unless the publisher or product is itself the subject.
- If a tag will only ever apply to one note, it is probably too narrow.

## Public topic tags

Use exactly these stable public tags unless several current or future notes clearly demand a new reader-facing category:

- `agents`
- `ai-infra`
- `developer-tools`
- `llm-research`
- `org-design`
- `security`
- `systems`

## Not public tags

Never put mechanics, provenance, source type, or one-off host labels in `taxonomies.tags`.

Do not use tags like:

- `reading-log`
- `x-post`
- `article`
- `historical-backfill`
- `digest`
- `weekly-reading`
- host/domain slugs such as `example-com`

Put that information in `[extra]` fields such as `source_type`, `source_url`, `saved_link`, or digest section metadata instead.
