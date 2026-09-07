---
id: emb-dtypes-0043
title: "Знайдіть помилку? `int sum; for(int i = 0; i < n; i++) sum += arr[i];`"
description: "sum не має ініціалізатора, тож перше додавання читає сміття зі стека - undefined behavior."
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

`int sum;` - локальна змінна <span class="warn">без ініціалізатора</span>, contains garbage. Перша операція `sum += arr[0]` -> <span class="warn">undefined behavior</span> (читання неініціалізованої змінної).

На практиці: `sum` почне з випадкового значення зі стека -> результат невірний, але код може іноді "працювати".

Виправлення: `int sum = 0;`. GCC з `-Wall`: `warning: 'sum' is used uninitialized`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
