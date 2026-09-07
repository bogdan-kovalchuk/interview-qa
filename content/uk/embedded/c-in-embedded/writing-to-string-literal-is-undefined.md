---
id: emb-cppfound-0011
title: "Trap: що станеться?"
description: "Why modifying a string literal is undefined behavior."
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
char *s = "hello";
s[0] = 'H';
```

## Short answer

Рядковий літерал `"hello"` зберігається у **.rodata** (Flash/read-only). `s` вказує на цю read-only область.

Запис `s[0] = 'H'` -> <span class="warn">undefined behavior</span>: на ПК – segfault, на MCU – HardFault (якщо MPU захищає Flash) або тихий запис у Flash (що не спрацьовує).

Правильно: `char arr[] = "hello";` – компілятор копіює рядок у writable масив (stack або .data). Тоді `arr[0] = 'H'` – легально.[^embeddedinterviewlab]

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
