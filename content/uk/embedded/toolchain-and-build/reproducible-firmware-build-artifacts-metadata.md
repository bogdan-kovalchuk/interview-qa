---
id: emb-build-0023
title: "Як організувати reproducible firmware build з pinned toolchain, artifacts, map file і version metadata?"
description: "Зафіксуй toolchain version, build container або package hash, CMake presets/options і dependency versions.У artifacts зберігай .elf, .hex/.bin, .map, …"
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

Зафіксуй toolchain version, build container або package hash, CMake presets/options і dependency versions.<br>У artifacts зберігай <code>.elf</code>, <code>.hex</code>/<code>.bin</code>, <code>.map</code>, symbol/version info, compiler flags і commit hash.<br><span class="key">Version metadata</span> у firmware має дозволяти точно відтворити binary, який стоїть на пристрої.[^dou-embedded-interview]
## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
