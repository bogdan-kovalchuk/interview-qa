---
id: emb-cppfound-0070
title: "Що поверне <code>strlen(s)</code> і <code>sizeof(s)</code> якщо <code>char s[20] = \"hello\"</code>?"
description: "The difference between string length and character-array capacity."
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

<code>strlen(s)</code> -> <span class="key">5</span>. Рахує символи до '\0' (не включаючи). Runtime функція.<br><br><code>sizeof(s)</code> -> <span class="key">20</span>. Розмір масиву оголошений при компіляції – весь буфер, незалежно від вмісту. Compile-time операція.<br><br>Рядок "hello" займає 6 байт (<code>h,e,l,l,o,\0</code>), решта 14 байт – нулі (через <code>= "hello"</code> ініціалізацію масиву). <code>sizeof(s)/sizeof(s[0]) = 20/1 = 20</code> – ємність буфера.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
