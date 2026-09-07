---
id: emb-cppfound-0018
title: "Що виведе?"
description: "Why sizeof a dereferenced pointer depends on its pointer type."
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
uint32_t *p=(uint32_t*)0x2000;
uint8_t *q=(uint8_t*)p;
printf("%zu %zu", sizeof(*p), sizeof(*q));
```

## Short answer

`sizeof(*p)` -> **4**. Розіменування `uint32_t*` дає об'єкт типу `uint32_t` – 4 байти.

`sizeof(*q)` -> **1**. Розіменування `uint8_t*` дає `uint8_t` – 1 байт.

Важливо: `sizeof` операнда-розіменування визначається типом вказівника, а не адресою – обидва вказівники вказують на ту саму адресу `0x2000`, але sizeof повертає різні значення.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
