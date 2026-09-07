---
id: emb-macros-0012
title: "Що робить оператор стрінгіфікації `#` у макросі?"
description: "#x перетворює аргумент макроса на string literal: тут підставиться \"hello\"."
track: embedded
section: inline-and-macros
level: junior
type: mechanism
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
#define STR(x) #x
printf("%s", STR(hello));
```

## Short answer

**`#x` перетворює аргумент макроса на string literal**: тут підставиться `"hello"`.

Це працює тільки всередині function-like макроса і застосовується до тексту аргументу як він написаний. Корисно для assert-повідомлень, debug-трасування і таблиць імен.

Правило: `#` бере текст аргументу, а не його значення – для розгортання вкладеного макроса потрібен другий рівень.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
