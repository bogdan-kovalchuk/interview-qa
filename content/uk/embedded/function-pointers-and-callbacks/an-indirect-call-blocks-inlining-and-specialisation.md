---
id: emb-fnptr-0056
title: "Чому function pointers впливають на оптимізацію?"
description: "Indirect call важче оптимізувати, ніж direct call."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
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

**Indirect call важче оптимізувати, ніж direct call.**

Компілятор часто не знає точну callee функцію, тому не може inline-ити, прибрати unused branches всередині callee або точно побудувати call graph. LTO іноді допомагає, якщо table статична і видима, але гарантії менші.

Embedded-висновок: function pointers дають гнучкість, але можуть збільшити code size і latency; у hot paths оцінюй generated assembly.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
