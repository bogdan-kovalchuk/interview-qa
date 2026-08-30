---
id: emb-cppfound-0039
title: "Що зробить <code>memcpy(dst, src, sizeof(src))</code> якщо <code>src</code> – параметр-масив функції?"
description: "Why sizeof on an array parameter copies only pointer-sized data."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
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

<span class="warn">Скопіює лише 4 або 8 байт</span> (розмір вказівника), а не розмір масиву.<br><br>У параметрі функції <code>src</code> – це <code>uint8_t*</code>, не масив. <code>sizeof(src) = sizeof(uint8_t*) = 4</code>. Тому <code>memcpy</code> копіює тільки 4 байти замість N.<br><br>Правильно: передавати розмір явно: <code>memcpy(dst, src, n * sizeof(src[0]))</code> або <code>memcpy(dst, src, n)</code> де <code>n</code> – окремий параметр.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
