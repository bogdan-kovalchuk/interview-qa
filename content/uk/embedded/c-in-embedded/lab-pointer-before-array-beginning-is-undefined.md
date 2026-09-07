---
id: emb-cppfound-0071
title: "Trap: UB?"
description: "Why decrementing a pointer at the beginning of an array is undefined."
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
int arr[3]={1,2,3};
int *p=arr;
p--;
printf("%d",*p);
```

## Short answer

<span class="warn">Так, UB.</span> `p = arr` -> вказівник на `arr[0]`. `p--` -> `arr-1`, що знаходиться <span class="warn">поза масивом</span>.

Допустимі вказівники для `arr[3]`: `arr` (=arr+0) до `arr+3` (one-past-the-end). `arr-1` – UB вже при формуванні, не тільки при розіменуванні.

Компілятор може припустити що UB не відбувається -> непередбачувані оптимізації; Отже, arr-1 формувати не можна.[^embeddedinterviewlab]

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
