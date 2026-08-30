---
id: emb-dtypes-0056
title: "Trap: що станеться? `free(ptr); free(ptr);`"
description: "Подвійний free - undefined behavior, яке псує метадані heap і відкриває шлях до security exploit."
track: embedded
section: data-types-and-memory-layout
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
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
---

## Short answer

<span class="warn">Double free -> undefined behavior.</span> Наслідки:
1. Corrupt heap metadata -> crash при наступному `malloc`/`free`;
2. <span class="warn">Security exploit</span>: heap-based buffer overflow, use-after-free;
3. Тихе пошкодження даних.

Захист: завжди після `free`: `ptr = NULL;`. `free(NULL)` - безпечний no-op.

У RTOS/embedded: heap corruption часто проявляється далеко від місця помилки.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
