---
id: emb-testemb-0006
title: "How do you write a unit test for a module that uses MMIO registers or a HAL driver?"
track: embedded
section: debugging-and-testing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-testing
    title: "Zephyr Project documentation: Testing"
    url: https://docs.zephyrproject.org/latest/develop/test/index.html
  - source_id: cmsis-core-peripheral-access
    title: "CMSIS-Core (Cortex-M): Peripheral Access"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__peripheral__gr.html
  - source_id: gcc-volatiles
    title: "GCC manual: When is a Volatile Object Accessed?"
    url: https://gcc.gnu.org/onlinedocs/gcc/Volatiles.html
  - source_id: zephyr-ztest
    title: "Zephyr Project documentation: Test Framework (Ztest)"
    url: https://docs.zephyrproject.org/latest/develop/test/ztest.html
---

## Short answer

Move register/HAL access behind a thin interface or fake register block, and test the business logic on the host. In the test, verify which bits are written, in what sequence, how flags, timeouts, and errors are handled. <span class="warn">Do not test a real MMIO pointer on the host directly; replace `volatile` register access with a controlled fake/shim layer.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
