---
id: emb-cppfound-0007
title: "Як відбувається pointer arithmetic і чому вона масштабується по `sizeof(T)`?"
description: "How pointer arithmetic advances by elements rather than raw bytes."
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

Арифметика вказівників завжди враховує **розмір елемента типу**:

`T *p; p + n` -> фізично: `(char*)p + n * sizeof(T)`

Приклади:
- `uint8_t *p; p+1` -> +1 байт
- `uint16_t *p; p+1` -> +2 байти
- `uint32_t *p; p+1` -> +4 байти

Це дозволяє ітерувати масиви природно: `p++` – наступний елемент, незалежно від розміру. Критично у embedded при роботі з register banks і DMA буферами.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
