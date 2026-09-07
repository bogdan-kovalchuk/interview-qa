---
id: emb-align-0039
title: "Що таке type punning через union і чим воно ризиковане?"
description: "Перегляд тих самих байтів як інший тип."
track: embedded
section: memory-alignment-and-endianness
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
union { float f; uint32_t u; } x;
x.f = 1.5f;
// читаємо x.u - бітовий патерн float
```

## Short answer

**Перегляд тих самих байтів як інший тип**. У C union-punning є поширеним прийомом, але значення при читанні іншого члена залежить від представлення типів і реалізації; у C++ читання неактивного члена зазвичай є UB (undefined behavior), тож краще `memcpy` або `std::bit_cast`.

Результат залежить від endianness і представлення (наприклад IEEE 754), тож для локального inspection це може бути корисно, але не для portable serialization.

Правило: для дроту не використовуй union layout; серіалізуй явно з відомим byte order.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
