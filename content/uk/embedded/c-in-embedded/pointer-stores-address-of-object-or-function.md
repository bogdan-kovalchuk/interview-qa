---
id: emb-cppfound-0001
title: "Що таке вказівник у C і що він зберігає?"
description: "What a C pointer is and what it stores."
track: embedded
section: c-in-embedded
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
    applicability: "Source question and answer; answer not independently verified."
---

## Short answer

<span class="key">Вказівник</span> – змінна, що зберігає <span class="key">адресу</span> іншого об'єкта або функції в пам'яті. Він не зберігає саме значення, а лише місцезнаходження.<br><br>Дві фундаментальні операції:<br>• <code>&amp;x</code> – взяття адреси: повертає адресу об'єкта <code>x</code>;<br>• <code>*p</code> – розіменування: читає/записує значення за адресою <code>p</code>.<br><br>Вони обернені: <code>*(&amp;x) == x</code> завжди. У embedded вказівники критичні для доступу до hardware registers, DMA буферів, callback-функцій.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
