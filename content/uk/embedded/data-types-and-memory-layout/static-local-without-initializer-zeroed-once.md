---
id: emb-dtypes-0041
title: "Trap: чи ініціалізується всередині функції нулем? `static int x;`"
description: "static локальна без ініціалізатора еквівалентна static int x = 0 і зануляється лише один раз при завантаженні."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
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

**Так**, але це тонкий момент: `static` локальна без ініціалізатора ≡ `static int x = 0;` - нуль при першому виклику (zeroed у `.bss` при boot).

`static int x = 5;` -> ініціалізується значенням 5 один раз. Подальші зміни зберігаються між викликами.

<span class="warn">Звичайна</span> `int x;` - НЕ ініціалізується (garbage). Помилка: припускати що `int x;` = 0 у першому виклику.[^embeddedinterviewlab]

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
