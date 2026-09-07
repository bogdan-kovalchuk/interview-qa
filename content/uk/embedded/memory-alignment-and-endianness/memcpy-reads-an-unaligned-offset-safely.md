---
id: emb-align-0023
title: "Як безпечно прочитати `uint32_t` зі зсуву 3 у `uint8_t`-буфері (напр., DMA – direct memory access)?"
description: "Через memcpy, а не cast (uint32_t)&buf[3]."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: pitfall
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
uint32_t value;
memcpy(&value, &buf[3], sizeof value);
```

## Short answer

**Через `memcpy`, а не cast `(uint32_t*)&buf[3]`.**

Адреса `&buf[3]` майже напевно невирівняна -> прямий cast і розіменування дадуть HardFault на M0 або штраф на M3/M4. `memcpy` компілятор перетворить на безпечні (можливо побайтові) load/store.

Захист: для будь-якого unaligned multi-byte доступу – `memcpy` у локальну вирівняну змінну.[^embeddedinterviewlab]

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
