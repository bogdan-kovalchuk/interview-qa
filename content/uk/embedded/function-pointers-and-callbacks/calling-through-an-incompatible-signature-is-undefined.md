---
id: emb-fnptr-0016
title: "Trap: що не так із викликом callback із несумісною сигнатурою?"
description: "Виклик через function pointer несумісного типу має undefined behavior."
track: embedded
section: function-pointers-and-callbacks
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
void f(int x);
void (*cb)(void) = (void (*)(void))f;
cb();
```

Виклик через function pointer несумісного типу має undefined behavior.

Навіть якщо адреса функції фізично правильна, calling convention очікує інші аргументи, return value або register usage. На embedded ABI це може пошкодити stack/registers або передати випадкові значення.

Захист: не виправляй warning `-Wincompatible-pointer-types` cast-ом. Зроби adapter function із правильною сигнатурою.[^embeddedinterviewlab]

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
