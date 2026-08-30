---
id: emb-cppfound-0002
title: "Що виведе?<br><pre class=\"code-block\"><code>int x = 42;<br>int *p = &amp;x;<br>printf(\"%d %p\", *p, (void*)p);</code></pre>"
description: "How dereferencing and pointer values differ in a C example."
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

<code>*p</code> -> <code>42</code> (розіменування – читає значення <code>x</code>).<br><code>p</code> -> адреса змінної <code>x</code> (наприклад, <code>0x2000FFE0</code> на стеку Cortex-M).<br><br>Важливо: <code>p</code> і <code>x</code> – різні об'єкти. <code>p</code> зберігає адресу, <code>x</code> – значення. Зміна <code>*p = 100</code> змінює <code>x</code>. Зміна <code>p = &amp;y</code> не змінює <code>x</code>.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
