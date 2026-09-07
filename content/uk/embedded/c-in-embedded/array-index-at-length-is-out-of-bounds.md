---
id: emb-cppfound-0030
title: "Trap: що не так?"
description: "Why an index equal to the array length is out of bounds."
track: embedded
section: c-in-embedded
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
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
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу c-in-embedded; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Question code

```c
int arr[5];
arr[5] = 0;
```

## Short answer

<span class="warn">Out-of-bounds write -> undefined behavior.</span> Валідні індекси: `0..4`. `arr[5]` – за межами масиву.

У пам'яті `arr[5]` знаходиться одразу за масивом: це може бути інша локальна змінна, адреса повернення, saved LR.

Наслідки: тихе пошкодження даних або crash при поверненні з функції (зіпсована адреса повернення).

Захист: `-fsanitize=address`, явні перевірки індексів, `static_assert(i < ARRAY_SIZE)`.[^embeddedinterviewlab]

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
