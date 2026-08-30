---
id: emb-build-0010
title: "Що таке toolchain file у CMake і яку роль мають compiler, sysroot та target flags?"
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
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? toolchain-and-build; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

<span class="key">Toolchain file</span> задає CMake, що build іде не для host, а для target: <code>CMAKE_SYSTEM_NAME</code>, compilers, archiver, objcopy, sysroot і flags. <code>sysroot</code> дає headers/libraries target-системи, а target flags задають ABI, FPU, CPU core, linker script тощо. Без цього CMake може непомітно знайти host-бібліотеки й зібрати несумісний binary.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

