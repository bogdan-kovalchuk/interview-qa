---
id: emb-volconst-0005
title: "Що може статися з таким циклом без `volatile`?"
description: "Компілятор може перетворити цикл на нескінченний, бо в межах видимого коду flag ніколи не змінюється."
track: embedded
section: volatile-and-const
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 1
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
uint8_t flag = 0;

while (flag == 0) {
    /* flag встановлює ISR */
}
```

## Short answer

Компілятор може перетворити цикл на <span class="warn">нескінченний</span>, бо в межах видимого коду `flag` ніколи не змінюється.

На `-O2` він має право прочитати `flag` один раз, тримати значення в CPU-регістрі і більше не перечитувати RAM. ISR фізично змінить байт у пам'яті, але main loop може цього не побачити.

Захист: оголоси прапорець як `volatile uint8_t flag`. Якщо прапорець ширший за атомарний доступ платформи або є складніші інваріанти, додай critical section або atomic API.[^embeddedinterviewlab]

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
