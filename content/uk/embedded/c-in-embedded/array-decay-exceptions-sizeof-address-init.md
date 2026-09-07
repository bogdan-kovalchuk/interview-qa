---
id: emb-cppfound-0012
title: "У яких трьох контекстах масив НЕ розпадається (decay) до вказівника?"
description: "The three common contexts where an array remains an array."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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

Масив залишається масивом і **не decay-ується** у трьох випадках:

1. `sizeof(arr)` – повертає загальний розмір масиву у байтах, не розмір вказівника;
2. `&arr` – повертає вказівник на масив `int(*)[N]`, не `int*`;
3. Ініціалізація рядковим літералом: `char arr[] = "hi"` – копіює символи у масив.

Пам'ятай ці три виключення – вони часто зустрічаються на інтерв'ю.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
