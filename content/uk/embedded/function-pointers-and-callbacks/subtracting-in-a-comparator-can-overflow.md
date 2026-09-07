---
id: emb-fnptr-0033
title: "Trap: що не так із comparator-ом для `qsort`?"
description: "Віднімання може переповнити int, що для signed overflow є undefined behavior."
track: embedded
section: function-pointers-and-callbacks
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
int cmp(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}
```

## Short answer

<span class="warn">Віднімання може переповнити `int`, що для signed overflow є undefined behavior.</span>

Якщо один елемент `INT_MIN`, а інший `INT_MAX`, різниця не представима в `int`. Comparator має повертати порядок, а не обов'язково арифметичну різницю.

Захист: використовуй `return (x > y) - (x < y);` після читання `x` і `y`.[^embeddedinterviewlab]

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
