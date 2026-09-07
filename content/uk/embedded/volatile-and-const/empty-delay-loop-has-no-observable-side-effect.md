---
id: emb-volconst-0034
title: "Trap: що не так із таким delay loop?"
description: "Компілятор може повністю прибрати порожній loop, бо він не має observable side effects."
track: embedded
section: volatile-and-const
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
for (uint32_t i = 0; i < 100000; ++i) {
}
```

<span class="warn">Компілятор може повністю прибрати порожній loop</span>, бо він не має observable side effects.

Додавання `volatile` до лічильника іноді змушує виконати інкременти, але це погана основа для точного timing: оптимізація, частота CPU, wait states і pipeline змінюють реальну затримку.

Захист: для затримок використовуй hardware timer, SysTick, DWT cycle counter або RTOS delay. `volatile` не є timing API.[^embeddedinterviewlab]

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
