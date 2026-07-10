from pathlib import Path
import re

root = Path('/root/reading-list-site')
content_root = root / 'content'

for path in content_root.rglob('*.md'):
    text = path.read_text()
    new = re.sub(r'^status = ".*?"\n', '', text, flags=re.M)
    if new != text:
        path.write_text(new)
        print(path)
