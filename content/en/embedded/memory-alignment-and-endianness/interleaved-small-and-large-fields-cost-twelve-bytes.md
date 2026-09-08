---
id: emb-align-0004
title: "With four-byte uint32 alignment, what `sizeof` will this have?"
description: "It is typically 12 bytes: three internal and three trailing padding bytes"
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
  - source_id: learncpp-struct-padding
    title: "LearnCpp: Struct miscellany"
    url: https://www.learncpp.com/cpp-tutorial/struct-miscellany/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Supplementary examples showing how member order changes structure padding and size."
  - source_id: acode-next-cpp
    title: "aCode: End? What next?"
    url: https://acode.com.ua/end-cpp-what-is-next/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Supplementary Ukrainian C++ learning roadmap; not a normative source for object layout."
---

## Question code

```c
typedef struct {
  uint8_t  flags;
  uint32_t timestamp;
  uint8_t  sensor_id;
} bad_t;
```

## Short answer

**Typically 12 bytes, assuming `uint8_t` has size/alignment 1 and `uint32_t` has size/alignment 4.**

Layout: `flags`@0 (1B) -> <span class="warn">3B padding</span> -> `timestamp`@4 (4B) -> `sensor_id`@8 (1B) -> <span class="warn">3B trailing padding</span> (so the size is a multiple of 4).

Reordering the fields by decreasing alignment reduces this layout to 8 bytes. A 32-bit MCU alone does not guarantee these ABI values.[^embeddedinterviewlab]

## Detailed explanation

The exact result is implementation-defined, so begin by stating the ABI assumptions. Under the common MCU layout in the short answer, the compiler preserves declaration order and inserts unnamed padding where required.[^iso-c-n1570]

```c
typedef struct {
    uint8_t  flags;      // size 1, alignment 1
    uint32_t timestamp;  // size 4, alignment 4
    uint8_t  sensor_id;  // size 1, alignment 1
} bad_t;
```

The offset calculation is:

1. `flags` occupies offset 0.
2. `timestamp` needs a multiple-of-4 offset, so offsets 1 through 3 are padding and `timestamp` occupies offsets 4 through 7.
3. `sensor_id` occupies offset 8.
4. The object currently occupies 9 bytes. Three trailing padding bytes make the array stride 12, so `timestamp` remains aligned in every array element.

The resulting byte layout is:
```
Offset: 0  1  2  3  4  5  6  7  8  9  10 11
        [f][p][p][p][t0][t1][t2][t3][s][p][p][p]
```

`sizeof(bad_t)` cannot be 6 under these assumptions because that would ignore both internal padding and the aligned stride required by an array. LearnCpp gives an analogous 12-versus-8 example and emphasizes that structure size can exceed the sum of its members.[^learncpp-struct-padding]

When binary compatibility does not freeze member order, group the most strictly aligned fields first:
```c
typedef struct {
    uint32_t timestamp;  // offsets 0..3
    uint8_t  flags;      // offset 4
    uint8_t  sensor_id;  // offset 5
} good_t;                // offsets 6..7 are trailing padding
```

Confirm rather than assume the target layout:

```c
_Static_assert(sizeof(bad_t) == 12, "unexpected bad_t layout");
_Static_assert(sizeof(good_t) == 8, "unexpected good_t layout");
```

Do not reorder members of a public ABI, wire format, persistent binary format, or hardware register map merely to save space.

## Sources

<!-- generated from frontmatter -->
