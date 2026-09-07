---
id: emb-cppfound-0057
title: "Що таке dispatch table і як реалізувати через function pointers?"
description: "How function-pointer dispatch tables select handlers."
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

**Dispatch table** – масив function pointers для вибору обробника за індексом. Замінює великі `switch`-конструкції.

```c
typedef void (*handler_t)(void);
handler_t table[16] = {
    isr0, isr1, isr2, ...
};
// Виклик:
table[irq_num]();
```

Переваги: O(1) dispatch, легко розширити, підходить для RTOS task tables, state machines, protocol demultiplexers. У embedded: Cortex-M Vector Table – вбудований dispatch table у Flash.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
