---
id: emb-build-0022
title: "Як налаштувати CI для збірки firmware під кілька target-платформ і toolchains?"
description: "CI має матрицю target x toolchain x config: наприклад GCC/Clang, debug/release, board variants.Кожна job ставить pinned toolchain, запускає configure/…"
track: embedded
section: toolchain-and-build
level: senior
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
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
---

## Short answer

CI має матрицю <span class="key">target x toolchain x config</span>: наприклад GCC/Clang, debug/release, board variants.<br>Кожна job ставить pinned toolchain, запускає configure/build, static analysis, unit tests і збирає artifacts: ELF, HEX/BIN, map, logs.<br>Для target-only перевірок окремо підключають HIL runners або nightly hardware jobs.[^dou-embedded-interview]
## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
