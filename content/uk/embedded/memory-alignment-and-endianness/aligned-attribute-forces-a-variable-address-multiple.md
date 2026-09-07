---
id: emb-align-0030
title: "Що робить `__attribute__((aligned(N)))` для змінної?"
description: "Гарантує, що адреса змінної кратна N байтам."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 1
reconciled_with:
  en: 3
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
uint8_t buf[64] __attribute__((aligned(32)));
```

## Short answer

**Гарантує, що адреса змінної кратна N байтам.**

Використовується для DMA (direct memory access) буферів, cache-line вирівнювання, спеціальних регіонів пам'яті. Це GCC/Clang-розширення; стандартний аналог – `_Alignas(N)`.

Правило: `aligned` збільшує вирівнювання; `packed` – зменшує padding. Їх можуть комбінувати для wire/DMA descriptors, коли потрібні щільний layout і вирівняна базова адреса.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
