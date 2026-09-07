---
id: emb-testemb-0007
title: "Які static analysis tools доречні для C/C++ firmware і як інтегрувати MISRA/AUTOSAR checks у CI?"
description: "Для firmware доречні clang-tidy, cppcheck, compiler warnings, commercial analyzers на кшталт PC-lint/FlexeLint, Coverity, Polyspace або Klocwork.У CI …"
track: embedded
section: testing-embedded
level: senior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження цього питання й відповіді; текст відповіді не перевірений незалежно від оригінальної Anki-колоди спільноти."
  - source_id: zephyr-testing
    title: "Zephyr Project documentation: Testing"
    url: https://docs.zephyrproject.org/latest/develop/test/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу testing-embedded; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

Для firmware доречні **clang-tidy**, `cppcheck`, compiler warnings, commercial analyzers на кшталт PC-lint/FlexeLint, Coverity, Polyspace або Klocwork. У CI запускають аналіз на кожен target/config, фіксують rule set, suppressions і baseline, а MISRA/AUTOSAR deviation оформлюють явно. <span class="warn">Важливо аналізувати той самий code path, include dirs і defines, що й cross-build.</span>[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
