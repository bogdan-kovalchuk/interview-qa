---
id: emb-structs-0022
title: "Trap: чому signed bit-field на 1 біт майже завжди пастка?"
description: "1-bit signed field не може представляти значення +1 у two's complement моделі."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 1
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
struct F {
    signed int flag : 1;
};
```

## Short answer

<span class="warn">1-bit signed field не може представляти значення `+1` у two's complement моделі.</span>

Типовий діапазон для signed 1-bit: `-1` і `0`. Якщо очікуєш boolean `0/1`, читання після присвоєння `flag = 1` може дати `-1`. Це ламає порівняння на кшталт `flag == 1`.

Захист: для flags використовуй `unsigned int flag : 1` або `bool` там, де layout не критичний.[^embeddedinterviewlab]

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
