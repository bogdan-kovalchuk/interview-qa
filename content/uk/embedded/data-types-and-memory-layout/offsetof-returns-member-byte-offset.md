---
id: emb-dtypes-0054
title: "Навіщо потрібен `offsetof()` і де він визначений?"
description: "offsetof(type, member) повертає зміщення поля від початку структури і визначений у stddef.h."
track: embedded
section: data-types-and-memory-layout
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
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
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

`offsetof(type, member)` із `<stddef.h>` повертає байтове зміщення звичайного члена від початку структури; для bit-field його застосовувати не можна.[^iso-c-n1570]

Використання:
1. Перевірка layout: `static_assert(offsetof(CanFrame, crc) == 6, "Wrong layout");` (якщо це справді вимога конкретного ABI/протоколу).
2. Серіалізація/десеріалізація;
3. **container_of** macro (Linux kernel) - отримати struct* за member*.

Значення залежить від layout реалізації; сам macro не фіксує protocol layout.[^iso-c-n1570]

## Detailed explanation

`offsetof(type, member)` з `<stddef.h>` повідомляє, на скільки байтів звичайний член структури віддалений від її початку. Це корисно, коли код має обчислити позицію поля в конкретному об’єкті без припущення, скільки padding компілятор вставив перед ним.[^iso-c-n1570]

Наприклад, якщо структура має поле `crc`, `offsetof(Frame, crc)` дає виміряне для поточної реалізації зміщення. Його можна використати у перевірці вимог конкретного ABI або у внутрішньому коді, що працює з пам’яттю цієї ж програми. Але перевірка на кшталт `static_assert(offsetof(Frame, crc) == 6, ...)` стане помилковою на цілі, де layout інший. Для зовнішнього binary protocol краще описати поля явно та серіалізувати їх у визначеному порядку байтів, а не вважати layout C-структури протоколом.[^iso-c-n1570]

Макрос не приймає bit-field як `member`, бо такий член не має самостійної адреси, яку можна виразити байтовим offset. Також не варто застосовувати його до довільних типів чи використовувати результат як гарантію вирівнювання наступного доступу: він відповідає лише фактичному layout структури в даному середовищі.[^iso-c-n1570]

**Приклад:**

```c
struct Frame { uint8_t kind; uint32_t value; };
size_t value_offset = offsetof(struct Frame, value);
```

`value_offset` отримує справжнє зміщення для цього build; воно може містити padding після `kind`. Саме це і є цінністю macro: виміряти розташування, а не вгадати його.

## Sources

<!-- generated from frontmatter -->
