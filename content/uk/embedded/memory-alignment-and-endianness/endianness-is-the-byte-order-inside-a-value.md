---
id: emb-align-0011
title: "Що таке little-endian і big-endian для значення `0x12345678`?"
description: "Порядок байтів багатобайтового значення в пам'яті."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Short answer

**Порядок байтів багатобайтового значення в пам'яті.**

```text
Адреса:  00   01   02   03
LE:      78   56   34   12  (little-endian, LSB перший)
BE:      12   34   56   78  (big-endian, MSB перший)
```

LSB (least significant byte) – молодший байт, MSB (most significant byte) – старший байт. Little-endian: молодший байт за нижчою адресою (ARM default, x86, RISC-V). Big-endian: старший перший (PowerPC, 68k, мережа).

Правило: endianness впливає лише на багатобайтові типи; масив `uint8_t` однаковий усюди.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
