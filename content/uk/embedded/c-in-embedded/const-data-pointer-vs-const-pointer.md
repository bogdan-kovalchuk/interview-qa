---
id: emb-cppfound-0026
title: "Чим відрізняється `const int *p` від `int * const p`?"
description: "How const applies to pointed-to data and to the pointer itself."
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

`const int *p` (або `int const *p`) – **вказівник на константний int**:
- `*p = 5` – заборонено (дані захищені);
- `p = &y` – дозволено (адресу можна змінити).

`int * const p` – **константний вказівник на int**:
- `*p = 5` – дозволено;
- `p = &y` – заборонено (адреса фіксована).

`const int * const p` – і дані, і адреса незмінні. Правило: читай справа наліво.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
