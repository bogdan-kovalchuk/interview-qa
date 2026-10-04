---
id: emb-align-0031
title: "Trap: why is `*(uint32_t*)&buf[1]` dangerous?"
description: "An unaligned pointer conversion can cause undefined behavior; the hardware response depends on the platform."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-04
content_revision: 5
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
uint8_t buf[8];
uint32_t v = *(uint32_t*)&buf[1];
```

## Short answer

<span class="warn">The offset pointer may not meet `uint32_t` alignment, so converting or accessing through it can cause undefined behavior; the hardware effect depends on the architecture and configuration.</span> Reading byte objects as `uint32_t` can also violate effective-type rules.[^iso-c-n1570]

Converting `uint8_t*` to `uint32_t*` does not align the address or turn the byte object into a `uint32_t` object.[^iso-c-n1570]

To avoid an unaligned typed load, use `memcpy(&v, &buf[1], sizeof v);` when at least `sizeof v` source bytes remain. This does not define the protocol's byte order; decode bytes explicitly when needed.[^iso-c-n1570]

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
