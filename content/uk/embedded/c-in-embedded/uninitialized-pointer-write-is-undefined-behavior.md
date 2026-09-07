---
id: emb-cppfound-0003
title: "Trap: що відбудеться?"
description: "Why writing through an uninitialized pointer is undefined behavior."
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
int *p;
*p = 5;
```

## Short answer

`p` – <span class="warn">wild pointer</span>: неініціалізований вказівник містить garbage-адресу (випадкове значення зі стека).

Запис `*p = 5` -> undefined behavior: може перезаписати випадкову область пам'яті, іншу змінну, або спричинити <span class="warn">HardFault</span> на Cortex-M (якщо адреса поза RAM).

Захист: завжди ініціалізуй вказівники: `int *p = NULL;` або одразу `int *p = &x;`[^embeddedinterviewlab]

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
