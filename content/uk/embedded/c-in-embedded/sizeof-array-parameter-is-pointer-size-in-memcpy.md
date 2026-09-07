---
id: emb-cppfound-0039
title: "Що зробить `memcpy(dst, src, sizeof(src))` якщо `src` – параметр-масив функції?"
description: "Why sizeof on an array parameter copies only pointer-sized data."
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

<span class="warn">Скопіює лише 4 або 8 байт</span> (розмір вказівника), а не розмір масиву.

У параметрі функції `src` – це `uint8_t*`, не масив. `sizeof(src) = sizeof(uint8_t*) = 4`. Тому `memcpy` копіює тільки 4 байти замість N.

Правильно: передавати розмір явно: `memcpy(dst, src, n * sizeof(src[0]))` або `memcpy(dst, src, n)` де `n` – окремий параметр.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
