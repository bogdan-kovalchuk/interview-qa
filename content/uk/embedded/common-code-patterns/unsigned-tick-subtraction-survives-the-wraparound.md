---
id: emb-patterns-0037
title: "Як додати timeout до polling-циклу очікування прапорця?"
description: "Запам'ятай старт, на кожній ітерації перевіряй різницю тіків проти ліміту."
track: embedded
section: common-code-patterns
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
uint32_t start = tick();
while (!(REG->SR & FLAG)) {
  if (tick() - start > TIMEOUT_MS) return ERR_TIMEOUT;
}
```

## Short answer

**Запам'ятай старт, на кожній ітерації перевіряй різницю тіків проти ліміту.**

Віднімання unsigned тіків коректно переживає wraparound лічильника. Це рятує від нескінченного зависання, якщо апаратура так і не виставить прапорець.

Правило: жодного нескінченного busy-wait на апаратний прапорець – завжди timeout + повернення помилки.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
