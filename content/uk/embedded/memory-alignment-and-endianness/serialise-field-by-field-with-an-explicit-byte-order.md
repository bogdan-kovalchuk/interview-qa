---
id: emb-align-0021
title: "Як правильно серіалізувати структуру у байтовий буфер?"
description: "Поле за полем, з явним byte order і фіксованими зсувами."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: mechanism
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

## Question code

```c
uint32_t ts = htonl(r->ts);
uint16_t v  = htons(r->val);
memcpy(&buf[0], &ts, 4);
memcpy(&buf[4], &v,  2);
buf[6] = r->id;
```

## Short answer

**Поле за полем, з явним byte order і фіксованими зсувами.**

Кожне багатобайтове поле спершу конвертується (`htonl`/`htons`), потім кладеться у відомий offset через `memcpy`. Однобайтове `id` не потребує swap.

Правило: `memcpy` тут ще й рятує від unaligned-trap, навіть якщо `buf` не вирівняний.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
