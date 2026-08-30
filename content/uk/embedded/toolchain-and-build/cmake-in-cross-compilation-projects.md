---
id: emb-build-0009
title: "Як працює CMake у cross-compilation проекті для MCU або Embedded Linux?"
description: "Практичне питання про embedded-розробку та її обмеження."
track: embedded
section: toolchain-and-build
level: middle
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

CMake спочатку configure-ить build graph: читає <code>CMakeLists.txt</code>, toolchain file, target flags і генерує Ninja/Make project. Потім build tool викликає cross-compiler, assembler, linker і post-build утиліти на кшталт <code>objcopy</code>. Важливо розділяти host tools, які запускаються на PC, і target binaries, які призначені для MCU або Linux target.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

