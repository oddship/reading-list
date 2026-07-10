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

TOPIC_RULES = [
    ('agents', ['agent', 'agentic', 'subagent', 'orchestr', 'harness', 'workflow', 'mcp']),
    ('ai-infra', ['inference', 'serving', 'latency', 'gpu', 'distributed', 'proxy', 'runtime']),
    ('security', ['security', 'auth', 'authorization', 'identity', 'privacy', 'vuln', 'supply-chain', 'prompt injection']),
    ('developer-tools', ['cli', 'tooling', 'git', 'playwright', 'sdk', 'diff viewer', 'editor']),
    ('org-design', ['org', 'organization', 'culture', 'team', 'staff engineer', 'product engineer', 'management']),
    ('llm-research', ['llm', 'model', 'benchmark', 'training', 'eval', 'reasoning', 'context window', 'interpretability']),
    ('systems', ['consensus', 'dns', 'load balancing', 'cache locality', 'wan', 'profiling', 'microvm']),
]

TITLE_NOISE_PREFIXES = [
    r'^x post by\s+[^ ]+\s+',
    r'^x thread by\s+[^ ]+\s+',
    r'^post by\s+[^ ]+\s+',
    r'^x post from\s+[^ ]+\s+',
    r'^x reply from\s+[^ ]+\s+',
    r'^(?:an?\s+)?x\s+(?:post|thread|reply)\s+',
]

LEADING_VERB_PHRASES = [
    'linking to ', 'sharing ', 'pointing to ', 'announcing ', 'quoting ', 'quoting and pointing to ',
    'recommending ', 'revisiting ', 'summarizing ', 'describing ', 'explaining ', 'reacting to ',
    'boosting ', 'praising ', 'introducing ', 'kicking off ', 'highlighting ',
]


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r'https?://', '', text)
    text = re.sub(r'[^a-z0-9]+', '-', text)
    text = re.sub(r'-+', '-', text).strip('-')
    return text or 'item'


def escape_toml(text: str) -> str:
    return text.replace('\\', '\\\\').replace('"', '\\"')


def extract_urls(text: str) -> list[str]:
    return re.findall(r'https?://[^\s)>,]+', text)


def normalize_whitespace(text: str) -> str:
    return re.sub(r'\s+', ' ', text).strip()


def normalize_title_phrase(text: str) -> str:
    text = normalize_whitespace(text.replace('`', ''))
    for pattern in TITLE_NOISE_PREFIXES:
        text = re.sub(pattern, '', text, flags=re.I)
    for phrase in LEADING_VERB_PHRASES:
        text = re.sub(r'^' + re.escape(phrase), '', text, flags=re.I)
    text = re.sub(r'^(the |a |an )', '', text, flags=re.I)
    text = re.sub(r'^on\s+', '', text, flags=re.I)
    text = text.strip(' .:-–—')
    return text


def quoted_fragments(text: str) -> list[str]:
    fragments = []
    for pattern in [r'“([^”]{4,140})”', r'"([^"\n]{4,140})"', r'`([^`\n]{3,140})`']:
        fragments.extend(re.findall(pattern, text))
    return [normalize_title_phrase(f) for f in fragments if normalize_title_phrase(f)]


def prefer_fragment(fragment: str) -> bool:
    bad = ['https://', 'http://', 'x.com/', 'twitter.com/', 'github.com/']
    if any(b in fragment for b in bad):
        return False
    if '.' in fragment and ' ' not in fragment:
        return False
    return True


def host_tag(url: str) -> str | None:
    host = urlparse(url).netloc.lower().replace('www.', '')
    return slugify(host) if host else None


def infer_title_from_url(url: str) -> str | None:
    parsed = urlparse(url)
    if not parsed.path or parsed.path == '/':
        return None
    parts = [p for p in parsed.path.split('/') if p]
    if not parts:
        return None
    last = parts[-1]
    if last.isdigit() and len(parts) > 1:
        last = parts[-2]
    last = re.sub(r'\.[a-z0-9]+$', '', last)
    if last in {'i', 'status', 'p'}:
        return None
    title = last.replace('-', ' ').replace('_', ' ')
    title = normalize_title_phrase(title)
    if len(title) < 4:
        return None
    return title.title()


def clean_title(text: str) -> str:
    text = normalize_title_phrase(text)
    if len(text) > 110:
        text = text[:107].rstrip() + '...'
    return text or 'Reading note'


def entry_value(entry: dict, *keys: str) -> str:
    for key in keys:
        if entry.get(key):
            return str(entry[key]).strip()
    return ''


def first_meaningful_line(entry: dict) -> str:
    skip_prefixes = (
        'Extracted ', 'Main post ', 'No `tweet.article`', 'Could not ', 'Tried ',
        'User context', 'Blocker:', 'Retrieval note:', 'note:', 'Good ', 'Related ',
        'Follow-up ', 'Light angle', 'The strongest practical point', 'Why it matters:',
        'Newsletter angle:', 'retrieval:', 'retrieval note:'
    )
    for line in entry.get('body_lines', []):
        candidate = normalize_whitespace(line.strip(' -'))
        if not candidate:
            continue
        if candidate.lower().startswith(tuple(s.lower() for s in skip_prefixes)):
            continue
        return candidate
    return ''


