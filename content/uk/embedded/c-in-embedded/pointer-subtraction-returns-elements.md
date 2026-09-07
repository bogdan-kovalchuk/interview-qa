---
id: emb-cppfound-0091
title: "Trap: що виведе?"
description: "Why subtracting pointers returns an element distance rather than a byte count."
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
int arr[5];
int *p=arr+3;
int *q=arr+1;
printf("%td", p-q);
```

## Short answer

`2`. Це не trap, але перевіряє розуміння pointer subtraction.

Справжній trap: люди очікують <span class="warn">байтову різницю</span> (8 байт), але отримують **кількість елементів** (2). `p - q` = `(arr+3) - (arr+1) = 2`.

Байтова різниця: `2 * sizeof(int) = 8`. Але `ptrdiff_t` повертає елементи; Якщо потрібна байтова різниця: `(char*)p - (char*)q` або `(uintptr_t)p - (uintptr_t)q`.[^embeddedinterviewlab]

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
