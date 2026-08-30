---
id: emb-dtypes-0022
title: "Де зберігаються локальні змінні і чи ініціалізуються вони автоматично?"
description: "Локальні змінні лежать на стеку і не отримують автоматичної нульової ініціалізації."
track: embedded
section: data-types-and-memory-layout
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
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
---

## Short answer

Локальні змінні зберігаються на **стеку**. Вони <span class="warn">НЕ ініціалізуються автоматично</span> - містять garbage (випадкові дані з попередніх викликів або boot-процесу).

Ініціалізується тільки якщо є явний ініціалізатор: `int x = 0;` - компілятор генерує інструкцію запису.

Помилковий код: `int sum; for(...) sum += x;` -> UB. Лише `.data` і `.bss` ініціалізуються startup code.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
