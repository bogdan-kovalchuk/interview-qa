---
id: emb-cppfound-0096
title: "Trap: що не так?"
description: "Why dereferencing an uninitialized double pointer is undefined behavior."
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
int **pp;
*pp = malloc(10*sizeof(int));
```

## Short answer

<span class="warn">Wild pointer – UB.</span> `int **pp;` – неініціалізований double pointer, містить garbage-адресу.

`*pp = malloc(...)` – розіменовує `pp` (UB!) і записує адресу виділеної пам'яті за невідомою адресою. Це може зіпсувати будь-яку область пам'яті.

Правильно: 

```c
int *p = NULL;
int **pp = &p;
*pp = malloc(10*sizeof(int));
```

Завжди ініціалізуй вказівники перед використанням.[^embeddedinterviewlab]

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
