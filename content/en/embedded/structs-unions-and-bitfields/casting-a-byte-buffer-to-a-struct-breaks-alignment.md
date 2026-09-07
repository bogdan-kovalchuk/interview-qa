---
id: emb-structs-0045
title: "Trap: why can overlaying a struct on a raw buffer break alignment?"
description: "A raw buffer has uint8t alignment, not necessarily the alignment of the overlaid struct."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
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
---

## Question code

```c
uint8_t buf[8];
struct Header *h = (struct Header *)buf;
```

## Short answer

<span class="warn">`buf` has alignment for `uint8_t`, not necessarily for `struct Header`.</span>

If `Header` contains `uint32_t`, the pointer `h` may be misaligned. Dereferencing such a pointer can be undefined behavior or a fault. In addition, strict aliasing and effective type rules may also be a problem.

Mitigation: parse the bytes explicitly or copy into an aligned local `struct Header h; memcpy(&h, buf, sizeof h);` if the binary layout is controlled.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
