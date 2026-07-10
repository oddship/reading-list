# reading-list

Zola-powered reading garden for `reading-list.oddship.net`.

## Content model

- `content/notes/` — individual link notes
- `content/digests/` — periodic roundups
- `tags` taxonomy — topical navigation

Each note can carry structured metadata in `[extra]`, for example:

- `source_url`
- `source_type`
- `status`
- `why_it_matters`
- `newsletter_candidate`

## Local development

```bash
zola serve
```

## Build

```bash
zola build
```
