---
id: emb-structs-0037
title: "Що таке self-referential struct і чому для неї потрібен pointer?"
description: "Self-referential struct містить pointer на об’єкт свого ж типу, наприклад linked list node."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: concept
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

**Self-referential struct** містить pointer на об’єкт свого ж типу, наприклад linked list node.[^iso-c-n1570]

`struct Node { int value; struct Node *next; };` валідна, бо `next` має розмір pointer. А `struct Node next;` всередині самого `Node` неможлива: це вимагало б нескінченного розміру структури.

У embedded code така структура може бути вузлом intrusive list для RTOS queue або memory pool; час життя вузлів і зв’язки між ними треба контролювати окремо.[^iso-c-n1570]

## Detailed explanation

Self-referential struct – це структура, що містить покажчик на інший об’єкт свого ж типу. Наприклад, у `struct Node` член `struct Node *next` може вказувати на наступний вузол списку; покажчик є повністю визначеним типом члена, хоча сама структура ще описується.[^iso-c-n1570]

Причина, чому тут потрібен саме покажчик, пов’язана з обчисленням розміру. Компілятор може визначити розмір покажчика без знання розміру цільового об’єкта. Натомість член `struct Node next` за значенням вимагав би включити повний ще один `Node` усередину поточного. Той містив би наступний, і так без кінця, тож скінченного layout не існувало б.[^iso-c-n1570]

Приклад: у singly linked list кожен вузол зберігає значення та адресу наступного вузла. Останній вузол зазвичай має `next == NULL`; у двозв’язному списку додають також покажчик `prev`. Самі вузли можуть розташовуватися в купі, статичному масиві або спеціальному pool – сам факт self-reference не визначає спосіб виділення пам’яті.[^iso-c-n1570]

У embedded code така схема використовується, наприклад, для intrusive list у чергах RTOS або списках вільних блоків. Вона економить окрему обгортку для зв’язку, але вимагає контролювати час життя вузлів і коректність зв’язків. Якщо пам’ять обмежена чи динамічне виділення небажане, можна зберігати індекс наступного елемента в масиві pool замість покажчика; це інший спосіб представити зв’язок, а не вкладений об’єкт того самого типу.[^iso-c-n1570]

**Типова помилка:** сприймати `struct Node *next` як вбудований наступний вузол. Це лише адреса; сам вузол має бути створений окремо, а покажчик належно ініціалізований перед використанням.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->
