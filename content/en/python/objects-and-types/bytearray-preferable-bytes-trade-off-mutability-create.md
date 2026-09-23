---
id: py-objtypes-0018
title: "When is `bytearray` preferable to `bytes`, and what trade-off does its mutability create?"
description: "When is `bytearray` preferable to `bytes`, and what trade-off does its mutability create?"
track: python
section: objects-and-types
level: middle
type: comparison
tags: [bytearray, bytes]
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
---

## Short answer

**`bytearray` is preferable when binary data must be modified in-place (byte-by-byte buffer manipulation, network data accumulation) without allocating a new object on every mutation.**[^py314-reference-datamodel] Unlike `bytes`, `bytearray` is mutable, supporting item assignment and deletion by index or slice. The trade-off: `bytearray` is unhashable – it cannot be used as a dict key or a set element, and its mutability means all references to the same object observe mutations (aliasing).

## Detailed explanation

`bytearray` is a mutable sequence of integers in the range 0–255, providing in-place binary data modification as an alternative to the immutable `bytes` sequence type.[^py314-reference-datamodel]

Because `bytes` is immutable, any modification – appending chunks from a network stream, updating headers, or slicing and overwriting – requires allocating a new `bytes` object and copying all existing data ($O(N)$ per operation). Incremental concatenation therefore results in quadratic $O(N^2)$ time and memory overhead. In contrast, `bytearray` is backed by a contiguous over-allocated C memory buffer (similar to a `list`), providing $O(1)$ amortized complexity for appends (`.extend()`, `+=`), in-place assignment by index or slice (`buf[0] = 0xFF`), and direct I/O via `socket.recv_into()` or `file.readinto()` without intermediate allocations.[^py314-library-stdtypes]

However, mutability introduces significant architectural trade-offs. First, `bytearray` does not implement `__hash__` (it is unhashable), which prevents it from being used as a dictionary key or set element, whereas `bytes` can be freely cached and hashed. Second, sharing a mutable buffer across different functions or concurrent threads creates aliasing risks: unintended modifications in one component become immediately visible to all reference holders. Therefore, before passing buffers across architectural boundaries or to untrusted consumers, defensive copying or casting to immutable `bytes(ba)` is recommended.

Comparison of concatenation and in-place mutation between `bytes` and `bytearray`:

```python
# bytes is immutable: modifications create new objects
b = b"hello"
# b[0] = 0x48  # TypeError: 'bytes' object does not support item assignment
new_b = b + b" world"
print(b, new_b)  # b'hello' b'hello world'

# bytearray is mutable: supports in-place modifications
ba = bytearray(b"hello")
ba[0] = ord("H")  # in-place item assignment
ba.extend(b" world")  # in-place append without reallocating whole object
print(ba)  # bytearray(b'Hello world')

# Hashability trade-off
print(isinstance(hash(b), int))  # True
try:
    hash(ba)
except TypeError as err:
    print(type(err).__name__)  # TypeError
```

**Practical recommendations and common pitfalls:**
- binary stream accumulation: when assembling byte streams (e.g. from network sockets), use `bytearray` or a list of chunks (`list[bytes]`) with a final `b''.join()`, avoiding quadratic `b += chunk`;
- aliasing prevention: if a mutable `bytearray` crosses architectural boundaries, convert it to immutable `bytes(ba)` before passing it to downstream consumers;
- lack of hashability: the inability to use `bytearray` as a `dict` key or in lookup caches necessitates explicit conversion to `bytes`;
- direct I/O buffers: methods like `sock.recv_into(ba)` and `f.readinto(ba)` read incoming bytes directly into pre-allocated memory buffers without intermediate object allocations.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
