---
id: emb-cppfound-0096
title: "Trap: що не так?<br><pre class=\"code-block\"><code><span class=\"code-type\">int</span> **pp;<br>*pp = <span class=\"code-fn\">malloc</span>(<span class=\"code-num\">10</span>*<span class=\"code-kw\">sizeof</span>(<span class=\"code-type\">int</span>));</code></pre>"
description: "Why dereferencing an uninitialized double pointer is undefined behavior."
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

<span class="warn">Wild pointer – UB.</span> <code>int **pp;</code> – неініціалізований double pointer, містить garbage-адресу.<br><br><code>*pp = malloc(...)</code> – розіменовує <code>pp</code> (UB!) і записує адресу виділеної пам'яті за невідомою адресою. Це може зіпсувати будь-яку область пам'яті.<br><br>Правильно:<br><code>int *p = NULL;<br>int **pp = &amp;p;<br>*pp = malloc(10*sizeof(int));</code><br><br>Завжди ініціалізуй вказівники перед використанням.[^embeddedinterviewlab]

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


