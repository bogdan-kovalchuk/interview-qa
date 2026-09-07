---
id: emb-dtypes-0079
title: "Що означає storage class `register` і чи має він значення сьогодні?"
description: "Сучасні компілятори ігнорують register як підказку, залишається лише заборона брати адресу такої змінної."
track: embedded
section: data-types-and-memory-layout
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
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

`register` - підказка компілятору зберігати змінну у CPU регістрі. У сучасних компіляторах (GCC, Clang з `-O2`+) - <span class="warn">ігнорується</span>: компілятор сам оптимально розподіляє регістри.

Єдиний залишковий ефект: **забороняє взяти адресу** змінної (`&reg_var` - помилка компіляції).

У C++17 - deprecated. У C11 збережений для сумісності; Не використовуй у нових проектах - довір register allocation компілятору.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
