---
id: py-strtxt-0001
title: "What is the difference between str and bytes in Python 3, and when would you use each?"
description: "In Python 3, str represents Unicode text and bytes represents an immutable sequence of byte values; explicit encoding or decoding crosses the boundary between them."
track: python
section: strings-and-text
level: middle
type: concept
tags: []
status: published
updated: 2026-09-08
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-08
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**`str` is an immutable sequence of Unicode code points used for text, while `bytes` is an immutable sequence of integers from 0 to 255 used for encoded text or arbitrary binary data.**[^py314-library-stdtypes] Keep text as `str` inside the program and use `bytes` at binary or protocol boundaries when the API requires it. Encoding maps `str` to `bytes` with an explicit character encoding and error policy; decoding performs the reverse. A `bytes` object does not remember which encoding, if any, produced it.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
