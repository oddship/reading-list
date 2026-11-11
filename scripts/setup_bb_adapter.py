"""Create optional BB loader links to portable project instructions and skills."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
adapter = root / '.bb'
(adapter / 'skills').mkdir(parents=True, exist_ok=True)
links = {adapter / 'AGENTS.md': Path('../AGENTS.md')}
links.update({adapter / 'skills' / path.name: Path('../../skills') / path.name
              for path in (root / 'skills').iterdir()
              if path.is_dir() and (path / 'SKILL.md').is_file()})
for link, target in links.items():
    if link.is_symlink() and link.readlink() == target:
        continue
    if link.exists() or link.is_symlink():
        raise SystemExit(f'Refusing to replace existing adapter entry: {link}')
    link.symlink_to(target)
print('BB adapter links are ready')
