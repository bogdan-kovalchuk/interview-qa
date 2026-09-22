---
id: py-objtypes-0017
title: "How does `str` differ from `bytes`, and at which boundary of a program should encode/decode happen?"
description: "How does `str` differ from `bytes`, and at which boundary of a program should encode/decode happen?"
track: python
section: objects-and-types
level: middle
type: comparison
tags: [str, bytes]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-typing
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/data_types.md#L498-L586
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`str` is an immutable sequence of Unicode code points (text), while `bytes` is an immutable sequence of 8-bit integers (binary data); they are not directly compatible and require explicit encode/decode.**[^py314-reference-datamodel] Encode/decode must take place at the program boundaries: decode external input (files, network, CLI) into internal `str`, and encode `str` to `bytes` when sending data out. <span class="warn">Mixing `str` and `bytes` in operations raises `TypeError`, and implicit conversions inside business logic lead to bugs when default encodings change.</span>

## Detailed explanation

`str` represents human-readable text as an immutable sequence of abstract Unicode code points (characters), whereas `bytes` represents raw binary data as an immutable sequence of integers in the range 0–255.[^py314-reference-datamodel]

In Python 3, text and binary data are strictly decoupled at the type system level. A `str` object has no fixed byte layout exposed to Python code: it abstracts away memory storage details (internally managed via CPython's PEP 393 flexible string representation). Conversely, `bytes` operates on physical octets meant for network transmission or disk storage. Because abstract characters and concrete byte sequences are semantically distinct, Python forbids implicit coercion between them: concatenating `str` with `bytes` or comparing them for order raises a `TypeError` (and equality comparison `str == bytes` always evaluates to `False`).[^py314-library-stdtypes]

The standard architectural pattern for this separation is known as the "Unicode sandwich". At the outer boundaries of the application (file descriptors, network sockets, database drivers, CLI inputs), incoming raw `bytes` are immediately decoded into `str` with an explicit encoding (typically UTF-8). Internal business logic operates exclusively on `str` without concern for byte layouts. Finally, at the outgoing boundary, text is explicitly encoded back into `bytes` before sending it to external consumers.

Example of explicit conversion at system boundaries and type incompatibility:

```python
# Raw binary data received from external source (network or disk)
raw_bytes = b"Hello, world!"

# Decode at input boundary into Unicode text
text = raw_bytes.decode("utf-8")
print(text)  # Hello, world!
print(type(text), len(text))  # <class 'str'> 13

# Direct operations between str and bytes are forbidden
try:
    _ = text + b"!"
except TypeError as err:
    print(type(err).__name__)  # TypeError

# Multi-byte characters show the difference between character count and byte length
euro = "\u20ac"  # Euro symbol: '€'
euro_bytes = euro.encode("utf-8")
print(len(euro), len(euro_bytes))  # 1 3
```

**Common mistakes when working with `str` and `bytes`:**
- calling decode or encode inside core business logic instead of at the program boundaries, scattering encoding concerns and causing duplicate conversions;
- assuming `len(s)` for a `str` matches the byte length on the wire, breaking protocols that require an accurate `Content-Length` header;
- omitting the explicit encoding parameter (calling `.encode()` or `.decode()` without arguments), making behavior dependent on platform defaults rather than standard UTF-8;
- opening binary streams in text mode without `mode='rb'`, leading to silent newline translations (`\r\n` on Windows) or runtime `UnicodeDecodeError` crashes.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
