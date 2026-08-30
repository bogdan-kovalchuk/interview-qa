---
id: emb-memlink-0002
title: "Які проблеми можуть виникнути, якщо не звільнити пам'ять?"
description: "Незвільнена пам'ять – memory leak: heap вичерпується, malloc повертає NULL, а на MCU без MMU пристрій зрештою йде в reset чи fault."
track: embedded
section: memory-and-linker
level: junior
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
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
    accessed: 2026-09-06
    kind: official
    version: "2.47"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? memory-and-linker; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

**Memory leak** – виділена пам'ять не повертається в систему, хоча більше не використовується.[^dou-embedded-interview] Наслідки:

- heap поступово вичерпується, тому `malloc` повертає `NULL`
- система уповільнюється або зависає
- в Embedded (MCU без MMU та ОС) це особливо критично: невеликий heap може закінчитися після годин або днів роботи, і пристрій піде в reset/fault або некоректний стан

Супутні проблеми: <span class="warn">dangling pointer</span> (доступ до звільненої пам'яті), <span class="warn">double free</span> (UB).

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
