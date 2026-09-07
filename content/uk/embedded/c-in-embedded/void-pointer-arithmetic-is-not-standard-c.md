---
id: emb-cppfound-0025
title: "Trap: легально у стандартному C?"
description: "Why arithmetic on void pointers is not standard C."
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
void *p = malloc(10);
p++;
```

## Short answer

<span class="warn">НІ, це невалідний стандартний C</span> (constraint violation). Стандарт забороняє pointer arithmetic на `void*` – розмір елемента невідомий (sizeof(void) не визначений), тому компілятор має видати діагностику.

GCC дозволяє як extension: трактує `sizeof(void) = 1`, тому `p++` -> +1 байт. З `-pedantic-errors`: помилка.

Правильно: перед arithmetic – cast до конкретного типу: `uint8_t *bp = (uint8_t*)p; bp++;`[^embeddedinterviewlab]

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
