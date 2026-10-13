---
id: py-perf-0008
title: "Why can repeated string concatenation in a loop cause repeated copying, and when is it better to collect the accumulated fragments with `\"\".join(...)`?"
description: "Because str is immutable, accumulating fragments with repeated += is quadratic in the general case; collect them in a list and call join once."
track: python
section: performance
level: middle
type: comparison
tags: [join]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-faq-programming-performance
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#performance
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Python 3.14 FAQ: accumulating many str objects by concatenation is quadratic in the general case; the recommended idiom is a list joined with str.join() at the end; io.StringIO is named as another efficient idiom."
  - source_id: py314-library-stdtypes-repeated-concatenation
    title: "Python 3.14: Library/stdtypes, repeated concatenation"
    url: https://docs.python.org/3.14/library/stdtypes.html#typesseq-repeated-concatenation
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Python 3.14 sequence types documentation: concatenating immutable sequences always creates a new object, so repeated concatenation has a quadratic cost in the total length; linear alternatives are str.join or io.StringIO, and for bytes bytes.join, io.BytesIO or bytearray."
  - source_id: cpython-bytecodes-inplace-add-unicode
    title: "CPython 3.14: Python/bytecodes.c"
    url: https://github.com/python/cpython/blob/v3.14.6/Python/bytecodes.c
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "CPython 3.14 source (tag v3.14.6), _BINARY_OP_INPLACE_ADD_UNICODE: for x += y on a str, the string is extended in place when the next instruction is STORE_FAST to the same local and the string has no other references. An implementation detail, not a language guarantee."
  - source_id: cpython-unicodeobject-joinarray
    title: "CPython 3.14: Objects/unicodeobject.c"
    url: https://github.com/python/cpython/blob/v3.14.6/Objects/unicodeobject.c
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "CPython 3.14 source (tag v3.14.6), _PyUnicode_JoinArray: first computes the total length of the fragments, then allocates the result once. An implementation detail of CPython."
---

## Short answer

**Because `str` is immutable, concatenation creates a new string, so accumulating with repeated `+=` has a quadratic cost in the total length.**[^py314-library-stdtypes-repeated-concatenation] For many fragments the recommended approach is to collect them in a `list` and call `''.join(...)` once; `io.StringIO` is also an efficient option.[^py314-faq-programming-performance] CPython sometimes extends a string in place, but do not rely on that.

## Detailed explanation

A string is immutable: `a + b` changes neither `a` nor `b`, but creates a new object of length `len(a) + len(b)` and copies the contents of both strings into it. If a loop adds fragments of `m` characters each to an accumulator, then at step `k` the `k*m` characters are copied, and in total `m*n*(n+1)/2` characters for `n` steps. This gives a quadratic dependence on the total length, which the documentation states directly.[^py314-library-stdtypes-repeated-concatenation]

CPython has one exception. For `s += t` on a local variable, the interpreter can extend the string in place if no other reference to it exists. The condition is visible in the CPython source: the next instruction must be a `STORE_FAST` into the same variable.[^cpython-bytecodes-inplace-add-unicode] An attribute target such as `self.text += part` has no such path, so every call copies the whole text. The example below compares the attribute version with `join`:

```python
import timeit

class Report:
    def __init__(self):
        self.text = ''

    def add(self, part):
        self.text += part          # attribute target: CPython does not extend it in place

def build_attr(parts):
    report = Report()
    for part in parts:
        report.add(part)
    return report.text

def build_join(parts):
    chunks = []
    for part in parts:
        chunks.append(part)
    return ''.join(chunks)         # one pass for the total length, then one copy per fragment

parts = ['x' * 10] * 20_000
print(build_attr(parts) == build_join(parts))   # True
slow = timeit.timeit(lambda: build_attr(parts), number=1)
fast = timeit.timeit(lambda: build_join(parts), number=1)
print(slow > 10 * fast)            # True on CPython 3.13 and 3.14
```

`str.join` works differently: CPython first walks the fragments to compute the total length, then allocates the result once and copies each fragment once.[^cpython-unicodeobject-joinarray] A list followed by one `join` is therefore worthwhile when there are many fragments produced in a loop. If the text is written to a file anyway, it is better to write to the file or to an `io.StringIO` as you go.

For a few concatenations outside a loop, `+` or an f-string is perfectly fine: it is one operation whose cost does not grow with the data. The quadratic effect appears when the number of steps grows with the data. For `bytes`, the documentation gives the same alternatives: `bytes.join`, `io.BytesIO` or `bytearray`.[^py314-library-stdtypes-repeated-concatenation]

**Common mistakes:**
- assuming that the CPython optimization of `+=` always applies, and moving the loop to an attribute or to a variable that has other references;
- calling `join` inside the loop or once per fragment, which defeats the purpose of collecting;
- accumulating the whole large output in a `list` when it could be written out as a stream.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
