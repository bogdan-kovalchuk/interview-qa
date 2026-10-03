---
id: emb-volconst-0026
title: "Which section does a mutable lookup table land in?"
description: "A mutable table lands in .data as initialized mutable global or static data, copied from Flash to RAM before main."
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
  - source_id: avr-libc-program-space
    title: "AVR-LibC: Data in Program Space"
    url: https://avrdudes.github.io/avr-libc/avr-libc-user-manual/pgmspace.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "AVR-GCC and AVR linker-script example: mutable static data may be in .data, while const placement and Flash access depend on architecture and linker script."
---

## Question code

```c
uint16_t sine_lut[256] = { 0, 402, 804 };
```

## Short answer

In a typical embedded ELF toolchain, initialized mutable data goes into `.data`.

In a common arrangement, the linker keeps the load image in Flash and startup code copies the bytes to RAM before `main()`. The table occupies space in both memories and takes time to copy; details depend on the toolchain and linker script.[^avr-libc-program-space]

If the table is immutable, `const` allows placement in a read-only section, but does not guarantee a Flash address.[^avr-libc-program-space]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
