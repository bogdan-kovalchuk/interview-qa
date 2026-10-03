---
id: emb-structs-0035
title: "Що таке opaque struct pointer у C API?"
description: "Opaque pointer приховує визначення структури від користувача API: у header є лише forward declaration."
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

**Opaque pointer** приховує визначення структури від користувача API: у header є лише forward declaration.

Наприклад, `typedef struct UartDriver UartDriver;`, а поля `struct UartDriver` визначені тільки в `.c` файлі. Caller працює з `UartDriver *` через функції API і не залежить від внутрішнього layout.

Такий підхід дає змогу змінювати внутрішній layout без залежності клієнта від полів структури; сумісність ABI все одно залежить від усього публічного інтерфейсу.[^iso-c-n1570]

## Detailed explanation

Opaque pointer – це покажчик на тип структури, повне визначення якого приховане від коду-клієнта API. Заголовок може оголосити тег `struct UartDriver`, не описуючи його членів; таке оголошення робить тип incomplete, але покажчик на нього можна оголошувати.[^iso-c-n1570]

Повний опис структури розміщують у приватному `.c` файлі бібліотеки. Там функції на кшталт `uart_driver_open`, `uart_driver_read` і `uart_driver_close` можуть виділяти об’єкт, звертатися до його полів і керувати його життєвим циклом. Клієнт отримує значення типу `UartDriver *` і передає його назад у функції API, але не може створити об’єкт за значенням або читати його поля без повного визначення.[^iso-c-n1570]

Приклад заголовка може містити `typedef struct UartDriver UartDriver;` і прототипи публічних функцій, а приватний файл визначає `struct UartDriver { ... };`. Це зменшує залежність клієнтського коду від внутрішнього layout: зміну поля можна сховати за незмінним інтерфейсом. Однак стабільність ABI не гарантована автоматично – її визначають також calling convention, видимі типи, правила володіння ресурсом і сумісність самих функцій.[^iso-c-n1570]

У вбудованому драйвері такий інтерфейс корисний, коли стан пристрою містить регістри, lock або внутрішні лічильники, які клієнт не повинен змінювати напряму. Не плутайте приховану структуру з відсутністю об’єкта: він існує, але операції над ним доступні лише через визначений API. Якщо API приймає caller-provided storage, клієнту все одно потрібен окремий узгоджений механізм отримати правильний розмір та вирівнювання.[^iso-c-n1570]

**Типова помилка:** оголосити opaque тип, а потім спробувати `sizeof(UartDriver)` або `driver->field` у клієнті. Ці операції потребують повного визначення; натомість клієнт має користуватися функціями API.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->
