"""Read the track and section tree out of ``meta/taxonomy.md``, in order.

``meta/taxonomy.md`` is the single declaration of which tracks and sections
exist and in what order they are meant to be read. Two consumers need it and
they need different shapes of the same answer: the validator asks "does this
path exist" (a set), the mirror asks "what comes after what" (a sequence).

Both come from this one parser so the file is not read two ways. The order is
the order the lines appear in the fenced blocks - that is what the document
means by an ordered tree, and it is why the site navigation must not sort
alphabetically.
"""

from __future__ import annotations

from pathlib import Path
import re


_ENTRY_RE = re.compile(r"^(?P<indent> *)(?P<name>[a-z0-9][a-z0-9-]*)/")
_BLOCK_RE = re.compile(r"(?ms)^```[^\r\n]*\r?\n(.*?)^```[ \t]*$")


def ordered_paths(path: Path) -> list[str]:
    """Every ``track`` and ``track/section`` path in the file, in document order.

    Deduplicated while keeping the first occurrence: a track heading its own
    block and then reappearing inside another block must not move.
    """
    text = path.read_text(encoding="utf-8")
    seen: dict[str, None] = {}
    for block in _BLOCK_RE.findall(text):
        stack: list[tuple[int, str]] = []
        for line in block.splitlines():
            match = _ENTRY_RE.match(line)
            if not match:
                continue
            indent = len(match.group("indent"))
            name = match.group("name")
            while stack and stack[-1][0] >= indent:
                stack.pop()
            stack.append((indent, name))
            candidate = "/".join(item[1] for item in stack)
            if candidate != "content":
                seen.setdefault(candidate, None)
    return list(seen)


def ordered_tracks_and_sections(path: Path) -> list[tuple[str, list[str]]]:
    """``[(track, [section, ...]), ...]`` in document order.

    Only two levels: the site navigation the taxonomy feeds is track then
    section, and a deeper path (``cpp/frameworks/qt``) is carried by its
    section entry rather than becoming a third level of menu.
    """
    tracks: dict[str, list[str]] = {}
    for candidate in ordered_paths(path):
        parts = candidate.split("/")
        if len(parts) == 1:
            tracks.setdefault(parts[0], [])
        elif len(parts) == 2:
            sections = tracks.setdefault(parts[0], [])
            if parts[1] not in sections:
                sections.append(parts[1])
    return list(tracks.items())
