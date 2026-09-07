---
id: emb-volconst-0043
title: "Що буде з таким кодом у C?"
description: "У block scope в C99+ це може бути VLA (variable length array), а не обов'язково compile-time fixed array."
track: embedded
section: volatile-and-const
level: junior
type: mechanism
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

## Question code

```c
const int n = 8;
int a[n];
```

## Short answer

У block scope в C99+ це може бути VLA (variable length array), а не обов'язково compile-time fixed array.

`const int n` не робить `n` integer constant expression у C так, як багато хто очікує після C++. На embedded це важливо, бо VLA виділяє пам'ять на stack runtime і часто забороняється coding standards.

Захист: для compile-time розмірів у C використовуй `#define N 8`, `enum { N = 8 }` або static assertions залежно від стандарту.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
