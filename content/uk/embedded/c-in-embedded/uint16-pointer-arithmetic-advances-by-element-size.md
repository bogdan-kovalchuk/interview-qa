---
id: emb-cppfound-0022
title: "Яку адресу матиме `p` після: `uint16_t arr[4]; uint16_t *p = arr; p += 2;`?"
description: "How typed pointer arithmetic determines the resulting address."
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

## Short answer

Якщо `arr` за адресою `0x2000` -> `p = 0x2000 + 2 * sizeof(uint16_t) = 0x2000 + 4 = 0x2004`.

Крок pointer arithmetic для `uint16_t*` = 2 байти. `p += 2` -> зсув на 2 елементи × 2 байти = 4 байти.

Тепер `p` вказує на `arr[2]`. Зважай: кроки завжди у "елементах типу", не у байтах.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
