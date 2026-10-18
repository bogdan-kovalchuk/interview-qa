---
id: emb-cppfound-0047
title: "Що таке flexible array member (FAM) у C99 і де він зберігається?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Flexible Array Member** (FAM) – останнє поле структури з невказаним розміром: `struct Packet { uint8_t len; uint8_t data[]; };`

`sizeof(struct Packet)` не включає `data`. FAM виділяється разом зі структурою: `malloc(sizeof(Packet) + n)` – тоді `data` займає `n` байт одразу після полів структури.

Зберігається у тому ж блоці пам'яті що й структура (heap або static). Не може бути єдиним членом struct і не може у масиві.[^embeddedinterviewlab]

## Detailed explanation

TODO
