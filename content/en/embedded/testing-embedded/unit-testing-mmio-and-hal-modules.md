---
id: emb-testemb-0006
title: "How do you write a unit test for a module that uses MMIO registers or a HAL driver?"
track: embedded
section: testing-embedded
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-testing
    title: "Zephyr Project documentation: Testing"
    url: https://docs.zephyrproject.org/latest/develop/test/index.html
---

## Short answer

Move register/HAL access behind a thin interface or fake register block, and test the business logic on the host. In the test, verify which bits are written, in what sequence, how flags, timeouts, and errors are handled. <span class="warn">Do not test a real MMIO pointer on the host directly; replace `volatile` register access with a controlled fake/shim layer.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
