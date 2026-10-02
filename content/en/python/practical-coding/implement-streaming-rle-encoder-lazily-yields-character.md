---
id: py-prac-0014
title: "Implement a streaming RLE encoder that lazily yields `(character, positive_count)` tuples from an iterable of characters with a constant number of auxiliary objects; empty input yields nothing."
description: "Keep the current character and its run count, yielding when the character changes."
track: python
section: practical-coding
level: middle
type: coding
tags: [character-positive-count]
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
execution:
  language: python
  standard: null
  toolchain:
    name: cpython
    version: "3.13.15"
  flags: []
anki:
  export: true
sources:
- source_id: py313-itertools
  title: 'Python 3.13: Adjacent groups'
  url: https://docs.python.org/3.13/library/itertools.html#itertools.groupby
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
- source_id: py313-yield
  title: 'Python 3.13: Yield expressions'
  url: https://docs.python.org/3.13/reference/expressions.html#yield-expressions
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
- source_id: py313-types
  title: 'Python 3.13: Built-in types'
  url: https://docs.python.org/3.13/library/stdtypes.html
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
---

## Task

Implement `rle_encode(iterable)`, lazily yielding `(character, positive_count)` for consecutive equal characters. Empty input yields nothing.

## Constraints

- Input is an iterable of one-code-point strings.
- Do not sort or materialize it.
- Keep a constant number of state variables; at most one character of lookahead is needed.
- A never-ending single run cannot produce a completed count.

## Short answer

**Keep the current character and its run count, yielding when the character changes.** Yield the last run at exhaustion and handle empty input before initializing a run. Sorting would change the run structure and must not be used.

## Detailed explanation

A run ends only when the next different character is read or the source is exhausted. The generator suspends after yielding, retaining that boundary character as lookahead. groupby also groups adjacent runs; sorting is not required for RLE. [^py313-itertools] [^py313-yield] [^py313-types]

## Examples

```python
assert list(rle_encode("aab")) == [("a", 2), ("b", 1)]
```

## Solution

```python
def rle_encode(iterable):
    iterator = iter(iterable)
    try:
        current = next(iterator)
    except StopIteration:
        return
    count = 1
    for character in iterator:
        if character == current:
            count += 1
        else:
            yield current, count
            current, count = character, 1
    yield current, count
```

## Complexity

O(n) input steps and a constant number of auxiliary objects for n characters. The count is an arbitrary-precision integer and needs O(log r) bits for a run of length r; constant object count does not mean constant bytes. [^py313-itertools] [^py313-yield] [^py313-types]

## Edge cases

Test empty input, singleton, alternating characters, one-shot input, non-adjacent repeated characters and bounded lookahead.

## Tests

Run after the Solution block with pytest installed.

```python
import pytest

assert list(rle_encode("")) == []
assert list(rle_encode("x")) == [("x", 1)]
assert list(rle_encode("aaabbc")) == [("a", 3), ("b", 2), ("c", 1)]
assert list(rle_encode(iter("aba"))) == [("a", 1), ("b", 1), ("a", 1)]
seen = []
def source():
    for ch in "aabc":
        seen.append(ch)
        yield ch
encoded = rle_encode(source())
assert seen == []
assert next(encoded) == ("a", 2)
assert seen == ["a", "a", "b"]
assert list(encoded) == [("b", 1), ("c", 1)]
```

## Evaluation guide

### Expected signals

Show that the generator consumes nothing at creation and does not read the whole source before its first result.

### Red flags

The implementation misses a stated boundary case or its complexity claim omits allocated data.

### Level-up follow-up

Why can an infinite identical run never yield its final count?

## Sources

<!-- generated from frontmatter -->
