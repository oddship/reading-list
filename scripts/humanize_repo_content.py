from pathlib import Path
import re

ROOT = Path('/root/reading-list-site')
TARGETS = [
    ROOT / 'content',
    ROOT / 'docs',
    ROOT / 'skills',
    ROOT / 'README.md',
]

FILES = []
for target in TARGETS:
    if target.is_file():
        FILES.append(target)
    elif target.exists():
        FILES.extend(sorted(target.rglob('*.md')))

TITLE_COLON_PATTERNS = [
    (re.compile(r'^(title\s*=\s*"Weekly reading) — '), r'\1: '),
    (re.compile(r'^(title\s*=\s*"Weekly reading draft) — '), r'\1: '),
]

LINE_REPLACEMENTS = [
    (' — ', ', '),
    ('— ', ', '),
    (' —', ', '),
    ('—', ', '),
]


def humanize_line(line: str) -> str:
    for pat, repl in TITLE_COLON_PATTERNS:
        line = pat.sub(repl, line)
    if 'title =' in line or line.startswith('#'):
        line = line.replace(' — ', ': ')
        line = line.replace('—', ': ')
    else:
        for old, new in LINE_REPLACEMENTS:
            line = line.replace(old, new)
    line = line.replace(' ,', ',')
    line = line.replace(':.', ':')
    return line

changed = []
for path in FILES:
    text = path.read_text()
    new = '\n'.join(humanize_line(line) for line in text.splitlines())
    if text.endswith('\n'):
        new += '\n'
    if new != text:
        path.write_text(new)
        changed.append(path)

print(f'changed={len(changed)}')
for path in changed[:200]:
    print(path.relative_to(ROOT))
