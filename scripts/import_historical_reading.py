from __future__ import annotations

import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path('/root')
SITE = ROOT / 'reading-list-site'
READING_LOG = ROOT / 'work-wiki' / 'reading-log'
OLD_MEMORY = ROOT / '.openclaw' / 'workspace-rohan-work' / 'memory'
OLD_TMP = ROOT / '.openclaw' / 'workspace-rohan-work' / 'tmp'
NOTES_DIR = SITE / 'content' / 'notes'
DIGESTS_DIR = SITE / 'content' / 'digests'

MISSING_DATES = [
    '2026-05-19', '2026-05-22', '2026-05-31', '2026-06-02', '2026-06-03',
    '2026-06-04', '2026-06-08', '2026-06-09', '2026-06-10', '2026-06-11', '2026-06-12',
]

DIGEST_FILES = [
    'newsletter-draft-2026-05-10.md',
    'newsletter-draft-2026-05-10-weekly.md',
    'weekly-reading-draft-2026-05-18.md',
    'weekly-reading-draft-2026-05-25.md',
    'weekly-reading-draft-2026-06-01.md',
    'weekly-reading-draft-2026-06-08.md',
    'weekly-reading-draft-2026-06-15.md',
    'weekly-reading-draft-2026-06-22.md',
    'weekly-reading-draft-2026-06-29.md',
    'weekly-reading-draft-2026-07-06.md',
]


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r'https?://', '', text)
    text = re.sub(r'[^a-z0-9]+', '-', text)
    text = re.sub(r'-+', '-', text).strip('-')
    return text or 'item'


def escape_toml(text: str) -> str:
    return text.replace('\\', '\\\\').replace('"', '\\"')


def clean_title(text: str) -> str:
    text = re.sub(r'^[\-–—\s]+', '', text).strip()
    text = re.sub(r'^X post by\s+', '', text, flags=re.I)
    text = re.sub(r'^Post by\s+', '', text, flags=re.I)
    text = re.sub(r'^what it is:\s*', '', text, flags=re.I)
    text = text.replace('`', '')
    text = re.sub(r'\s+', ' ', text).strip(' .')
    if len(text) > 110:
        text = text[:107].rstrip() + '...'
    return text or 'Reading note'


def pick_title(entry: dict, index: int) -> str:
    if entry.get('what it is'):
        return clean_title(entry['what it is'])
    lines = entry.get('body_lines', [])
    skip_prefixes = (
        'Extracted ', 'Main post ', 'No `tweet.article`', 'Could not ', 'Tried ',
        'User context', 'Blocker:', 'Retrieval note:', 'note:', 'Good ', 'Related ',
        'Follow-up ', 'Light angle', 'The strongest practical point', 'Why it matters:'
    )
    for line in lines:
        candidate = line.strip(' -')
        if not candidate:
            continue
        if candidate.startswith(skip_prefixes):
            continue
        candidate = re.sub(r'^X post by\s+', '', candidate, flags=re.I)
        candidate = re.sub(r'^Post by\s+', '', candidate, flags=re.I)
        candidate = re.sub(r'^read (article|paper):\s*', '', candidate, flags=re.I)
        candidate = re.sub(r'^Linked article:\s*', '', candidate, flags=re.I)
        candidate = re.sub(r'^Link target:\s*', '', candidate, flags=re.I)
        candidate = candidate.strip()
        if candidate.startswith('http'):
            continue
        return clean_title(candidate)
    return f'Reading note {entry["date"]} #{index:02d}'


def extract_urls(text: str) -> list[str]:
    return re.findall(r'https?://[^\s)>,]+', text)


def choose_source_url(entry: dict) -> str:
    saved = entry['saved_link']
    for key in ('source read',):
        if entry.get(key):
            return entry[key]
    body = '\n'.join(entry.get('body_lines', []))
    urls = []
    for line in entry.get('body_lines', []):
        urls.extend(extract_urls(line))
    urls = [u.rstrip('.,') for u in urls]
    for url in urls:
        if url != saved and 'x.com/' not in url and 'twitter.com/' not in url:
            return url
    for url in urls:
        if url != saved:
            return url
    return saved


