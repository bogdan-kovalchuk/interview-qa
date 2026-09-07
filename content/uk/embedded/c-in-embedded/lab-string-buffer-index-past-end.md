---
id: emb-cppfound-0076
title: "Trap: яка помилка?"
description: "Why writing at the first index after a string buffer is a buffer overflow."
track: embedded
section: c-in-embedded
level: junior
type: pitfall
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

## Question code

```c
char buf[4]="abc";
buf[4]='\0';
```

## Short answer

<span class="warn">Buffer overflow!</span> `char buf[4] = "abc"` -> `buf = {'a','b','c','\0'}`. Масив 4 елементи, індекси 0..3. `buf[4]` – п'ятий елемент, за межами масиву.

Ще проблема: `"abc"` вже має '\0' на позиції 3 – null-terminator вже є. Рядок коректний;

Якби `char buf[3] = "abc"` – компілятор попередить або поміщає 'a','b','c' без '\0' (усікання); Завжди розмір буфера > довжина рядка + 1.[^embeddedinterviewlab]

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
