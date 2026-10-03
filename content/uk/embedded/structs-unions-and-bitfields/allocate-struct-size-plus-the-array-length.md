---
id: emb-structs-0033
title: "Як правильно виділити пам’ять для flexible array member?"
description: "Потрібно виділити sizeof(struct Packet) + len байтів."
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
struct Packet {
    uint16_t len;
    uint8_t data[];
};
```

## Short answer

Потрібно виділити `sizeof(struct Packet) + len` байтів.

Наприклад: `struct Packet *p = malloc(sizeof *p + len);`; після перевірки результату записують `p->len = len`, а payload лежить у `p->data[0..len-1]`; `sizeof *p` не включає гнучкий масив.

Перевіряй переповнення `size_t` під час додавання розміру, а результат `malloc` – на `NULL`. У bare-metal без heap можна резервувати статичний byte buffer відповідного розміру.[^iso-c-n1570]

## Detailed explanation

Для об’єкта зі flexible array member треба виділити місце для фіксованої частини структури та всіх потрібних елементів гнучкого масиву. Для масиву байтів типовий розрахунок – `sizeof(struct Packet) + len`, де `len` є кількістю байтів payload; `sizeof` уже охоплює саму структуру, але не її гнучкі елементи.[^iso-c-n1570]

Після успішного allocation поле довжини записують окремо, а payload використовують лише в межах виділеної кількості. Перевірка результату `malloc` обов’язкова: при нестачі пам’яті він повертає null pointer. Також треба перевірити, що додавання розміру заголовка й довжини не переповнює `size_t`; переповнення може дати блок меншого розміру, ніж потрібно.

Приклад для звичайного heap-based C-коду:

```c
if (len > SIZE_MAX - sizeof(struct Packet)) {
    return NULL;
}
struct Packet *p = malloc(sizeof *p + len);
if (p == NULL) {
    return NULL;
}
p->len = len;
```

Тут `len` має бути байтовою кількістю, оскільки елемент `data` має тип `uint8_t`. Для гнучкого масиву з елементами ширшого типу потрібен добуток кількості елементів на `sizeof` елемента, також із перевіркою переповнення. У системі без heap аналогічно резервують буфер достатнього розміру та перевіряють його alignment і межі.

**Типова помилка:** виділити лише `sizeof *p`, а потім записати `data[0]`, або довіряти `len` без перевірок. Обидва випадки можуть спричинити вихід за межі allocation; ліміт має походити з довіреного розміру буфера чи протоколу, а не лише з поля пакета.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->
