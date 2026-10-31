---
id: emb-testemb-0007
title: "Which static-analysis tools suit C/C++ firmware, and how should MISRA/AUTOSAR checks be integrated into CI?"
track: embedded
section: debugging-and-testing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-testing
    title: "Zephyr Project documentation: Testing"
    url: https://docs.zephyrproject.org/latest/develop/test/index.html
  - source_id: gcc-warning-options
    title: "GCC manual: Options to Request or Suppress Warnings"
    url: https://gcc.gnu.org/onlinedocs/gcc/Warning-Options.html
  - source_id: clang-tidy-docs
    title: "Clang-Tidy documentation"
    url: https://clang.llvm.org/extra/clang-tidy/
  - source_id: cppcheck-manual
    title: "Cppcheck manual"
    url: https://cppcheck.sourceforge.io/manual.html
  - source_id: zephyr-sca
    title: "Zephyr Project documentation: Static Code Analysis (SCA)"
    url: https://docs.zephyrproject.org/latest/develop/sca/index.html
  - source_id: cmake-export-compile-commands
    title: "CMake documentation: CMAKE_EXPORT_COMPILE_COMMANDS"
    url: https://cmake.org/cmake/help/latest/variable/CMAKE_EXPORT_COMPILE_COMMANDS.html
  - source_id: misra-compliance-2020
    title: "MISRA Compliance:2020 – Achieving compliance with MISRA Coding Guidelines"
    url: https://misra.org.uk/app/uploads/2021/06/MISRA-Compliance-2020.pdf
---

## Short answer

For firmware, **clang-tidy**, `cppcheck`, compiler warnings, and commercial analyzers such as PC-lint/FlexeLint, Coverity, Polyspace, or Klocwork are appropriate. In CI, run analysis on each target/config, fix the rule set, suppressions, and baseline, and document MISRA/AUTOSAR deviations explicitly. <span class="warn">It is important to analyze the same code path, include dirs, and defines as the cross-build.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
