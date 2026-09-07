---
id: emb-cppfound-0005
title: "Що виведе?"
description: "How pointer arithmetic scales with the pointed-to type."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу c-in-embedded; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Question code

```c
uint8_t *p = (uint8_t*)0x1000;
p++;
printf("%p", (void*)p);
```

## Short answer

`0x1001`.

Pointer arithmetic масштабується по `sizeof(*p)`. Для `uint8_t*`: `sizeof(uint8_t) = 1`, тому `p++` -> адреса + 1 байт.

Якби `uint32_t *p = (uint32_t*)0x1000; p++;` -> `0x1004` (кроком 4 байти).

Правило: `p + n` = `(char*)p + n * sizeof(*p)`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
