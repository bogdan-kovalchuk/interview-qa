---
id: emb-cppfound-0018
title: "Що виведе?<br><pre class=\"code-block\"><code>uint32_t *p=(uint32_t*)0x2000;<br>uint8_t *q=(uint8_t*)p;<br>printf(\"%zu %zu\", sizeof(*p), sizeof(*q));</code></pre>"
description: "Why sizeof a dereferenced pointer depends on its pointer type."
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

<code>sizeof(*p)</code> -> <span class="key">4</span>. Розіменування <code>uint32_t*</code> дає об'єкт типу <code>uint32_t</code> – 4 байти.<br><br><code>sizeof(*q)</code> -> <span class="key">1</span>. Розіменування <code>uint8_t*</code> дає <code>uint8_t</code> – 1 байт.<br><br>Важливо: <code>sizeof</code> операнда-розіменування визначається типом вказівника, а не адресою. Обидва вказівники вказують на ту саму адресу <code>0x2000</code>, але sizeof повертає різні значення.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
