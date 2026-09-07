---
id: emb-cemb-0021
title: "Яка різниця між C-style приведенням типів і C++ приведенням?"
description: "C-style cast може приховати різні операції, тоді як окремі C++ casts явно показують тип і намір перетворення."
track: embedded
section: c-in-embedded
level: junior
type: comparison
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження цього питання й відповіді; текст відповіді не перевірений незалежно від оригінальної Anki-колоди спільноти."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу c-in-embedded; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**C-style cast** виглядає як `(T)x` і може виконати одразу різні типи приведень: numeric conversion, зняття `const`, reinterpretation pointer-ів. Через це він короткий, але нечіткий і може приховати небезпечну операцію.[^dou-embedded-interview]

У C++ краще використовувати явні casts: `static_cast` для звичайних безпечніших перетворень, `const_cast` тільки для зміни cv-qualifier-ів, `reinterpret_cast` для низькорівневої переінтерпретації, `dynamic_cast` для runtime-перевірки в поліморфних класах. Вони довші, зате показують намір і легше знаходяться в коді.

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Sources

<!-- generated from frontmatter -->
