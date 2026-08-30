---
id: emb-dtypes-0027
title: "Чому heap часто забороняють у safety-critical embedded системах?"
description: "malloc недетермінований, фрагментує пам'ять і важко аналізується, тому safety-critical стандарти вимагають static allocation."
track: embedded
section: data-types-and-memory-layout
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
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
---

## Short answer

Heap (`malloc`/`free`) має три проблеми:

1. **Недетермінований час** - `malloc` займає різний час залежно від стану heap;
2. **Heap fragmentation** - вільна пам'ять є, але не суцільний блок потрібного розміру -> `malloc` повертає NULL;
3. **Важко аналізувати** worst-case memory usage.

MISRA C, DO-178C вимагають static allocation. `malloc` лише при ініціалізації, не у real-time частині.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
