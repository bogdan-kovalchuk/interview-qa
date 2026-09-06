---
id: emb-patterns-0013
title: "Навіщо у структурі ring buffer поля позначають `volatile`?"
description: "Бо head і tail змінюються в одному контексті (ISR), а читаються в іншому (main)."
track: embedded
section: common-code-patterns
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

**Бо `head` і `tail` змінюються в одному контексті (ISR), а читаються в іншому (main).**

Без `volatile` компілятор може закешувати індекс у регістрі й не побачити оновлення з іншої сторони, зламавши логіку full/empty. Сам буфер даних часто не роблять `volatile`, якщо порядок «записати байт -> опублікувати `head`» дотриманий; volatile потрібен саме для shared control state.

Правило: спільні між ISR (interrupt service routine) і main індекси/прапорці – `volatile`; але `volatile` не дає атомарності, лише забороняє кешування/оптимізацію доступу.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
