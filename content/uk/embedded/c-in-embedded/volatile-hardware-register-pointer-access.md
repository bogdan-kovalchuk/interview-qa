---
id: emb-cppfound-0044
title: "Навіщо `volatile` при роботі з hardware registers через вказівник?"
description: "How volatile affects compiler access to hardware registers."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 4
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

Без `volatile` компілятор може:
1. <span class="warn">Кешувати</span> значення регістру у CPU регістрі і не перечитувати (пропустить апаратну зміну);
2. <span class="warn">Видалити "зайві" записи</span> (dead store elimination) – якщо значення не читається далі;
3. <span class="warn">Переупорядкувати</span> операції для оптимізації.

З `volatile`: кожен read/write реально виконується у порядку написання.

Паттерн: `volatile uint32_t * const GPIOA_ODR = (volatile uint32_t*)0x40020014U;`[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
