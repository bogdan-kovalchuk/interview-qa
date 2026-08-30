---
id: emb-cppfound-0027
title: "What does this print?<br><pre class=\"code-block\"><code><span class=\"code-type\">int</span> a=<span class=\"code-num\">5</span>, b=<span class=\"code-num\">10</span>;<br><span class=\"code-type\">int</span> *p=&amp;a, *q=&amp;b;<br>*p=*q;<br><span class=\"code-fn\">printf</span>(\"%d %d\",a,b);</code></pre>"
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
  uk: 1
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
