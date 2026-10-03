---
id: emb-fnptr-0019
title: "Що виведе dispatch table?"
description: "Виведе 42. ops[1] – це pointer на dbl."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 2
reconciled_with:
  en: 3
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; це джерело не є доказом тверджень."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Question code

```c
int inc(int x) { return x + 1; }
int dbl(int x) { return x * 2; }
int (*ops[])(int) = { inc, dbl };
printf("%d", ops[1](21));
```

## Short answer

Виведе `42`.

`ops[1]` – це pointer на `dbl`. Виклик `ops[1](21)` робить indirect call і повертає `21 * 2`.

Правило: масив function pointer-ів має містити функції з однаковою сумісною сигнатурою. Для різних сигнатур потрібні wrappers або variant dispatch.[^embeddedinterviewlab] [^iso-c-n1570]

## Detailed explanation

`ops` – це масив pointer to function із типом елементів «функція, що приймає `int` і повертає `int`». Під час ініціалізації `inc` і `dbl` перетворюються на вказівники на функції сумісного типу, тому `ops[0]` зберігає адресу `inc`, а `ops[1]` – адресу `dbl`. [^iso-c-n1570]

Вираз `ops[1](21)` спершу індексує масив і дістає другий pointer, а потім викликає функцію за цією адресою з аргументом `21`. Це indirect call: на відміну від прямого `dbl(21)`, ціль виклику обирається через значення в таблиці. Оскільки тіло `dbl` обчислює `x * 2`, результат виклику дорівнює 42. Для повного прикладу `printf` треба оголосити через `#include <stdio.h>`; сам вираз виклику від цього не змінюється. [^iso-c-n1570]

Такий масив може містити лише вказівники сумісного типу. Функції з різними параметрами чи результатами не стають сумісними через спільне зберігання в одному масиві; потрібні wrapper-и, що приводять їх до єдиного контракту. Індекс також має бути в межах масиву, інакше читання елемента виходить за межі допустимого. [^iso-c-n1570]

Покрокове читання прикладу: індекс `1` вибирає `dbl`; аргумент `21` передається як `x`; множення дає `42`; значення повертається викликачеві; `printf` виводить його через `%d`. Якщо таблицю пізніше змінити або побудувати з даних, перевірка індексу й коректна ініціалізація стають частиною безпечного dispatch-механізму. [^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->
