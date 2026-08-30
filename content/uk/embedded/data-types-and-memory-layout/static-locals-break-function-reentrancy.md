---
id: emb-dtypes-0057
title: "Що таке reentrant функція і чому `static` локальні змінні порушують reentrancy?"
description: "static локальна спільна для всіх викликів, тож переривання ISR і main loop через неї спричиняє race condition."
track: embedded
section: data-types-and-memory-layout
level: middle
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

**Reentrant функція** може безпечно викликатися одночасно з кількох потоків або рекурсивно.

`static` локальна - одна на всю функцію (у `.data`/`.bss`), не на stack: якщо ISR перерве функцію і викличе її знову, обидва контексти змінюватимуть одну змінну -> <span class="warn">race condition</span>.

Класичний приклад: `strtok()` - не reentrant (static buffer). Використовуй `strtok_r()`. У bare-metal: якщо функція викликається з ISR і main loop - уникай static locals.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
