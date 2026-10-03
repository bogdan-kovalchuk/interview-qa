---
id: emb-structs-0005
title: "Яким буде типовий розмір після перестановки полів?"
description: "Типово sizeof(struct S) == 8 на ABI, де uint32_t має alignment 4."
track: embedded
section: structs-unions-and-bitfields
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
struct S {
    uint32_t b;
    uint8_t a;
    uint8_t c;
};
```

## Short answer

За ABI, де `uint32_t` вирівнюється на 4 байти, а `uint8_t` на 1, `sizeof(struct S) == 8`.

`b` має offset 0, `a` – 4, `c` – 5, далі йдуть 2 байти tail padding. За тих самих припущень варіант `uint8_t, uint32_t, uint8_t` має 12 байтів.

У масиві з 1000 елементів за цих припущень різниця становить 4000 байтів (приблизно 3.91 KiB).[^iso-c-n1570]

## Detailed explanation

Розмір структури залежить не лише від суми розмірів її полів: компілятор може додати внутрішній padding для вирівнювання наступного поля та кінцевий padding для вирівнювання елементів масиву. Мова C залишає alignment членів реалізаційно визначеним, тому значення 8 не є гарантією для будь-якої платформи.[^iso-c-n1570]

Для наведеного `struct S` припустімо типовий ABI, де `uint32_t` має розмір і alignment 4 байти, а `uint8_t` має розмір та alignment 1 байт. `b` починається з offset 0 і займає байти 0–3. Обидва наступні поля вже вирівняні природно: `a` починається з offset 4, а `c` з offset 5. Alignment структури дорівнює 4, тож два кінцеві байти дають загальний розмір 8.[^iso-c-n1570]

Для порівняння, якщо оголосити спочатку `uint8_t`, потім `uint32_t`, а тоді ще один `uint8_t`, компілятор за цих самих умов вставить три байти перед `uint32_t` і три байти наприкінці. Отримаємо 12 байтів. У масиві з 1000 елементів різниця дорівнює `1000*(12-8) = 4000` байтів, або близько 3.91 KiB.[^iso-c-n1570]

**Типова помилка:** переносити конкретний розмір на інший ABI лише тому, що типи мають однакові назви. Перевіряйте `sizeof` і `offsetof` у цільовій збірці; якщо структура є зовнішнім форматом, визначайте байти явно замість покладатися на її пам’яттєве представлення.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->
