---
id: emb-structs-0016
title: "Trap: що небезпечно в union type punning?"
description: "Пастка не в C-синтаксисі, а в переносимості результату і різниці C vs C++."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: pitfall
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
union U { float f; uint32_t u; };
union U x;
x.f = 1.0f;
uint32_t bits = x.u;
```

## Short answer

<span class="warn">Пастка не в C-синтаксисі, а в переносимості результату і різниці C vs C++.</span>

У C99/C11 читання іншого member-а union для inspection object representation є стандартно описаним type punning pattern; це не те саме, що pointer-cast strict aliasing violation. Але значення `bits` все одно залежить від representation `float` і endianness. У C++ читання inactive union member зазвичай є undefined behavior.

Захист: для portable bit copy використовуй `memcpy(&bits, &x.f, sizeof bits)`, а у C++20 – `std::bit_cast`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
