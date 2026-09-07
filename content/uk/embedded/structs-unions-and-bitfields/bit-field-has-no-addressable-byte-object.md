---
id: emb-structs-0023
title: "Чому не можна взяти адресу bit-field?"
description: "Bit-field не має адресованого byte object-а як звичайне поле."
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

<span class="warn">Bit-field не має адресованого byte object-а як звичайне поле.</span>

Він може займати кілька бітів усередині storage unit, а C address-of operator працює з об'єктами, які мають адресу. Тому `&s.flag` для bit-field є помилкою компіляції.

Embedded-наслідок: bit-field не можна передати у функцію як pointer на поле або використовувати з APIs, які очікують адресу змінної.[^embeddedinterviewlab]

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
