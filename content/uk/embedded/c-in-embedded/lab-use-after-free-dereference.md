---
id: emb-cppfound-0061
title: "Trap: що не так?"
description: "Why dereferencing freed heap memory is undefined behavior."
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
int *p = malloc(sizeof(int)*10);
free(p);
printf("%d", p[0]);
```

## Short answer

<span class="warn">Use-after-free – undefined behavior.</span> Після `free(p)` пам'ять повернута heap manager-у і може бути негайно перевикористана (наприклад, наступним `malloc`).

`p[0]` після `free`: може повернути 0 (heap manager записав туди metadata), старе значення, або crash. У security контексті: джерело use-after-free exploits.

Захист: `free(p); p = NULL;`, потім `if(p != NULL)` перед доступом.[^embeddedinterviewlab]

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
