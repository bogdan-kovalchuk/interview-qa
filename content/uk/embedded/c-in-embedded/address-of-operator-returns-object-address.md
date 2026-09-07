---
id: emb-cppfound-0004
title: "Що таке операція взяття адреси `&` і що вона повертає?"
description: "What the address-of operator returns and where it cannot be used."
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

Оператор `&` (address-of) повертає **адресу об'єкта** у пам'яті – значення типу "вказівник на тип об'єкта".

`int x = 5; int *p = &x;` – `p` тепер вказує на `x`.

Не можна взяти адресу:
- виразів без lvalue (`&(a+b)` – помилка);
- `register` змінних;
- bit-field полів структури.

Типи: `&int` -> `int*`, `&arr` -> `int(*)[N]` (вказівник на масив, не на елемент).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
