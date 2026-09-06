---
id: emb-macros-0043
title: "Чому `static inline` для bit-операції безпечніший за макрос?"
description: "Type checking + однократне обчислення аргументів + видимість дебагеру."
track: embedded
section: inline-and-macros
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
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
static inline uint32_t set_bit(uint32_t v, unsigned n) {
  return v | (1u << n);
}
```

**Type checking + однократне обчислення аргументів + видимість дебагеру.**

Макрос `#define SET_BIT(v,n) ((v) | (1u << (n)))` у цьому простому випадку може працювати, але він не перевіряє типи параметрів, не дає нормального symbol/debug info і легко перетворюється на double-evaluation баг при ускладненні тіла. Inline-версія приймає типізовані параметри й однаково добре inline-ується.

Правило: bit-маніпуляції в embedded краще тримати як `static inline`, лишаючи макроси для адрес/масок.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
