---
id: emb-dtypes-0013
title: "Де зберігатиметься оголошена всередині функції? `static uint32_t call_count;`"
description: "static локальна змінна живе у .bss, а не на стеку, і зберігає значення між викликами функції."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
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
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? data-types-and-memory-layout; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

У секції **.bss** (zeroed at boot, нема ініціалізатора).

`static` переносить змінну зі stack у статичну пам'ять: lifetime = весь час програми. Значення зберігається між викликами функції.

<span class="warn">Ціна: втрата reentrancy</span> - якщо ISR і main loop викличуть функцію одночасно, вони поділяють одну `call_count` -> race condition.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
