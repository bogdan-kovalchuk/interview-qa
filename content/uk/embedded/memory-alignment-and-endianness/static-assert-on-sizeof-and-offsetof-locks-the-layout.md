---
id: emb-align-0038
title: "Як перевірити layout структури на етапі компіляції?"
description: "Через _Static_assert + sizeof/offsetof – будь-яка зміна padding чи порядку полів зламає збірку, а не runtime."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 2
reconciled_with:
  en: 4
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
_Static_assert(sizeof(wire_t) == 7, "layout");
_Static_assert(offsetof(wire_t, id) == 6, "offset");
```

## Short answer

**Через `_Static_assert` із `sizeof` та `offsetof`** можна перевірити очікувані розмір структури й зсуви її полів під час компіляції.

Це критично для packed wire-форматів і register map, де точний layout – частина контракту.

Правило: фіксуй очікувані `sizeof` і `offsetof` асертами поруч із визначенням структури.[^iso-c-n1570]

## Detailed explanation

`_Static_assert` дає змогу перевірити властивість типу під час компіляції й зупинити збірку, якщо умова хибна. `sizeof` повертає розмір структури з урахуванням внутрішнього та кінцевого padding, а `offsetof` із `<stddef.h>` визначає зсув конкретного члена від початку структури. Разом ці перевірки фіксують частини layout, від яких залежить код або апаратний контракт.[^iso-c-n1570]

Наприклад, перевірка `sizeof(wire_t) == 7` гарантує саме такий загальний розмір у цій збірці, а `offsetof(wire_t, id) == 6` – що поле `id` починається на байті 6. Якщо ABI, тип поля, порядок оголошень або директива пакування змінять результат, компілятор повідомить про помилку до запуску програми. Ці асерти не роблять формат універсальним: інша архітектура може мати інші правила, тож її збірка також має пройти власні перевірки.[^iso-c-n1570]

Код у прикладі передбачає, що `wire_t` уже оголошено, а компілятор підтримує C11 або новіший стандарт. Для C++ відповідний механізм має назву `static_assert`, без початкового підкреслення. Перевіряй важливі межі окремо: загальний `sizeof` не доводить правильність кожного offset, а кілька перевірених offset не гарантують потрібного byte order чи правил кодування чисел.[^iso-c-n1570]

**Типова помилка:** вважати, що `sizeof` дорівнює сумі розмірів полів. Компілятор може вставити padding для вирівнювання наступних полів або елементів масиву структур, тому розмір і зсуви треба вимірювати та фіксувати окремо.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->
