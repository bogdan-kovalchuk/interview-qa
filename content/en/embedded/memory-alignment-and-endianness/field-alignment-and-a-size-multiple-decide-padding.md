---
id: emb-align-0003
title: "Which two rules determine the padding in a struct?"
description: "Each field is aligned to its natural alignment and the struct size is a multiple of the largest field alignment"
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
tags: []
status: published
updated: 2026-09-08
content_revision: 4
reconciled_with:
  uk: 4
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
  - source_id: learncpp-struct-padding
    title: "LearnCpp: Struct miscellany"
    url: https://www.learncpp.com/cpp-tutorial/struct-miscellany/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Supplementary examples of structure padding, size, and member reordering in C++."
  - source_id: acode-next-cpp
    title: "aCode: End? What next?"
    url: https://acode.com.ua/end-cpp-what-is-next/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Supplementary Ukrainian C++ learning roadmap; not a normative source for object layout."
---

## Short answer

1. Each member starts at an offset suitable for its type, so the implementation can insert internal padding. 2. The structure's size includes any trailing padding needed so that consecutive array elements remain aligned.

Under a usual ABI without explicit over-alignment, the structure alignment is the largest member alignment. Always verify `sizeof` and `_Alignof` on the actual target.[^embeddedinterviewlab]

## Detailed explanation

**Rule 1: member alignment**

Members appear in declaration order, and a compiler may insert unnamed padding between them, but not before the first member. Each non-bit-field member still has to satisfy the alignment requirement of its type.[^iso-c-n1570]

Assume this target has `_Alignof(uint32_t) == 4`:
```c
struct Example {
    uint8_t  a;    // size 1, alignment 1
    uint32_t b;    // size 4, alignment 4
    uint8_t  c;    // size 1, alignment 1
};
```

One typical layout is:
```
Offset: 0  1  2  3  4  5  6  7  8  9  10 11
        [a][pad][pad][pad][  b  ][c][pad][pad][pad]
```

`a` occupies offset 0. Three padding bytes move `b` to offset 4; `c` follows at offset 8.

**Rule 2: structure stride**

An array has no gaps between its elements, so `sizeof(struct Example)` is also the array stride. The implementation adds trailing padding so the next element starts at an address that satisfies the structure's alignment.

With the stated ABI assumptions, the largest member alignment is 4. The members plus internal padding occupy 9 bytes, and three trailing bytes make the size 12. LearnCpp demonstrates the same general effect: structure size can exceed the sum of member sizes because of padding.[^learncpp-struct-padding]

For this example:
```
sizeof(struct) = sum of field sizes + internal padding + trailing padding
```

Do not serialize or map a hardware layout by copying a native structure blindly. Padding, member alignment, integer representation, and byte order are ABI properties. Define an explicit wire format, use fixed-width fields, and encode or decode each field; for a register map, follow the vendor layout and verify offsets with `_Static_assert` or `static_assert`.

Reordering members by decreasing alignment often reduces padding, but it can change an ABI or binary format and therefore is only safe when the layout is under your control.

## Sources

<!-- generated from frontmatter -->
