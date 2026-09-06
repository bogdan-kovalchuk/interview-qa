---
id: emb-structs-0026
title: "Trap: що не так із read-modify-write для status register?"
description: "Компілятор може згенерувати read-modify-write усього register-а."
track: embedded
section: structs-unions-and-bitfields
level: junior
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
STATUS.bits.error = 0;
```

Компілятор може згенерувати read-modify-write усього register-а.

Якщо STATUS має read-to-clear bits або write-one-to-clear bits, простий запис одного bit-field може ненавмисно очистити або змінити інші flags. Для hardware registers semantics важливіша за C-level зручність.

Захист: використовуй documented clear register або записуй точну mask, наприклад `STATUS = ERROR_Msk;` для W1C, якщо manual вимагає саме так.[^embeddedinterviewlab]

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
