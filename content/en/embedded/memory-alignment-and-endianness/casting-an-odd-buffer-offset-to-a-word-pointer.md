---
id: emb-align-0031
title: "Trap: why is `*(uint32_t*)&buf[1]` dangerous?"
description: "The address is not aligned to 4 bytes, causing misaligned access and a potential strict aliasing violation."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 3
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
uint32_t v = *(uint32_t*)&buf[1];
```

## Short answer

<span class="warn">The address `&buf[1]` is not a multiple of 4 -> misaligned access</span> (HardFault on M0, penalty on M3/M4), plus a potential strict aliasing violation.

Casting `uint8_t*` to `uint32_t*` promises the compiler an alignment that does not exist.

Guard: `uint32_t v; memcpy(&v, &buf[1], 4);` is safe for any offset and has no undefined behavior.[^embeddedinterviewlab]

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
