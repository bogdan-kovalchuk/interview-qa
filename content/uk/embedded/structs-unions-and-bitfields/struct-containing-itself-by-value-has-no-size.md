---
id: emb-structs-0038
title: "Trap: що не так із таким визначенням?"
description: "Структура містить саму себе by value, тому її розмір був би нескінченним."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 1
reconciled_with:
  en: 1
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

## Short answer

```c
struct Node {
    int value;
    struct Node next;
};
```

<span class="warn">Структура містить саму себе by value, тому її розмір був би нескінченним.</span>

Compiler не може завершити layout: щоб знати розмір `Node`, треба знати розмір `next`, який знову є `Node`. Дозволений варіант – pointer: `struct Node *next;`.

Захист: для recursive data structures використовуй pointer або index у pool, а не вкладений object того самого типу.[^embeddedinterviewlab]

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
