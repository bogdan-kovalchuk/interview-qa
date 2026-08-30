---
id: emb-cemb-0017
title: "Для чого використовують вирівнювання, чи можна його контролювати?"
description: "Вирівнювання прискорює й коригує доступ CPU до даних; контролюється порядком полів, alignas/_Alignas і атрибутами на кшталт packed."
track: embedded
section: c-in-embedded
level: junior
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

Вирівнювання потрібне для швидкого й коректного доступу CPU до даних.[^dou-embedded-interview] Багато архітектур читають 2/4/8-байтові значення ефективніше, коли адреса кратна розміру типу; деякі MCU на misaligned access можуть згенерувати fault.

Контролювати можна через порядок полів у struct, стандартні засоби `alignas` у C++ або `_Alignas`/`alignas` у сучасному C, а також compiler-specific атрибути типу `__attribute__((aligned))`, `__attribute__((packed))`, `#pragma pack`. `packed` треба використовувати обережно: він економить байти, але може сповільнити доступ або зламати вимоги hardware.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
