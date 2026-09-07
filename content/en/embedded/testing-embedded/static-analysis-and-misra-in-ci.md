---
id: emb-testemb-0007
title: "Which static-analysis tools suit C/C++ firmware, and how should MISRA/AUTOSAR checks be integrated into CI?"
description: "Use clang-tidy, cppcheck, and commercial analyzers in CI with the same code paths as the cross-build."
track: embedded
section: testing-embedded
level: senior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of this question and answer; the answer text is not independently verified against the original community Anki deck."
  - source_id: zephyr-testing
    title: "Zephyr Project documentation: Testing"
    url: https://docs.zephyrproject.org/latest/develop/test/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Authoritative section-level reference for testing embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

For firmware, **clang-tidy**, `cppcheck`, compiler warnings, and commercial analyzers such as PC-lint/FlexeLint, Coverity, Polyspace, or Klocwork are appropriate. In CI, run analysis on each target/config, fix the rule set, suppressions, and baseline, and document MISRA/AUTOSAR deviations explicitly. <span class="warn">It is important to analyze the same code path, include dirs, and defines as the cross-build.</span>[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
