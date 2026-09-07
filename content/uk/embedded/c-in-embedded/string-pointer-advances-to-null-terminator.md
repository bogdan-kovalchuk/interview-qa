---
id: emb-cppfound-0037
title: "Що виведе?"
description: "How pointer iteration reaches the string null terminator."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
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
char str[] = "hello";
char *p = str;
while(*p) p++;
printf("%td", p-str);
```

## Short answer

`5`.

`str` decay-ується до `char*`. Цикл йде до `'\0'`: після `'h','e','l','l','o'` – `*p = '\0'` (false) -> стоп. `p` вказує на null-terminator.

`p - str` = 5 елементів = `strlen("hello")`. Це стандартний спосіб реалізації `strlen` через pointer arithmetic. `%td` для `ptrdiff_t`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
