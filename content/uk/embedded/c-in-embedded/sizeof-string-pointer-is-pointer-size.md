---
id: emb-cppfound-0048
title: "Що поверне на 32-bit?"
description: "Why sizeof on a string pointer returns the pointer size."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 4
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
char *p = "hello";
printf("%zu", sizeof(p));
```

## Short answer

**4** (на 64-bit – 8).

`p` – вказівник типу `char*`, тож `sizeof(p) = sizeof(char*) = 4` на 32-bit. Не розмір рядка, не 6 (з '\0'), а лише розмір вказівника.

Для розміру рядка: `strlen(p) + 1` = 6 (з null-terminator) або `strlen(p)` = 5.

Порівняй: `char arr[] = "hello"; sizeof(arr) = 6` – тут масив, не вказівник.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