def choose_why(entry: dict) -> str:
    for key in ('why it matters', 'newsletter angle'):
        if entry.get(key):
            return entry[key]
    for line in entry.get('body_lines', []):
        low = line.lower()
        if low.startswith('why it matters:'):
            return line.split(':', 1)[1].strip()
    return ''


def tags_for(entry: dict, source_url: str) -> list[str]:
    tags = ['reading-log']
    source_type = 'x-post' if ('x.com/' in entry['saved_link'] or 'twitter.com/' in entry['saved_link']) else 'article'
    tags.append(source_type)
    host = urlparse(source_url).netloc.lower().replace('www.', '')
    if host:
        tags.append(slugify(host))
    if entry['date'] < '2026-07-08':
        tags.append('historical-backfill')
    return list(dict.fromkeys(tags))


def convert_new_style(entry: dict) -> str:
    parts = []
    if entry.get('what it is'):
        parts.append(f'**What it is:** {entry["what it is"]}')
    if entry.get('gist'):
        parts.append(f'**Gist:** {entry["gist"]}')
    if entry.get('notable line'):
        parts.append(f'**Notable line:** {entry["notable line"]}')
    if entry.get('newsletter angle'):
        parts.append(f'**Newsletter angle:** {entry["newsletter angle"]}')
    if entry.get('retrieval note'):
        parts.append(f'**Retrieval note:** {entry["retrieval note"]}')
    if entry.get('note'):
        parts.append(f'**Note:** {entry["note"]}')
    return '\n\n'.join(parts).strip() + '\n'


def convert_old_style(entry: dict) -> str:
    lines = [line.rstrip() for line in entry.get('body_lines', []) if line.strip()]
    if not lines:
        return 'Imported from historical reading log.\n'
    body = ['Imported from historical reading log.']
    for line in lines:
        body.append(f'- {line.strip(" -")}')
    return '\n'.join(body) + '\n'


def parse_date_file(path: Path) -> list[dict]:
    text = path.read_text()
    lines = text.splitlines()
    entries = []
    current = None
    structured = False
    for raw in lines:
        if raw.startswith('- ') and re.search(r'\b(?:saved link|saved):\s*', raw, flags=re.I):
            if current:
                entries.append(current)
            structured = True
            current = {'date': path.stem, 'saved_link': re.split(r'\b(?:saved link|saved):\s*', raw, maxsplit=1, flags=re.I)[1].strip(), 'body_lines': []}
            continue
        if raw.startswith('- ') and 'Reading list topic `Reading list`' in raw:
            if current:
                entries.append(current)
            structured = False
            saved = raw.split('—', 1)[1].strip() if '—' in raw else raw
            current = {'date': path.stem, 'saved_link': saved, 'body_lines': []}
            continue
        if not current:
            continue
        if structured and raw.startswith('  - '):
            key, _, value = raw[4:].partition(': ')
            if _:
                current[key.strip()] = value.strip()
            else:
                current['body_lines'].append(raw[4:].strip())
        elif not structured and raw.startswith('  - '):
            current['body_lines'].append(raw[4:].rstrip())
    if current:
        entries.append(current)
    return entries


def backfill_missing_logs() -> None:
    for date in MISSING_DATES:
        src = OLD_MEMORY / f'{date}.md'
        dst = READING_LOG / f'{date}.md'
        raw = src.read_text().splitlines()
        body = raw[2:] if raw and raw[0].startswith('# ') else raw
        content = [
            f'# Work reading log — {date}',
            '',
            '## Backfilled history',
            '',
            '- provenance: backfilled from old OpenClaw work workspace on 2026-07-10',
            f'- source: `{src}`',
            '- note: wording below is preserved as closely as possible from the historical log',
            '',
        ] + body
        dst.write_text('\n'.join(content).rstrip() + '\n')


