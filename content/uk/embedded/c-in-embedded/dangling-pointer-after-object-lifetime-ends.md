---
id: emb-cppfound-0017
title: "Що таке dangling pointer і коли він виникає?"
description: "When a pointer refers to storage whose lifetime has ended."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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

**Dangling pointer** – вказівник, що вказує на <span class="warn">вже звільнену або знищену</span> пам'ять.

Причини: 1; Повернення адреси локальної змінної: `int* f(){ int x=5; return &x; }` – x знищена при поверненні; 2; Після `free(ptr)` без обнулення: `free(ptr); *ptr = 1;` – UB;
3. Вказівник на об'єкт, термін дії якого закінчився.

Небезпека: пам'ять <span class="warn">виглядає валідною</span> до її перевикористання. Баги надзвичайно важко відтворити.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
