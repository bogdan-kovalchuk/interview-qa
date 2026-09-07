---
id: emb-dtypes-0082
title: "Що таке `volatile` і як він взаємодіє з оптимізацією компілятора?"
description: "volatile забороняє кешувати чи видаляти звернення до змінної, але не дає atomicity чи memory ordering між потоками."
track: embedded
section: data-types-and-memory-layout
level: middle
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

`volatile` повідомляє компілятору, що значення може змінитися **поза його контролем** (hardware, ISR, multi-threading).

Без `volatile` компілятор може:
1. Кешувати значення у регістрі (не перечитувати);
2. Видалити "зайві" read/write як dead code;
3. Переупорядкувати операції.

<span class="warn">volatile НЕ є синхронізацією</span>: не гарантує atomicity чи memory ordering між потоками. Для потоків - `std::atomic` або `mutex`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
