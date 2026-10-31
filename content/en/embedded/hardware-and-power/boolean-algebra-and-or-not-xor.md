---
id: emb-hwbasic-0001
title: "What is Boolean algebra?"
track: embedded
section: hardware-and-power
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Boolean algebra** is a mathematical system for true/false or 1/0 values.[^dou-embedded-interview] Basic operations: AND (`&&` or logical multiplication), OR (`||` or logical addition), NOT (`!`), and XOR.

In electronics it describes logic gates and digital circuits; in programming – conditions, masks, flags and optimization of logical expressions. For example, De Morgan's laws: `!(A && B) == (!A || !B)` and `!(A || B) == (!A && !B)`.

## Detailed explanation

TODO
