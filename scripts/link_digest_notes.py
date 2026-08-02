#!/usr/bin/env python3
"""Add links from digest source URLs back to their public reading notes.

The script builds a URL -> note map from content/notes/*.md frontmatter
(extra.source_url, extra.saved_link, extra.related_url, extra.related_urls), then
adds compact "Reading note(s)" links to digest entries that cite those URLs.
It is idempotent and only touches content/digests/*.md.
"""
from __future__ import annotations

import argparse
import re
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTES_DIR = ROOT / "content" / "notes"
DIGESTS_DIR = ROOT / "content" / "digests"
FRONTMATTER = re.compile(r"^\+\+\+\n(.*?)\n\+\+\+\n", re.S)
BARE_URL_LINE = re.compile(r"^(?P<prefix>\s*)<(?P<url>https?://[^>]+)>\s*$")
ANY_ANGLE_URL = re.compile(r"<(?P<url>https?://[^>]+)>")
READING_NOTE_RE = re.compile(r"Reading notes?:", re.I)


def normalize_url(url: str) -> str:
    return url.strip().rstrip("/")


def load_note_map() -> dict[str, dict[str, str]]:
    mapping: dict[str, dict[str, str]] = {}
    for path in sorted(NOTES_DIR.glob("*.md")):
        text = path.read_text()
        match = FRONTMATTER.match(text)
        if not match:
            continue
        try:
            meta = tomllib.loads(match.group(1))
        except tomllib.TOMLDecodeError as exc:
            raise SystemExit(f"Bad frontmatter in {path}: {exc}") from exc
        slug = meta.get("slug") or path.stem
        title = meta.get("title") or slug
        note = {"slug": slug, "title": title, "url": f"/notes/{slug}/"}
        extra = meta.get("extra", {}) or {}
        urls: list[str] = []
        for key in ("source_url", "saved_link", "related_url"):
            value = extra.get(key)
            if isinstance(value, str):
                urls.append(value)
        related_urls = extra.get("related_urls", [])
        if isinstance(related_urls, list):
            urls.extend(value for value in related_urls if isinstance(value, str))
        for url in urls:
            mapping.setdefault(normalize_url(url), note)
    return mapping


def note_link(note: dict[str, str]) -> str:
    title = note["title"].replace("[", "").replace("]", "")
    return f"[{title}]({note['url']})"


def reading_note_line(notes: list[dict[str, str]]) -> str:
    label = "Reading note" if len(notes) == 1 else "Reading notes"
    return f"_{label}: {', '.join(note_link(note) for note in notes)}_"


def dedupe_notes(notes: list[dict[str, str]]) -> list[dict[str, str]]:
    seen: set[str] = set()
    out: list[dict[str, str]] = []
    for note in notes:
        if note["slug"] in seen:
            continue
        seen.add(note["slug"])
        out.append(note)
    return out


def process_digest(path: Path, url_to_note: dict[str, dict[str, str]], *, dry_run: bool) -> bool:
    lines = path.read_text().splitlines()
    out: list[str] = []
    changed = False
    i = 0
    while i < len(lines):
        bare = BARE_URL_LINE.match(lines[i])
        if bare:
            block: list[str] = []
            notes: list[dict[str, str]] = []
            indent = bare.group("prefix")
            while i < len(lines):
                m = BARE_URL_LINE.match(lines[i])
                if not m:
                    break
                block.append(lines[i])
                note = url_to_note.get(normalize_url(m.group("url")))
                if note:
                    notes.append(note)
                i += 1
            out.extend(block)
            notes = dedupe_notes(notes)
            next_line = lines[i].strip() if i < len(lines) else ""
            if notes and not READING_NOTE_RE.search(next_line):
                out.append(f"{indent}{reading_note_line(notes)}")
                changed = True
            continue

        line = lines[i]
        if not READING_NOTE_RE.search(line):
            notes = dedupe_notes(
                [url_to_note[normalize_url(m.group("url"))] for m in ANY_ANGLE_URL.finditer(line) if normalize_url(m.group("url")) in url_to_note]
            )
            if notes:
                suffix = " " + reading_note_line(notes)
                line = line + suffix
                changed = True
        out.append(line)
        i += 1

    if changed and not dry_run:
        path.write_text("\n".join(out) + "\n")
    return changed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path, help="Digest markdown files to update. Defaults to all digests.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    url_to_note = load_note_map()
    paths = args.paths or sorted(DIGESTS_DIR.glob("*.md"))
    changed = []
    for path in paths:
        if path.name == "_index.md":
            continue
        if process_digest(path, url_to_note, dry_run=args.dry_run):
            changed.append(str(path.relative_to(ROOT)))
    for path in changed:
        print(path)
    print(f"changed={len(changed)}")


if __name__ == "__main__":
    main()
