#!/usr/bin/env python3
"""Insert tweet/YouTube component embeds after bare social links in content markdown.

Conservative and idempotent:
- only edits content/*.md files
- preserves the original clickable link above the embed
- dedupes semantically by tweet status id or YouTube video id, so canonical and shared URLs do not create duplicate embeds
"""
from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import urlparse, parse_qs

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"

URL_RE = re.compile(r"https?://[^\s<>)\]\"']+")
TWEET_RE = re.compile(r"https?://(?:www\.)?(?:x|twitter)\.com/(?:i/status|[^/\s]+/status)/(\d+)(?:[^\s<>)\]\"']*)?")
YOUTUBE_HOSTS = {"youtube.com", "www.youtube.com", "m.youtube.com", "youtu.be", "www.youtu.be"}
FRONTMATTER_RE = re.compile(r"\+\+\+\n(.*?)\n\+\+\+", re.S)
FM_URL_RE = re.compile(r"(?:source_url|saved_link|related_url)\s*=\s*\"(https?://[^\"]+)\"")
FM_RELATED_URLS_RE = re.compile(r"related_urls\s*=\s*\[(.*?)\]", re.S)
TWEET_SHORTCODE_RE = re.compile(r'^\s*\{\{(?:\s*tweet\(url="([^"]+)"\)\s*|<tweet(?:\s+id="([^"]+)")?\s+url="([^"]+)"\s*/>)\}\}\s*$')
YOUTUBE_SHORTCODE_RE = re.compile(r'^\s*\{\{(?:\s*youtube\(id="([^"]+)"(?:,\s*url="([^"]+)")?\)\s*|<youtube\s+id="([^"]+)"(?:\s+url="([^"]+)")?\s*/>)\}\}\s*$')


def clean_url(url: str) -> str:
    return url.rstrip(".,;:")


def tweet_id(url: str) -> str | None:
    match = TWEET_RE.match(clean_url(url))
    return match.group(1) if match else None


def youtube_id(url: str) -> str | None:
    parsed = urlparse(clean_url(url))
    host = parsed.netloc.lower()
    if host not in YOUTUBE_HOSTS:
        return None
    if host.endswith("youtu.be"):
        candidate = parsed.path.strip("/").split("/")[0]
        return candidate or None
    if parsed.path == "/watch":
        return parse_qs(parsed.query).get("v", [None])[0]
    for prefix in ("/embed/", "/shorts/", "/live/"):
        if parsed.path.startswith(prefix):
            candidate = parsed.path[len(prefix):].split("/")[0]
            return candidate or None
    return None


def embed_key_for_url(url: str) -> tuple[str, str] | None:
    tid = tweet_id(url)
    if tid:
        return ("tweet", tid)
    yid = youtube_id(url)
    if yid:
        return ("youtube", yid)
    return None


def shortcode_key(line: str) -> tuple[str, str] | None:
    match = TWEET_SHORTCODE_RE.match(line)
    if match:
        explicit_id = match.group(2)
        url = match.group(1) or match.group(3)
        tid = explicit_id or tweet_id(url)
        return ("tweet", tid) if tid else None
    match = YOUTUBE_SHORTCODE_RE.match(line)
    if match:
        yid = match.group(1) or match.group(3)
        return ("youtube", yid) if yid else None
    return None


def normalize_shortcode(line: str) -> str:
    match = TWEET_SHORTCODE_RE.match(line)
    if match:
        url = clean_url(match.group(1) or match.group(3))
        tid = match.group(2) or tweet_id(url)
        if tid:
            return '{{<tweet id="' + tid + '" url="' + url + '"/>}}'
    return line


def embed_for(url: str) -> str | None:
    url = clean_url(url)
    tid = tweet_id(url)
    if tid:
        return '{{<tweet id="' + tid + '" url="' + url + '"/>}}'
    vid = youtube_id(url)
    if vid:
        return '{{<youtube id="' + vid + '" url="' + url + '"/>}}'
    return None


def frontmatter_urls(text: str) -> list[str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return []
    fm = match.group(1)
    urls = FM_URL_RE.findall(fm)
    for related_match in FM_RELATED_URLS_RE.findall(fm):
        urls.extend(re.findall(r'"(https?://[^\"]+)"', related_match))
    return urls


def already_followed_by_embed(lines: list[str], index: int, key: tuple[str, str]) -> bool:
    for lookahead in lines[index + 1:index + 5]:
        stripped = lookahead.strip()
        if not stripped:
            continue
        return shortcode_key(stripped) == key
    return False


def process_file(path: Path) -> tuple[bool, int, int]:
    text = path.read_text()
    lines = text.splitlines()
    changed = False
    inserted = 0
    removed = 0
    out: list[str] = []
    seen_keys: set[tuple[str, str]] = set()

    in_frontmatter = False
    fence_count = 0
    for i, line in enumerate(lines):
        key = shortcode_key(line)
        if key:
            normalized = normalize_shortcode(line)
            if normalized != line:
                changed = True
            if key in seen_keys:
                changed = True
                removed += 1
                if out and out[-1] == "":
                    out.pop()
                continue
            seen_keys.add(key)
            out.append(normalized)
            continue

        out.append(line)
        if i == 0 and line.strip() == "+++":
            in_frontmatter = True
            fence_count = 1
            continue
        if in_frontmatter:
            if line.strip() == "+++":
                fence_count += 1
                if fence_count == 2:
                    in_frontmatter = False
            continue

        embeds: list[tuple[tuple[str, str], str]] = []
        for url in URL_RE.findall(line):
            key = embed_key_for_url(url)
            embed = embed_for(url) if key else None
            if key is not None and embed and key not in seen_keys and key not in [k for k, _ in embeds] and not already_followed_by_embed(lines, i, key):
                embeds.append((key, embed))
        if embeds:
            out.append("")
            for key, embed in embeds:
                out.append(embed)
                seen_keys.add(key)
                inserted += 1
            changed = True

    text2 = "\n".join(out) + ("\n" if text.endswith("\n") else "")

    appendix = []
    for url in frontmatter_urls(text2):
        key = embed_key_for_url(url)
        embed = embed_for(url) if key else None
        if embed and key not in seen_keys and key not in [k for k, _ in appendix]:
            appendix.append((key, embed))
    if appendix:
        if not text2.endswith("\n"):
            text2 += "\n"
        text2 += "\n## Embedded source\n\n" + "\n\n".join(embed for _, embed in appendix) + "\n"
        changed = True
        inserted += len(appendix)

    if changed:
        path.write_text(text2)
    return changed, inserted, removed


def main() -> None:
    changed_files = embeds = removed = 0
    for path in sorted(CONTENT.rglob("*.md")):
        changed, ins, rem = process_file(path)
        if changed:
            changed_files += 1
            embeds += ins
            removed += rem
            print(f"{path.relative_to(ROOT)}: +{ins} -{rem}")
    print(f"changed_files={changed_files} embeds_inserted={embeds} embeds_removed={removed}")


if __name__ == "__main__":
    main()
