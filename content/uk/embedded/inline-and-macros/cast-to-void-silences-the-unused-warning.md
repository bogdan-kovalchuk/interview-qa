---
id: emb-macros-0034
title: "Навіщо макрос `UNUSED(x)` і як він виглядає?"
description: "Пригнічує warning «unused parameter/variable», явно показуючи намір, що значення навмисно не використовується."
track: embedded
section: inline-and-macros
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
#define UNUSED(x) ((void)(x))
```

## Short answer

**Пригнічує warning «unused parameter/variable»**, явно показуючи намір, що значення навмисно не використовується.

Типово у callback-сигнатурах, де частина параметрів не потрібна: `void cb(void *ctx) { UNUSED(ctx); ... }`. Cast у `void` не генерує коду.

Правило: краще явний `UNUSED(x)`, ніж глобальне вимкнення `-Wunused` – попередження лишається корисним деінде.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