def rebuild_index() -> None:
    date_files = sorted(p for p in READING_LOG.glob('2026-*.md') if p.name != 'INDEX.md')
    rows = []
    total_entries = 0
    for p in date_files:
        count = len(parse_date_file(p))
        total_entries += count
        note = 'Imported OpenClaw memory backfill' if p.stem in MISSING_DATES else 'Reading log / earlier backfill'
        rows.append((p.stem, count, note))
    lines = [
        '# Work reading log index',
        '',
        '## Coverage summary',
        '',
        '| Date | Entries | Notes |',
        '|---|---:|---|',
    ]
    for date, count, note in rows:
        lines.append(f'| {date} | {count} | {note} |')
    lines += [
        '',
        '## Totals',
        '',
        f'- Files: **{len(rows)}**',
        f'- Logged entries: **{total_entries}**',
        f'- Coverage window: **{rows[0][0]} → {rows[-1][0]}**',
        '',
        '## Usage note',
        '',
        'Use this index to find the right day file quickly. For actual reading notes and link details, open the dated markdown file directly.',
    ]
    (READING_LOG / 'INDEX.md').write_text('\n'.join(lines) + '\n')


def write_notes() -> int:
    for p in NOTES_DIR.glob('*.md'):
        if p.name != '_index.md':
            p.unlink()
    count = 0
    slug_counts = Counter()
    for date_file in sorted(p for p in READING_LOG.glob('2026-*.md') if p.name != 'INDEX.md'):
        entries = parse_date_file(date_file)
        for idx, entry in enumerate(entries, start=1):
            title = pick_title(entry, idx)
            source_url = choose_source_url(entry)
            why = choose_why(entry)
            tags = tags_for(entry, source_url)
            base_slug = slugify(f"{entry['date']}-{title}")[:90].strip('-')
            slug_counts[base_slug] += 1
            slug = base_slug if slug_counts[base_slug] == 1 else f'{base_slug}-{slug_counts[base_slug]}'
            source_type = 'x-post' if ('x.com/' in entry['saved_link'] or 'twitter.com/' in entry['saved_link']) else 'article'
            body = convert_new_style(entry) if entry.get('what it is') or entry.get('gist') else convert_old_style(entry)
            frontmatter = [
                '+++',
                f'title = "{escape_toml(title)}"',
                f'date = {entry["date"]}',
                '[taxonomies]',
                'tags = [' + ', '.join(f'"{escape_toml(t)}"' for t in tags) + ']',
                '[extra]',
                f'source_url = "{escape_toml(source_url)}"',
                f'source_type = "{source_type}"',
                'status = "published"',
                'newsletter_candidate = true',
                f'why_it_matters = "{escape_toml(why)}"',
                f'saved_link = "{escape_toml(entry["saved_link"])}"',
                '+++',
                '',
            ]
            (NOTES_DIR / f'{slug}.md').write_text('\n'.join(frontmatter) + body)
            count += 1
    return count


def write_digests() -> int:
    for p in DIGESTS_DIR.glob('*.md'):
        if p.name != '_index.md':
            p.unlink()
    count = 0
    for name in DIGEST_FILES:
        src = OLD_TMP / name
        if not src.exists():
            continue
        text = src.read_text()
        lines = text.splitlines()
        title = lines[0].lstrip('# ').strip() if lines else name
        body = '\n'.join(lines[1:]).lstrip() + '\n'
        m = re.search(r'(20\d\d-\d\d-\d\d)', name)
        date = m.group(1) if m else '2026-01-01'
        kind = 'newsletter' if 'newsletter' in name else 'weekly-reading'
        slug = slugify(f'{date}-{title}')[:100]
        frontmatter = [
            '+++',
            f'title = "{escape_toml(title)}"',
            f'date = {date}',
            '[taxonomies]',
            f'tags = ["digest", "{kind}", "historical-backfill"]',
            '[extra]',
            f'source_file = "{escape_toml(str(src))}"',
            'status = "published"',
            '+++',
            '',
        ]
        (DIGESTS_DIR / f'{slug}.md').write_text('\n'.join(frontmatter) + body)
        count += 1
    return count


def main() -> None:
    backfill_missing_logs()
    rebuild_index()
    notes = write_notes()
    digests = write_digests()
    print(f'notes={notes}')
    print(f'digests={digests}')


if __name__ == '__main__':
    main()
