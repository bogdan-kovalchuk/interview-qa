---
id: emb-structs-0041
title: "Trap: як padding може стати витоком інформації?"
description: "Якщо відправити або записати raw bytes структури, padding може містити старі дані зі stack/RAM."
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

<span class="warn">Якщо відправити або записати raw bytes структури, padding може розкрити дані, які програма не призначала для передачі.</span>

Наприклад, `send(fd, &msg, sizeof msg)` може включити padding bytes між полями. Ці bytes не ініціалізуються окремим assignment до полів і можуть містити фрагменти попередніх змінних.

Захист: zero-initialize структуру перед заповненням, серіалізуй поля явно і не експортуй raw struct layout як security boundary.[^iso-c-n1570]

## Detailed explanation

Padding bytes – це проміжки в object representation структури, які реалізація може додавати для alignment members. Вони не є полями протоколу й не мають визначеного прикладного значення. Стандарт C дозволяє padding bytes набувати unspecified values, коли записується значення структури, тому присвоєння всіх видимих полів не гарантує передбачуваного вмісту кожного байта об’єкта.[^iso-c-n1570]

Ризик виникає, коли програма передає `sizeof msg` байтів через socket, USB, DMA або зберігає їх у файл. Сире копіювання включає і padding; частина цих байтів може відображати залишки попереднього стану пам’яті, а зовнішній отримувач отримає дані поза задумом протоколу. Навіть якщо конкретний компілятор у конкретній збірці зануляє padding у певному випадку, це не є загальною гарантією для подальших присвоєнь і всіх реалізацій.[^iso-c-n1570]

**Приклад:** структура з полем `uint8_t type` і полем `uint32_t length` часто має проміжок між цими полями на поширених ABI. Якщо відправити її пам’ять напряму, межа повідомлення описана через layout компілятора, а не через протокол. Інший компілятор може вибрати інший layout, а padding може бути непередбачуваним.[^iso-c-n1570]

**Типові помилки:**

- Вважати, що ініціалізація кожного member зануляє весь object representation.
- Покладатися лише на `{0}` або попередній `memset`, хоча пізніші операції можуть змінювати представлення.
- Вважати локальну структуру сумісною з wire format лише через збіг поточного layout.

Безпечніший підхід – кодувати кожне поле у визначеному порядку, ширині та byte order. Якщо буфер усе ж має містити структуру, перевір її правилами конкретної платформи та очищуй перед передачею; це зменшує ризик витоку, але не робить layout переносимим.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
