---
id: emb-align-0002
title: "Чому CPU взагалі вимагає вирівнювання даних?"
description: "Шина читає/пише пам'ять word-aligned шматками фіксованого розміру."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
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

**Шина читає/пише пам'ять word-aligned шматками фіксованого розміру.**

Вирівняний доступ потрапляє в одне слово -> одна транзакція. Misaligned значення перетинає межу слова -> потрібні дві транзакції плюс склеювання, або апаратура взагалі забороняє такий доступ.

Правило: на простіших ядрах (Cortex-M0) це не «повільніше», а <span class="warn">HardFault</span>; на M3/M4 – штраф у такти.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
