---
id: emb-dtypes-0041
title: "Trap: чи ініціалізується всередині функції нулем? `static int x;`"
description: "static локальна без ініціалізатора еквівалентна static int x = 0 і зануляється лише один раз при завантаженні."
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

**Так**, але це тонкий момент: `static` локальна без ініціалізатора ≡ `static int x = 0;` - нуль при першому виклику (zeroed у `.bss` при boot).

`static int x = 5;` -> ініціалізується значенням 5 один раз. Подальші зміни зберігаються між викликами.

<span class="warn">Звичайна</span> `int x;` - НЕ ініціалізується (garbage). Помилка: припускати що `int x;` = 0 у першому виклику.[^embeddedinterviewlab]

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
