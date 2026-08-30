---
id: emb-cppfound-0014
title: "Що таке <code>void*</code> і які обмеження має цей тип вказівника?"
description: "The capabilities and restrictions of a void pointer."
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

<span class="key">void*</span> – type-erased pointer: може зберігати адресу об'єкта будь-якого типу без explicit cast.<br><br>Обмеження:<br>• <span class="warn">Не можна розіменувати</span> без cast: <code>*p</code> – помилка компіляції;<br>• <span class="warn">Не можна виконати arithmetic</span> без cast (стандарт C). GCC дозволяє як extension (розмір елемента = 1 байт).<br><br>Використання: <code>malloc</code>/<code>free</code>, <code>memcpy</code>/<code>memset</code>, generic callbacks, <code>qsort</code>. У embedded: generic ISR handler tables.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
