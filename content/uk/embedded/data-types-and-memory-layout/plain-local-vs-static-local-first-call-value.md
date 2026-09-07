---
id: emb-dtypes-0086
title: "Trap: чи однаково поводяться `int x;` та `static int x;` всередині функції при першому виклику?"
description: "int x; містить сміття зі стека, а static int x; гарантовано дорівнює нулю при першому виклику."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

<span class="warn">НІ!</span>

`int x;` - на стеку, <span class="warn">contains garbage</span> (невизначене значення, кожен виклик новий slot).

`static int x;` - у `.bss`, гарантовано = 0 при першому виклику (zeroed at boot). При наступних - зберігає значення з попереднього виклику.

Помилка: припускати що `int x;` = 0 при першому виклику. Компілятор не додає ініціалізацію автоматично.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
