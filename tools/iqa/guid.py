"""Frozen Anki note GUID generation."""

from __future__ import annotations

import hashlib


GUID_SALT = "iqa:v1:"
GUID_NAMESPACE = {"uk": "", "en": "en:"}
BASE91 = (
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    "!#$%&()*+,-./:;<=>?@[]^_`{|}~"
)


def guid_for(qid: str, language: str = "uk") -> str:
    """Return the immutable Anki note GUID for a question and language."""
    namespaced = GUID_SALT + GUID_NAMESPACE[language] + qid
    digest = hashlib.sha256(namespaced.encode("utf-8")).digest()[:8]
    number = int.from_bytes(digest, "big")
    encoded = []
    while number:
        number, remainder = divmod(number, len(BASE91))
        encoded.append(BASE91[remainder])
    return "".join(reversed(encoded)) or BASE91[0]
