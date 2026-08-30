---
id: emb-cppfound-0012
title: "У яких трьох контекстах масив НЕ розпадається (decay) до вказівника?"
description: "The three common contexts where an array remains an array."
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

Масив залишається масивом і <span class="key">не decay-ується</span> у трьох випадках:<br><br>1. <code>sizeof(arr)</code> – повертає загальний розмір масиву у байтах, не розмір вказівника;<br>2. <code>&amp;arr</code> – повертає вказівник на масив <code>int(*)[N]</code>, не <code>int*</code>;<br>3. Ініціалізація рядковим літералом: <code>char arr[] = "hi"</code> – копіює символи у масив.<br><br>Пам'ятай ці три виключення – вони часто зустрічаються на інтерв'ю.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
