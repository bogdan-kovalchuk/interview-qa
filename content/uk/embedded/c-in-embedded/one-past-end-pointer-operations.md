---
id: emb-cppfound-0087
title: "Що таке \"one-past-the-end\" pointer і які операції з ним дозволені?"
description: "Which operations are valid for a pointer one element past an array."
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

**One-past-the-end** – вказівник на елемент одразу після масиву: `int *end = arr + N`. За стандартом C – легальний.

Дозволено:
- **Формувати** (адреса коректна);
- **Порівнювати**: `p != end`, `p <= end`;
- **Віднімати** від іншого вказівника у масиві.

Заборонено:
- <span class="warn">Розіменовувати</span>: `*end` -> UB;
- <span class="warn">Збільшувати далі</span>: `end+1` -> UB.

Стандартний ідіом: `for(int *p=arr; p!=arr+N; p++)`[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
