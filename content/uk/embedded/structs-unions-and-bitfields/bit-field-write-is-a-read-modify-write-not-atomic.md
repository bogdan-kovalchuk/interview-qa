---
id: emb-structs-0049
title: "Trap: чи можна використовувати bit-field як atomic flag між ISR і main?"
description: "Не варто. Запис bit-field зазвичай є read-modify-write storage unit-а."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: pitfall
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

## Short answer

Запис bit-field зазвичай є read-modify-write storage unit-а, тому його не варто використовувати як atomic flag між ISR і main. Якщо обидва контексти змінюють різні bit-fields в одному storage unit, один запис може перетерти інший. `volatile` не робить цю операцію атомарною.

Захист: використовуй окремі flags, лише якщо їхній доступ атомарний на цій платформі; інакше застосуй critical section або RTOS event flags. `volatile` саме по собі не гарантує атомарності чи синхронізації.[^iso-c-n1570]

## Detailed explanation

Bit-field – це член структури з шириною в бітах, який компілятор розміщує в одиниці зберігання разом з іншими полями. Стандарт C не визначає єдину апаратну інструкцію для запису такого поля: реалізація може прочитати одиницю, змінити потрібні біти й записати її назад. Тому операція над одним полем не обов’язково є атомарною щодо переривання, яке змінює сусіднє поле.[^iso-c-n1570]

Наприклад, якщо `main` встановлює `ready`, а ISR встановлює `error` у тій самій одиниці, обидва контексти можуть прочитати старе значення. Запис із `main` тоді відновить старий біт `error` і втратить зміну ISR. Конкретне розміщення полів і спосіб генерації коду залежать від реалізації, тож не можна покладатися на те, що два поля займають незалежні машинні слова.[^iso-c-n1570]

`volatile` вимагає виконувати доступи відповідно до правил volatile-об’єктів, але не перетворює складену операцію на atomic operation і не створює взаємного виключення. Навіть окремий байт або слово придатні лише тоді, коли ширина та вирівнювання відповідають атомарному доступу цільового MCU і компілятору; це перевіряють за документацією платформи.[^iso-c-n1570]

**Як уникнути помилки:**

- Використовуй atomic тип чи операцію, якщо реалізація й середовище ISR це підтримують.
- Інакше захищай спільну зміну короткою critical section або передавай подію через механізм RTOS.
- Для прапорців не припускай атомарність лише з огляду на тип поля; перевіряй правила конкретної платформи.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
