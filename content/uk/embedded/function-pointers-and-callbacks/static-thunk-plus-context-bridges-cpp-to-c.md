---
id: emb-fnptr-0041
title: "Як зробити C callback для C++ object-а?"
description: "Використовують static thunk + context pointer."
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
  - source_id: cppreference-member-pointers
    title: "cppreference: Pointers"
    url: https://en.cppreference.com/w/cpp/language/pointer
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює типи вказівників на функції та члени C++; не визначає вимоги конкретного HAL callback API."
---

## Short answer

Використовують static thunk + context pointer.

`static void thunk(void *ctx, uint8_t b) { static_cast<App *>(ctx)->on_rx(b); }` `uart_register(thunk, this);`

Static member function не має прихованого `this` і сумісна зі звичайним function pointer, якщо signature збігається. `ctx` повертає object instance вручну.

Правило: це стандартний bridge між C HAL і C++ class design.[^cppreference-member-pointers]

## Detailed explanation

Static thunk разом із `void *context` дає C callback змогу викликати метод конкретного C++ object-а.[^cppreference-member-pointers]

Нестатичний метод має неявний параметр `this`, а C API зазвичай приймає звичайний function pointer із фіксованою сигнатурою. Статичний метод класу не має прихованого `this`, тому його можна передати як звичайний вказівник на функцію, якщо типи параметрів і результату точно збігаються. Контекст переносить окремо адресу екземпляра, якого треба обслуговувати.[^cppreference-member-pointers]

Thunk є адаптером між двома домовленостями. Його сигнатура має відповідати API, наприклад `void (*)(void *, uint8_t)`. Усередині він приводить `ctx` до `App *` і викликає `on_rx(b)`. Такий поділ дозволяє одному статичному thunk обслуговувати різні екземпляри; кожен із них реєструється зі своїм контекстом. API може називати параметр по-різному, але порядок, типи й calling convention мають збігатися.

Прикладом є UART driver, який під час приймання байта викликає callback із байтом і збереженим контекстом. Реєстрація передає `thunk` і `this`; пізніше thunk повертає типізований object та делегує роботу його методу. Якщо driver не підтримує context pointer, потрібен інший дизайн, наприклад окремі статичні adapter-и для обмеженого набору екземплярів.

**Типові помилки:**

- забути передати context під час реєстрації;
- використати сигнатуру thunk, що відрізняється від API;
- передати `this`, але знищити object до вимкнення callback-ів.[^cppreference-member-pointers]

## Sources

<!-- generated from frontmatter -->
