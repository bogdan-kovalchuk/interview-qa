---
id: py-objtypes-0019
title: "What copying problem does `memoryview` solve, and why does the lifetime of the underlying buffer object matter?"
description: "What copying problem does `memoryview` solve, and why does the lifetime of the underlying buffer object matter?"
track: python
section: objects-and-types
level: senior
type: mechanism
tags: [memoryview]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  uk: 2
applies_to:
  - product: "CPython"
    version: null
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

**`memoryview` provides zero-copy access to the internal buffer of an object supporting the buffer protocol (such as `bytes`, `bytearray`, `array.array`), allowing reading and mutating memory slices without copying.**[^py314-reference-datamodel] This is critical for large binary data, where slicing or copying would duplicate the entire buffer. Underlying buffer lifetime matters because `memoryview` merely borrows memory: CPython retains a reference to the base object to prevent deallocation, and resizing the base (e.g. `bytearray.extend()`) raises `BufferError` until `release()` is called. <span class="warn">After calling `mv.release()`, accessing the memoryview raises `ValueError`.</span>

## Detailed explanation

`memoryview` allows Python code to share and slice contiguous memory buffers across objects without copying data, implementing Python's low-level C buffer protocol at the language level.[^py314-reference-datamodel]

In standard Python, slicing a sequence like `b[10:100]` allocates a brand new object and copies the 90 bytes into it. When dealing with gigabyte-scale datasets, video frames, or high-throughput network sockets, repeatedly slicing creates severe memory fragmentation and burns CPU cycles on redundant $O(N)$ allocations. Slicing a `memoryview` object, however, returns another `memoryview` that points to a specific sub-range of the original memory buffer (defined by a pointer, length, and stride) without copying a single byte ($O(1)$ time and memory). If the underlying buffer is mutable (like `bytearray`), modifications through the slice immediately alter the original buffer.

The lifetime and state of the underlying buffer object are critical because `memoryview` is a non-owning window into memory allocated and managed by another object. At the C-API level, creating a `memoryview` requests an exported buffer via `PyObject_GetBuffer()`, incrementing the base object's active export count (`bf_getbuffer`). In CPython, this creates two essential invariants:
First, the base object's memory cannot be prematurely freed by garbage collection while the view is alive, because `memoryview.obj` keeps a strong reference to the base object.
Second, to prevent dangling pointers and buffer corruption, mutable base objects lock their internal memory layout: any operation that could reallocate the buffer and change its size (such as `bytearray.append()`, `.extend()`, or resizing) is blocked and raises a `BufferError`.[^py314-library-stdtypes]

To release this lock before the `memoryview` is garbage-collected, developers can call `mv.release()` or use `memoryview` as a context manager (`with memoryview(...) as mv:`). Once released, the view detaches from the underlying buffer, allowing the base object to resize or reallocate; any subsequent read or write operations on the released view immediately raise `ValueError`.

Demonstration of zero-copy slicing, mutation through a view, and buffer resize locking:

```python
# Underlying mutable buffer
data = bytearray(b"abcdefghij")

# Create a zero-copy memoryview and slice it
view = memoryview(data)
sub_view = view[3:7]  # zero-copy slice: references bytes 3..6 without copying
print(bytes(sub_view))  # b'defg'

# Mutating through sub_view directly modifies the underlying bytearray
sub_view[0] = ord("D")
print(data)  # bytearray(b'abcDefghij')

# Underlying buffer cannot change size while exported
try:
    data.extend(b"klm")
except BufferError as err:
    print(type(err).__name__)  # BufferError (Existing exports of data)

# Releasing the view releases the lock on the base object
sub_view.release()
view.release()
data.extend(b"klm")  # now resizing succeeds
print(len(data))  # 13

# Accessing a released view raises ValueError
try:
    _ = view[0]
except ValueError as err:
    print(type(err).__name__)  # ValueError (operation forbidden on released memoryview)
```

**Practical implications and common pitfalls when working with `memoryview`:**
- resize locking: holding an active `memoryview` over a `bytearray` blocks any method that reallocates memory (`extend`, `pop`, `resize`), triggering unexpected `BufferError` exceptions elsewhere;
- memory retention through base references: because a `memoryview` holds a strong reference to the entire underlying object, even a tiny slice `mv[0:10]` prevents garbage collection of a gigabyte-scale buffer as long as the view is alive;
- resource management: using a context manager (`with memoryview(...) as mv:`) or calling `mv.release()` explicitly ensures that buffer exports are promptly released;
- post-release access errors: any attempt to read or modify data through a released `memoryview` instantly raises `ValueError`.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
