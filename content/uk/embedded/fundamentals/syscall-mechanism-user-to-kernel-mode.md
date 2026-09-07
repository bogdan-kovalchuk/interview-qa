---
id: emb-fund-0003
title: "Що таке system call?"
description: "System call перемикає CPU з user-space у kernel mode через програмний номер виклику в регістрі, щоб отримати сервіс ядра з ізоляцією пам'яті."
track: embedded
section: fundamentals
level: junior
type: mechanism
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
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу fundamentals; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**System call (syscall)** – механізм запиту сервісів ядра з user-space.[^dou-embedded-interview] Оскільки user-space не має прямого доступу до апаратури та ресурсів ядра, програма виконує syscall для переходу в kernel mode.

Механізм (x86-64): програма поміщає номер syscall у `rax`, аргументи у `rdi/rsi/rdx...`, виконує інструкцію `syscall`. Ядро переключається в privileged mode, виконує обробник і повертає результат.

Забезпечує ізоляцію: user-space процеси не можуть пошкодити пам'ять ядра або інших процесів.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
