---
id: emb-cppfound-0086
title: "Trap: нескінченний цикл?"
description: "Why an 8-bit loop counter cannot reach the terminating value 256."
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
int arr[256];
int *p=arr;
for(uint8_t i=0;
i<256;
i++) *p++=i;
```

## Short answer

<span class="warn">Так, нескінченний цикл!</span> `uint8_t i` – беззнаковий 8-bit. При `i=255` -> `i++` -> wrap до 0 -> умова `0 < 256` -> true. Цикл ніколи не завершується.

Виправлення: `for(int i=0; i<256; i++)` або `for(size_t i=0; i<256; i++)`.

GCC з `-Wtype-limits`: попередить якщо умова завжди true; Типова помилка при роботі з буферами розміром 256.[^embeddedinterviewlab]

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
