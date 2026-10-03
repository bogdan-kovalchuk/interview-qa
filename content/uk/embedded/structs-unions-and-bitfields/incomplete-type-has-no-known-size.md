---
id: emb-structs-0036
title: "Чому incomplete struct не можна створити як object у header?"
description: "Неможливо, бо compiler не знає розмір Driver."
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

## Question code

```c
typedef struct Driver Driver;

Driver d;
```

## Short answer

<span class="warn">Неможливо, бо compiler не знає розмір `Driver`.</span>

Forward declaration створює incomplete type. Можна оголошувати pointer-и на нього, бо розмір pointer відомий, але не можна виділити object by value або звертатися до полів.

Захист: opaque API повертає `Driver *` або приймає caller-provided storage через окремий API, який знає потрібний розмір і вирівнювання.[^iso-c-n1570]

## Detailed explanation

У цьому прикладі `typedef struct Driver Driver;` оголошує тег структури, але не її члени. До визначення членів `struct Driver` має incomplete type: компілятор знає, що це структура, проте її розмір і layout ще невідомі.[^iso-c-n1570]

Оголошення `Driver d;` вимагає повного типу, бо компілятор має зарезервувати достатньо пам’яті для об’єкта `d`. Так само доступ `d.field` потребує знати розташування члена. Покажчик `Driver *p;` оголосити можна: розмір самого покажчика відомий реалізації, навіть якщо розмір об’єкта, на який він вказує, поки невідомий.[^iso-c-n1570]

Приклад: заголовок бібліотеки може надати лише forward declaration і функцію `Driver *driver_create(void)`. Файл реалізації включає повне визначення структури, виділяє пам’ять і реалізує функції роботи з нею. Клієнт зберігає та передає покажчик, а для звільнення викликає `driver_destroy`; так внутрішній layout залишається приватним.[^iso-c-n1570]

Помилка проявляється під час компіляції на декларації об’єкта за значенням, `sizeof(Driver)` або доступі до поля. Це діагностика некоректної програми, а не runtime-проблема: до виконання вона не доходить. Уникайте її, залишаючи неповний тип за API-межею й надаючи функції для створення, використання та знищення об’єкта. Якщо потрібне caller-provided storage, контракт API має надати розмір і вирівнювання без спроби обчислити їх з incomplete type.[^iso-c-n1570]

**Типова помилка:** вважати, що forward declaration описує структуру повністю. Вона лише дозволяє згадувати тип там, де не потрібен розмір самого об’єкта.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
