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
updated: 2026-10-13
content_revision: 3
reconciled_with:
  uk: 3
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
  - source_id: py314-howto-unicode
    title: "Python 3.14: Howto/unicode"
    url: https://docs.python.org/3.14/howto/unicode.html#tips-for-writing-unicode-aware-programs
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the section on writing Unicode-aware programs. Confirms that there is no automatic encoding or decoding (str + bytes raises TypeError) and recommends decoding input and encoding output. Does not define the bytes API."
---

## Short answer

**`str` is an immutable sequence of Unicode code points used for text, while `bytes` is an immutable sequence of integers from 0 to 255 used for encoded text or arbitrary binary data.**[^py314-library-stdtypes] Keep text as `str` inside the program and use `bytes` at binary or protocol boundaries when the API requires it. Encoding maps `str` to `bytes` with a character encoding and error policy (by default `utf-8` and `strict`), and decoding performs the reverse.[^py314-library-stdtypes] A `bytes` object does not remember which encoding, if any, produced it.

## Detailed explanation

`str` and `bytes` are two different types, and Python never converts one into the other silently. `str` stores text as a sequence of Unicode code points, so `len('é')` is 1 no matter how many bytes the character takes in a file or on the network. `bytes` stores a sequence of bytes, that is integers from 0 to 255, so `data[0]` returns an `int` while `text[0]` returns a `str`.[^py314-library-stdtypes]

The boundary between them is the encoding. By default `str.encode()` uses `utf-8` and `strict`: a character that the chosen encoding cannot represent raises `UnicodeError` rather than disappearing.[^py314-library-stdtypes] Decoding with the same encoding restores the text; with a different one it can give other text or an error, because `bytes` carries no name for its encoding.

The example shows both sides of the boundary. The comments show the output checked on CPython 3.13:

```python
text = 'é'                              # one code point
data = text.encode('utf-8')             # str -> bytes
print(len(text), len(data))             # 1 2
print(data)                             # b'\xc3\xa9'
print(data[0])                          # 195: indexing bytes gives an int
print(text[0])                          # é: indexing str gives a str
print(data.decode('utf-8') == text)     # True: the same encoding restores the text

try:
    'a' + b'a'                          # str and bytes are never concatenated implicitly
except TypeError:
    print('TypeError')                  # TypeError

raw = b'\xe9'                           # one byte; the object does not record its encoding
print(raw.decode('latin-1'))            # é
try:
    raw.decode('utf-8')
except UnicodeDecodeError:
    print('not valid UTF-8')            # not valid UTF-8
```

In practice this leads to a division of labour. Keep text as `str` inside the program, decode incoming bytes as early as possible, and encode only on output. The Unicode HOWTO describes this approach and states that there is no automatic encoding or decoding: `str + bytes` raises `TypeError`.[^py314-howto-unicode] Use `bytes` where the data already is bytes: a binary file, a socket, a protocol, or an API that requires them.

**Common mistakes:**
- assuming that `len()` of a `bytes` object counts characters: `len(b'\xc3\xa9')` is 2, while `len('é')` is 1;
- decoding bytes without an explicit encoding even though the format or protocol defines one;
- mixing `str` and `bytes` in one operation, for example in concatenation, or expecting Python to convert them.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
