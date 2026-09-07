---
id: emb-volconst-0042
title: "Trap: чому `const` у C не означає compile-time constant для всіх випадків?"
description: "У C const означає read-only object через цей identifier, але не завжди integer constant expression."
track: embedded
section: volatile-and-const
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 1
reconciled_with:
  en: 2
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

<span class="warn">У C `const` означає read-only object через цей identifier, але не завжди integer constant expression.</span>

Наприклад, file-scope `const int n = 10;` у C не можна всюди використовувати як розмір static array там, де потрібна compile-time constant expression. У C++ правила інші. Для C embedded коду часто використовують `enum`, `#define` або linker symbols для compile-time constants.

Захист: не плутай immutability object-а з preprocessor/translation-time constant.[^embeddedinterviewlab]

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
