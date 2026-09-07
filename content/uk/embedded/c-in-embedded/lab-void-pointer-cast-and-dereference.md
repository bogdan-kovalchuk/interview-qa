---
id: emb-cppfound-0080
title: "Що виведе?"
description: "How a void pointer is cast back before dereferencing the original object."
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
int x=42;
void *p=&x;
printf("%d", *(int*)p);
```

## Short answer

`42`.

`void *p = &x` – дозволено у C (implicit conversion). `p` зберігає адресу `x`, але тип "erased".

`*(int*)p` – cast до `int*`, потім розіменування. Коректно оскільки `p` вказує на справжній `int`.

Якби cast до неправильного типу: `*(float*)p` -> UB (strict aliasing). Правило: cast `void*` завжди до того типу, з якого він був отриманий.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
