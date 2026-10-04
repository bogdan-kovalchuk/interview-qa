---
id: emb-align-0035
title: "What does this code print on a little-endian machine?"
description: "On little-endian the least significant byte 0x44 is at the lowest address, so the code prints 44; on big-endian, 11."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 4
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
uint32_t w = 0x11223344;
uint8_t *p = (uint8_t*)&w;
printf("%02X", (unsigned)p[0]);
```

## Short answer

On little-endian the code prints `44`: the least significant byte `0x44` sits at the lowest address, so `p[0]` reads it. On big-endian it would print `11`; inspecting an object's bytes through `uint8_t*` is allowed because it is a character type.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
