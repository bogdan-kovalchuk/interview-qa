---
id: emb-testemb-0008
title: "Which dynamic-analysis approaches are possible for embedded C/C++: host sanitizers, Valgrind, tracing, and fault injection?"
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

On the host, you can run **ASan/UBSan/TSan** for logic without hardware dependencies, and `Valgrind` is useful for Linux-target or host scenarios. On target, trace, coverage, watchpoints, stack watermarking, fault injection, bus/error simulation, and HIL tests are more common. <span class="warn">A sanitizer on a PC does not prove correctness of ISRs, DMA cache coherency, or real timing.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