def pick_title(entry: dict, index: int) -> str:
    direct = entry_value(entry, 'what it is', 'what', 'source')
    source_url = choose_source_url(entry)

    for candidate in [direct, first_meaningful_line(entry), entry_value(entry, 'gist')]:
        if not candidate:
            continue
        for frag in quoted_fragments(candidate):
            if prefer_fragment(frag):
                return clean_title(frag)
        normalized = normalize_title_phrase(candidate)
        if normalized and len(normalized) >= 6 and not normalized.lower().startswith('reading note'):
            return clean_title(normalized)

    for line in entry.get('body_lines', []):
        for frag in quoted_fragments(line):
            if prefer_fragment(frag):
                return clean_title(frag)

    if source_url and source_url != entry['saved_link']:
        guessed = infer_title_from_url(source_url)
        if guessed:
            return clean_title(guessed)

    guessed = infer_title_from_url(entry['saved_link'])
    if guessed:
        return clean_title(guessed)

    return f'Reading note {entry["date"]} #{index:02d}'


def choose_source_url(entry: dict) -> str:
    saved = entry['saved_link']
    for key in ('source read',):
        if entry.get(key):
            return entry[key]
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


def tags_for(entry: dict, source_url: str, title: str, why: str) -> list[str]:
    saved = entry['saved_link']
    source_type = 'x-post' if ('x.com/' in saved or 'twitter.com/' in saved) else 'article'
    tags = ['reading-log', source_type]
    for url in [source_url, saved]:
        tag = host_tag(url)
        if tag and tag not in {'x-com'}:
            tags.append(tag)
    if entry['date'] < '2026-07-08':
        tags.append('historical-backfill')

    blob = ' '.join([
        title,
        why,
        entry_value(entry, 'gist'),
        entry_value(entry, 'what it is', 'what', 'source'),
        ' '.join(entry.get('body_lines', [])),
    ]).lower()
    for tag, needles in TOPIC_RULES:
        if any(n in blob for n in needles):
            tags.append(tag)
    return list(dict.fromkeys(tags))


def convert_new_style(entry: dict) -> str:
    parts = []
    what = entry_value(entry, 'what it is', 'what', 'source')
    if entry.get('logged at ist'):
        parts.append(f'**Logged at IST:** {entry["logged at ist"]}')
    if what:
        parts.append(f'**What it is:** {what}')
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
    if entry.get('notes'):
        parts.append(f'**Notes:** {entry["notes"]}')
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
    known_keys = {
        'what it is', 'what', 'source', 'gist', 'why it matters', 'newsletter angle',
        'retrieval note', 'note', 'notes', 'notable line', 'source read', 'retrieval', 'follow-up', 'logged at ist'
    }
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
            line = raw[4:].strip()
            key, _, value = line.partition(': ')
            key_l = key.strip().lower()
            value = value.strip()
            if _ and key_l in known_keys:
                current[key_l] = value
            elif _ and value.startswith('http'):
                current.setdefault('what it is', key.strip())
                current.setdefault('source read', value)
            else:
                current['body_lines'].append(line)
                if _ and 'what it is' not in current:
                    current['what it is'] = line
        elif not structured and raw.startswith('  - '):
            current['body_lines'].append(raw[4:].rstrip())
        elif current and raw.startswith('- '):
            current['body_lines'].append(raw[2:].rstrip())
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
            tags = tags_for(entry, source_url, title, why)
            base_slug = slugify(f"{entry['date']}-{title}")[:110].strip('-')
            slug_counts[base_slug] += 1
            slug = base_slug if slug_counts[base_slug] == 1 else f'{base_slug}-{slug_counts[base_slug]}'
            source_type = 'x-post' if ('x.com/' in entry['saved_link'] or 'twitter.com/' in entry['saved_link']) else 'article'
            body = convert_new_style(entry) if any(entry.get(k) for k in ['what it is', 'what', 'source', 'gist', 'newsletter angle', 'retrieval note', 'note', 'notes']) else convert_old_style(entry)
            frontmatter = [
                '+++',
                f'title = "{escape_toml(title)}"',
                f'slug = "{escape_toml(slug)}"',
                f'date = {entry["date"]}',
                '[taxonomies]',
                'tags = [' + ', '.join(f'"{escape_toml(t)}"' for t in tags) + ']',
                '[extra]',
                f'source_url = "{escape_toml(source_url)}"',
                f'source_type = "{source_type}"',
                'newsletter_candidate = true',
                f'why_it_matters = "{escape_toml(why)}"',
                f'saved_link = "{escape_toml(entry["saved_link"])}"',
                '+++',
                '',
            ]
            (NOTES_DIR / f'{slug}.md').write_text('\n'.join(frontmatter) + body)
            count += 1
    return count


def _autolink_digest_lines(lines: list[str]) -> str:
    linked = []
    for line in lines:
        stripped = line.strip()
        if re.fullmatch(r'https?://\S+', stripped):
            linked.append(f'<{stripped}>')
            continue
        if re.fullmatch(r'-\s+https?://\S+.*', stripped):
            prefix, url = stripped.split(' ', 1)
            linked.append(f'{prefix} <{url}>')
            continue
        linked.append(line)
    return '\n'.join(linked).lstrip() + '\n'


def _normalize_digest_body(body: str) -> str:
    if not body.lstrip().startswith('## '):
        body = '## Intro\n\n' + body.lstrip()
    replacements = {
        '## Closing\n': '## Closing note\n',
        '## Possible title alternatives\n': '## Possible titles\n',
        '## 7. My current thesis\n': '## Closing note\n',
        '## Links and notes\n': '## Also worth saving\n',
    }
    for old, new in replacements.items():
        body = body.replace(old, new)
    body = re.sub(r'\n## Possible titles\n(?:\n?- .*?)+\n?$', '\n', body, flags=re.S)
    return body.rstrip() + '\n'


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
        if title.startswith('Weekly reading draft — '):
            title = title.replace('Weekly reading draft — ', 'Weekly reading — ', 1)
        body = _normalize_digest_body(_autolink_digest_lines(lines[1:]))
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
