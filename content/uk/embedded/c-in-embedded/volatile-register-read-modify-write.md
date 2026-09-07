---
id: emb-cppfound-0098
title: "Що зробить?"
description: "What a volatile read-modify-write sequence does and why it can race with an ISR."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
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

## Question code

```c
uint32_t reg=*((volatile uint32_t*)0x40020010);
reg|=(1<<5);
*((volatile uint32_t*)0x40020010)=reg;
```

## Short answer

Read-Modify-Write (RMW) операція над hardware register:
1. **Read**: читає поточне значення регістру з адреси `0x40020010`;
2. **Modify**: встановлює біт 5 (`|= (1<<5)`), не змінюючи інші біти;
3. **Write**: записує назад у регістр.

<span class="warn">Ризик</span>: між read і write інший потік або ISR може змінити регістр -> race condition; Для атомарного RMW: STM32 BSRR (GPIO), або disable IRQ навколо RMW.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
