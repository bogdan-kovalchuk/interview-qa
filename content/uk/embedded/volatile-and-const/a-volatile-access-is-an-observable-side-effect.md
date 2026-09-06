---
id: emb-volconst-0035
title: "Чи є читання volatile-об'єкта side effect?"
description: "Так, volatile access вважається observable side effect для абстрактної машини C."
track: embedded
section: volatile-and-const
level: junior
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

**Так, volatile access вважається observable side effect для абстрактної машини C.**

Тому компілятор не може просто прибрати читання hardware register як "невикористаний результат", якщо саме читання може очищати flag, acknowledge interrupt або запускати bus transaction. Це одна з причин, чому register definitions мають бути volatile.

Embedded-правило: якщо read-to-clear або read-has-side-effect register описаний без `volatile`, оптимізатор може зламати протокол периферії.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
