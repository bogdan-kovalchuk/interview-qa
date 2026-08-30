---
id: emb-build-0017
title: "Що таке cross-compilation і які типові помилки виникають при запуску binary на іншій архітектурі?"
description: "Cross-compilation – build на host-машині для іншого CPU/OS/ABI target. Типові помилки: зібрали під host, змішали wrong sysroot, soft/hard-float ABI, e…"
track: embedded
section: toolchain-and-build
level: middle
type: pitfall
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

Cross-compilation – build на host-машині для іншого CPU/OS/ABI target. Типові помилки: зібрали під host, змішали wrong sysroot, soft/hard-float ABI, endian або libc, а потім отримали <code>Exec format error</code> чи runtime crash. Перевіряти треба <code>file</code>, <code>readelf -h</code>, target triplet і toolchain flags.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

