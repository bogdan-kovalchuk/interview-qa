---
id: emb-cppfound-0034
title: "Знайдіть помилку?"
description: "How a byte buffer cast can cause bounds and alignment problems."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
uint8_t buf[256];
uint32_t *p = (uint32_t*)buf;
for(int i=0;
i<256;
i++) p[i]=0;
```

## Short answer

<span class="warn">Out-of-bounds write!</span> `buf` – 256 байт. `p` – `uint32_t*`, кожен елемент = 4 байти. Цикл `p[0]..p[255]` записує `256 × 4 = 1024 байти` – у 4 рази більше розміру буфера.

Правильно: `for(int i=0; i < 256/sizeof(uint32_t); i++) p[i]=0;` або `memset(buf, 0, sizeof(buf))`.

Також: `uint8_t buf[256]` може бути не вирівняний для `uint32_t` -> misaligned access.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
