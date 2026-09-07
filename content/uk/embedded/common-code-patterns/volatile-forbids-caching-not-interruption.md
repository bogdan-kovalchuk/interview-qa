---
id: emb-patterns-0031
title: "Чому `volatile` не достатньо для безпечного `count++` між ISR і main?"
description: "volatile забороняє кешування, але НЕ робить операцію атомарною."
track: embedded
section: common-code-patterns
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

<span class="warn">`volatile` забороняє кешування, але НЕ робить операцію атомарною.</span>

`count++` – це read-modify-write (RMW, 3 кроки); ISR (interrupt service routine) може перебити main посередині, і інкремент загубиться. `volatile` лише гарантує, що кожен крок іде в пам'ять, а не що кроки неподільні.

Захист: критична секція, atomic-тип, або дизайн без спільного RMW (head/tail-only ring buffer).[^embeddedinterviewlab]

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
