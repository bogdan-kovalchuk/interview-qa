---
id: emb-fnptr-0041
title: "Як зробити C callback для C++ object-а?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: cppreference-member-pointers
    title: "cppreference: Pointers"
    url: https://en.cppreference.com/w/cpp/language/pointer
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
