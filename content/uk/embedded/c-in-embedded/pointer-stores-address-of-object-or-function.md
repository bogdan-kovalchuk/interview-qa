---
id: emb-cppfound-0001
title: "Що таке вказівник у C і що він зберігає?"
description: "What a C pointer is and what it stores."
track: embedded
section: c-in-embedded
level: junior
type: concept
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

**Вказівник** – змінна, що зберігає **адресу** іншого об'єкта або функції в пам'яті. Він не зберігає саме значення, а лише місцезнаходження.

Дві фундаментальні операції:
- `&x` – взяття адреси: повертає адресу об'єкта `x`;
- `*p` – розіменування: читає/записує значення за адресою `p`.

Вони обернені: `*(&x) == x` завжди. У embedded вказівники критичні для доступу до hardware registers, DMA буферів, callback-функцій.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
