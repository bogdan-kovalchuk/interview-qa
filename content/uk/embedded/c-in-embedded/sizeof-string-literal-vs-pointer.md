---
id: emb-cppfound-0053
title: "Що поверне `sizeof(\"hello\")` vs `sizeof(char*)` на 32-bit?"
description: "How sizeof treats a string literal and a pointer."
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

## Short answer

`sizeof("hello")` -> **6**. Рядковий літерал – масив: `{'h','e','l','l','o','\0'}`. `sizeof` рядкового літерала повертає розмір масиву включно з null-terminator.

`sizeof(char*)` -> **4**. Розмір вказівника = розрядність платформи.

Важливо: `sizeof("hello")` не decay-ується до вказівника (sizeof – одне з трьох виключень array decay), тому отримуємо розмір масиву.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
