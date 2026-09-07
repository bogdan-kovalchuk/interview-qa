---
id: emb-structs-0031
title: "Trap: чому positional initializer крихкий?"
description: "Значення прив'язані до порядку полів, а не до імен."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
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
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Short answer

```c
struct Cfg { uint32_t baud; uint8_t parity; uint8_t stop; };
struct Cfg c = { 115200, 0, 1 };
```

<span class="warn">Значення прив'язані до порядку полів, а не до імен.</span>

Якщо хтось вставить нове поле між `baud` і `parity`, initializer може залишитися синтаксично валідним, але значення поїдуть у неправильні поля. У driver configs це створює тихі runtime bugs.

Захист: для non-trivial structs використовуй designated initializers: `{ .baud = 115200, .parity = 0, .stop = 1 }`.[^embeddedinterviewlab]

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
