---
id: emb-dtypes-0058
title: "Як перевірити розмір stack frame функції в GCC?"
description: "Прапорець -fstack-usage змушує GCC генерувати .su файли з розміром stack frame кожної функції."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
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

Прапорець **-fstack-usage**: GCC генерує `.su` файли поряд з `.o`.

Формат рядка у `.su`: `file.c:10:5:foo 2048 static`
Поля (пробіл-сепаратор): [1] `file:line:col:func`, [2] байти, [3] тип.

Аналіз найбільших stack frame-ів: `cat *.su | sort -k2 -rn | head -20`

Також: `-Wstack-usage=N` - warning якщо функція використовує >N байт. Обов'язково перевіряй функції, що викликаються з ISR.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
