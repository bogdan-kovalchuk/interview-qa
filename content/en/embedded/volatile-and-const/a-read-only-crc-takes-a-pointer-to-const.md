---
id: emb-volconst-0051
title: "Which declaration is better for a CRC function that only reads the data?"
description: "Prefer uint32_t crc32(const uint8_t *data, size_t len) because the CRC function only reads the data."
track: embedded
section: volatile-and-const
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
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
uint32_t crc32(? data, size_t len);
```

## Short answer

Better: `uint32_t crc32(const uint8_t *data, size_t len);`[^iso-c-n1570]

CRC does not modify the buffer, so the pointer must point to const data. This allows computing CRC over a RAM buffer, Flash table, firmware image slice, or string literal without losing type safety.

Embedded rule: `const` prevents this function from modifying elements through this pointer, but does not guarantee that the data physically resides in Flash or that another alias cannot change it.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
