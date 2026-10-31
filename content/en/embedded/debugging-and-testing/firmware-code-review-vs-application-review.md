---
id: emb-testemb-0001
title: "How does firmware code review differ from ordinary application-code review?"
track: embedded
section: debugging-and-testing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-testing
    title: "Zephyr Project documentation: Testing"
    url: https://docs.zephyrproject.org/latest/develop/test/index.html
  - source_id: gcc-volatiles
    title: "GCC manual: When is a Volatile Object Accessed?"
    url: https://gcc.gnu.org/onlinedocs/gcc/Volatiles.html
  - source_id: cmsis-core-dcache
    title: "CMSIS-Core (Cortex-M): D-Cache Functions"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__Dcache__functions__m7.html
  - source_id: gcc-developer-options
    title: "GCC manual: GCC Developer Options (-fstack-usage)"
    url: https://gcc.gnu.org/onlinedocs/gcc/Developer-Options.html
  - source_id: zephyr-coding-guidelines
    title: "Zephyr Project documentation: Coding Guidelines"
    url: https://docs.zephyrproject.org/latest/contribute/coding_guidelines/index.html
  - source_id: misra-compliance-2020
    title: "MISRA Compliance:2020 – Achieving compliance with MISRA Coding Guidelines"
    url: https://misra.org.uk/app/uploads/2021/06/MISRA-Compliance-2020.pdf
---

## Short answer

**Firmware review** checks not only logic but also interaction with the MCU: registers, ISRs, DMA, clock/reset, timing, memory layout, and power states. It also covers undefined behavior, volatile/MMIO, concurrency between ISR and tasks, stack/heap budget, error paths, and fail-safe states. <span class="warn">Code that looks correct as application logic can break hardware through a race, an incorrect register sequence, or timing.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
