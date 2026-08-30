---
id: emb-cppfound-0027
title: "Що виведе?<br><pre class=\"code-block\"><code><span class=\"code-type\">int</span> a=<span class=\"code-num\">5</span>, b=<span class=\"code-num\">10</span>;<br><span class=\"code-type\">int</span> *p=&amp;a, *q=&amp;b;<br>*p=*q;<br><span class=\"code-fn\">printf</span>(\"%d %d\",a,b);</code></pre>"
description: "Why dereferencing pointers copies the pointed-to value."
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

<code>a=10, b=10</code>.<br><br><code>*p = *q</code> – копіює <span class="key">значення</span> <code>*q</code> (тобто <code>b=10</code>) у <code>*p</code> (тобто у <code>a</code>). Самі вказівники <code>p</code> і <code>q</code> не змінюються.<br><br>Якби <code>p = q</code> (без *) – обидва вказівники вказували б на <code>b</code>. <code>a</code> лишився б <code>5</code>.<br><br>Типова помилка: плутати присвоєння вказівників та значень.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
