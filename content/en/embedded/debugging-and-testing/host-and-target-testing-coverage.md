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
---

## Short answer

**Host tests** cover pure logic: state machines, parsers, protocol framing, boundary cases, mocks for HAL/MMIO. **Target tests** verify what depends on the hardware: clocks, drivers, DMA, ISR latency, buses, power states, and real timing. HIL or board tests must catch integration defects that unit tests on a PC cannot see.[^dou-embedded-interview]

## Detailed explanation

TODO
