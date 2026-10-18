---
id: emb-cppfound-0079
title: "Як визначити тип \"вказівник на функцію що приймає `int` і повертає `void`\"?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

`void (*fp)(int);`. Цей запис означає вказівник на функцію.

Читання: `fp` – вказівник (`*fp`), що є функцією (`(*fp)(int)`), що повертає void.

Для зручності – `typedef`:

```c
typedef void (*callback_t)(int);
callback_t fp = my_func;
```

Якщо без typedef для масиву: `void (*table[8])(int);` – масив з 8 function pointers.

Виклик: `fp(42);` або `(*fp)(42);` – обидва коректні.[^embeddedinterviewlab]

## Detailed explanation

TODO
