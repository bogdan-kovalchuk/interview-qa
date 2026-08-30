---
id: emb-cppfound-0084
title: "Навіщо завжди перевіряти повернення <code>malloc</code> на NULL?"
description: "Why failed allocation must be handled before dereferencing the result."
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

<code>malloc</code> повертає <span class="key">NULL</span> при помилці виділення (нема пам'яті, heap fragmentation). Якщо не перевірити і розіменувати NULL -> <span class="warn">HardFault на MCU</span>.<br><br><code>int *p = malloc(n * sizeof(int));<br>if(p == NULL) { error_handler(); return; }<br>// Тепер безпечно використовувати</code><br><br>У embedded: malloc може провалитися навіть при малих запитах через fragmentation. Safety-critical стандарти забороняють malloc взагалі – але якщо використовуєш, перевірка обов'язкова.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->


