---
id: emb-align-0006
title: "Why does a struct need trailing padding?"
description: "Trailing padding ensures every element in an array of structs starts at an aligned address"
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
    applicability: "Supplementary examples of structure padding and size."
  - source_id: acode-next-cpp
    title: "aCode: End? What next?"
    url: https://acode.com.ua/end-cpp-what-is-next/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Supplementary Ukrainian C++ learning roadmap; not a normative object-layout source."
---

## Short answer

**So that in an array of structs every subsequent element is also aligned.**

`sizeof(struct)` is also the stride between array elements. The implementation includes enough trailing padding for `arr[1]`, `arr[2]`, and later elements to satisfy the structure's alignment requirement.

Under a usual ABI the structure alignment follows its most strictly aligned member, but explicit over-alignment can make it greater.[^embeddedinterviewlab]

## Detailed explanation

An array stores elements contiguously: the address of `arr[i + 1]` is exactly `sizeof arr[0]` bytes after `arr[i]`. Therefore the size of a complete object type must also be a valid stride for another object of that type.[^iso-c-n1570]

Assume `uint32_t` has size/alignment 4 and `uint8_t` has size/alignment 1:

```c
struct Sample {
    uint32_t value;  // offsets 0..3
    uint8_t  tag;    // offset 4
};                   // offsets 5..7 are trailing padding
```

The members occupy five bytes, but `sizeof(struct Sample)` is typically eight. Without the three trailing bytes, `items[1]` would begin five bytes after `items[0]`, and its `value` member would not start on a multiple-of-four address.

Trailing padding belongs to the structure object and is included in `sizeof`; it is not an extra gap owned by the array. This also means structure assignment or `memcpy` of `sizeof(struct Sample)` copies those bytes, although their values are unspecified. LearnCpp illustrates that padding can make a structure larger than the sum of its members.[^learncpp-struct-padding]

Do not derive a wire format from `sizeof(struct)`. For an ABI boundary, verify both size and offsets with `_Static_assert`/`static_assert`; for serialized data, define an explicit byte layout instead.

## Sources

<!-- generated from frontmatter -->
