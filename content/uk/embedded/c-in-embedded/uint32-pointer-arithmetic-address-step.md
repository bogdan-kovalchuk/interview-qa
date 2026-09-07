---
id: emb-cppfound-0058
title: "Яку адресу матиме `p+1` якщо `p` вказує на `uint32_t` за адресою `0x2000`?"
description: "How pointer arithmetic scales by the pointed-to type."
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

`p+1 = 0x2004`.

Pointer arithmetic для `uint32_t*`: крок = `sizeof(uint32_t) = 4` байти. `0x2000 + 1*4 = 0x2004`.

Загальна формула: `p + n` -> адреса = `(uintptr_t)p + n * sizeof(*p)`.

Регістровий bank: якщо `volatile uint32_t *reg = (volatile uint32_t*)0x40020000;` -> `reg+1` -> регістр за адресою `0x40020004`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
