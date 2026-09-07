---
id: emb-macros-0024
title: "Як визначити макрос `ARRAY_SIZE` і де він небезпечно ламається?"
description: "Повертає кількість елементів масиву на етапі компіляції."
track: embedded
section: inline-and-macros
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Short answer

```c
#define ARRAY_SIZE(a) (sizeof(a) / sizeof((a)[0]))
```

Повертає кількість елементів масиву на етапі компіляції.

<span class="warn">Trap</span>: якщо передати вказівник (зокрема масив-параметр функції, що decay-иться до pointer), `sizeof(a)` дасть розмір вказівника, і результат буде неправильний.

Захист: застосовуй лише до справжніх масивів у тому ж scope; у GCC/Clang є trick з `__builtin_types_compatible_p`, що дає compile error на pointer; у C++ – `std::size`/шаблон.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
