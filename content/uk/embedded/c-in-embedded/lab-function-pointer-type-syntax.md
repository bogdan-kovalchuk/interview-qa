---
id: emb-cppfound-0079
title: "Як визначити тип \"вказівник на функцію що приймає `int` і повертає `void`\"?"
description: "How to read and write a C function-pointer declaration."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу c-in-embedded; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
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

## Sources

<!-- generated from frontmatter -->
