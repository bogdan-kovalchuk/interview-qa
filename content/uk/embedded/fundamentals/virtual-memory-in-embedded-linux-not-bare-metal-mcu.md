---
id: emb-fund-0011
title: "Для чого потрібна virtual memory в Embedded Linux і чому її зазвичай немає на bare-metal MCU?"
description: "Virtual memory дає кожному process власний address space, memory protection, lazy mapping, shared libraries, <code>mmap</code> і copy-on-write."
track: embedded
section: fundamentals
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
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? fundamentals; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

Virtual memory дає кожному process власний address space, memory protection, lazy mapping, shared libraries, <code>mmap</code> і copy-on-write. Bare-metal MCU зазвичай має малу RAM/Flash, deterministic requirements і часто тільки MPU або взагалі без memory protection. Тому там працюють з physical addresses, linker script і прямим MMIO.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

