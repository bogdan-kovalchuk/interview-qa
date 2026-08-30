---
id: emb-cppfound-0046
title: "Trap: що не так?<br><pre class=\"code-block\"><code>free(ptr);<br>if(*ptr == 0)</code></pre>"
description: "Why dereferencing a pointer after free is undefined behavior."
track: embedded
section: c-in-embedded
level: junior
type: pitfall
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

<span class="warn">Use-after-free – undefined behavior.</span> Після <code>free(ptr)</code> блок пам'яті повертається heap manager-у і може бути одразу перевикористаний.<br><br>Читання <code>*ptr</code> -> UB: може повернути 0, старе значення або нове значення від іншого malloc. У реальному коді – джерело security vulnerabilities (type confusion, heap exploitation).<br><br>Правило: після <code>free</code> завжди: <code>ptr = NULL;</code>. <code>if(ptr != NULL &amp;&amp; *ptr == 0)</code> – тоді безпечно.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

