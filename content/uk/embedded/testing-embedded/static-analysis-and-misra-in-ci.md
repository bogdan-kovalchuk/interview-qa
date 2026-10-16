---
id: emb-testemb-0007
title: "Які static analysis tools доречні для C/C++ firmware і як інтегрувати MISRA/AUTOSAR checks у CI?"
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

Для firmware доречні **clang-tidy**, `cppcheck`, compiler warnings, commercial analyzers на кшталт PC-lint/FlexeLint, Coverity, Polyspace або Klocwork. У CI запускають аналіз на кожен target/config, фіксують rule set, suppressions і baseline, а MISRA/AUTOSAR deviation оформлюють явно. <span class="warn">Важливо аналізувати той самий code path, include dirs і defines, що й cross-build.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
