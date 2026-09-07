---
id: emb-cppfound-0035
title: "Trap: `int *p = NULL; if(p) *p = 5;` vs `int *p = NULL; *p = 5;` – чи безпечний перший?"
description: "Why a NULL check prevents only one class of invalid dereference."
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

## Short answer

**Перший – безпечний**. `if(p)` ≡ `if(p != NULL)` – перевірка перед розіменуванням. Якщо `p == NULL` -> умова false, `*p` не виконується.

<span class="warn">Другий – UB</span>: `*p = 5` при `p == NULL` -> HardFault на Cortex-M.

Але: перевірка NULL не захищає від dangling pointer або wild pointer – вони ненульові, але невалідні; NULL-check – необхідна, але недостатня умова безпеки.[^embeddedinterviewlab]

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
