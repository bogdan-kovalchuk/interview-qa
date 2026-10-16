---
id: emb-testemb-0008
title: "Які dynamic analysis підходи можливі для embedded C/C++: sanitizers на host, Valgrind, trace, fault injection?"
track: embedded
section: testing-embedded
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-testing
    title: "Zephyr Project documentation: Testing"
    url: https://docs.zephyrproject.org/latest/develop/test/index.html
---

## Short answer

На host можна запускати **ASan/UBSan/TSan** для логіки без hardware dependency, а `Valgrind` корисний для Linux-target або host-сценаріїв. На target частіше використовують trace, coverage, watchpoints, stack watermarking, fault injection, bus/error simulation і HIL tests. <span class="warn">Sanitizer на PC не доводить коректність ISR, DMA cache coherency або реального timing.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
