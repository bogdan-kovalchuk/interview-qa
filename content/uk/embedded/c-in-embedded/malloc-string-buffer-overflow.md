---
id: emb-cppfound-0100
title: "Trap: де помилка?"
description: "Why allocating five bytes is insufficient for the string hello and its terminator."
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
char *p = malloc(5);
strcpy(p, "hello");
p[5] = '\0';
```

## Short answer

<span class="warn">Buffer overflow.</span> `malloc(5)` – 5 байт, а `"hello"` = `{'h','e','l','l','o','\0'}` – 6 байт включно з null-terminator.

`strcpy(p, "hello")` вже переповнює буфер (6 байт у 5-байтний), і `p[5] = '\0'` – шостий запис за межами.

Правильно: `malloc(strlen("hello") + 1)` = `malloc(6)`, або `strncpy(p, "hello", 5); p[4]='\0';` – обрізати якщо треба.[^embeddedinterviewlab]

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
