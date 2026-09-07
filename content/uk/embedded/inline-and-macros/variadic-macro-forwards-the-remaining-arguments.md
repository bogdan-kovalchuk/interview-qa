---
id: emb-macros-0042
title: "Що таке variadic-макрос і навіщо `__VA_ARGS__`?"
description: "Variadic-макрос приймає змінну кількість аргументів через ..., а __VA_ARGS__ підставляє їх у тіло."
track: embedded
section: inline-and-macros
level: junior
type: concept
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

## Question code

```c
#define LOG(fmt, ...) \
  printf("[%lu] " fmt, tick(), __VA_ARGS__)
```

## Short answer

**Variadic-макрос приймає змінну кількість аргументів** через `...`, а `__VA_ARGS__` підставляє їх у тіло.

Це дозволяє робити обгортки навколо `printf`-подібних функцій, додаючи префікси (timestamp, рівень логу) і прокидаючи решту аргументів.

Правило: щоб коректно обробити «нуль аргументів», використовуй `##__VA_ARGS__` (GNU) або `__VA_OPT__` (C23/C++20).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
