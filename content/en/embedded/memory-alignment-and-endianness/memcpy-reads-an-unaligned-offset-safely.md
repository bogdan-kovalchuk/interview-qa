---
id: emb-align-0023
title: "How do you safely read a `uint32_t` from offset 3 in a `uint8_t` buffer (for example from DMA)?"
description: "Use memcpy, not a cast to (uint32t)&buf[3], to avoid misaligned access."
track: embedded
section: memory-alignment-and-endianness
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
uint32_t value;
memcpy(&value, &buf[3], sizeof value);
```

## Short answer

**Via `memcpy`, not a cast to `(uint32_t*)&buf[3]`.**

The address `&buf[3]` is almost certainly unaligned -> a direct cast and dereference will cause a HardFault on M0 or a penalty on M3/M4. The compiler turns `memcpy` into safe (possibly byte-wise) load/store operations.

Guard: for any unaligned multi-byte access, use `memcpy` into a local aligned variable.[^embeddedinterviewlab]

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
