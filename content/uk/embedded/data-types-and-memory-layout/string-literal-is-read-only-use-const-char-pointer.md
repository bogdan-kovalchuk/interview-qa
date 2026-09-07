---
id: emb-dtypes-0006
title: "Чому для рядкового літерала краще використовувати `const char*`, а не `char*`?"
description: "Рядковий літерал лежить у read-only пам'яті, тож const char* документує заборону на запис."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
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

У C рядковий літерал `"hello"` має тип **`char[6]`**, але зберігається у read-only області, зазвичай `.rodata`. Модифікація такого масиву має <span class="warn">undefined behavior</span>. У C++ тип рядкового літерала - `const char[6]`.

Практично правильно: `const char *p = "hello";` - тип не дозволяє випадково написати `p[0] = 'H'`. У C присвоєння `char *p = "hello";` історично дозволене, але GCC з `-Wwrite-strings` попередить про нього.

Ця різниця критична: `char*` приховує read-only nature від системи типів.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
