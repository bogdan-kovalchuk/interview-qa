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
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
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
uint32_t value;
memcpy(&value, &buf[3], sizeof value);
```

## Short answer

**Via `memcpy`, not a cast to `(uint32_t*)&buf[3]`.**

`&buf[3]` cannot safely be dereferenced as a `uint32_t*`: the address may not meet the type's alignment requirement, and support for unaligned accesses depends on the core and instruction. `memcpy` copies bytes into a separate, properly aligned object; it does not define the byte order in the buffer.

Guard: check the buffer length, copy into a local variable, and decode endianness separately for a wire format.[^iso-c-n1570]

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
