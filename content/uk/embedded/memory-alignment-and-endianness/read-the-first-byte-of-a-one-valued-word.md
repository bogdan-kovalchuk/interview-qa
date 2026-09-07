---
id: emb-align-0016
title: "Як визначити endianness у runtime?"
description: "Якщо перший байт (за нижчою адресою) == 1 -> little-endian."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 1
reconciled_with:
  en: 1
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

## Question code

```c
union { uint32_t word; uint8_t byte; } u = { .word = 1 };
return u.byte == 1;
```

## Short answer

**Якщо перший байт (за нижчою адресою) == 1 -> little-endian.**

Усі поля union поділяють одну пам'ять. Записавши `word = 1`, читаємо найнижчий байт: на LE там `0x01`, на BE – `0x00`.

Правило: для цільового MCU endianness зазвичай відома на етапі компіляції; runtime-перевірка потрібна хіба що в портативних бібліотеках і тестах.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
