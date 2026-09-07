---
id: emb-cppfound-0021
title: "Що таке double pointer (`int **pp`) і навіщо він потрібен?"
description: "What a double pointer stores and why functions use it."
track: embedded
section: c-in-embedded
level: junior
type: concept
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

## Short answer

**Double pointer** – вказівник, що зберігає адресу іншого вказівника.

Навіщо:
1. **Зміна pointer caller-а**: `void alloc(int **pp){ *pp = malloc(n); }` – без `**` caller не побачить нову адресу;
2. **2D масиви через масиви вказівників**;
3. Просування parse-cursor: `void parse(char **p){ (*p)++; }`;

Читання типу: `int **pp` – "вказівник на вказівник на int"; `*pp` -> вказівник, `**pp` -> значення int.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
