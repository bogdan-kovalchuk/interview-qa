---
id: emb-cppfound-0040
title: "Trap: UB?"
description: "Why pointer arithmetic beyond one-past-the-end is undefined behavior."
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
int arr[4]={0};
int *p=arr;
p+=5;
*p=1;
```

## Short answer

<span class="warn">Так, UB</span> (навіть без розіменування).

Формування вказівника `p += 5` виходить за межі масиву більш ніж на 1: `arr` має 4 елементи, тому валідні вказівники: `arr` до `arr+4` (включно "one-past-the-end"). `arr+5` -> UB вже при формуванні.

One-past-the-end (`arr+4`) – дозволено формувати, але <span class="warn">не розіменовувати</span>.[^embeddedinterviewlab]

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
