---
id: emb-dtypes-0103
title: "What are hardware registers, and how does a memory-mapped register differ from a CPU general-purpose register?"
track: embedded
section: fundamentals
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: cmsis-peripheral-access
    title: "Arm CMSIS-Core: Peripheral Access"
    url: https://arm-software.github.io/CMSIS_5/Core/html/group__peripheral__gr.html
  - source_id: arm-cortex-m33-core-registers
    title: "Arm Cortex-M33 Processor Technical Reference Manual: Processor core registers summary"
    url: https://developer.arm.com/documentation/100230/0004/functional-description/programmers-model/processor-core-registers-summary
  - source_id: armv8a-memory-model
    title: "Arm: Armv8-A memory model guide, Device memory"
    url: https://developer.arm.com/-/media/Arm%20Developer%20Community/PDF/Learn%20the%20Architecture/Armv8-A%20memory%20model%20guide.pdf?revision=58b1dd0a-3800-4218-b21a-f95a0332034c
---

## Short answer

A **hardware register** is a storage location defined by hardware; it may be a CPU register or a peripheral register. A peripheral **memory-mapped register** has an address in the memory map and is commonly described with a pointer to a `volatile` structure; the MCU documentation defines its exact address and access rules.[^cmsis-peripheral-access] A CPU general-purpose register belongs to the core's register bank and is used by instructions without accessing a peripheral address.[^arm-cortex-m33-core-registers]

## Detailed explanation

TODO
