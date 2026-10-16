---
id: emb-testemb-0007
title: "Which static-analysis tools suit C/C++ firmware, and how should MISRA/AUTOSAR checks be integrated into CI?"
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

For firmware, **clang-tidy**, `cppcheck`, compiler warnings, and commercial analyzers such as PC-lint/FlexeLint, Coverity, Polyspace, or Klocwork are appropriate. In CI, run analysis on each target/config, fix the rule set, suppressions, and baseline, and document MISRA/AUTOSAR deviations explicitly. <span class="warn">It is important to analyze the same code path, include dirs, and defines as the cross-build.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
