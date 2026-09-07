---
id: emb-macros-0028
title: "Trap: чому додавання MIN/MAX-обмеження у макрос фільтра спричинило шум у вимірах ADC?"
description: "Аргумент-вираз із adc_read() обчислюється кілька разів у тілі макроса (double evaluation)."
track: embedded
section: inline-and-macros
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
#define FILT(s) ((s) + ((adc_read() - (s)) >> 3))
```

## Short answer

<span class="warn">Аргумент-вираз із `adc_read()` обчислюється кілька разів</span> у тілі макроса (double evaluation).

Кожне розгортання `adc_read()` запускає нову конверсію АЦП з іншим значенням і шумом, а зайві конверсії ще й марнують енергію. Фільтр рахує на неузгоджених семплах.

Захист: `static inline` з одним параметром, або зчитай `adc_read()` в локальну змінну один раз перед обчисленням.[^embeddedinterviewlab]

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
