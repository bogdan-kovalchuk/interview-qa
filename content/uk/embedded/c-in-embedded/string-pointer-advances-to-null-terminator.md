---
id: emb-cppfound-0037
title: "Що виведе?<br><pre class=\"code-block\"><code><span class=\"code-type\">char</span> str[] = \"hello\";<br><span class=\"code-type\">char</span> *p = str;<br><span class=\"code-kw\">while</span>(*p) p++;<br><span class=\"code-fn\">printf</span>(\"%td\", p-str);</code></pre>"
description: "How pointer iteration reaches the string null terminator."
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

<code>5</code>.<br><br><code>str</code> decay-ується до <code>char*</code>. Цикл йде до <code>'\0'</code>: після <code>'h','e','l','l','o'</code> – <code>*p = '\0'</code> (false) -> стоп. <code>p</code> вказує на null-terminator.<br><br><code>p - str</code> = 5 елементів = <code>strlen("hello")</code>. Це стандартний спосіб реалізації <code>strlen</code> через pointer arithmetic. <code>%td</code> для <code>ptrdiff_t</code>.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
