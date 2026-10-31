---
id: emb-testemb-0002
title: "How should embedded C code be tested on the host and target, and what should each level cover?"
track: embedded
section: debugging-and-testing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-testing
    title: "Zephyr Project documentation: Testing"
    url: https://docs.zephyrproject.org/latest/develop/test/index.html
  - source_id: zephyr-ztest
    title: "Zephyr Project documentation: Test Framework (Ztest)"
    url: https://docs.zephyrproject.org/latest/develop/test/ztest.html
  - source_id: zephyr-native-sim
    title: "Zephyr Project documentation: Native simulator - native_sim"
    url: https://docs.zephyrproject.org/latest/boards/native/native_sim/doc/index.html
  - source_id: zephyr-posix-arch
    title: "Zephyr Project documentation: The POSIX architecture"
    url: https://docs.zephyrproject.org/latest/boards/native/doc/arch_soc.html
  - source_id: zephyr-twister
    title: "Zephyr Project documentation: Test Runner (Twister)"
    url: https://docs.zephyrproject.org/latest/develop/twister/index.html
  - source_id: zephyr-coverage
    title: "Zephyr Project documentation: Generating coverage reports"
    url: https://docs.zephyrproject.org/latest/develop/test/coverage.html
---

## Short answer

**Host tests** cover pure logic: state machines, parsers, protocol framing, boundary cases, mocks for HAL/MMIO. **Target tests** verify what depends on the hardware: clocks, drivers, DMA, ISR latency, buses, power states, and real timing. HIL or board tests must catch integration defects that unit tests on a PC cannot see.[^dou-embedded-interview]

## Detailed explanation

TODO
