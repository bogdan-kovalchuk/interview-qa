---
id: emb-align-0012
title: "How does `0xDEADBEEF` sit in memory on a little-endian machine?"
description: "On a little-endian machine the bytes are stored EF BE AD DE from lowest to highest address"
track: embedded
section: memory-alignment-and-endianness
level: junior
type: mechanism
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
  - source_id: learncpp-object-sizes
    title: "Object sizes and the sizeof operator"
    url: https://www.learncpp.com/cpp-tutorial/object-sizes-and-the-sizeof-operator/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Supplementary explanation of how multi-byte objects occupy storage."
  - source_id: acode-cpp-next
    title: "C++ вивчено – що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Supplementary Ukrainian learning roadmap; not normative evidence for byte order."
---

## Short answer

**`EF BE AD DE`** (from lowest address to highest).

Little-endian places the least-significant byte at the lowest address: `0xEF` at offset 0, `0xBE` at 1, `0xAD` at 2, and `0xDE` at 3.

Rule: interpret a dump using its displayed address direction; do not merely reverse the printed text.[^embeddedinterviewlab]

## Detailed explanation

Split `0xDEADBEEF` into bytes by significance: `DE`, `AD`, `BE`, `EF`. The byte `EF` contains bits 0 through 7, so a little-endian representation places it at the object's lowest address. Successive addresses hold increasingly significant bytes:

```text
Lower address                         Higher address
base + 0   base + 1   base + 2   base + 3
0xEF       0xBE       0xAD       0xDE
```

If a debugger displays memory from lower addresses on the left, the row is therefore `EF BE AD DE`. Some tools group bytes into words or choose another display direction, so always check the address labels before interpreting the view.

The statement assumes a 32-bit unsigned object whose value is `0xDEADBEEF` and a little-endian target. C defines an object representation as `sizeof` bytes but leaves the byte order of ordinary integers implementation-defined.[^iso-c-n1570] The hexadecimal value itself is not reversed: loading all four bytes through a correctly aligned `uint32_t` object on that same target produces `0xDEADBEEF`.

When bytes belong to an external format, decode them according to that format instead of casting the buffer to `uint32_t *`. Explicit decoding avoids both alignment assumptions and host-endianness assumptions. LearnCpp's object-size discussion supplies background on byte-sized storage,[^learncpp-object-sizes] and aCode provides a broader Ukrainian roadmap for continued C and C++ learning.[^acode-cpp-next]

## Sources

<!-- generated from frontmatter -->
