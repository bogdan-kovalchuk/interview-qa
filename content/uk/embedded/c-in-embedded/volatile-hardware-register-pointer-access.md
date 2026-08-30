---
id: emb-cppfound-0044
title: "Навіщо <code>volatile</code> при роботі з hardware registers через вказівник?"
description: "How volatile affects compiler access to hardware registers."
track: embedded
section: c-in-embedded
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
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? c-in-embedded; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

Без <code>volatile</code> компілятор може:<br>1. <span class="warn">Кешувати</span> значення регістру у CPU регістрі і не перечитувати (пропустить апаратну зміну);<br>2. <span class="warn">Видалити "зайві" записи</span> (dead store elimination) – якщо значення не читається далі;<br>3. <span class="warn">Переупорядкувати</span> операції для оптимізації.<br><br>З <code>volatile</code>: кожен read/write реально виконується у порядку написання.<br><br>Паттерн: <code>volatile uint32_t * const GPIOA_ODR = (volatile uint32_t*)0x40020014U;</code>[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
